## **map/reduce/shuffle 阶段优化(☆☆☆)**

基础定义：Hive是maper reduce的一个客户端，它将我们编写的hivesql 通过hive的一个解析引擎转化成mapreduce的一个程序 最终提交到yarn上运行

### 三个阶段

在wordcount模式上，我们用户在编写程序上分为三个部分 ：

就是将我们编写的hivesql 通过hive 的一个解析引擎转换成mapreduce的一个程序，最终提交到yarn上去运行

mapper阶段

map是干什么的，map是需要集成mapper类，重写map方法

进行一个数据的切分kv键值对

进行数据的简单过滤

map的基本过程：

Map-map,map-sort

reducer阶段

计算reduce,然后把业务逻辑就是如何聚合写到reduce方法中

reduce过程基本的3个阶段 copy-sort-redcue

       1.第一阶段复制map输出数据

2.第二阶段就是数据合并排序

3.数据进行reduce的聚合处理

Driver阶段

### MR运行过程

基础版本：

首先我们输入文件 然后哪些文件需要处理

mapper进行处理 切分

处理完之后  然后进入到shuffle阶段 将文件分发给reduce reduce在进行一次聚合处理

最终把 output输出到不同的应用系统里

细化版：

input:

首先我们针对于input做一个切分，我们把整个数据按照多大的一个块去切

然后我们去读这个数据 比如读这个文件要分一个a.txt的文本文件 去统计wordcount 那么文件首先要知道那个文件是按照什么样的存储格式行列分隔符 序列化的模式什么样的

其实就是我们任务在提交到yarn上面的时候其实已经计算好了 通过getsplit方式 通过公式已经计算好了这个任务需要多少map 需要多少reduce 然后到yarn进行申请资源

读完数据之后,我们传给整个map去处理，map处理完数据之后 传给环形缓冲区，超过缓冲区的时候进行排序和溢出

这里加了一个combiner ，这里combiner可以做一个数据合并，做一个简单的预聚合，这样可以减少reduce上的一个数据量

但是combiner有个注意点 不能影响结果集才可以用

最终序列化本地化文件，在进行分区排序 写到本地文件系统

map处理完之后，把处理好的结果按照reduce的个数 写入到本地

### shuffle过程

首先这个图里读的相当于是3个block，相当于起3个map任务，每个map任务处理一个block

首先当我们去读block的数据，按照行列分隔符，数据是按照什么格式存储的，通过map把它读成kv键值对

然后把kv键值对写到内存里面就是写到环形缓冲区，缓冲区的底层其实是一个数组

环形缓冲区是有默认大小的，100m,这个大小很小，比如一个文件读完解压缩有上g，那么内存里面是肯定放不下的，放不下怎么办呢，那么我们就要往本地磁盘溢写，类似于大家用虚拟内存一样，内存不够我调用本地磁盘空间。

但是实际的生产力我们的环形缓冲区远比默认的大，有可能设置为1个g

环形缓冲区这里的数据超过了阈值 也就是80%，会把整个数据往磁盘里溢写

我们对整个数据进行一个分区，进行一个排序，就是多少个文件在进行合并

如果我们处理的数据很大的时候，我们可能会对整个溢写的文件进行一个合并，如果表很小的话装这表的话可能就没有这个过程了，就不存在所谓的把数据溢写到一个本地磁盘的过程，这就是为什么生产上环形缓冲区会设的很大

然后把溢写的数据，写到磁盘以后，多个溢写的文件要进行合并

因为最终reduce是要到节点上拉数据，如果数据很多的话肯定是不行的，最终要给reduce呈现一个文件，溢写合成一个大的文件方便reduce读取

那么我们在溢写过程中，合并文件的过程中，我们要调用partition

因为每个redufce,要去map上拉数据，那么我怎么知道每个reduce拉的是属于自己的数据

这个时候我们就通过hash partition我们给它分组，数据进行一个排序

比如哪些数据通过hashpartition，hash取值。所谓的hash取值就是取余数

比如现在是3个map 2个reduce，那么我就给这3个map除以2取余，结果就是2  ，就是0和1最多2个值，这个时候就相当于把数据分成了2份，那么每个reduce就知道自己属于那份了！比如第一个reduce 给她的分区partition就是 1

第二个就是 2 这样的

**为什么环形缓冲区的值要设置的很大？**

1.为了避免调用到磁盘

2.减少溢写文件，减少合并文件，因为reduce是要到节点上拉数据的，所以最好就是给reduce呈现为一个文件，溢写乘一个大的文件方便reduce读取

3.减少spil次数，防止阻塞

**为什么我们在合并还有溢写的时候要进行排序呢？**

排序的目的就是为了相同的数据连贯在一起的，那么reduce在拉数据 ，在磁盘寻址的时候会非常快，比如spil里面的 文件里面有几十亿行，胡乱放的时候也能拉但是要寻址，但是按照顺序放的话寻址就非常快很高效！

**为什么在map阶段进行了排序**

这个是为了减少reduce在copy拉去map数据的寻址时间，其次提高 reduce 阶段 的数据排序合并的效率；

### 日志层面去看map/reduce执行流程

reduce过程基本3个阶段

copy-sort-reduce

### shuffle过程集群层面的优化

集群里的map没有跑完，reduce就开始跑了

其是在正常的跑任务的时候，应该是所有的map都跑完了再开始启动reduce，但是有时候在不同的公司会发现，为什么我的map还没有结束，reduce就开始去跑了，那么这个原因是什么？

那么这个就是

mapreduce.job.reduce.slowstart.completedmaps 这个参数影响的

这个参数是干啥的？

简单来说就是map完成多少的时候，才回去启动reduce

默认是0.05 表示maptask至少完成5%以上 才会为reduce申请资源

## yarn任务提交流程熟悉

### 整体组件：

ResourceManager：全局资源管理器

NodeManager ：负责接受作业提交、协商（得到）用于执行某一个具体应用程序的ApplicationMaster的第一个容器，并提供在失败时重新启动ApplicationMaster容器的服务

ResourceManager 和 NodeManager 构成了数据计算框架

ApplicationMaster：每个应用程序的应用程序主控器

ApplicationMaster：负责应用的监控，跟踪应用执行状态，重启失败任务等，是每台计算机框架的代理，它负责容器、监视其资源使用情况（CPU、内存、磁盘、网络），并向资源管理器（ResourceManager）/调度程序（Scheduler）报告这些情况。

它的任务是与ResourceManager协商资源，并与节点管理器一起执行和监视任务

ResourceManager：有两个主要组件：调度器（Scheduler ）和应用程序管理器（ApplicationsManager）

Container：是YARN中的资源抽象，它封装了某个节点上的多维度资源，如内存、CPU、磁盘、网络等

YARN 的总体架构模式是 Master/Slave 主从模式。

主是ResourceManager

从是NodeManager

YARN 是为了给计算框架做资源调度分配与管理的，那么少不了应用程

序管理相关的框架：**ApplicationMaster**

AM的作用呢就是负责管理整个系统中的应用程序，向ResourceManager申请资源实际上是在NodeManager上执行

客户端向yarn提交 资源，ResourceManager就根据每个NodeManager上的资源使用情况，分配一个container来执

其实我们一般说的yarn就是说的ResourceManager

行，container执行以后，在container上启动一个**ApplicationMaster，这个就是应用的管理者，**

然后**应用的管理者再向ResourceManager申请资源，启动整个任务**

整个任务所有的运行执行，从启动到结束所有的过程都是**ApplicationMaster管**

ResourceManager和NodeManager并不管你任务运行的失败与否

任务挂了之后应该是**ApplicationMaster 发现以后，那就向yarn重新申请资源，重新跑一下这个任务**

## **Hive/HDFS/MR/YARN 协作流程**

### **Hive/MR/数据库交互关系**

haiv查询一个表的数据

1.我们查一份数据的时候，首先提交到hive引擎

2.hive是把他的元数据存在数据库里面，比如以mysql为准，生产上可能用的是orcial，把元数据就是表的相关一些信息，表有多少分区，表有多少行，表的状态是什么样的，表的模式是什么样的，这些建表结构等等

这些元数据信息存在mysql上，那么实际的数据存在hdfs上，所以hive只是一个引擎

我们查询一张表的时候，首先通过hive引擎执行

hive引擎生成执行计划，读mysql,这是什么表，大概多少行

读完元数据以后再跟hive引擎进行结合生成一个执行计划，可以理解为是一个mr的程序，转成mapereduce的一个程序，又可能这个代码写的很长的时候，就有可能给到多个mr去执行

将mr程序提交到yarn上执行

yarn执行的时候，计算什么数据，实际读取数据的时候，数据存在哪里就去hdfs上进行交互

## 调优实战和案例

企业调优主要分为两个模块

代码层面

任务运行参数层面

## **Hive 的 map/reduce 内存与核数调优**

### **控制 map/reduce 内存与核数相关参数**

设置每个map的内存和核数大小

- [ ]

设置每个reduce的内存大小

- [ ]

这两个是常用的

**比如有些是 **

**报 oom，堆内存溢出等时，可以适调大这几个参数，通过增加内存 cpu 的方 **

**式提高 task 运行速度，但是坏处是可能造成资源的浪费； **

### 如何控制map个数与性能调优

在 Hive 中配置“set mapred.map.tasks=task 数量（默认值 2）”

无法真正 控制 Map 的任务数，调节 Map 任务数需要一套算法

**实际生产中，我们一般不用这个参数：set mapred.map.tasks，新版替代的参数 **

**是 mapreduce.job.maps**

- [ ]

### 控制map个数的常用参数介绍

- [ ]

- [ ]

set hive.input.format =

org.apache.hadoop.hive.ql.io.CombineHiveInputFormat;

Set hive.merge.mapfiles=true;

Set hive.merge.mapredfiles = true;

Set hive.merge.smallfiles.avgsize = 256000000;

Set hive.merge.size.per.task = 12800000;

set mapred.max.split.size=256000000;

set mapred.min.split.size= 64000000;

set mapred.min.split.size.per.node=64000000;

set mapred.min.split.size.per.rack=64000000;

set mapred.min.split.size

set mapred.min.split.size.per.node

set mapred.min.split.size.per.rack

### 案例

1.使用上方文档的默认参数

set hive.input.format =
org.apache.hadoop.hive.ql.io.CombineHiveInputFormat;
set mapred.max.split.size=256000000;
set mapred.min.split.size= 8000000;
set mapred.min.split.size.per.node=8000000;
set mapred.min.split.size.per.rack=8000000;

结论：map数是84个

2.再上方默认的参数上，增加split的值

set hive.input.format =
org.apache.hadoop.hive.ql.io.CombineHiveInputFormat;
set mapred.max.split.size=256000000;
set mapred.min.split.size= 128000000;
set mapred.min.split.size.per.node=128000000;
set mapred.min.split.size.per.rack=128000000;

结论：map数是17个

3.**只调整 min.split.size,其他跟他方案 2**

set hive.input.format =

org.apache.hadoop.hive.ql.io.CombineHiveInputFormat;

Set hive.merge.mapfiles=true;

Set hive.merge.mapredfiles = true;

Set hive.merge.smallfiles.avgsize = 256000000;

Set hive.merge.size.per.task = 12800000;

set mapred.max.split.size=256000000;

set mapred.min.split.size= 8000000;

set mapred.min.split.size.per.node=128000000;

set mapred.min.split.size.per.rack=128000000;

结论：17个

4.**方案 2 基础上调整 min.split 和 split.per.node 参数**

set hive.input.format =

org.apache.hadoop.hive.ql.io.CombineHiveInputFormat;

set mapred.max.split.size=256000000;

set mapred.min.split.size= **8000000; **

set mapred.min.split.size.per.node=**8000000; **

set mapred.min.split.size.per.rack=128000000;

结论：map个数 79个

5.**在方案 2 的基础上把 split.per.rack 调小**

set hive.input.format =

org.apache.hadoop.hive.ql.io.CombineHiveInputFormat;

set mapred.max.split.size=256000000;

set mapred.min.split.size= 128000000;

set mapred.min.split.size.per.node=128000000;

set mapred.min.split.size.per.rack=**64000000;**

结论：报错

1

2

3

4

5

max.split.size

256000000

256000000

256000000

256000000

256000000

min.split.size

8000000

128000000

8000000

8000000

128000000

min.split.size.per.node

800000

128000000

128000000

8000000

128000000

min.split.size.per.rack

800000

128000000

128000000

128000000

64000000

map个数

84

17

17

79

报错

**总结：**

总体来说，min.split.size.per.node ，min.split.size.per.rack这个参数对于map的小文件合并影响最大，调高能够有效的减少map的数量

**map 个数过多浪费资源，同时会造成资源抢占。map 过少造成 **

**单个 map 处理数据量过大，会造成任务跑的慢。建议单个 map 的处理数据 **

**量在 128Mb-512Mb 之间**

**一般我们企业设置参数的收 max.split.size>= min.split.size>  **

**min.size.per.rack= min.size.per.node**

### reduce个数控制和优化

参数 1：直接指定 reduce 个数

set mapred.reduce.tasks/ mapreduce.job.reduces

默认值是-1

- [ ]

参数3

当我们使用参数 1，参数 2 设置活推断 reduce 个数时，需

要受这个参数限制，推断的 reduce 个数不能超过这个数的限制

Set hive.exec.reducers.max

## **Task 容错机制**

一个task任务有多个attmpt实例在跑

### **APPMaster 的内存和 cpu 参数**

set yarn.app.mapreduce.am.resource.mb=6144;

set yarn.app.mapreduce.am.resource.cpu-vcores=2;

这个参数一般会在集群的时候设置好

## **Hive 任务 Task 任务容错机制 **

### **Hive 任务****实例出现 failed/killed 的场景**

**Task type 与 Attemp Type **

关于Task，MapRecue/Hive 任务分成 maptask 和 reducetask

一个task允许尝试多次，那么每次运行的就是Task Attempt

也就是 yarn 任务 日志界面 Attempt Type 里统计的数据

所以就是为啥map/reduce 的实例都是 以 attmp_****开头的原因

因为任务的运行实例是 attemp。

一个task可以有多个**attmpt实例在跑**

### ** map/reduceTask 容错机制**

map/reduce task实例失败是正常的，可能因为机器老化，资源不足，进程崩溃，等等的问题造成失败

所以为了减少损失就有了一套容错机制

本质上来说就是，再map/reduce实例失败了之后，再推出之前向APPMaster 发送错误报告,这个错误报告就会记录到用户日志，APPMaster 然后将这个任务实例标记为 failed,将其 containner 资源释放

给其他任务使用

这也就是我们上面说的，再yarn里是APPMaster管理程序的运行成功与否，和rm没有关系

一般来说任务失败了之后APPMaster会进行重试，只要不超高=过4次成功就行，超过四次基本上整个任务就会失败！

那么这个失败次数能改么？

- [ ]

但是我认为还是保持默认就好

**APPmaster 失败后，已经在跑完的 task 并不会重跑，因为新的 **

**APPmaster 会通过作业历史来恢复失败的应用程序所运行的任务状态；**

### **failed场景**

首先出现最多的就是 attempt的超时

任务实例 attempt 长时间没有向 MRAPPMaster 报告

attempt 实例和MRAPPMaster 是每三秒通信一次 心跳时间，那么如果 MRAPPMaster 超过10分钟没有收到attempt 的任务 进度状态，那就会把这个任务标记为僵死状态 也就是失败

然后MRAPPMaster  会把它的jvm杀掉，释放资源，会尝试在其他的节点启动一个新的任务实例

mapreduce.task.timeout=600000   --ms，10分钟

任务attempt失败fialed的其他原因比较多，比如代码有问题，

outofmemory,GC，数据有问题，逻辑有问题，进程崩溃,通信超时等，生产中我

们常见需要处理的就是这个场景，需要具体问题具体排查；

### **任务任务实例出现Killed的场景**

一个任务实例 attempt 被 killed 一般就两种情况**，一是客户端主动请求杀死任务**

yarn application -kill applicationID

**二是框架主动杀死任务，既 APPMaster 发出任务 kill 的指令**。

比如 nodemanager 节点故障或者失败任务数

过多，比如停止等，这时候上面的所有任务实例都会被标记为 killed

推测执行

我们说task只要有一个attempt跑完就行了，如果发现有个任务跑的很慢的时候就启动多个实例去跑，然后那个跑成功了就算那个！然后其他的就kill掉

## **Hive 任务****推测执行参数优化**

reduce启动了多个实例，比如一个reduce task启动了多个实例并行在跑，那么我们要了解到什么时候reduce task 和 map task要启动多个实例去跑呢

多个实例去计算同一个实例，最终是采用哪一个呢 这个就是任务推测

**MRappMaster 当监控到一个任务实例的运行速度慢于其他任务实例时，会为该任务启动一个备份任务实例，让这个两个任务同时处理一份数据，**

**如map/reduce。谁先处理完，成功提交给 MRappMaster 就采用谁的，另一个则 会被 killed，这种方式可以有效防止那些长尾任务拖后腿。是为任务推测**

好处就是空间换时间

推测执行有利有弊，在一定程度上会造成资源的浪费！

- [ ]

### 任务计数器

这个是干什么的？

计数器时对运行 job 的数据统计收集，这个是动态的

什么时候用？

## 小文件治理

### 为什么要关注小文件的治理？

1.首先来说大数据开发就是小文件的治理者

2.资深大数据开发需要企业中参与数据治理，小文件治理是其中重要的组成

部分，大数据开发是小文件治理的参与者

3.资深大数据开发，技术专家往往需要具有大数据全局统筹的能力

### 什么是小文件？

在日常上的生产中，HDFS上生产小文件是一个非常正常的事情，常见的小文件比如jar包，xml配置文件，tmp临时文件。那么小文件的大头也就是主要来源呢，就是我们业务上的数据，因为集群参数设置不合理，实际上跑任务参数不合理啊，比如map reduce,把map reduce参数调的很多的时候，map任务个数很多，reduce任务个数很多，会产生大量的小文件。

### 那么小文件的大小定位是多少呢？

这个一般来说没有统一的定位，每个公司不一样，像我们公司的话8M就是小文件，还比如1m 8m 16m甚至更大

**根据公司实 际集群状态定义，因为有些情况合并小文件需要消耗额外的资源**

### 为什么要治理呢？

首先第一就是小文件是非常耗元数据的空间，hdfs存储的是块block,这些block会在集群中的datanode的本地文件系统上存储和复制

而且每个块也维护自己的blockmeta信息，而小文件呢非常耗元数据的空间，所以我们要治理

hdfs的存储分为两种

1.namenode元数据管理文件

2.实际的数据文件 block文件

所有的hdfs上的数据都被分为block，不管数据多大，哪怕小一点也是按照文件去存储，大的话就分为多个block

为什么说小文件多的时候会造成元数据的一个压力呢？

其实每个block都会维护一个block.meta的元数据信息，所以小文件多，很多的时候就会维护很多的block的meta信息，就会造成namenode压力很大，因为namedone的存储空间是有限的，比如namenode我们在生产上配一个256g ,我分配哦70%-80%给它，而且block.meta元数据信息是有大小的150kb左右，比如说有几亿个block.meta元数据信息，光存这个meta就要上百G的存储规模。

### 哪些途径会产生小文件？

1.流式数据，比如flume,kafak,sparkstreaming,storm,flink 等，这种流式增量文件，比如小窗口文件，几分钟一次

2.MapReduce引擎任务，比如存map任务大量的map，因为我们说纯map任务，map的个数就决定文件的个数，如果是mapreduce任务的话，reduce的个数就决定的文件的个数，大量的redcue就会造成大量的文件！

其实这两个都会造成大量的文件

比如分区表过度的分区，动态分区，这种很多分区的时候，那么每个分区里面，数据量就是很小，说严格点治理都没法治理，

3.spark 任务过度并行化，Spark 分区越多，写入的文件就越多。

4.文件的压缩与存储格式不合理；

**注意文件存储 **

**格式和压缩不合理只是加剧小文件问题，不是产生小文件的本质**

### 那么小文件不管行不行？如果不管有什么危害？

1.对namenode和datanode都有影响，而且小文件对计算机的性能浪费是比较严重的！，还拖慢任务的执行时长

#### 小文件对namenode的影响

**一个文件 192Mb，默认 blocksize=128Mb，副本个数为 3,存储为 2 个 block。**

为什么我们说blok数过多时候会造成 namenode压力很大的，因为namenode 的 namespace 中主要占存储对象是文件的目录个数

namenode里面存的就是对象！

文件（文 件名长度）以及文件 block 数

所以说我们一般不建议说把表的命名特别长，block数也不能特别多，目录数量也不能特别多

### 面试吹牛逼用

**从上面可以看出，同样的一个文件，大小不同形态的存储占用 namenode **

**的内存之比相差了 109 倍之多。所以如果对于单 namenode 的集群来说，大量 **

**的小文件的会占用大量的 namenode 堆内存空间，给集群的存储造成瓶颈**

## Hive小文件治理，从源头治理，参数优化！记住！！

1.**开启 map 前小文件合并，官方默认开启（Hive0.5.0）**

- [ ]

2.hive任务只有 两种情况会产出小文件，map任务，reduce任务

我们要判断什么文件是叫做小文件

**下面这个参数表示当一个 MR 作业的平均输出文件大小小于这个数字时，Hive 将启 动一个额外的 map-reduce 作业，分别针对 map-only/map-reduce 任务的 **

**比如这里设置 32Mb 当输出文件小于 32Mb 时我们进行合并。 **

- [ ]

### 小文件合并，小文件合并到多大合适呢？那么这个合并的大小怎么控制？

hive.merge.size.per.task=25600000;

这个参数就是作业结束时候合并文件的大小，但是这个一般是跟生产集群的block大小一致

## 小文件治理参数总结

1.第一步开启小文件的合并

- [ ]

2.第二步为要合并的小文件启动mr程序

- [ ]

但是对于第二步的参数来说

mapred.min.split.size.per.rack

mapred.min.split.size.per.node

mapred.min.split.size

这三个参数要大于等于hive.merge.smallfiles.avgsize 才会生效

- [ ]

### 对于小文件合并有什么好处么？

小文件合并对于namenode的影响可以减少，减少计算资源，节省资源的使用率

而且乐意降低表的总存储，对于列式存储表表现更好

合并小文件，成为一个比较大的文件之后，可以提高文件的压缩率，降低存储

但是我们要注意这个小文件合并，是按照文件的平均计算大小来看看是否满足小文件的阈值

**所 以会有输出文件大小小于小文件的值。**

## **并行执行优化以及适用场景**

HiveSQL会分为多个job/stage执行，但是默认的情况下，Hive一次只能执行一个阶段

但是有些特定的job肯呢个包含多个阶段，而且这些阶段也不是说一定是依赖在一起的，

所以这些阶段是可以并行执行的！

这就是并行执行！

### **但是并行执行等够有什么好处！**

如果有更多的阶段可以并行执行，那么 job 可能就越快完成。 也就是节省时间

但是这个并执行是有条件的，系统资源比较空闲才有优势，否则的话也并行不起来

而且并行开的太猛的话，也会造成一个任务占用过多的资源

### 并行执行有两个参数

set hive.exec.parallel=true; 开启并行执行参数，默认是false

这个就看任务的优先级，如果想要快速的跑完就开启

SET hive.exec.parallel.thread.number=8;

这个参数简单来说，就是任务有10个job，如果有8个job并行的话可以同时开启8个job

比如有20个job，16个同时并行，但是设置的是8最多也只有8个job并行

### 只能顺序执行的代码开启并行执行也不生效

Group by 有这个就牵扯到二次的分发和分布，必须要启一个完整的MR去执行

### 向量化执行-慎用

#### 向量化执行是什么东西？

简单来说向量化执行，在hive和mapreduce里我们说map函数每次都是按照行分隔符依次去读一行，然后一行在按照，列分隔符进行把数据进行切分，切分成kv键值对，最终把切分的数据合并然后分发给reduce去执行

但是吧这种模式可能会效率很低

我们能不能把一次处理一行的，变成一次处理多行的，比如一次处理个一万多行

所以向量化就是把一次处理一行变成一次处理数行，一次处理一个批次

而且向量化执行的文件存储格式必须是orc格式！！-这就是一个限制

为什么向量化可以提高效率？

因为向量化就是把传统处理一行的数据，变成开启一次处理1024行数据

也就是说 从一次处理一行变成一次处理一批了

但是吧这个向量化执行是有个坑的！

并不是所有的语法都支持的，所以这也就是为啥**向量化模式是默认关闭的**

- [ ]

这个参数表示是否开启向量模式，默认值为 false。

**若要使用向量化查询执行，必须将数据存储为 ORC 格式,本质就是一次读取一行，变 **

**成一次读取 1024 行处理。 **

**前 MapReduce 计算引擎只支持 Map 端的向量化执行模式**

**Tez 和 Spark 计算引擎可以支持 Map 和 Reduce 端的向量化执行模式**

因为有坑这个模式，我们的公司就把这个在集群层面给关掉了

这个坑比如：在简单的逻辑下还好，但是在全字段的 group by结果有重复的字段，会把空字符串转变为null

### **limit 限制调整**

**limit 是我挺喜欢用的，但是在使用Limit的时候，还是需要执行整个查询语句，然后再返回部分结果**

这就相当于又查了一遍

那么有没有办法限制一下呢，不让它再查询一遍呢？

- [ ]

这个参数可以，避免这种情况—可以直接对数据 ，源进行抽样，提高查询效率

但是我们集群是false，因为

**这种参数一般从集群层面配置。注意如果开启 limit 限制调整，由于是抽样，可能有用的数据永远不会被处理到**

## **分区与动态分区的参数**

- [ ]

### 动态分区的本质是什么？

**注意动态分区是基于查询字段的（个数）位置去推断分区的名称，所以动态 **

**分区的字段需要放到业务数据的后面**

举个例子

- [ ]

标红的字段就是分区字段，和partition(stat_day,user_name,db_name) 里的字段是对应的

这个动态分区不会说我去校验这个字段是不是正确的，它只会按照字段的位置进行推断，推断这个字段名称到底是啥

**查询的字段个数必须和目标的字段个数 相同，不能多，也不能少,否则会报错**也就是说动态分区就和函数里的形参有点类似

这个就是

- [ ]

a=1,b=1 这种是固定的

function（a） 中的a类似

动态分区是有弊端的：

1.可能会造成大量的小文件

**动态分区弊端可能造成大量文件和目录数，大量小文件，增加元数据压 力，其次不利于数据压缩合并，整体会增加数据存储**

## **Map-Join 系列企业优化实战**

### Common Join

Common Join就是普通的join

这个时候有两个表 X和 Y表进行一个join的时候，首先hive的执行引擎会把它转换成mapreduce任务去执行，

这两个表是完整的进行join，既有map也有reduce，map去做一个切分

每个表起了map，把x表和y表的数据进行一个切分，切分成kv键值对然后再reduce阶段，按照key，就是join key的值进行哈希，比如key是id，就按照id进行哈希，分发到不同的reduce上进行聚合

shuff过程是牵扯到键值对的排序和合并，在下落的过程中是非常耗性能的一点，就是排序和合并

那么在做shuff优化的时候，我们尽量在内存中去做排序和合并

那么像Majoin的目的就是为了减少Shuffle 和 Reducer 阶段的代价，仅仅在map阶段进行join

所以基本上所有的Mapper 都可以将数据保存在内存中并完成 Join。因此，所有 Join 操作都可以

在 Mapper 阶段完成。

### 但是虽然说可以这样做，如果数据量非常大的时候呢？

**当成千上万个 Mapper 同时从 HDFS 将小的连接表读入内存时，连接表很 容易成为性能瓶颈，导致 Mapper 在读取操作期间超时**



这就是传统的join，但是传统的join容易出数据倾斜的问题，如果一key特别多的时候，某些reduce处理的数据量会特别多

在0.7版本以后，其实已经把这个问题给解决了

在0.7以后，把小表以缓存的形式去实现的！

优化后的map-join 是在正常 join的时候 ，只有map的情况也要启一个MR，我们会在启MR任务之前，先启动一个本地任务，就是local模式

就是会启一个本地任务，本地任务会从hdfs上将小表读取出来到内存的hash表中，

然后本地任务把这个内存中的哈希表序列化成哈希文件，然后再把这个哈希文件上传到HDFS分布式缓存中

然后我们在启动MR的时候，分布式缓存会把文件，分发到每一个Mapper的本地磁盘上。

这样的话Mpa都可以将持久化的哈希表文件加载到内存，就能跑的很快

### 参数

- [ ]

左侧是原始的join

右侧就是自动化的，在编译期间，会生成一个包含任务列表的Conditional Task，在执行期间会运行一个，这个阶段是自动进行处理的。

并且在执行阶段，Conditional Task知道每个输入表的确切文件大小

如果两张表都太大，无法转换为Map Join 那么就要像以前一样运行Common Join

如果其中一个表很大而其他表足够小可以运行 Map Join， 则将 Conditional Task 选择相应 Map Join 本地任务来运行。通过这种机制， 可以自动和动态地将 Common Join 转换为 Map Join。

### 注意

小表的总大小大于25MB，就会选择**原始 Common Join 来运行，但是这个25可以修改**

- [ ]

### Map Join

Map Join 的目的是减少 Shuffle 和 Reducer 阶段的代价，并仅在 Map 阶 段进行 Join

首先所有的mapjoin肯定可以用Common Join去实现的

mapjoin只是Common Join的一个优化， 也可以理解为mapjoin只是Common Join的一个特定场景的一个使用

#### 那么什么样的Common Join可以优化成Map Join

比如有一张表，它足够小的时候可以装进内存的时候，我们就在内存中进行一个join

那么所有的join只在map阶段完成了，就拒绝reduce阶段的一个shuff

这种map join会出现一个问题！！

如果有几千个map去并行的时候，如果资源很充足，这些map会同时去hdfs读这个小表，那么可能出现性能瓶颈!

这个问题子啊hive 0.7以前的问题

在0.7以后得版本已经解决了

优化后的map join,会在正常启动mr之前，先启动一个本地任务，就是用的本地模式

那么这个本地任务干嘛呢！本地任务会将小表从hdfs上读取到内存的哈希表中！

然后将内存中的哈希表序列化为哈希表文件

在下一阶段，当 MapReduce 任务启动时，会将这个哈希表文件上传到 Hadoop 分布式缓存中

然后启动mr任务的时候，分布式huancu分到每个map所在的本地磁盘上，这样的所有的map就可以将持久化的哈希表文件，就是我已经分发到本地磁盘上了，你不用再去拉去数据量，你启动一个map我给你分发一个，在分布式缓存里面，你在往每个机子上分发就会很快，然后每个map再跑的时候再将持久化的哈希表加载到内存里面，再像之前进行join

### mapjoin使用

在hive 0.7以后

hive.0.7.x 以后实现 mapjoin 的自动推断，通过自动将 Common Join 转换 为 Map Join 来解决此问题

## GROUP BY

这个在sql里干啥啥？

1.分组去重

2.在分组的时候，对非分组的字段进行一个去重，聚合统计

## Hive代码层面企业优化案例-未完

### **Hive-SQL 的执行顺序**

**执行流程**

先是从From中读原表，

- [ ]

我们知道整个hive的执行是一个mapreduce

mapreduce又分成两个模块，一个是map，一个就是reduce，如果是hive-on-mr模式就是两个  一个是map 另外一个就是reduce

### HIIE SQL执行流程

hive的执行流程分为了两个部分，MAP 和 reduce这两个阶段

在Mapper阶段 首先进行FROM进行表的SCAN查找和加载

然后就会惊醒where的操作，因为Hive是对语句进行了优化，如果符合谓词下推就进行下推

然后的话就进行join 按照join-key进行shuff数据

Reduce

shuff完成之后的话就进行reduce端执行

这个时候进行on 如果on里面有飞等值的过滤表达式，就会在join关联前进行过滤on里面的谓词

最后才是group by hiving orderby 这些

**两个表 join，把过滤条件写到 on 里和写到 where 里有区别吗？如有区 **

**别什么场景有区别？区别在哪？ **

首先来说mysql和hive是不一样的

mysql的话把条件写到on where里会造成一个数据的缺失，会把数据重新过滤掉，就是主表已经补齐的数据

在on where再过滤掉

但是在hive里面过滤条件就不一样了，优势后并不是简单的把数据过滤掉，反而是会得到一些意想不到的结果，因为hive的执行流程和mysql的执行流程是完全不一样的，底层的执行原理是不一样的！

### **过滤条件放到 on 和 where 区别？**

#### **Inner join 时，放到 on 和 where 里的区别？**

没啥区别 其实都是可以的？

#### **LEFT JOIN ？**

**单独针对左表的过滤条件必须放在 WHERE 上**

**放在 ON 上 的效果是不可预期的，在查看执行计划的时候，放在on上的时候是在reduce阶段执行的**

#### Right **JOIN**

针对右表的话，放在on上是先过滤右表，在和左表关联，

放在where上则是先关联表在进行过滤

## **Hive SQL 优化思路**

### Sql过滤模式优化

从过滤的粒度上来看，主要就是分为，行过滤，数据列过滤，文件过滤和目录过滤

在语法的体现就是WHERE HAVING DISTINT语句上

#### 分区|目录过滤|裁剪

第一点为什么要做分区表？

做分区的本质就是减少数据量，避免进行全表扫描

因为分区在hdfs的体现就是，一个文件夹，就是一个目录我们按照分区进行分割目录，需要那个分区数据的时候

我直接去那个分区读数据。

分区过滤的条件我们是写在WHERE里

但是这里需要注意的就是，分区过滤是在表扫描阶段就完成了的，分区过滤是发生在map之前的，相当于直接指定路径读取文件的

而其他的where是在map阶段阶段过滤的，是通过maptask实现一行行过滤！

map分区的过滤和其他的过滤条件的过滤执行顺序是有区别的

一个是读文件的时候就过滤

一个是切分文件读文件的时候过滤

分区裁剪的使用

就是保证使用的分区要生效

那么什么情况下使用的分区不生效呢！

## **分区裁剪放到 on 里和 where 的情况**

分区在hive里本身也是一个字段，所以我们在使用分区表的时候，分区没有生效的话，那可造成全表扫描的这种严重后果

### **inner join  分区裁剪**

把分区条件放到where中实现了分区裁剪

where t1.day='20230223' and t2.day='20230219' and length(trim(t2.device)) >0

同样的放到on里也是可以实现的！

### **left/rightjoin 时分区裁剪放到 on/where**

left join，主表的分区裁剪条件放到where中生效

但是从表的分区裁剪条件放到where并没有生效

从表进行了全表的扫描，从表的分区裁剪是在join之后的在reduce阶段最后进行过滤的

on t1.device=t2.device and t1.day='20221231' and t2.day='20221231'



left join，分区裁剪条件放到，on里的时候实现了分区裁剪，但是主表没有实现分区裁剪，而是进行了全表的扫描，同样在reduce阶段，join时过滤

正好相反

### full **join 时分区裁剪放到 on/where **

**特别注意：fulljoin 时分区裁剪条件放到 on、where 里都不会实现分区裁剪，而是全表扫 **

**描**

full **join 时直接使用子查询得了**

join类型

分区裁剪的放置位置

分区裁剪的效果

普通join

**两个表分区裁剪放到到 on 里**

**主表，从表的分区裁剪均生效**

**两个表分区裁剪放到到 where里**

**主表，从表的分区裁剪均生效**

**Left join **

**两个表分区裁剪放到到 on 里**

**主表不生效，****从表生效 **

**两个表分区裁剪放到到 where里**

**主表生效，****从表不生效**

**Right join **

和 left join相反

**两个表分区裁剪放到到 on 里**

**主表生效，****从表不生效**

**两个表分区裁剪放到到 where里**

**主表不生效，****从表生效 **

**Full join **

**两个表分区裁剪放到到 on和where 里 **

**主表从表都不生效**

总体来说：

Inner jioin 放到on和where里 都会生效的

Full join放到哪里都不会生效

Left join 在 on里 从表生效 主表不生效 在where里 主表生效 从表不生效

Right join 和left正好相反

## 谓词下推

谓词就是条件表达式，类似于where 里的表达式 ，就是返回布尔的值，true和false

SQL中的谓词主要有

LKIE、BETWEEN、IS NULL、IS NOT NULL、IN、EXISTS 其结果为布尔值

所以谓词的使用场景就是过滤语句中：在 SELECT 语句的 WHERE 子句或

HAVING 子句中，确定哪些行与特定查询相关。

**hive.optimize.ppd 默认为 true，即开启谓词下推 这个就是开启谓词下推的参数**

**就是 **

**在不影响结果的情况下，尽量将过滤条件提前执行。谓词下推后，过滤条 **

**件在 map 端执行，减少了 map 端的输出，降低了数据在集群上传输的 **

**量，节约了集群的资源，也提升了任务的性能**

## **Count(1),count(*),count(cloumn)的区别？**

我在计数的时候反正是这三个都用过，也都正常的出了结果！还真没想过有啥区别！！

count（（列））：这个的话就是有空值不会被计数

**count(*)：不会出现count(cloumn)的问题，也就是不会出现空值不计入**

count(1):这个就是时代的产物，hive0.6以前支持

## Order by全局排序优化

全局排序会把所有的数据分发到一个reduce里进行执行，如果数据量大的时候是真的跑不出来

Reduce 个数决定问价的个数

## 连接模式join相关优化

hive 支持的join方式有inner join 和 outer join

JOIN类型分为 无shuffle的join,有shuffle的jion

### 无shuffle的join优化

1.普通的mapjoin :其实mapjoin本质就是解决小表join大表的场景

2.SMB 也叫 smb-join 这个是桶表的主要使用方式

特殊的Bucket-Mapjoin 在这个基础上 Bucket-Mapjoin 在大表join其实已经被SMB给提带了

Join key= sort(key) = clusterby(key)

优点就是针对于大表的join优化方案 使用SMB实现

3.Skewd-MapJoin

这个只针对于特殊场景的innerjoin生效

而且这个innerjoin 有数据倾斜 但是可以通过参数开启数据倾斜的处理

### 有shuffle join

问题：在数据倾斜这里，讲了一个把reduce key给打散了，如果是join 就把join key打散

这我没明白‘key给打散’这句话

## 面试吹牛逼-为什么需要分区分桶？ 什么场景下使用！

分桶的桶数等于文件数量

什么时候用分桶表：其实并不是说出现了数据倾斜我们才用分桶表，而是大表join大表的时候，key分布均匀

单纯的就是因为数据量很大的时候 ，每个reduce处理的数据量很大是所有的reduce都很慢，这个时候我们就可以考虑分桶，分桶分桶 分而治之

## 面试吹牛逼-什么时候使用SMB-Join

面对两表 大表join大表，key值分布也均衡，单纯的就是reduce慢 数据量太大了

set mapreduce.job.queuename=root.paas_test ;

**set hive.optimize.bucketmapjoin = true;  **

**set hive.auto.convert.sortmerge.join=true; **

**set hive.optimize.bucketmapjoin.sortedmerge = true;  **

**set hive.input.format=org.apache.hadoop.hive.ql.io.BucketizedHiveInputFormat;  **

set hive.mapjoin.smalltable.filesize= 100000000;

set hive.auto.convert.join=true;

### 案例

121页

## 数据倾斜
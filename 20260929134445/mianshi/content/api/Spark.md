**数据计算的方式 ：批处理 流处理**

### 批处理

这个是针对大规模的数据的批量处理

数据计算的方式：批处理

批处理主要是解决大规模数据的批量处理

特点就是：有界，持久，大量

有界：批处理数据集代表数据的有限集合

持久：数据通常是持久存储的

大量：批处理操作通常是处理海量数据集的唯一方法

### 流处理

流处理指的是时间分布和数量上无限的一系列**动态数据集合体**，数据的价值随着时间的流逝而降低

所以要提供一个秒级的处理

### 内存计算

Spark 是基于内存计算的

mr是基于磁盘计算的

为什么磁盘计算比内存计算快

### 什么是spark:

用于大规模数据分析的统一引擎，它支持批/流处理，支持纯 SQL 开发等。

#### 特点：

简单，速度快，通用，兼容好

### spark生态体系

主要来说分为上中下三层

上层：Spark SQL、Spark Streaming、MLlib、GraphX

#### Spark SQL：

#### Spark Streaming：

SparkStreaming是SparkCode的扩展应用，然后就是有可扩展，高吞吐等特点

监控来自Kafka,Flume,HDFS。Kinesis,Twitter， ZeroMQ 或者 Scoket 套接字的数据通过复杂的算法以及一系列的计算分析数据

#### MLlib：

spark.mllib 是基于 RDD 的原始算法 API，目前处于维护状态

这个是最初提供的一个机器学习库

但是这个库有一个明显的缺点，如果面对复杂的数据集，是需要做多次处理

#### GraphX：

这个是一个分布式图处理框架，他是基于Spark平台提供对图计算和和图挖掘简洁易用的而丰富的接口

中层：

#### Spark Core

Spark Core 是 Spark 的核心与基础，实现了 Spark 的基本功能包含任务调度，内存管理，错误恢复与存储系统交互等模块

下层：

#### spark 的部署模式

5种部署模式

#### 最底层：存储系统

Spark 提供多存储系统的接口，比如HDFS、AmazonS3、HBase等

Spark和Hadoop 的结合使用在企业中目前使用是最广泛的一套“存-算”解决方案

#### spark集群架构

Spark的框架核心是一个计算引擎，从上面的图里可以很清楚的看到，Spark是一个典型的master-slave主从架构

对于standalone独立部署模式下，Driver和Executor是负责计算这块

Master和Worker是负责资源调度

ApplicationMaster是负责协调资源和计算

图的入口是sparkContext(spark上下文)，但是sparkContext(spark上下文)是包裹在DriverProgram(驱动程序里)

DriverProgram(驱动程序)指向Executor,Executor是整个资源的汇集地，

Executor里面包含Cash和Task

Executor是有Worker Node1 2 3的 所以这就是一个集群的结构

这个集群是被Cluster Manage管理着的

并且Spark是一个典型的 master-slave主从架构，像核心的组件有Driver 和 Executor、Master 和 Worker、ApplicationMaster

#### 组件介绍

Master：Master 是一个进程，负责资源的调度和分配，并对集群进行监控，类似于 YARN模式下的 ResourceManager。（ResourceManager（rm）：负责集群所有资源的监控、分配和管理。）

Worker：Woker 是 Spark 集群中的一台具体的机器，由Master分配资源对数据进行并行的处理和计算，有点类似 YARN 模式下的 NodeManager（NodeManager（nm）：负责单个节点的维护，一个集群有多个）

并且一台 Worker 机器会运行很多 Executor，每一个 Executor 都是一个 JVM 进程，这些进程才是 Spark 真正进行计算的地方，而每个 Executor 的内部又会有很多的 Task，而每个 Task 都是一个线程，提高整个计算的并行度。

Driver：这个是用来创建Spark上下文对象环境的应用程序，Driver 用于执行 spark 任务中的 main 方法

Driver 在 Spark 作业执行时主要负责：

>

>

>

>

Executor：是worker的一个jvm进程，主要是负责Spark作业中运行具体的任务TASK，但是各个的task是相互独立的

Executor是伴随整个Spark整个应用的生命周期而存在的。

Executor出错的话就把这个节点任务放到别的Executor上

Executor核心功能：

1.负责运行组成 Spark 应用的任务，然后返回给驱动器

2.RDD 是直接缓存在 Executor 进程内的

ApplicationMaster：ResourceManager（资源）和 Driver（计算）之间的解耦合靠的就是 ApplicationMaster。

#### Spark on yarn 架构☆☆

##### Client模式

步骤

1.spark-submit提交Spark Job之后，会在提交的本地机器上启动一个对应的Driver

2.Driver启动之后就会和ResourceManager建立通讯并同时发起启动ApplicationMasterqi

3.ResourceManage收到这个job之后，就会再集群中选一个NodeManager,同时分配一个Container，以及启动ApplicationMaster（初始化 SparkContext）

4.ApplicationMaster这个功能是负向 ResourceManager申请 Container 资源； ResourceManage 便会与 NodeManager 通信，并启动Container；

5.ApplicationMaster对指定NodeManager分配的Container发出启动Executor 进程请求

6.Executor 进程启动后会向 Driver 反向注册，Executor 全部注册完成后 Driver 开始执行执行 Job 任务

7.Driver 中的 SparkContext 分配 Task 给 Executor 执行，Executor 运行 Task 并向

Driver 汇报运行的状态、进度、以及最终的计算结果；

8.应用程序运行完成后，ApplicationMaster 向ResourceManager 申请注销并关闭自己。

##### cluster 模式

1.再YARN Cluster 模式下Spark 任务提交之后会与 ResourceManager 建立通讯，同时发出申请启动 ApplicationMaster 请求

2.然后ResourceManage收到spark发送的这个job时候，就会再集群了选一个合适的NodeManager,然后再分配一个Container,同时还会再Container里启动ApplicationMaster,然后就是角色互换了，这个时候ApplicationMaster 就是

Driver

3.那么ApplicationMaster启动之后会向ResourceManager申请资源，ResourceManager接到ApplicationMaster的资源之后会在合适的NodeManager中分配Container

4.ApplicationMaster会对NodeManager分配的Container发出启动Exector进程请求

5.Executor 进程启动后会向 Driver 反向注册，Executor 全部注册完成后 Driver 开始执

行执行 Job 任务；

6.ApplicationMaster 中的 SparkContext 分配 Task 给 Executor 执行，Executor 运行

Task 并向 ApplicationMaster 汇报运行的状态、进度、以及最终的计算结果；

7.应用程序运行完成后，ApplicationMaster 向 ResourceManager 申请注销并关闭自己

##### Yarn Client 与 Yarn Cluster

1.Driver创建的位置不一样

Client 方式是直接在本地机器上创建一个 Driver 进程

Cluster 方式在通过 ResourceManager 在某一个 NodeManager中创建一个 Driver。

2.使用场景

Yarn Client 方式一般适用于进行 Job 的调试（Debug）

Yarn Cluster 方式一般适用于生产环境

两种部署模式

1.整个yarn调度流程

2.Driver生成的位置

3.说出两种模式的优缺点

Executor：

spark安装流程

1.在linux中找到spark的tag包

2.tar -zxvf spark-....  进行解压

#### **三个开发入门类**

###### **SparkConf**

SparkConf 是 Spark 的配置类，基本上Spark中的每一个组件都是直接或者间接地使用着它所存储的属性

###### **SparkContext**

这个就是一个上下文，通过SparkContext就能打入到Spark的内部，所以**SparkContext非常重要，只要创建spark任务都会直接或者间接的创建一个SparkContext**

SparkContext 是通往 Spark 集群的唯一入口

SparkContext 的核心作用是初始化，像高层调度器，底层调度器，调度器的通信终端等

但是SparkContext实例只能有一个在JVM内存中，就是排他行为

###### **SparkSession**

这是一个切入点来使用spark各项功能，也允许用户通过它调用DataFrame和Dataset相关 API 来编写 Spark 程序

区别：

1.位置上parkConf 和 SparkContext 是位于org.apache.spark 包下，是一个通用的包

SparkSession 位于 org.apache.spark.sql 包下

#### spark-submit 工具

spark-submit 是什么？

spark-submit 他是 spark 安装目录中 bin 目录下的一个 shell 脚本文件

作用就是：在集群中启动应用程序（如*.jar、*.py 脚本等）

常见参数

--master

该参数表示提交任务到哪里执行

>

>

>

>

>

>

>

 --deploy-mode

spark on yarn 的启动方式

分别是 spark 的 driver 是在本地 (client) 启动还是在 yarn的 container 中启动，默认是 client

 --class

应用程序的主类，仅针对 java 或 scala 应用

 --name

指定应用程序的名称

在 yarn 调度系统下，只对 cluster 模式生效

 --jar

设置后，这些 jar 将包含在 driver 和 executor 的 classpath下

 --conf prop=value

指定 spark 配置属性的值

格式为 PROP=VALUE

 例如 --conf spark.executor.extraJavaOptions=“XX:MaxPermSize=256m”

--properties-file

指定需要额外加载的配置文件

用逗号分隔，如果不指定，默认为 conf/spark-defaults.conf

--driver-memory 和--driver-core

前者表示 driver 内存，默认 1G

后者表示 driver 的核数，默认是 1

在 yarn 或者standalone 下使用

**spark-submit 工具的使用及常见的参数**

**spark-submit是什么？**

--master 重点掌握  local三个要掌握 yarn

--num-executors

executors是一个jvm进程，它里面的task，是真正运行任务的，task是线程，线程是包裹在进程当中的

如果任务执行的比较慢，增大executors的数量，增大并行，就可以增加他运行的速度（优化点）

### Rdd

1.全称叫什么

RDD 是 Spark 提供的核心抽象，是 Resillient Distributed  Dataset，即弹性分布式数据集。所以名字中就包含了 RDD 的所有的特征：弹性、分布式、数据 集

##### 重点弹性区间

弹性区间背下来

---

rdd并不存储数据，只是存储元数据

rdd本质上就是各个分区合并的一个数据集

弹性的意思就是说，RDD的数据默认情况下是放到内存中的，但是内存不足就会写入到磁盘，就像rdd搬家，突然发现它的屋子小了东西放不下了，突然和对面舍友说，你帮我存存呗，这就是弹性

###### 但是弹性也是分情况的

>

>

**什么是Lineage？**

Lineage 是 RDD 维护的一系列确定性转换记录，它记住了 RDD 是如何从其他 RDD（或稳定存储的数据）演变而来的。本质上是一个DAG有向无环图

>

>

>

但是同样spark也是有分布式的可以借助集群提供的统一资源，大大增加了自己的计算能力

 RDD 本质上就是各个分区合并的数据集，类似 HDFS 的磁盘分片，但是spark只是内存分片。

---

同样rdd是一个抽象类，还是可以序列化的，因为它要发往其他的机器上进行计算，所以必须是要可以序列化的

涉及到 RDD 相关的数据结构都是要可序列化

#### **RDD 的核心属性☆☆**

##### 五元组

一个spark的数据集可能会很大，以hdfs上来说,假如分4个block，每个block都相当于起了一个分区，从每个block里去读

在相对应的spark中就会出现4个分区函数，

那么从block到spark的分区过程就是read过程

做了分区函数之后又做了一个map函数，然后进行重分区，4个分区变成两个分区

Spark rdd在每一步，在最终的结果之前，他每一步都会生成一个新的rdd

那么这5个属性，第一个属性分区列表，这个数据集，需要知道分布在那些分区上面吧

第二个，每一个分区，我需要实现什么样的操作能到下一个分区，这个过程是有一个计算的操作，比如实现一个computer，那么这个分区，计算父分区如何到子分区，在合并前一个分区是子分区，再往前一个阶段时父分区

分区器：我这个数据是如何到下一个分区的，这种一般是在产生shuff的时候 ，分区数据这些数据，合在一块给它打乱，打乱之后的数据网线一个分区，哪一个会跑，这个时候就会涉及一个分区器

第四个依赖关系，每一个子rdd,它的上游依赖到哪些父rdd，这样的好处，就是当前的rdd，一旦出现错误可以通过父rdd重新生成子rdd

**五元组是怎么工作的**

这五元组其实也是弹性的一种体现经常取第一 个元素或者遍历。简记：获取每个rdd的依赖，即血缘

protecteddefgetDependencies:Seq[Dependency[_]] -也就是依赖列表

然后的话分区列表定义在一个数组中，这里使用Array的原因是随时使用下标来访问 分区内容。计算分区信息，只会被调用一次，简记：获取分区信息

protecteddefgetPartitions:Array[Partition] - 分区

接口定义，具体由子类实现，对输入的RDD分区进行计算，将某个分区的数 据读成一个Iterator。简记：获取分区信息之后对每个分区进行子计算

defcompute(split:Partition,context:TaskContext): Iterator[T]

分区器，可选，子类可以重写以指定新的分区方式，Spark支持Hash和Range 两种分区方式

@transientvalpartitioner:Option[Partitioner]=None

可选，每个partition数据驻留在集群中的位置，子类可以指定分区的位置如HadoopRDD可以重写此方法，让分区尽可能与数据在相同的节点上

protecteddefgetPreferredLocations(split:Partition):Seq[String]=Nil

这里

#### RDD分区和并行度

job:这个就是提交给spark的任务，一个Action算子就是属于一个job

Stage:  stage是每一个job处理过程要分几次任务，Stage就是看是否发生shuff，即使看有没有产生宽窄依赖

task:这个是一个job处理过程要分几次任务，task是任务运行的最小单位，一个stage要处理的partition对应一个task并且task在executor是进程里面的一个进程

stage的task是谁来决定的？

是由输入文件的切片个数决定的，一个分区对应着一个task

一个job任务的task是由谁来决定的？

job里面可以有一个或者多个stage但是stage又可以有多个task所以数量就是（stage 数量 * task 数量）的总和。

**关系：**

包含关系Job ⊃ Stage ⊃ Task（Job 包含 Stage，Stage 包含 Task）

- [ ]

**一个stage的task数量是由谁来决定的？**

结论：这里的task是由分区数量来决定的

首先是由输入文件的切片个数来决定的：

这里的切片不是mr的map，走的是指 Hadoop 的 InputSplit（输入切片）。

在 Spark 读取 HDFS 文件时，分区（Partition）的生成逻辑继承了 Hadoop 的切片机制

- [ ]

通过算子修改了某一个rdd的分区数量，task数量也会 同步修改

这里就是如果算子修改了分区数量，task也会同步修改，主要明确一个传导作用

**一个job任务的task数量是由谁来决定的？**

一个job任务可以有一个或多个stage，一个stage又可以有一个或多个task。所以一个job 的task 数量是 （stage数量 *task数量）的总和。

**每一个stage中的task最大并行度**

什么是并行度？

并行度是值得指令并行执行的最大条数。

理论上每一个stage下有多少个分区，就有多少个task，task的数据就是任务的最大并行度，因为一般情况下一个task运行的时候使用一个cores

**如果task数量超过这个cores的总数怎么办**

先执行core个数量的task，然后等待cpu资源空闲后，继续执行剩下的task

100个Task → 调度器 → 先启动80个（占满core） → 剩余20个在Pending队列

                ↓

         任意Task完成 → Core释放 → 从队列取新Task执行

那么这里其实可以配

动态资源分配

- [ ]

还有一种就是超额配置，即使只有80个逻辑核，可以配置100个core"

Spark官方建议：`spark.executor.cores` 不超过物理逻辑核数，通常留1-2核给OS（如8核机器配6-7核）

##### 分区和并行度的关系

什么是分区？

分区是一个相对静态的概念，初始大小是由数据源的分布情况决定

分两种情况：1.内存数据，分区数和设置的并行度是一致的 如果读取hdfs，，有10个block块，那么分区数就是10

什么是并行度？

这个就是一个相对概念，这个是根据当前的计算引擎可用的资源来决定的，但是最小值是小于等于分区数的

#### RDD算子

算子是方法，算子分为转换算子（Transformation）和行动算子（Action算子）

Transformation：这个会针对已有的RDD创建一个新的Rdd，特点是lazy特性

Action是对RDD进行最后的操作也可以称为触发操作，像遍历，reduce等

##### Transformation

###### map

map 是对 RDD 中的每个元素都执行一个指定函数来产生一个新的 RDD

- [ ]

###### mapPartitions

mapPartitions的输入函数应用于每个分区，也就是把每个分区中的内容作为整体来处理的

但是mapPartitions因为是对整个分区做处理可能会造成内存溢出

####### map 和 mapPartitions 的区别

>

>

>

>

>

>

>

###### mapPartitionsWithIndex

### RDD 中的 DAG 及宽窄依赖

##### DAG☆☆☆

DAG是有向无环图，这是执行计划的核心概念

代表的是spark应用程序中的一系列操作步骤和它们之间的依赖关系

DAG 是一组顶点与边的组合，顶点代表 RDD，边代表对 RDD 的一系列操作

1.逻辑 DAG

描述了应用程序中的转换操作和它们之间的依赖关系，而不考虑具体的执行计划和物理执行细节

2.物理 DAG

那么这个就和逻辑相反了，描述了 Spark 应用程序的实际执行计划

3.DAG为什么要出现？

DAG 的出现主要是为了解决 MapReduce 框架的局限性

4.MapReduce 框架的局限性

每个 MapReduce 操作都是独立的，hadoop 框架也不知道接下来会有哪些MapReduce

每一步的输出结果，都会持久化到硬盘或者 HDFS 上。

#### 宽依赖和窄依赖

它会根据 RDD 之间的依赖关系来划分不同的阶段（Stage），而一个Stage 则包含一系列执行任务（TaskSet）

>

>

>

>

**主要判断条件是：父 RDD 的 Partition 流向，要是流向单个 RDD 就是窄依赖，流向多个 RDD 就是宽依赖**

**父 RDD                子 RDD 其实是在一个分区内操作就是窄依赖对吧，所以只要是没有shuff的操作就都是窄依赖**

>

>

>

同样在spark中task只有这两种类型要么是ResultTask，要么是ShuffleMapTask

其实ShuffleMapTask的计算结果需要shuffle到下一个Stage中，本质上相当于MapReduce中的 Mapper

ResultTask 则相当于 MapReduce 中的 reducer

在上图中，整个过程是根据数据依赖关系自后向前的建立，遇到宽依赖就形成Stage，那么宽依赖也就是父RDD的分区会被子RDD的多个分区使用所以图中的stage1 和 stage2就是这样体现的

stage1 和 stage2相当于 MapReduce 中的 Mapper

ResultTask 所代表的 stage3 就相当于 MapReduce 中的 Reducer

####  RDD 依赖之间的 shuffle☆☆☆

1.为什么要排序？

>

>

>

>

>

#### 为什么要文件合并（combine）

>

>

>

总的来说:减少系统去管理小文件所需要的开销

####  spark shuffle

Shuffle 的本意是洗牌、混洗的意思，把一组有规则的数据尽量打乱成无规则的数据

进行数据处理时，需要将数据重新分配到不同的节点上进行处理，从而引发了数据重组的过程。那

么我们再说什么是 shuffle？其实就是将需要的数据揉合在一起，然后按照某一种规则重新发往下游

那么在mapreduce中
Shuffle 更像是洗牌的逆过程，指的是将 map 端的无规则输出按

指定的规则“打乱”成具有一定规则的数据，以便 reduce 端接收处理

spark 的 shuffle 是在 MapReduce shuffle 基础上进行的调优。其实就是对排序、合并逻辑做了一些优化

在 spark 中 shuffle write 相当于 MapReduce 的 map，shuffle read 相当于MapReduce 的 reduce。

##### spark shuffle 分 4 种

###### 未经优化的 HashShuffleManager

比 MapReduce，排序不见了，文件合并不见了

从上面的图可以分为上半部分Shuffle Write 端（Map 端）4 个上游 Task，分布在 2 个 Executor 上

下半部分Shuffle Read 端（Reduce 端） 3 个下游 Task，负责拉取数据

上半部分：Shuffle Write

左边的 Executor（1 cpu core）：

task（上游任务）

  │

  ▼

Buffer 内存（内存缓冲区）

  │

  ├→ buffer → block file  （给下游 reduce task 0 的数据）

  ├→ buffer → block file  （给下游 reduce task 1 的数据）

  └→ buffer → block file  （给下游 reduce task 2 的数据）

每个上游 Task 的工作流程：

Task 处理数据：对每条数据计算 hash，确定它应该发给哪个下游分区

写入 Buffer：按下游分区数（3个），在内存中开辟 3 个 buffer（bucket）

刷写 block file：每个 buffer 满了就刷写到磁盘，生成一个 block file

⚡ 关键点：每个上游 Task 会为每个下游分区生成 1 个文件

下半部分：Shuffle Read 过程

下游 reduce task 0（青色）

  ← 从上游 task 0 拉取属于自己的 block file

  ← 从上游 task 1 拉取属于自己的 block file

  ← 从上游 task 2 拉取属于自己的 block file

  ← 从上游 task 3 拉取属于自己的 block file

每个下游 Task 通过 buffer 从所有上游 Task 那里拉取属于自己分区的 block file，读入 reduce memory 进行聚合计算。

图中的交叉连线就表示：每个下游 task 都要从所有上游 task 那里拉数据。

>

>

>

>

###### 优化的 HashShuffleManager

>

>

>

>

###### SortShuffleManager

>

>

>

######  SortShuffle 优化之 bypass 运行机制

这个相比与SortShuffleManager 少了排序的步骤

这个和未经优化的HashShuffleManager的区别？

1.其实机制都是一样的，都要创建数量惊人的文件，但是SortShuffle 优化之 bypass 运行机制 这里会进行最终的一个文件合并 所以shuffle read的性能可能会好点

###  RDD 持久化☆☆

#### RDD 数据持久化/缓存

数据持久化也称为缓存，在多个操作间都可以访问这些持久化的数据

但是缓存是针对某个 RDD 或者说是某个 Transformation 算子的结果

缓存的目的是 action 操作计算速度加快

RDD 可以使用 persist() 方法或 cache() 方法进行持久化

如果一个缓存的 RDD 的某个分区丢失了，Spark 将按照原来的计算过程，自动重新计算并进行缓存

缓存有可能丢失，或者存储于内存的数据由于内存不足而被删除

RDD缓存容错机制，RDD 的各个 Partition 是相对独立的，因此只需要计算丢失的部分即可， 并不需要重算全部 Partition

####  cache 和 persist

这俩既不是transformation算子也不是action算子

因为他俩没有生成新的RDD算子，只是标记了当前RDD需要cache或者persist

cache 和 persist 是 lazy 的，当第一次遇到 Action 算子的时侯才会进行缓存或持久化，以后再触发 Action 会读取、复用缓存的 RDD 的数据再进行操作

cache 和 persist的关系：

 cache 底层调用了 persist 方法：

- [ ]

这就涉及到了储存级别

- [ ]

我们单独的来看

>

>

>

>

同 MEMORY_ONLY区别是，会将 RDD 中的数据进行序列化，RDD的每个 partition 会被序列化成一个字节数组

好处就是节省内存

同 MEMORY_AND_DISK会将 RDD 中的数据进行序列化，RDD 的每个 partition 会被序列化成一个字节数组

>

>

>

>

8.推荐使用持久化级别顺序：

MEMORY_ONLY ----> MEMORY_ONLY_SER ----> MEMORY_AND_DISK_SER ----> MEMORY_AND_DISK

这个要看下视频

#### RDD CheckPoint（检查点）

通过将 RDD 中间结果写入磁盘

由于血缘依赖过长会造成容错成本过高，这样就不如在中间阶段做检查点容错

如果检查点之后有节点出现问题，可以从检查点开始重做血缘，减少了开销

#### cache 和 checkpoint区别

>

>

>

>

>

### RDD分区器

什么是分区器：

分区器决定了数据按什么规则分配到哪个分区。

Spark分区器描述的是RDD的数据在各个分区之间的分布规则，比如上游数据shuffle到下游时， 分区器就决定了上游的哪些数据需要进入下游对应的哪些分区

但只有kv类型的rdd才有分区器 比如map keyby groupby

分区器种类

HashPartitioner（哈希分区 器）和RangePartitioner（范围分区器）

Shuffle 和分区器之间的关系是：Shuffle操作执行后，根据分区器的规则，将shuffle后的数据 分配到新的分区

#### HashPartitioner

这个就是字面意思采用了hash的方式对键值对数据进行分区。数据分区的规则为：partitionId= Key.hashCode % numPartitions

这个图两部分一个是2个分区，一个是三个分区

规则是partitionId= Key.hashCode % numPartitions

对于整数的key,Key.hashCode = key

所以2个分区就是

key=1 → 1 % 2 = 1 → 分区1

key=2 → 2 % 2 = 0 → 分区0

key=3 → 3 % 2 = 1 → 分区1

key=4 → 4 % 2 = 0 → 分区0

分区 0        (2,b)(2,d)(4,e)(4,f)(4,g)(4,h)(4,c)(4,a)        8 个

分区 1        (1,a)(3,c) 2个

同样3个的也是这样计算的

但是这里就能看到被分到同一个分区的特别多，也就是倾斜

HashPartitioner 用 `key % 分区数` 来分配数据，简单高效，但当某个 key 的数据量特别大时，会导致数据倾斜，增加分区数也解决不了。

#### RangePartitioner

哪这个的目的显而易见就是为了解决HashPartitioner 带来的分区倾斜的问题

RangePartitioner是基于抽样的思想来对数据进行分区，就是将一定范围内的数据映射到某一个分区内

实现步骤：

(1,a) (2,b) (3,c) (2,d) (4,e) (4,f) (4,g) (4,h) (4,c) (4,a)

key 有：`1, 2, 2, 3, 4, 4, 4, 4, 4, 4`

分区 0：key ∈ [1, 3]  → (1,a)(2,b)(2,d)(3,c)     → 4 个

分区 1：key ∈ [4, 4]  → (4,e)(4,f)(4,g)(4,h)(4,c)(4,a) → 6 个

### 从算子的角度去理解spark的分区策略

叠个甲在Spark中，RDD的分区器不仅适用于键值对类型的RDD，也适用于其他类型的RDD

### 共享变量

####  广播变量☆☆

由 Driver 端发送数据，所有 Executor 端接收并保存这份数据，用于每个 Executor 上的数据计算工作

特点：

广播变量是保存在 Executor 内存中的，每个 Executor 一份。如果一个 Executor上执行多个 Task，那么多个 Task 将共享一份广播变量

广播变量是只读变量，即 Driver 端将变量发送到 Executor 端后，Executor 端只能读取变量数据，而不能修改变量数据

这里要说的一点就是当广播变量被广播到Executor里的时候 在Driver里将刚才广播的变量修改是没有用的

执行运算时再Executor端的

广播变量时单独由Driver端发往Executor端,而不是在计算逻辑发往Executor 端时，闭包(closure)后一同发送过去的

### 累加器变量☆☆

这个和广播变量类似，也是由Driver发到各个Executor上进行辅助运算

然后在Executor 累加 在把结果返回Driver 因为读取只能在Driver上读取 ，有个回收的过程

累加器的完整生命周期：

    ① 创建阶段：Driver 定义累加器（初始值=0）

         │

         ▼

    ② 分发阶段：Driver 把累加器随 Task 发到各 Executor  ← 你说的"发到各Executor"

         │

         ├──→ Executor 1: 拿到累加器，执行 add 操作

         ├──→ Executor 2: 拿到累加器，执行 add 操作

         └──→ Executor 3: 拿到累加器，执行 add 操作

         │

         ▼

    ③ 回收阶段：各 Executor 的累加结果汇总回 Driver

         │

         ▼

    ④ 读取阶段：Driver 端读取最终值

自定义累加器这个看视频

### 总结：

这里总结的是广播变量和累加器变量

广播变量总的来说就是减少数据的传输，提高性能，共享数据

累加器这里又分为分布式累加器和统计信息收集

分区列表

hadoop支持hash和自定义分区器

什么是job-spark任务相关第6级5分

有个任务从hdfs上读一个文件，在hdfs上会有三个block

算子rdd

transfromation算子 转换算子 只是一个声明但是并没有进行触发

Action算子 行动算子  这个是触发行动的

transfromation算子有什么好处

我在没有做最终执行的命令的时候，他不会产生中间结果

mapPations非常zhongy

Distinct 是全局的去重 每个分区放在一起都没有重复的数据

父Rdd的一个分区的数据不会进入子Rdd的多个分区就不会产生shuff,因为数据没有没打乱

repartition和coalesce和区别  （这两个特别重要）

1.repartition能够产生shuff

2.repartition内部调用的是coalesce

集合算子

intersection

zippartition

partitionBy

什么是分区器？

aggregateByKey

两种规则

1.分区内计算

2.分区间计算

combineByKey

groupbyke是对一个rdd里面的key进行分组

cogroup对多个rdd里面的key进行分组

自定义Transformation算子

foreache

sum这块图

aggregate和fold

分区内的操作和分区间的操作不一样的话只能用aggregate

如果两个操作数是一样的话可以简化成fold

save相关算子

**saveAsTextFile：**用于将 RDD 以文本文件的格式存储到指定的文件系统中

saveAsTextFile 函数是依赖于 saveAsHadoopFile 函数

用法：

//即使想指定文件，但是生成的依旧是文件夹（包含校验文件，是否写入成功文件，数据文件）

.saveAsTextFile("src/main/resources/data/abcd.txt")

//但是写入位置文件已经存在就会报错

//利用repartition进行优化

//textfile可以读取一个目录，然后会读取该目录下所有除了“：”·“和”_“开头的所有文件

//以”·“和”_“开头的文件会被认为不存在

transformation算子和Action算子的区别

**DAG☆☆☆（Directed Acyclic Graph，有向无环图）**

图类型：有 向无向  有环无环

组合：有向无环图  无向无环 有向有环

每一个算子在最后一个action算子之前都是transform算子

DAG节点就是算子 就是RDD=分区

边就是分区之间的依赖关系

Spark 两种task类型

ResultTask：除了最后生成结果的task叫ResultTask，其他的都是ShuffleMapTask

ShuffleMapTask

Shuff

持久化

缓存针对的是rdd

容错机制在62课

cache是缓存   的是transfrom算子 写在哪个后面缓存的就是哪一个算子

persist是持久化

## spark项目

### 美股分析

gitlab管理代码

 git config user.name看用户名字

### spark为什么比MapReduce快

我这里之前是认为spark是基于内存，mr是要落磁盘所以 spark会比mr快

但是其实两个都是基于内存计算的，任何框架都是基于内存的

而且DAG计模型减少的是磁盘i/o次数，相比于mr来说

他对于shuffle来说不会减少shuffle次数，因为shuffle是根据数据重组的次数来定的

所以真正的快是因为DAG相比比Hadoop的MapReduce在大多数情况下可以减少磁盘I/O次数

mr计算模型只能包含一个map和一个reduce 所以reduce之后必须落盘

而dag是可以连续shuffle，一个dag可以完成好几个mr，它只需要在最后一次reduce落盘，这样就比mr少了落盘的步骤，总shuffle次数越多，减少的落盘次数就越多

还有就是spark shuffle的优化 mr在shuffle默认是要排序的

spark在这个阶段只有部分场景才需要排序（bypass机制不需要排序）。排序是非常耗时的，这 样就可以加快shuffle速度

还有就是Spark 支持将需要反复用到的数据进行缓存

所以对于下次再次使用此RDD时， 不用再次计算，而是直接从缓存中获取，因此可以减少数据加载耗时

Chekpoint 这些

任务级别并行度上的不同。MapReduce采用了多进程模型，而Spark采用了多 线程模型。

MapReduce的MapTask和ReduceTask 是进程级别的，都是 jvm 进程，每次启动都需要重新申请资源，消耗了不必要的时 间

而SparkTask则是基于线程模型的，通过复用线程池中的线程来减少启动、关 闭task 所需要的开销。

## spark SQL

框架之间一定要解耦，不解耦的话shark就只能依赖hive

DateFram

DataSet

一条完整的数据信息是由data+schema=Schema RDD

DateFram就是表示DataSet一种特殊的结构 row 就是DataSet的子集

rdd DataSet DateFram 异同

spark原生的

Spark core里面的 DataSet DateFram

基本数据结构要掌握

缓存

1.spark常见的部署模式

 2.什么叫宽依赖什么叫窄依赖

8.rdd一开始只有数据没有元数据就是sechm 所以就出现了一个sechm的rdd也就是dataframe 这个dataframe 的数据结构是row 这个就是rdd中mei的数据映射晨一个row

rdd中的数据对应的是datafram中的一行

所以rdd中不管是什么数据解析下来都会是一个rowA

**Repartition和Coalesce关系与区别**

在两种阶段会使用到**Repartition 分区数增加这个肯定用shuff 数量级相差**

小文件合并**Coalesce用的多 把分布降下来 读一个文件就是一个task 分区降下来多个文件就合成一个文件了**

** 数据倾斜 分区要打开就用Repartition  扩大分区 分散下 然后再聚合**

**简述Spark中共享变量（广播变量和累加器）的基本原理与用途**

**缓存机制cache与checkpoint机制**

cache就是为了做重复计算的

**checkpoint就是一个复活点 就是容错点 防止算子嘎调 **

rdd看法

rdd是弹性分布式数据集自动的进行内存和磁盘数据存储的切换

然后还有一个容错机制，这个是基于RDD的不可变性和依赖关系，如果当某个节点失败时，Spark会重新计算该节点上的RDD分区，而不是整个数据集

优化非常给力像缓存、持久化、分区策略等都可以提高效率减小资源的浪费

什么叫弹性，通俗的理解弹性就是一个区间，并不会固定的处于某一个值，

比如我们说 RDD 的数据默认情况下存放在内存中的，但是在内存资源不足时，Spark 会自动将

RDD 数据写入磁盘，这种就是我们所说的 RDD 的存储可弹

因为五元组才不会存储数据

那么这5个属性，第一个属性分区列表，这个数据集，需要知道分布在那些分区上面吧

第二个，每一个分区，我需要实现什么样的操作能到下一个分区，这个过程是有一个计算的操作，比如实现一个computer，那么这个分区，计算父分区如何到子分区，在合并前一个分区是子分区，再往前一个阶段时父分区

分区器：我这个数据是如何到下一个分区的，这种一般是在产生shuff的时候 ，分区数据这些数据，合在一块给它打乱，打乱之后的数据网线一个分区，哪一个会跑，这个时候就会涉及一个分区器

第四个依赖关系，每一个子rdd,它的上游依赖到哪些父rdd，这样的好处，就是当前的rdd，一旦出现错误可以通过父rdd重新生成子rdd

spark的oom会发生在那个组件上，解决方案

Driver 做数据的收集 collect

Exector 具体的算子是在这上面执行的 比如mappartion整体去处理分区的量 如果这个分区太大就肯呢个溢出

**RDD、DataFrame、DataSet三者之间的区别与三者之间怎么相互转换**

什么是宽依赖什么是窄依赖

cbo基于时间花费的比较

spark算子中的cache和persist

cashe底层调用的就是persist

RDD 的 cache 默认方式采用 MEMORY_ONLY，DataFrame 的 cache 默认采用 MEMORY_AND_DISK

spark sql中df和ds的区别和使用场景

**宽依赖，父 RDD 的一个分区会被子 RDD 的多个分区使用。 **

**窄依赖，父 RDD 的分区最多只会被子 RDD 的一个分区使用**

父 RDD 的 Partition 流向，要是流向单个 RDD 就是

窄依赖，流向多个 RDD 就是宽依赖
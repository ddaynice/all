https://c.wss.ink/f/k372qjtahwl 复制链接到浏览器打开

## 面试补充：

### 第一等级： 最高频率（覆盖80%以上面试）⭐⭐⭐⭐⭐

>

>

>

>

>

>

>

>

>

>

>

>

>

>

>

>

>

>

>

### 第二等级： 中等频率（覆盖50%以上面试）⭐⭐⭐⭐

**1.四大排序子句（By的区别）**[**03-HiveSQL执行|Join|SQL语法等**](http://wiki.dsbigdata.com/pages/viewpage.action?pageId=71067316)

>

>

>

>

2.**内部表 vs 外部表 **[**02-Hive表操作|存储|压缩|序列化等**](http://wiki.dsbigdata.com/pages/viewpage.action?pageId=46581389)

>

>

>

**3.动态分区与静态分区 **[**02-Hive表操作|存储|压缩|序列化等**](http://wiki.dsbigdata.com/pages/viewpage.action?pageId=46581389)

>

>

**4.分桶表与分区表**

>

>

>

**5.核心操作 **[**02-Hive表操作|存储|压缩|序列化等**](http://wiki.dsbigdata.com/pages/viewpage.action?pageId=46581389)

>

>

>

>

>

### 第三等级： 低等频率（覆盖20%以上面试）⭐⭐

**1.自定义函数（UDF/UDTF/UDAF）**[**04-Hive窗口|自定义函数等**](http://wiki.dsbigdata.com/pages/viewpage.action?pageId=67255268)

>

>

>

**2.Hive其他函数分类**

>

>

>

**3.hive与数据库的区别 **[**01-Hive基础架构与底层原理等**](http://wiki.dsbigdata.com/pages/viewpage.action?pageId=7012362)

>

>

>

**4.深度知识**

>

>

>

## 什么是https://docs.qq.com/sheet/DQkN3S1VyQWxlekNI?tab=c7kf2q

HIVE就是一种数据仓库工具，明确的一点就是hive只是工具，

**可以用 Hive 将结构化的数据文件映射为一张数据库表，并提供完整的 SQL 查询功能，可以将 SQL 语句转换为MapReduce 任务运行。**所以 Hive 本身并不具备存储功能，要将它和数据库区分开

### 为什么hive比较重要，在我面试的时候包括现在这个公司，hive都是比较主要的

#### 这个问题要弄清楚来源，hive是基于什么场景下诞生的他是为了解决什么问题？

首先hive是facebook开发并且构建在Hadoop集群之上的数据仓库应用，同时他也提供了hql这种类似sql的语言

#### 原因：

facebook一开始的数仓是用mysql但是数据量增加查询的时间非常长，然后转移到oracle，但是oracle几TB没问题数据量又增加，然后自研了一个Cheetah日志系统，但是时间还是长，最后就用hadoop基础上开发了hive

### 但是数据库不就是数据仓库么？

数据库和数据仓库虽然只有一字之差但是他们存放的数据结构和使用场景是完全不同的！

数据库：数据库他的作用主要是为了支撑像网站这种一个底层的服务的，比如说创办个电商网站，这个网站肯定会产生一些数据，比如用户数据，商品数据，订单数据，那么我这些数据可以存放到一个数据库里，如果用户要登录就要实时的从我们的数据库中区查，能够匹配到才能登录

所以数据库也叫联机事务，是一个实时及时处理的一个架构，里面放的数据呢也是以状态为主，就是我们打开网站的那一刻展现在我们面前的都是状态数据，最新的数据，而且数据体量也不会太大

那么数据仓库存放的是历史的一个数据，这里的数据是用来做一些历史的分析的，是非常大的，还是拿电商网站来说，今天产生一整天的状态数据，昨天也产生了，上个月产生的，我们吧所有的历史数据都放到仓库里去，然后在结合所有的历史数据去做一个分析，比如分析这个电商网站的运营，哪个商好，哪个用户价值大等等！

还有就是HIVE可以将结构化的数据映射成为一张数据库表，并且提供完整的sql查询功能

### hive可以干什么？

用 Hive 将结构化的数据文件

映射为一张数据库表，并提供完整的 SQL 查询功能，可以将 SQL 语句转换为

MapReduce 任务运行

Hive 本身并不具备存储功能

Hive 有两个典型的特点

Hive 是建立在 Hadoop 上的数据仓库基础架构

较低的学习代价

### hive本质

hive其实就是对Hadoop进行了封装，提供sql来操作Hadoop

1.hive的处理数据都是在HDFS上

2.Hive 分析数据底层的实现是 MapReduce（也可配置为 Spark 或者 Tez）

3.执行程序运行在 Yarn 上

4.是一种特殊的 Hadoop 的客户端，最终的计算和存储还是由 Hadoop 来完成的

Hive 实际上是一个翻译的角色，Hive 的使用依赖于 Hadoop。

### 比较Hive和数据库

这两个很容易搞混！

1.存储位置：

Hive是建立在Hadoop上的。数据是存在HDFS上，数据库是存在块设备或者本地文件系统中的

2.查询语言

这个还好Hive是也是类SQL语言，在实际的写的过程没什么太大的区别！

3.索引

这个不是很明白，在hive这里是没有索引的，不会做处理

mysql会做索引来提高效率

虽然在hive 0.8之后加入了索引 但是实际生产中很少使用

4.数据格式

在hive中数据格式没有专门的数据格式，数据格式可以由用户指定。

在hive中默认有TextFile、SequenceFile及RCFile

在hive加载中不会对数据本身进行任何修改，就是复制粘贴到对应的hdfs上

但是在数据库中，不同的数据库有不同的存储引擎，有自己定义的数据格式！

5.数据更新

hive是读多写少，Hive中不支持对数据的改写和添加，所有数据都是在加载的时候确定好的

而数据库中的数据通常是需要修改的，因此可以使用INSERT INTO VALUES添加数据，使用UPDATE…SET修改数据。

6.扩展

hive是在hadoop上的所以hive是和hadoop一致的，但是数据库由于ACID语义的严格限制，扩展性非常有限

### Hive体系组成

先看结构

首先我要弄明白这个里面有那些组件，这些组件的作用是什么！

首先先拿自己分析的来看，整体是分为两部分，客户端和服务端

#### 客户端这里是向外暴露的

比如cli,JDBC/ODBC,WebGui

**CLI（命令行组件）**-可以写一些sql程序，然后把sql提交到服务端去进行一个运行 - 但是当我们使用这个命令行组件的时候，要求我们使用这个命令行的本机必须装有hive,如果没有hive这个命令行是使用不了的

**JDBC/ODBC** - 这个允许我们远程链接hive去进行编程开发的工作！ 但是在服务端需要有一个hiveserver2框架

hiveserver2 -这是facebook推出的一个框架（作用就是实现跨语言的开发 - 像 java py sql spark）,还有作用就是权限的管理

**Webgui** 网页上进行编程,提供的一个网页ui

Web Gui+CLI（命令行组件）+JDBC/ODBC(允许我们远程去链接hive编程)

Hive客户端提供了一种通过网页访问Hive所提供的服务的方式。这个接口对应Hive的HWI(Hive Web Interface)组件，使用前要启动HWI服务。

#### 接下来就是服务端，这里其实是个黑盒

服务端这里三大组成部分driver，matestore,hiveserver2

Driver - hive里面最核心的

Driver里面还有 解析器 - 编译器 - 优化器 - 执行器

**Driver组件:驱动   包括Compiler、Optimizer和Executor**

整体的作用就是将客户端里面写的sql 拿到这里面进行一个解析，或者编译，最终生成一个可执行的计划去执行

matestore是链接元数据的东西,**元数据服务组件  元数据就是数据的数据**

Hive的MetaStore组件是Hive元数据的集中存放地。MetaStore组件包括两个部分:MetaStore服务和后台数据的存储。

默认情况下，MetaStore服务和Hive服务是安装在一起的

也可以把MetaStore服务从Hive服务中剥离出来独立安装在一个集群里，Hive远程调用MetaStore服务。

hiveserver2（核心作用实现跨语言的开发）

**这里还有一个**

**Thrift服务**

Thrift是Facebook开发的一个软件框架，用来进行可扩展且跨语言服务的开发

它用来进行可扩展且跨语言服务的开发

可以让不同的编程语言调用Hive的接口

#### 自己话说

hive这个架构从整体上分为了客户端-服务端-计算引擎-hdfs存储这些

然后再客户端这里有Cli,**JDBC/ODBC,Webgui**

同时cli和webgui是适用方去用的，cli就是命令行接口，webui是提供通过网页来访问hive

然后到服务端，服务端这里肯定要接受客户端传过来的命令什么的，那么这个时候就是使用，hiveserver2来实现

这个组件就是进行扩展和跨语言的服务的开发，当我们创建了一个表的时候会生成一个hdfs目录，通过metastore将元数据存放在mysql中

然后客户端穿过来的命令，比如sql会通过hiveserver2提供给driver组件，在经过解析-编译-优化 生成执行计划

driver通过metastore读取我们刚才放元数据的mysql中，拿去相关的信息

拿到元数据后，相对的执行计划生成，交给执行器去执行，如果走mr提交给yarn

#### 组件的整体协调

 拿创建表来举例子

创建一张学生表stu

那么创建表的语句是在客户端 命令行 cli 或者webGUI 上执行创建语句

然后会在hdfs上生成一个目录  其实我们一张表就是一张目录

创建完目录之后，通过metastore将元数据存放在mysql/deby等数据库中（比如字段，字段类型，hdfs位置等）

表创建完之后就可以对表进行查询等操作，这个查询语句也是在命令行，webui上执行的！或者jdbc 远程链接

写完sql之后会把sql提交到Driver 组件当中去

然后在通过四个器 解析器 - 编译器 - 优化器 - 执行器

在执行的时候，他是需要走mr这个程序的，然后提交给yarn 托管执行mr的程序

如果不走mr 直接从datanode节点上拿数据

### hive的有点缺点 和关系数据库的对比

#### 优点：

1.类sql 简单 容易上手

2.避免了写mr，减少开发成本

3.以mr作为计算引擎，hdfs作为存储系统，提供大量数据计算，扩展

4.统一元数据管理，可以和别的框架共享

#### 缺点：

1.hive延迟是比较高的，常常是用于一些数据分析的地方，比如我们的腾讯视频 就是大量用来做离线的数据的计算，适用于对实时要求不高的场合

2.hive的数据是存在hdfs上，但是hdfs不支持随机写，所以只能追加，所以在hive中不能高效的update 和 delete

3.hive 自动生成mr 所以调优比较难



### HIVE和数据库比较💕

### Hive执行过程面试必面试

Hive将我们写的SQL转化为MapReduce等计算引擎可识别的程序的过程

#### Hive底层执行架构

UI这就相当于一个入口，提交sql命令行的入口

DRIVER:本身是一个驱动他主要是用来接收来自用户提交的一个查询，通过调用Driver的API，接收到之后再做进一步的处理

COMPILER：编译器主要是将咱们得SQL转换成平台可执行的一个执行计划，对于查询操作，以及查询里涉及到的一些表达式进行一些分析，借助一些表从META&TORE的存储里面去生成一些执行计划

META&TORE（元数据存储的一个信息）：元数据库   存的是各种表，以及表的分区，字段一些很基础的信息

EXECUTIONENGINE：执行引擎   负责提交在编译（COMPILER）阶段已经编译好了的执行计划 然后再分发不同的平台上执行！那也就是Hdoop平台上

Hadoop阶段：

JOB TRACKER:这个就是Mast 作业的管理 监控 任务调度

这个得在找找有点迷糊

#### Hive执行流程

用户在UI提交了SQL的语句  那么UI就会通过jdbc->发送到HiveServer2

HS2创建Session和QueryID调用DRIVER的接口 ，将查询提交到DRIVER这里来了

第二步就是DRIVER拿到查询请求之后，就会为这次查询创建一个唯一的ID（Session和QueryID）

将查询的信息发送到COMPILER，那么这个编译器就会为我们生成一个编译计划

编译器拿到这个查询信息之后，会向META&TORE进行元数据的存储，大致的意思就是我有个请求，我想查一些表，查点字段，在查的过程中我还要过滤写信息，就把这些东西告诉META&TORE

META&TORE拿到这些信息之后呢，就把COMPILER想要的信息返回给他

第五步

编译器拿到这些元数据之后，它会生成一个执行计划，哪这个计划呢可能是MAPreduce作业，也可能是一个HDFS的一个操作。

这个计划就会被返回到DRIVER里

如果COMPILER里生成了一个任务如果是MAPreduce作业，就可能包括一个MAP的擦做数或者一个Readuce的操作数，然后执行引擎再把这些作业发给reduce

第6步

DRIVER在拿到这个计划之后 就会把这个计划提交给EXECUTIONENGINE：执行引擎，那这个执行引擎它会操作元数据库，得到这个程序需要的一些基础的信息

在得到这些元数据数据信息之后，就会发起一个请求给到JOB TRACKER

哪JOB TRACKEP 干啥呢就进行一个HDFS上面的一个文件的读写，就肯呢个涉及到namdNODE和datanode的一些处理！

获取到处理后的信息后，通过序列化的一个容器，把它写到一个临时HDFS的文件里，这个临时的文件主要是是向咱们得一个计划中EXECUTIONENGINE后面的一个mapreduce阶段提供一个数据

第七步获取结果

第八步发送结果

第九步获取数据的存储结果

这几步就是将我们生成的那个临时文件移动到表的一个位置，确保不会读取到其他脏数据

对于用户的查询，临时文件的内容，其实是由执行引擎直接由HDFS中读取，然后由DRIVER再发送给UI

789是一个往返的操作

最开始是UI有个请求说我要获取结果

告诉执行引擎我要拿结果，第九步先把数据存起来，拿到临时存储计算的一个结果

然后就逆向的返回客户端

#### HiveSQL在编译过程

1.词法语法解析

2.语义解析

3.生成逻辑执行计划

4.优化逻辑执行计划

5.生成物理执行计划

6.优化物理执行计划

本章小结：

能说出来传统数据库和数据仓库的区别；

讲清楚hive体系架构和数据仓库的区别

为什么maoreduce效率低

MapReduce的执行效率很低，这种低效是由它的执行模式决定的，所有的Map Task、Reduce Task全部是以进程的方式执行的，要启动进程、销毁进程，即使可以开启JVM重用，但是也是用的时候开启，结束之后关闭，而且JVM成本很高。

随着时代的发展，人们开发出计算处理能力更强大的数据处理工具，如Spark、Tez等，因此有：Hive on MapReduce、Hive on Spark、Hive on Tez

所以Hive底层所支持的执行引擎有MapReduce、spark、tez。

### HIVE数据类型

数据类型这里死记硬背没什么用我感觉，你想比如 int,bigint,布尔，double,string,char这些mysql有的hive也是基本支持了，用的是再查

还有像int 字节长度也没啥用第一面试不会问，第二在工作的时候是个人都知道用大的类型

##### 数据类型转换

数据类型这里转换的用的比较多

但是像double转int这种的其实是用round和floor函数进行的

像别的比如bigint转string用的就是cast-cast(bigint as string)

## Hive元数据

Hive数据库相关的元数据表

**元数据表字段**

**说明**

**示例数据**

**DB_ID**

数据库ID

1

**DESC**

数据库描述

测试库

**DB_LOCATION_URI**

数据库HDFS路径

**hdfs://dscluster/user/hive/warehouse**

**NAME**

数据库名

default

**OWNER_NAME**

数据库所有者用户名

public

**OWNER_TYPE**

所有者角色

ROLE

DATABASE_PARAMS：该表存储数据库的相关参数，在CREATE DATABASE时候用

WITH DBPROPERTIES (property_name=property_value, …)指定的参数。

**元数据表字段**

**说明**

**示例数据**

**DB_ID**

数据库ID

2

**PARAM_KEY**

参数名

name

**PARAM_VALUE**

参数值

zhu

### 探查元数据应用场景

TABLE_PARAMS里面的PARAM_KEY常见取值：

numFiles:文件数

numRows:行数

totalSize:占用HDFS空间大小

rawDataSize:原生数据大小

transient_lastDdlTime:最近一次操作空间

#### 么个数据库占据的储存大小

#### 查看数据表最近一次被使用的时间，判断使用热度

### SQL语句的执行顺序

#### MYSQL

##### 写的话直接就是，书写顺序

##### 逻辑执行顺序

首先是from，确定查询的数据源

然后有join 和on的话就对from子句中的表进行连接操作，并应用on子句中的链接条件

在然后就是where，对链接后的结果进行筛选，只保留满足where条件的记录

接着就是group by 进行分组

有hiving的话就对分组后的结果进一步筛选，只保留满足的结果

在然后就是select选择select中的字段或列

最后就是DISTINCT：如果SELECT子句中包含DISTINCT关键字，则对查询结果进行去重处理。

在然后就是order by 对结果进行排序

这个样子

#### HIVE

拆分成map阶段和reduce阶段

Map阶段：

1.执行from加载：进行表的查找与加载。 就是选表 看数据库里有没有这个表

2.执行where过滤：进行条件过滤与筛选。  一个基本的筛选减少数据量

3.执行select查询：进行输出项的筛选。

4.执行group by分组：描述了分组后需要计算的函数。  函数其实字这一步还没有执行

5.map端文件合并：map端本地溢出写文件的合并操作，每个map最终形成一个临时文件。然后按列映射到对应的

Reduce阶段：

1.group by：对map端发送过来的数据进行分组并进行计算。

2.select：最后过滤列用于输出结果。

3.limit排序后进行结果输出到HDFS文件。

和mysql其实差不多就是分成了map和reduce两个阶段

#### 查询计划

explain select name,count(distinct id) from ds_hive.ch4_emp t group by name;

- [ ]

这里的话

- [ ]

#### Hive SQL语句的执行原理

##### Join的实现原理

select u.name, o.orderid from order o join user u on o.uid = u.uid;

第一步在Map阶段将第一个表<user>字段做了一个标记

o.uid = u.uid;

第一个表，就是 key值，也就是关联字段的一个值 1和2

value是什么？

第一个表即为表一user

第二个表就是表二order

value就包含了两个部分 第一个就是表一的序号，第二个就是除了uid另外的字段

有select u.name, o.orderid from order o join user u on o.uid = u.uid;一条join的语句

对应的做两个表的关联

在关联的时候把关联的键作为我们的key值，其他字段是做一个value值，然后进行一个数据的分发，分发到节点上面去之后，做一个数据的清洗，然后会把key值相同的放到一块，放在一块之后按照join的一个操作，我们把需要的列做一个排列组合，最终得到我们想要的一个执行结果！

##### Group By的实现原理

select rank, isonline, count(*) from city group by rank, isonline;

这是两个块的内容 第一块是两条数据  第二个块也存储了两个数据

在map阶段  生成了一个key value的键值对

key就是rank，isonline 两个字段的值 刚好和join的想反 value就是对第一个块中的数据的计数

接着就是洗牌然后排序  使用key值进行分组统计

总结:

能讲清楚内嵌模式、本地模式、远程模式的差异。(基本要求)看来还是要搭建一下

能阐述元数据数据库包含的具体内容

## 数据模型

四种数据类型 s

Hive中的所有数据都存储在HDFS中。 Hive中包含4种数据模型:Database、Table、Partition和Bucke

### 1.Database数据库

相当于关系数据库里的命名空间

作用是将用户

和数据库的应用隔离到不同的数据库或模式中

### 2.Table表

Hive里的Table有两种类型:

**内部表：数据文件存储在Hive的数据仓库里**

**外部表：数据文件可以存放在Hive数据仓库外部的分布式文件系统上，也可以放到Hive数据仓库里**

### 3.Partition分区

弄清楚什么是分区，为什么要有分区

**作用**：使用分区是为了加快数据的查询速度

### 4.Bucke桶

### 两类数据类型

#### 基础数据类型！

INT

INT

4byte,-2,147,483,648 ~ 2,147,483,647

有符号整型

BIGINT

BIGINT

8byte,-9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807

有符号整型

DECIMAL

DECIMAL



可带小数的精确数字字符串，常用于交易金额的计算，从Hive0.11.0开始支持

DATE

DATE



从Hive0.12.0开始支持，日期，内容格式：YYYYMMDD

**关于float、double的说明**：

#### 基础数据类型应用示例

#### 集合数据类型

ARRAY

数组

ARRAY类型是由一系列相同数据类型的元素组成，这些元素可以通过下标来访问。比如有一个ARRAY类型的变量fruits，它是由['apple','orange','mango']组成，那么我们可以通过fruits[1]来访问元素orange，因为ARRAY类型的下标是从0开始的；

MAP

字典

MAP包含key->value键值对，可以通过key来访问元素。比如"userlist"是一个map类型，其中username是key，password是value；那么我们可以通过userlist['username']来得到这个用户对应的password；

STRUCT

结构体

STRUCT可以包含不同数据类型的元素。这些元素可以通过"点语法"的方式来得到所需要的元素，比如user是一个STRUCT类型，那么可以通过user.address得到这个用户的地址。

#### 基础数据类型应用示例1-基础

- [ ]

- [ ]

- [ ]

- [ ]

#### 基础数据类型应用示例2-集合

- [ ]

#### 数据类型转换

隐式转换：一般是自动转换好的，和java类型小的能转大但是大的不能转小

**显式转化：可以用CAST来显式的将一个类型的数据转换成另一个数据类型**

CAST的语法为cast(value AS TYPE)

举个例子：假如我们一个员工表employees，其中有name、salary等字段；salary是字符串类型的

SELECT name, salary FROM employees

WHERE cast(salary AS FLOAT) < 100000.0;

### **HIVE 中的序列化和反序列化****(☆☆理解记住)**

#### **SerDe的产生背景**

对象序列化：发送方需要把对象转化为字节序列才可在网络上传输，称为对象序列化

对象反序列化：接收方则需要把字节序列恢复为对象，称为对象的反序列化

Hive的反序列化是对key/value反序列化成hive table的每个列的值

上面的意思就是把查询到的数据，映射成hive表里的每一个值，然后呈现给我们用进行一个展示。

**Hive有三大核心组件：**

>

>

>

SerDe是Serializer和Deserializer的缩写,是序列化器与反序列化器，Hive使用SerDe接口去完成IO操作，接口的三个主要功能：

（1）序列化(Serialization)，从Hive写FS

（2）反序列化（Deserialization），从FS读入Hive

（3）解释读写字段，加起文件到字段结构的桥梁

#### SerDe所处的位置

hive读写文件的机制

从上往下看可以看到，hive的行数据通过一系列的数据化，将数据的对象转换成为机器可以识别的键值对，然后再转换成hadoop的一个存储格式，最终会将数据以字节码形式存到hdfs上。

右边就是hdfs转换为行数据文件的过程 ，就是反序列化

就是反着来

#### **序列化和反序列化的目的**

序列化的目的是Hive格式输出成为特定格式

反序列化的目的是HDFS格式读入Hive内存中

#### Serde分为内置SerDe与外置SerDe

>

>

#### 面试：

能讲清楚常用的数据类型有哪些。(基本要求)

2.能举例说明集合数据类型的应用场景。

答：例如map类型常用来做扩展字段，避免多次修改表结构；而array类型常常出现在行列转化中。

map类型通常放到表的末尾作为一个扩展的字段，比如新建了一个表，表里面有3，40哥字段然后我们想加一些字段加些地址，把城市街道这些信息，如果没有map字段那可能就是，修改一次表的结构 alter一个表 alter一个列,第二个字段你还得这样弄，但是有了这个map之后，其实这些新增的字段直接塞到map里面去，存到value里面去，就能避免修改表

3.能讲清楚Hive读写文件的机制。

基于序列化和反序列化讲清楚hive读写文件的机制

## **数据库操作**

### 查看数据库

- [ ]

切换到指定库

use **db**名称;

### 创建数据库

【1】创建数据库

**create** **database** dbname;



----【2】通过location指定数据库路径

**create** **database** dbname location 'path路径';



----【3】给数据库添加描述信息

**create** **database** dbname comment 'dbname描述信息';

### 删除数据库

----【1】删除数据库，这种删除，需要将数据库中的表全部删除，才能删除数据库

**drop** **database** dbname;

或者

**drop** **database** if exists dbname;    如果存在就删除

----【2】强制删除数据库

Drop table dbname;

**drop** **database** dbname **cascade**;

### **查看数据库的详细描述**

Desc database dbname;  只能查空表！！！

但是加了database就出不来了，这个看把

Desc  dbname;

### **数据库键值对信息**

----【1】创建带键值对的数据库

**create** **database** foo **with** dbproperties ('own'='cc', 'day'='20180120');



----【2】查看数据库的键值对信息

describe **database** extended foo;

还能简写

  desc database extended zh_foo;

----【3】要修改数据库的键值对信息

**alter** **database** foo **set** dbproperties ('k1'='v1', 'k2'='v2');

### 数据表

数据表：是数据库中的基本对象元素，用于存储数据

#### **内部表、外部表的区别****(☆☆☆重点掌握)**

#### 区别：

1.内部表数据由Hive自身管理，外部表数据由HDFS管理；

内部表的创建和删除都是由hive自己去管理的 比如执行drop就能删除

但是外部表你用drop就删不掉

2.两个表的存储位置是不一样的

内部表的位置是和hive的配置相关的：

“内部表的数据存储位置是hive.metastore.warehouse.dir，默认位置：/user/hive/warehouse，”

**内部表这里其实就是我们正常创建的表，就是我们在工作中常用的表**

外部表：它的 位置是自己决定的

如果没有LOCATION，Hive将在HDFS上的/user/hive/warehouse文件夹下以外部表的表名创建一个文件夹，并将属于这个表的数据存放在这里

内部表存再的是Hive自己的元数据存储系统中，这个位置是由Hive自身管理的

而外部表的数据是直接存储在HDFS，这个位置是由Hadoop系统管理的

3.删表的变化情况

内部表：删除内部表会直接删除元数据（metadata）及存储数据

外部表：删除外部表仅仅会删除元数据，HDFS上的文件并不会被删除；

4.对表的修改情况

内部表：对内部表的修改会将修改直接同步给元数据

外部表：对外部表的表结构和分区进行修改，则需要修复

### **内部表、外部表的生产应用****(☆☆理解记忆)**

具体的使用场景：

>

>

>

>

>

>

>

>

>

### **数据表操作**

#### 显示数据库中的表

----【1】显示表清单

show tables;



----【2】使用like模糊匹配，查询包含tb_前缀的表

show tables like 'test*';

或者

Show tables 'test*';

#### **显示表的分区**

----【1】显示表分区

show partitions tb_test;

分区表就是在表里继续分表 比如

你有一个销售记录表，记录着每个每个商场的销售情况，那么你就可以把这个销售记录表按时间分成几个小表

例如说5个小表吧。2009年以前的记录使用一个表，2010年的记录使用一个表，2011年的记录使用一个表，2012年的记录使用一个表，2012年以后的记录使用一个表。那么，你想查询哪个年份的记录，就可以去相对应的表里查询，由于每个表中的记录数少了，查询起来时间自然也会减少。

#### **显示表的详细信息**

----【1】显示表分区

**desc** tb_name;

describe tb_name;

#### **创建内部表/外部表/分区表/分桶表**

- [ ]

### **修改表分区/列/表名**

- [ ]

### 内部表与外部表的切换

- [ ]

### **分区表&非分区表**

分区的定义：

Hive的一个分区名对应一个目录名

子分区名就是子目录名，并不是一个实际字段

一个表可以拥有一个或者多个分区，每个分区以文件夹的形式单独存在表文件夹的目录下

分区是以字段的形式在表结构中存在

但是该字段不存放实际的数据内容，仅仅是分区的表示

也就是说分区就是个目录，比如我现在有个销售数据的表，日期被定义为了分区，新建分区date=2017

同样的就会出现一个2017的分区，那么在逻辑上分区就会将这些数据进行划分，2017年的数据都在2017分区下管理，当我要查的时候直接where data=2017限定这个查询条，减小检索范围，这也是分区高效的原因！

##### **静态分区**

静态分区是手动指定

静态分区的列是在编译时期，通过用户传递来决定的

写入的时候的区别:

静态分区在插数语句的后边就要添加字段和字段值后，不需要再sql的查询语句再添加该字段

##### **动态分区**

动态分区是通过数据来进行判断

动态分区只有在SQL执行时才能决定

写入的时候的区别:

动态分区在插数语句后边添加字段后，还需要在sql的查询语句的最后，把该字段加上。

动态分区具体的案例代码

标红的就是动态分区的使用

就是类似一个变量 我先不定义等有了具体的需求你在转变对应的类型

- [ ]

##### **单级分区**

也就是说在表文件夹目录下只有一级文件夹目录

##### **多级分区**

另外一种是多分区，表文件夹下出现多文件夹嵌套模式。

### **分区的操作**

- [ ]

### 问题：

1.再创建分区的时候，我使用show partitions去查分区查到的确是0啥都没有？

这是因为

在创建表的时候指定了分区只是定义了分区结构，并不会自动填充数据到分区中。分区只是对数据进行逻辑上的划分，方便管理和查询。

也就是说这个分区是空的！

2.再加分区的时候看见了

ADDPARTITION (user_year='1990',sex='male')

 location '/tmp/my_student_info_1990'

PARTITION (user_year='1991',sex='female')

location '/tmp/my_student_info_1991'

按理说分区不是因该加到表的下面去么？

不是的

在Hive中，分区数据不是直接存储在表的目录下，而是存储在独立的分区目录下

每个分区都有自己的目录，并且这些目录通常位于Hive的warehouse目录之外

就比如上面的路径

`student_part`表的路径是`/user/hive/warehouse/sh_hive.db/zh_student_par`t

这是表的元数据存储位置

而分区的路径是`/tmp/my_student_info_1991`，这是分区数据的实际存储位置

3.添加分区的操作

- [ ]

查看分区:

- [ ]

删除分区: 加PURGE后，数据不会放到回收箱，会直接删除。

- [ ]

实际执行

- [ ]

##### 修复分区

- [ ]

为什么要修复分区

我们在使用Hive的时候肯定遇到过建立了一张分区表，然后手动（比如使用 cp 或者 mv ），就像上面复制文件到hdfs上，一个两个还行，多了肯定不行但是如果初始化的分区太多

### 动态分区演示--z这个们有弄明白

- [ ]

在动态分区中，主分区和副分区必须采用相同类型的列，即要么都是动态列，要么都是静态列。如果主分区采用了动态列而副分区采用了静态列，那么所有的主分区都必须创建与副分区的静态列相匹配的分区

## 分桶

### 什么是分桶？

Hive分桶是指将数据按照指定的列进行哈希运算，然后将结果分配到不同的桶中。每个桶包含一部分数据，可以看作是一个小的数据子集。通过这种方式，数据被分散到多个桶中，每个桶中的数据量相对较小。这种数据划分方式有助于提高查询效率和数据处理效率。

数据分桶的原理:  与MR中的HashPartitioner的原理一模一样，MR中按照key的hash值去模除以reductTask的个数；Hive中按照分桶字段的hash值去模除以分桶的个数。

HashPartitioner这个是默认的分区划分器，原理就是对于给定的key，计算他的hashCode并除以分区的个数取余

如果余数小于0，则用余数+分区的个数（否则加0），最后返回的值就是这个key所属的分区ID。当key为null值时，返回0。

### 分桶的作用：

获得更高的查询效率：全表查询或分区查询转换成桶查询。

大表join：对于两张大表的join，执行reduce join(shuffle join)肯定不合适，只能做map join。reduce join只适合做小表和大表的join,如何做大表间的join呢？此时可以对两张大表的连接字段分桶，此时的join是按照桶来的，一个桶一个桶join，这样就完美解决了。

抽样查询

传统抽样：select * from emp tablesample(10%);

这是hive提供的按照百分比进行抽样的方式，这种是基于行数，按照输入路径下的数据块百分比进行抽样

这种抽样不适合所有文件，并且这种抽样单元是一个HDFS块。也就决定了如果表数据大小小于普通的块的大小128m的话，将会返回所有行！

分桶抽样：select * from emp tablesample(bucket x out of y);

在分桶抽样里y必须是table总bucket数的倍数或者因子

hive根据y的大小，决定抽样的比例

table总共分了4份（4个bucket），当y=2时，抽取(4/2=)2个bucket的数据，当y=8时，抽取(4/8=)1/2个bucket的数据

x表示从哪个bucket开始抽取。

table总bucket数为4，tablesample(bucket 4 out of 4)，表示总共抽取（4/4=）1个bucket的数据，抽取第4个bucket的数据。

x的值必须小于等于y的值，否则会报错

### 分桶建表操作：

- [ ]

- [ ]

往桶表插入数据：

**insert** overwrite **table** olist_customers_dataset_bucket **selectfrom** olist_customers_dataset;

查看hdfs目录：

hdfs dfs -ls /user/hive/warehouse/sh_hive.db/

## 视图

视图是什么?

Hive中的视图（view）是一种虚拟表，只保存定义，不实际存储数据

视图是用来简化操作的，它其实是一张虚表，在视图中不缓冲记录，也没有提高查询性能

----【1】创建视图：

- [ ]

----【2】查看视图定义：

show **create** **table** v_test;

----【3】删除视图：

**drop** **view** v_test;

----【4】更改视图定义：

**alter** **view** v_test **as**  **select** customer_id,customer_city,customer_state **from** olist_customers_dataset;

这个就是在现有的视图里在增加字段

### 那么我在查视图的时候发现和普通的表没有什么不同啊？

视图表常用场景

## 知识总结

本章重点把握内部表与外部表的定义与区别，在此基础上进行实践操作

## DML操作

#### 基础查询

- [ ]

#### 设置别名

- [ ]

- [ ]

- [ ]

- [ ]

- [ ]

- [ ]

- [ ]

union :不管union 了多少部分的数据，那么他union 出来的字段，字段名称字段类型都要保持一致 数据会去重

union  all：数据不会被去重

### **四类排序操作**

Hive共有四种排序

order by，sort by，distribute by，cluster by

### order by

全局排序；

对输入的数据做排序，故此只有一个reducer(多个reducer无法保证全局有序)；

只有一个reducer，会导致当输入规模较大时，需要较长的计算时间；

### sort by

非全局排序

在数据进入reducer前完成排序

当mapred.reduce.tasks>1时，只能保证每个reducer的输出有序，不保证全局有序

- [ ]

### distribute by

按照指定的字段对数据进行划分输出到不同的reduce中；后面不能跟desc、asc排序；

常和sort by一起使用，并且distribute by必须在sort by前面；

### cluster by

相当于distribute by+sort by，只能默认升序，不能使用倒序

- [ ]

### **join的类型与用法**

什么是join

join就是将两个表给关联起来！

中间是内连接

它是在结果表中删除与其他被连接表中没有匹配行的所有行，所以可能会丢失信息。

内连接是从两个表之间的共同列匹配返回满足连接条件的行，只有当两个表中的数据项相等时，才会返回结果。参与连接的两个表（或连接）的地位是相等的

左上的是左连接

意思是 把A表中的数据全查出来B表中的数据如果和A表有关联就查出了没有关联就不查询 根据关联条件

左连接是左表加上右表符合连接条件的数据

左中：A表中有的数据全都给留下来，同时把B表中在A表中出现过的数据就给去掉！

右上：

右中：

左下：全连接  所有的数据保留下来！

右下：两个表的交集就去掉 也就是取两个表不相关的

内连接[inner] join:

两个表中关联键相同的记录才会查询出来

- [ ]

外连接—左外连接left [outer] join:

以左表为主表，右表中有的就会关联上，右表中没有关联上的数据就用 null 补齐

- [ ]

#### **Join的原理和机制****(☆☆☆重点掌握)**

简单来说join可以分为3个部分

Map阶段

在map阶段第一步是读取原表的数据，那么在map输出的时候是以join on条件中的列位key，这里的key指的就是连接条件，那么如果有多个关联键，则这些关联键的组合为key

在第二步： Map输出的value为join之后所关心的(select或者where中需要用到的)列；同时在value中还会包含表的Tag信息，用于标明此value对应哪个表；

第三步就是按照key进行排序了！

shuffle阶段

根据key的值进行hash，并将key/value按照hash值推送至不同的reduce中，这样确保两个表中相同的key位于同一个reduce中。

reduce阶段

根据key的值完成join操作，期间通过Tag来识别不同表中的数据

案例：

**SELECT**

 a.id,a.dept,b.age

**FROM** a join b

**ON** (a.id = b.id);

##### **Hive Map Join**

这个通常是用于一个小表和一个大表进行join的场景，小表的标准是有参数hive.mapjoin,smalltable,filesize决定的

这个参数的意思是表示小表的总大小，默认是25000000字节，即25M

但是在hive0.7之前，需要使用hint提示 /*+ mapjoin(table) */才会执行Map join 不适用hint就执行Common join

但是在0.7之后的话就由hive.auto,convert,join来控制 默认就是map join

假设a表为一张大表，b为小表，并且hive.auto.convert.join=true,那么Hive在执行时候会自动转化为Map Join。

案例

**select** /*+ MAPJOIN(time_dim) */ count(1) **from**

store_sales as a join time_dim as b **on** (a.ss_sold_time_sk = b.t_time_sk)

这个图的执行过程

首先Task A，他是一个local task 一个客户端在本地执行的Task,它的作用就是就是扫描小表（b）并且将小表转换为一个Hash table的数据结构，写入到本地里去，然后将写入本地的文件在加载到Diastribute里面去,

Task a结束之后 就是task b，这个任务是一个处理大表的阶段，但是在这个任务里，这个MR阶段是没有Reduce的

扫描完大表a之后，根据a的每一条记录去和Distribute Cache中b表对应的Hash Table关联，然后输出结果

由于Map Join没有Reduce，所以 由Map直接输出结果文件，有多少个Map Task，就有多少个结果文件。

这也是有限制的

## **函数****(☆☆☆重点掌握)**

### **字符串函数**

##### **字符串连接函数:concat 就是拼接**

- [ ]

##### **带分隔符字符串连接函数:concat_ws 这个就是连接的时候用什么分隔符连接**

- [ ]

##### **小数位格式化成字符串函数:format_number 是四舍五入**

- [ ]

##### **字符串截取函数:substr,substring  hive下标是从1开始**

- [ ]

##### **字符串查找函数: instr **

- [ ]

##### **字串转换成map函数: str_to_map**

- [ ]

##### **字符串转大写函数:upper,ucase**

- [ ]

##### **字符串转小写函数:lower,lcase**

- [ ]

##### **正则表达式替换函数:regexp_replace**

- [ ]

##### **正则表达式解析函数:regexp_extract**

- [ ]

##### 分割字符串函数:split

- [ ]

### **日期函数**

#### **UNIX时间戳转日期函数:from_unixtime**

- [ ]

#### 获取当前UNIX时间函数:unix_timestamp

- [ ]

#### 日期转UNIX时间函数:unix_timestamp

- [ ]

#### 日期时间转日期函数:to_date

- [ ]

#### 日期转年数:year

- [ ]

#### 日期转月函数:month

- [ ]

#### 日期转天函数:day

- [ ]

##### **日期转周函数:weekofyear**

- [ ]

##### **日期比较数:datediff**

- [ ]

#### 日期增加函数date_add

- [ ]

#### 日期减少函数:date_sub

- [ ]

### 数学函数

##### **取整函数:round**

- [ ]

#### 指定精度取整函数:round

- [ ]

### 集合函数

#### map类型大小:size

- [ ]

#### array类型大小:size

- [ ]

##### **判断数组否包含元素:array_contains**

- [ ]

##### **获取map中所有value集合**

- [ ]

#### **条件函数**

- [ ]

### **UDF函数介绍**

一对一的输入输出,只能输入一条记录当中的数据，同时返回一条处理结果

#### 实现方式

hive的udf有两种实现方式或者实现的API

一种是udf比较简单，一种是GenericUDF比较复杂。

开发udf中关键的点！！

1.udf函数是继承UDF的类

- [ ]

首先是DateFormatConvert 这个类继承UDF

接下来创建创建evaluate方法 这个方法的目的就是将一个日期类的的字符从一个格式转换成另外一个格式

evaluate有三个参数

第一个参数是text(要转换的日期字符串)

第二个参数srcFormat(源日期格式)

第三个参数destFormat（目标日期格式）

然后抛出ParseException 异常

在这个方法体内 有个if判断 判断有没有传入null如果传入了null的话就不做任何的转换

再接着就是老套路创建日期格式化对象

在这里创建了两个SimpleDateFormat

第一个是用来解析日期 第二个是用来格式化日期的

首先srcFormat将传入的日期字符串解析为Date对象。在使用destFormat将解析后的日期对象格式化为新的字符串。

最后，将格式化后的日期字符串封装在一个新的`Text`对象中并返回。

使用

### UDAF函数

多行进一行出，in:out=n:1,即接受输入N条记录当中的数据，同时返回一条处理结果

一共是两个阶段：

第一个是Map阶段

输入了多行数据，相当于读字段

首先要进行一个init初始化的操作，初始化map相关的变量，用作后续的传递

第二步数据过来之后，因为是多条数据，就要把数据一条一条的处理

第三步对数据进行一个局部的汇总

第二个是Reduce阶段

做了一个对局部数据汇总之后，就是要输出结果

同样的到了reduce之后我们也要初始化reduce的变量，用于后续的传递

初始化之后我们要执行marge方法 这个方法主要是对map汇总过来的数据进行合并，相当于迭代了

数据处理完之后我们就要进入到terminate 这个阶段就是要对咱们marge的数据进行处理

- [ ]

这个函数是找最大值

第一步还是继承 UDAF类 第二步定义一个MaximumintUDAFEvaluator 实现UDAFEvaluator接口

第三步就是定义一个最大值存储ressult

第四步接口的初始化方法

第五步public boolean iterate(IntWritable value)这个是接口的迭代方法 它会接收一个IntWritable 类型的参数，表示当前要处理的整数值，如果该值是null就返回true表示的就是继续处理其他值 ，否则的话它会更新result为当前的最大值

要点：

udf对于类的实现

1.udaf是继承UDAF里的类

2.udaf类里构建了个静态类 这个类是实现了UDAFEvaluator接口  这个接口里有5个方法

init,iterate,terminatePartial,merge,terminate，

3.多行数据的输入 一行数据的输出

###  UDTF函数介绍

## **窗口函数****(☆☆☆重点掌握)**

什么事窗口函数：

窗口函数是hive中特有的函数，提供了数据筛选、转换、聚合等操作，

并能借助 Hive 和 Hadoop 进行大数据量的处理

因为传统的 SQL 语句并不能支持诸如分组排名、滑动平均值等计算，原因是 GROUP BY 语句只能为每个分组的数据返回一行结果，而非每条数据一行

**【函数定义】：**窗口函数又名开窗函数，属于分析函数的一种，用于解决复杂报表统计需求的功能强大的函数

窗口函数用来计算基于组的某种聚合值，但是他和聚合函数不同的是 窗口函数对于每个组返回多行，而聚合函数对于每个组只返回一行！

**【三个概念】：窗口分区、窗口帧、以及窗口函数。**

**窗口分区:可以理解为表的分区有点类似**

**窗口帧：可以理解为每个分区里的单条数据**

Hive 提供了两种定义窗口帧的形式：ROWS 和 RANGE。两种类型都需要配置上界和下界

**窗口函数：对于这些分区进行处理**

在hive中有

>

>

>

>

>

最右边是表，往左是表里面取出来的一部分数据的结果集 在往左就是把结果表拆成了不同的分区 每个分区里面就是可以认为是帧，可以是一条或者多条数据！

### 窗口函数表达形式：

窗口函数的语法分为四个部分：

（1）函数子句：指明具体操作，如sum-求和，first_value-取第一个值；

（2）partition by子句：指明分区字段，如果没有，则将所有数据作为一个分区；

（3）order by子句：指明了每个分区排序的字段和方式，也是可选的，没有就是按照表中的顺序；

（4）窗口子句：指明相对当前记录的计算范围，可以向上（preceding），可以向下（following），也可以使用between指明上下边界的值，没有的话默认为当前分区。以下是所有可能的窗口子句定义组合

- [ ]

### 窗口函数操作

### **NTILE函数操作**

NTILE(n)，用于将分组数据按照顺序切分成n片，返回当前切片值

- [ ]

### ROW_NUMBER函数操作

ROW_NUMBER()从1开始，按照顺序，生成分组内记录的序列。

比如，按照pv降序排列，生成分组内每天的pv名次。

ROW_NUMBER() 的应用场景非常多，再比如，获取分组内排序第一的记录。

### RANK和DENSE_RANK函数操作

RANK() 生成数据项在分组中的排名，排名相等会在名次中留下空位  这个空位是什么意思呢

就是12335

出现相同的序号直接跳过4 留了一个空位 到 5

DENSE_RANK() 生成数据项在分组中的排名，排名相等会在名次中不会留下空位

###  LAG函数操作

用于统计窗口内往上第n行值

第一个参数为列名，第二个参数为往上第n行（可选，默认为1），第三个参数为默认值（当往上第n行为NULL时候，取默认值，如不指定，则为NULL）

- [ ]

##### **LEAD函数操作**

与LAG相反，LEAD(col,n,DEFAULT) 用于统计窗口内往下第n行值

第一个参数为列名，第二个参数为往下第n行（可选，默认为1），第三个参数为默认值（当往下第n行为NULL时候，取默认值，如不指定，则为NULL）

###  FIRST_VALUE函数操作

取分组内排序后，截止到当前行，第一个值

### **ROWS BETWEEN窗口子句操作**

- [ ]

## **数据压缩与存储**

### **行式存储和列式存储**

#### **行式存储**

特点：查询速度快 因为你只需要找一个 其余的都在附近 没必要在去其他块里寻找了

优点：具备快速数据加载和动态负载的高适应能力，因为行存储保证了相同记录的所有域都在同一个集群节点。

高负载的意思就是能够在数量大的时候进行扩容

缺点：但是它不太满足快速的查询响应时间的要求，特别是在当查询仅仅针对所有列中的少数几列时，它就不能直接定位到所需列而跳过不需要的列，由于混合着不同数据值的列，行存储不易获得一个极高的压缩比。

#### 列存储的特点

1.因为每个字段的数据聚集存储，在查询只需要少数几个字段的时候，能大大减少读取的数据量

2.每个字段的数据类型一定是相同的，列式存储可以针对性的设计更好的设计压缩算法。

**优点**是：这种结构使得在查询时能够直接读取需要的列而避免不必要列的读取，并且对于相似数据也可以有一个更好的压缩比。

**缺点**是：它并不能提供基于Hadoop系统的快速查询处理，也不能保证同一记录的所有列都存储在同一集群节点之上，也不适应高度动态的数据负载模式。

#### 常见的存储格式

TEXTFILE 、SEQUENCEFILE、AVRO、RCFILE、ORCFILE、PARQUET

其中TEXTFILE 、SEQUENCEFILE和AVRO是行式存储

RCFILE、ORCFILE、PARQUET是列式存储

传统的关系型数据库，如 Oracle、DB2、MySQL、SQL SERVER 等采用行式存储(Row-based)

新兴的 Hbase、HP Vertica、EMC Greenplum 等分布式数据库均采用列式存储

### 文件存储格式

TextFile：每一行都是一条记录，每行都以换行符（\ n）结尾。数据不做压缩，磁盘开销大，数据解析开销大可结合Gzip、Bzip2使用，使用这种方式，hive不会对数据进行切分，从而无法对数据进行并行操作。

1.正常的文本格式

2.TEXTFILE 存储文件默认每一行就是一条记录，可以指定任意的分隔符进行字段间的分割

3.一般只有与其他系统由数据交互的接口表采用TEXTFILE 格式，其他事实表和维度表都不建议使用

使用场景：与其他系统由数据交互的接口 还有就是实验场景

SequenceFile：

是Hadoop API提供的一种二进制文件支持，其具有使用方便、可分割、可压缩的特点。支持三种压缩选择：NONE, RECORD, BLOCK。 Record压缩率低，一般建议使用BLOCK压缩。

SequenceFile是Hadoop API 提供的一种二进制文件，它将数据以<key,value>的形式序列化到文件中

RCFile：

是一种行列存储相结合的存储方式，首先，其将数据按行分块，保证同一个record在一个块上，避免读一个记录需要读取多个block。其次，块数据列式存储，有利于数据压缩和快速的列存取。

1.存储结构遵循的是“先水平划分，再垂直划分

2.RCFile结合了行存储和列存储的优点

3.RCFile保证同一行的数据位于同一节点，因此元组重构的开销很低

4.像列存储一样，RCFile能够利用列维度的数据压缩，并且能跳过不必要的列读取

左边是关系式的表 有ABCD四列 有n行数据 ，把其中某些行进行一个划分，划分成单元格的一个数据模块 ，那么划分出来的数据模块就叫做行组

对于一张表，所有行组大小都相同

对于这张表来说，在hdfs上存储的时候，一般是按照hdfs块存储的，那么每一块的话，包含一个或多个行组

行组包括：

中间就是就是hdfs的一个块，拆成了n个行组，每行对应的就是右边的结构

那么这个结构的第一个部分就是行组的一个标识，这个标识存的就是用来分割hdfs中两个连续的行组

也就是是行组头部的同步标识，

第二部分就是行组的元数据头部信息，这里存的就是行组单元的信息，比如行组的记录数，每一列的字节数，每一列要用多少个字节存储

第三部分就是表格数据段，也就是表格的数据存储

4.RCFile采用游程编码，相同的数据不会重复存储，很大程度上节约了存储空间，尤其是字段中包含大量重复数据的时候

什么是游程编码

ORC：

提供了一种将数据存储在Hive表中的高效方法，这个文件系统实际上是为了克服其他Hive文件格式的限制而设计的。Hive从大型表读取，写入和处理数据时，使用ORC文件可以提高性能。

1.其实就是对RCFile做了一些优化

2.种文件格式可以提供一种高效的方法来存储Hive数据

3.它的设计目标是来克服Hive其他格式的缺陷

4.运用ORC File可以提高Hive的读、写以及处理数据的性能。

a、integer类型的列用行程长度编码(run-length encoding);b、String类型的列用字典编码(dictionary encoding)；

比如RCFile中的游程编码（行程长度编码）

和RCFile格式相比，ORC File格式有以下优点：

1.每个task只输出单个文件，这样可以减少NameNode的负载；

namenode里面记载的就是数据的元数据信息，你文件少，你读这个文件的数据量就少啊

2.支持各种复杂的数据类型，比如： datetime, decimal, 以及一些复杂类型(struct, list, map, and union)；

3.在文件中存储了一些轻量级的索引数据；

4.基于数据类型的块模式压缩

##### **ORC File文件结构**

stripe

咱们得表被划分多个stripe后

最下面有个file footer这么一个块 这个存的就是一些辅e助信息的记录

而且还包含了在orc file文件中的stripe的一些信息

比如说数据类型是什么样子的，还比如说第一列最大值最小值都会记录到file foote这个区域里

在file footer下还有一个Postscript,这个快是用来存储 压缩参数，以及压缩页脚的大小

stripe是250m的大小

包含了index data row data stripe footer这三个区域

其中stripe footer是包含了流位置的目录

row data就是一个具体的数据

index data是每一列最大最小值 每一列所在行的位置

stripe就相当于rc file里面的一个行组概念，只不过由4m到了250m

一般来说每隔1万行就做一个索引，这个索引是轻量级的，只记录每行的字段

读文件

一般是从后往前读

先Postscript 解析它里面存的和file footer相关的一些长度的信息，读取完之后通过file footer解析到stripe的各个信息

从而读取出数据

Hive里面如何用ORCFile

STORED **AS** ORC

### Parquet：

是一个面向列的二进制文件格式

来源：在大数据环境下，通常数据的来源是服务端的埋点数据，很可能需要把程序中的某些对象内容作为输出的一部分，而每一个对象都可能是嵌套的，所以如果能够原生的支持这种数据，这样在查询的时候就不需要额外的解析便能获得想要的结果。

支持嵌套结构的存储格式

parquet相较于orc的仅有优势：支持嵌套结构

不支持update操作(数据写成后不可修改),不支持ACID等

Parquet格式文件是自解析的

文件中包括该文件的数据和元数据

Parquet的数据模型:

HDFS块(Block)：它是HDFS上的最小的副本单位

HDFS文件(File)：一个HDFS的文件，包括数据和元数据，数据分散存储在多个Block中。

行组(Row Group)：按照行将数据物理上划分为多个单元

列块(Column Chunk)

页(Page)

映射下推、谓词下推

映射下推

AVRO：

是开源项目，为Hadoop提供数据序列化和数据交换服务,是一种用于支持数据密集型的二进制文件格式

### **数据压缩**

在 Hadoop 中用的比较多的有 lzo、gzip、snappy、bzip2。

压缩配置

- [ ]

中间压缩

就是处理作业map任务和reduce任务之间的数据，对于中间压缩，最好选择一个节省CPU耗时的压缩方式

输出压缩

作业最终的输出也可以压缩，hive.exec.compress.output这个属性控制这个操作

压缩格式

### gzip压缩

**【优点】**：

压缩率比较高，而且压缩/解压速度也比较快

hadoop本身支持，在应用中处理gzip格式的文件就和直接处理文本一样

大部分linux系统都自带gzip命令

**【缺点】**：不支持split。

### **lzo压缩**

**【优点】**：压缩/解压速度也比较快，合理的压缩率；支持split，是hadoop中最流行的压缩格式；支持hadoop native库；可以在linux系统下安装lzop命令，使用方便。

**【缺点】**：压缩率比gzip要低一些；hadoop本身不支持，需要安装；

### **snappy压缩**

高速压缩速度和合理的压缩率；支持hadoop native库。

不支持split；压缩率比gzip要低；hadoop本身不支持，需要安装；linux系统下没有对应的命令

### **bzip2压缩**

支持split；具有很高的压缩率，比gzip压缩率都高；hadoop本身支持，但不支持native；在linux系统下自带bzip2命令，使用方便

压缩/解压速度慢；不支持native。

## **性能调优****(☆☆☆重点掌握)**

### **查看SQL的执行计划**

执行计划就是描述SQL实际执行的整体轮廓

可以说执行计划是打开SQL优化大门的一把钥匙。

怎么查看执行计划？

**【方式】**

explain：查看执行计划的基本信息

explain dependency：

dependency在explain语句中使用，会产生有关计划中输入的额外信息，它显示了输入的各种属性。

**功能说明：**

Hive提供了explain命令来展示一个查询的执行计划

使用语法如下：explain query;

- [ ]

hive查询会被转换成一个或多个阶段组成的序列

这个查询是包括两个部分

- [ ]

- [ ]

在上方的map阶段做了什么操作呢？

第一就是TableScan操作，这个操作就是扫描输入的表

在这里有一些常用的属性

alias:这个就是输入的表的名称

Statistics：统计信息，统计了比如表的大小，表的行数，还有一些其他的信息

表扫描完就是 Select Operator查询操作

下面就是表达式 查询出来了哪一个字段

然后的操作就是输出了什么：outputColumnNames在上方的查询中输出的是pv

接着就是Statistics统计了下表的基础信息

然后接着就出现了一个Group By Operator的操作，分组聚合 这是一个模块

在分组聚合这个模块里的aggregations: 这个就是显示我们用了什么聚合函数  上表中使用的sum函数

接下来就是mode：这个意思是你聚合用的是什么模式 比如hash partitiom 等

Reduce Output Operator reduce的输出，这里是把map阶段的数输出给到reduce做一个相应的处理

在这里的话有sort order: 这里是排序 如果是空就是不排序 +号就是正排序 -号就是至少有一个字段做倒序排序

接下来就是reduce操作树了

 Group By Operator 也是有个这个操作

aggregations:

 mode

 outputColumnNames:
          Statistics

和map的操作是类似的

接下来就是文件的输出的操作File Output Operator

输出的时候文件是否压缩 compressed:

接着还是统计信息Statistics

接着就是表的格式信息/信息

     table:

上面就是Stage: Stage-1干的事情

那么Stage: Stage-0干了什么东西？

Stage: Stage-0，把结果拿到之后，再回到根节点的一个状态

STAGE DEPENDENCIES:

  Stage-1 is a root stage

根任务有一个最终拿结果的一个操作

 Fetch Operator

limit:这个是查多少条数据给客户端

#### **explain的使用场景**

场景案例-join语句

join 语句会过滤 null 的值吗？

- [ ]

从上述结果可以看到 predicate:user_id is not null 这样一行，说明join时会自动过滤掉关联字段为 null 值的情况，但left join或full join 是不会自动过滤null值的。

### explain dependency：

dependency在explain语句中使用，会产生有关计划中输入的额外信息，它显示了输入的各种属性

explain authorization：查看SQL操作相关权限的信息。

通过explain authorization可以知道当前SQL访问的数据来源(INPUTS)和数据输出(OUTPUTS)，以及当前Hive的访问用户(CURRENT_USER)和操作(OPERATION)。

explain vectorization：查看SQL的向量化描述信息。

用于描述一段SQL需要的数据来源，输出是一个json格式的数据

里面包含以下两个部分的内容：

>

>

>

### explain dependency使用

**【非分区表依赖】**

**简单SQL的执行计划**

>

#### explain dependency的使用场景

有两个

场景一：快速排除

快速排除因为读取不到相应分区的数据而导致任务数据输出异常

场景二：理清表的输入。

帮助理解程序的运行，特别是有助于理解有多重子查询，多表连接的依赖输入。

### 不同场景下的SQL的执行计划

#### 简单的SQL的执行计划

- [ ]

这个的执行流程可以很明确的看到只有一个Map树

执行的顺序就是

向select-from-where这种简单的SQL只有Map阶段，所以在效率上是不输spark的

### 普通函数SQL的执行计划

- [ ]

这个执行也只有select-from-where和简单的一样都是在map端过滤 都是在本地计算

### 聚合函数的SQL执行计划

- [ ]

这个就不一样了聚合函数的有map和reduce两个阶段

在这里只运行了count（*）则map可以输出context.write(null, count)，即key值能为null。如果hive.map.aggr=false，则map端没有Group By Operator。

设置hive.map.aggr=true，提高HiveQL聚合的执行性能。

这个设置可以将顶层的聚合操作放在Map阶段执行，从而减轻清洗阶段数据传输和Reduce阶段的执行时间，提升总体性能。

缺点：该设置会消耗更多的内存。

### **带窗口函数SQL的执行计划**

- [ ]

### **性能调优****(☆☆☆重点掌握)**

### 开启Fetch抓取（默认已开启）

Hive中对某些情况的查询可以不必使用MapReduce计算

例如：select * from user_base_info;

Hive可以简单地读取user_base_info对应的存储目录下的文件， 然后输出查询结果到控制台。

**【参数设置】**

hive.fetch.task.conversion默认是 more或者minimal）  在全局查找、字段查找、limit查找等都不走mapreduce。

hive.fetch.task.conversion设置成none  全局查找、字段查找、limit查找等都会执行mapreduce程序。

### **本地模式（默认未开启）**

hive.exec.mode.local.auto的值为true

**【参数设置】**：

//开启本地 mr

**set** hive.**exec**.mode.**local**.auto=**true**;



//设置**local** mr的最大输入数据量，当输入数据量小于这个值时采用**local** mr的方式，

默认为 134217728，即128M

**set** hive.**exec**.mode.**local**.auto.inputbytes.**max**=50000000;



//设置**local** mr的最大输入文件个数，当输入文件个数小于这个值时采用**local** mr 的方式，

默认为 4

**set** hive.**exec**.mode.**local**.auto.input.files.**max**=8;

### 表的优化

小表Join大表：

将 key 相对分散，并且数据量小的表放在 join 的左边，这样可以有效减少内存溢出错误发生的几率

使用 Group 让小的维度表（1000 条以下的记录条数）先进内存，在map 端完成 reduce。

Join小表默认进**内存的大小为25M**

**修改hive.mapjoin.smalltable.filesize=250**0000配置，改变默认大小一般修改最大值不能超过128M这个值刚好是MapReduce分块的最小单元，也是HDFS一个块的默认大小。

大表Join大表

1.空KEY过滤

除了要对null key 过滤，有时也会对key值为0的情况下进行过滤。事实上，就是过滤掉非法的或者异常的、无效的或者无意义的key值。

2.空key转换

又是空key不是异常数据，必须在join的结果中可以表 a 中 key 为空的字段赋一个随机的值，使得数据随机均匀地分不到不同的 reducer 上。

- [ ]

### **MapJoin（默认已开启）**

这个不指定或者不符合**MapJoin的条件，hive会将 Join操作转换成Common Join，在 Reduce 阶段完成 join**

容易发生数据倾斜

所以可以用 MapJoin 把小表全部加载到内存在 map 端进行 join，避免 reducer 处理。

- [ ]

一般修改最大值不能超过128M

#### MapJoin工作机制：

1.taska,在客户端本地执行task(Local Task)这是用来扫描小表的

将小表转换成HashTable的数据结构然后写入到本地文件中，加载到DistributeCache

2.taskb 这是一个没有reduce的Mr任务

启动Maptask扫描大表a

在Map阶段，根据a的每一条记录和DistributeCache 中的b表对应的HashTable进行关联 并输出结果

由于MapJoin没有Reduce，所以由Map直接输出结果文件，有多少个 MapTask，就有多少个结果文件。

### Group By优化

默认情况下，Map 阶段同一Key 数据分发给一个reduce，当一个 key 数据过大时就会产生数据倾斜

并不是所有的聚合操作都需要在Reduce端完成，很多聚合操作都可以先在Map端进行部分聚合，最后在Reduce端得出最终结果。

- [ ]

这样做生成的计划就会有两个MR Job

第一个 MR Job

Map 的输出结果会随机分布到Reduce中每个 Reduce 做部分聚合操作，并输出结果

这样处理的结果是相同的 Group By Key 有可能被分发到不同的 Reduce中，从而达到负载均衡的目的

第二个 MR Job

根据预处理的数据结果按照Group By Key 分布到Reduce中（这个过程可以保证相同的 Group By Key 被分布到同一个 Reduce 中），最后完成最终的聚合操作。

第一个预处理 第二个去报数据准确性

### Count(Distinct)去重统计

数据量小的时候无所谓，数据量大的情况下，由于 COUNT DISTINCT 操作需要用一个Reduce Task 来完成，这一个Reduce 需要处理的数据量太大，就会导致整个Job很难完成，一般 COUNT DISTINCT使用先GROUP BY再COUNT的方式替换。

- [ ]

虽然会多用一个Job来完成，但在数据量大的情况下，group by 依旧是去重的一个优化手段。如果说需要统计的字段有Null 值,最后只需要null值单独处理后union即可。

### 笛卡尔积

尽量避免笛卡尔积，join 的时候不加on条件，或者无效的on条件都有可能会产生笛卡尔积。Hive 只能使用1个reducer来完成笛卡尔积，会导致计算性能较低。

### 行列过滤

列处理：

在SELECT中，只拿需要的列，如果有，尽量使用分区过滤，少用SELECT *。

行处理：

在分区剪裁中， 当使用外关联时， 如果将副表的过滤条件写在 Where后面， 那么就会先全表关联，之后再过滤。

### **动态分区调整**

- [ ]

## **数据倾斜问题****(☆☆☆重点掌握)**

#### 什么是数据倾斜

绝大多数task执行得都非常快，但个别task执行极慢。比如，总共有1000个task，997个task都在1分钟之内执行完了，但是剩余两三个task却要一两个小时，这种情况很常见。进入任务的执行界面：reduce阶段卡在99.99%不动；各种container报错OOM（内存溢出）；读写数据量很大，超过其他正常reduce。

#### 数据倾斜的原理

在数据处理的时候map到reduce阶段 中间还有个shuff阶段 对数据进行一个重新排列的过程，将各个节点上相同的key拉取到某个节点上的一个task(任务)来进行处理，比如按照key进行聚合或join等操作。都要按照相应的key值进行一个处理

此时如果某个key对应的数据量特别大的话，就会发生数据倾斜。比如大部分key对应10条数据，但是个别key却对应了100万条数据，那么大部分task可能就只会分配到10条数据，然后1秒钟就运行完了；但是个别task可能分配到了100万数据，要运行一两个小时。因此，整个作业的运行进度是由运行时间最长的那个task决定的。

发生数据倾斜的原因在于Task的数据分配不均衡

分为两种情况：

数据本身就是倾斜的，数据中某种数据出现的次数过多

分区规则导致这些相同的数据都分配给了同一个Task，导致这个Task拿到了大量的数据，而其他Task数据量比较少，所以运行起来较慢。

#### 怎么解决数据倾斜 处理

一般看到map 100%和reduce99%的情况基本上就是数据倾斜了！

**【解决方法】**：

(1)开启 Map 端聚合参数设置（详见上文Group By）。

- [ ]

(2)或者根据业务，合理调整分组维度。

### **count(distinct)产生数据倾斜**

如果数据量非常大，执行如select a,count(distinct b) from t group by a;类型的SQL 时，会出现数据倾斜的问题。

**【解决方法】**：

使用 sum…group by 代替

如select a,sum(1) from (select a, b from t group by a,b) group by a;

有些时候是可以将倾斜的数据单独拿出来处理，最后union回去。

### **大表和小表 join产生数据倾斜**

使用 mapjoin 将小表加载到内存中。详见上文小表 join 大表

### **空值产生数据倾斜**

遇到需要进行 join 的但是关联字段有数据为空数据量大时也会产生数据倾斜

例子：

如日志中，常会有信息丢失的问题，比如日志中的user_id，如果取其中的user_id和用户表中的user_id 关联，会碰到数据倾斜的问题。表一的 id 需要和表二的 id 进行关联。

- [ ]

- [ ]

一般分配随机 key 值得方法更好一些。

### 合理设置map和reduce数避免数据倾斜

**【调整Map数】**

1.小文件进行合并，减少map数（默认开启）

在 map 执行前合并小文件，减少 map 数：

- [ ]

2.复杂文件增加Map数

场景：

input的文件都很大，任务逻辑复杂，map执行非常慢的时候

增加Map数，来使得每个map处理的数据量减少，从而提高任务的执行效率

- [ ]

增加map的方法为：根据公式，调整maxSize最大值：

computeSliteSize(Math.max(minSize,Math.min(maxSize,blocksize)))=blocksize=128M

让maxSize 最大值低于 blocksize 就可以增加 map 的个数。

**【调整Reduce数】**

调整 reduce 个数方法一：

- [ ]

调整 reduce 个数方法二：

- [ ]

## 面试实例

### 多维组合查询

group by可以进行分组统计的，我们将分组称之为统计的维度，例如GROUP BY month 我们认为维度是月份

例如GROUP BY month,day，我们的维度就是月份+日期的组合,这个组合也还是单维度的，因为什么呢，你依然得不到每个月的单独统计信息，也得不到每天的单独统计信息！

#### 所以以怎么解决呢？

使用Hive OLAP多维聚合函数

多维组合查询就是增强版的Group BY的语句，也叫多维聚合函数

hive三中常用的多维聚合函数：

##### With Cube任意维度聚合

Cube简称数据魔方，可以实现hive多个任意维度的组合查询，cube(a,b,c)则首先会对(a,b,c)进行group by，然后依次是(a,b),(a,c),(a),(b,c),(b),(c),最后在对全表进行group by，他会统计所选列中值的所有组合的聚合。

这就像穷举法 吧所有的组合都给列出来

- [ ]

- [ ]

聪哥对比就能很简单的看出来 把所有可能的结果全部输出出来

但是同样的数据太多不合格的数据太多 一般就是将结果解析了之后在使用！！

- [ ]

##### Grouping Sets指定维度聚合

在一个GROUPING SETS查询中，根据不同的单维度组合进行聚合，等价于将不同维度的GROUP BY结果进行UNION ALL操作。

- [ ]

这个查询和

- [ ]

第一栏是按照month

第二栏是day

第三列是按照month或day分组，统计这一组有几个不同的userid；

第四列grouping_id 这个是表示这个数据是属于哪一个分组的！

##### With Rollup层级维度聚合

Rollup可以实现从右到左的递减多级的统计，显示统计某一层次结构的聚合。

它是CUBE的子集，以最左侧的维度为主，从该维度进行层级聚合。

比如以month维度进行层级聚合，可以实现这样的上卷过程：

月天的UV->月的UV->总UV

- [ ]

NULL    NULL            7       0

2021-04 NULL            6       1

2021-03 NULL            5       1

2021-04 2021-04-16      2       3

2021-04 2021-04-15      2       3

2021-04 2021-04-13      3       3

2021-04 2021-04-12      2       3

2021-03 2021-03-12      1       3

2021-03 2021-03-10      4       3

这几个分析函数通常不能累加，而且需要根据不同维度上钻和下钻的指标统计，比如，分小时、天、月的UV数。

### **行转列**

行转列的代码是

-使用函数：concat_ws(',',collect_set(column))

--说明：collect_list不去重，collect_set去重。column的数据类型要求是string

**select** user_id,

concat_ws(',',collect_list(order_id)) **as** order_value

**from** user_order

**group** **by** user_id

这个的意思就是他从user_order表中选取user_id通过concat_ws函数连接order_id 并且使用collect_set函数对order_id进行去重

在通过user_id进行分组

什么意思呢

现在不是 104399 有7行么 现在让104399变成1行

这就是查出来的结果简单来说就是让对应关系转变一下！

### **Top-N问题**

这个问题的本意就是找到前几名的选项

原始数据

- [ ]

#### **查询每个店铺访问次数最多的前三名用户**

**【问题描述】**

每个顾客访客访问任何一个店铺的任何一个商品时都会产生一条访问日。

访问日志存储的表名为Visit，访客的用户id为user_id，被访问的店铺名称为shop.

请统计每个店铺访问次数top3的访客信息.输出店铺名称、访客id、访问次数

**【解决方案】**

// 3. 取前三名

**select** shop,user_id,visit_num **from**(

// 2. 统计每个店铺各用户的访问次数排序

    **select** shop,user_id,visit_num,

    row_num() over(partition **by** shop **order** **by** visit_num **desc**) **as** visit_sort

     **from**(

        // 1. 统计每个店铺中每个用户的访问次数

        **select** shop,user_id,count(1) **as** visit_num **from** visit

        **group** **by** shop,user_id

        )temp1

)temp2

**where** visit_sort<=3

这个查询也是子查询嵌套

首先从最外层开始  统计每个店铺中每个用户的访问次数

查询了shop,user_id

count(1) **as** visit_num是对每一个shop,user_id进行统计

最后进行shop,user_id  分组

这个子查询查完的结果会到上一个子查询里

这个子查询 统计每个店铺各用户的访问次数排序

这里是窗口查询 将按照shop 分区按照visit_num从高到低进行排序 并且为每行分配一个唯一的数值

### 拉链表的实现
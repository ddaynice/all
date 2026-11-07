### spark生态？

主要来说分为上中下三层

上层：Spark SQL、Spark Streaming、MLlib、GraphX

中层：spark core

下层：5种部署模式Local，Standalone，Yarn，Mesos，K8s

最底层就是存储系统

### Spark SQL

这个是spark用来处理结构化数据的一个模块，它提供了DataFrame和DataSet，并且还有作为分布式SQL查询引擎的作用。

Spark SQL是通过spark core转换成rdd算子，然后提交到集群中执行

### 你刚才说了部署模式，能具体的说一说么？

#### Spark on yarn分为那两种模式?能具体的说一说么？

分为Client模式和cluster 模式

#### Client模式

步骤

#### cluster 模式

### 使用场景

### Spark的集群架构你讲一下？

#### 核心组件

Driver、Executor  Mester  Worker  AplicationMaster

### 那么Driver是什么？

> 

> 

> 

> 

> 

> 

### Executor是什么？Executor的作用是什么？

> 

> 

### SparkConf、SparkContext、SparkSession三个类的用途？

      SparkContext 是通往 Spark 集群的唯一入口

### Spark的任务执行流程？

### 那你能说下spark在运行的流程么？

### 那你能说下什么是stage么？

Stage：由宽依赖数决定，一个Job可能包括多个Stage

### 一个Stage的Task数量由什么决定？

是由输入文件的切片个数决定的，一个分区对应着一个task，取决于该Stage最后一个RDD的分区数。

### Stage的划分逻辑？

> 

> 

> 

### 宽窄依赖能讲一讲么？

> 

> 

> 

> 

> 

### Application/Job/Task的关系？各自如何划分？

### 一个Job的总Task数量有什么决定？

job里面可以有一个或者多个stage但是stage又可以有多个task所以数量就是（stage 数量 * task 数量）的总和。

### RDD是什么？

### rdd5大核心是什么？

### 那你说下spark的宽窄依赖？

Spark的调度系统会通过DagScheduler 这个组件把DAG拆分成为不同的运行阶段，，也就是Stages

Stages的拆分过程其实是以 Actions 算子为起点，从后向前回溯 DAG，以 Shuffe 操作为边界去划分 Stages.

宽依赖，父 RDD 的一个分区会被子 RDD 的多个分区使用。

窄依赖，父 RDD 的分区最多只会被子 RDD 的一个分区使用。

**父 RDD 的 Partition 流向，要是流向单个 RDD 就是窄依赖，流向多个 RDD 就是宽依赖**

### 宽窄依赖常见的算子有哪些？

窄依赖：filter(),map,flatMap()

宽依赖：aggregateBykey(),reduceBykey()

### 那么Spark的Stage是怎么划分的

Spark Application中可以因为不同的Action触发众多的job，每个Application中可以有很多的job，每个job是由一个或者多个Stage构成的，后面的Stage依赖于前面的Stage

也就是说只有前面依赖的Stage计算完毕后，后面的Stage才会运行。

Spark划分Stage的整体思路是,根据DAG计算流图,从后往前推,遇到宽依赖就断开,划分为一个Stage,遇到窄依赖就将这个RDD加入该Stage。

### 一个Stage的Task数量由什么决定？

是由输入文件的切片个数决定的，一个分区对应着一个task，取决于该Stage最后一个RDD的分区数

### spark的容错机制你能讲一讲么？

容错机制一般来说是有两种，数据检查和记录数据的更新

那么spark的容错机制是记录数据的更新！

因为数据检查点其实需要通过数据中心的网络连接在不同的机器之间复制数据，而网络的带责往往比内存的带宽低的多，并且需要消耗大量的存储资源，但记录的太细其实也会消耗大量的资源，所以RDD只支持相粒度的转换，也就是RDD的DD的容错机制又称“血统(ineage)”)记录下来，以便恢复丢失的分区

### Spark Checkpoint可以详细说明一下嘛 ?

Checkpoint检查点是通过将 RDD 中间结果写入磁盘

由于血缘依赖过长会造成容错成本过高，这样就不如在中间阶段做检查点容错

如果检查点之后有节点出现问题，可以从检查点开始重做血缘，减少了开销

### cache 和 checkpoint区别

> 

> 

> 

> 

> 

### Spark Checkpoint的本质是做了什么呢?

检查点(本质是将RDD写入磁盘做检查点)是为了lineage做容做的辅助,Lineage过长会导致容做成本过高,可以在中间做检查点,如果之后有节,点出问题而丢失数据,从检查点开始做lineage;减少开销,

### 可以举例说明你在场景情况下会用Checkpoint ?

我在开发过程中使用检查点的场景不是很多,唯一用的场景就是在Spak开启动态分区播入的场景中，有时候两个应用同时写一张表会有冲突，会抛出异常，这时我们会在异常地出之后进行checkpoint，,在尝试写入。这里有点要注意一下，我们在做检查点一般都有要先对df.cache一下，因为checkpoint操作其实也是action操作，会触发runJob

### RDD的分区器有过了解么？

Spark目前支持hash分区和Range分区，hash分区是当前的默认分区

但是只有key-value类型的RDD才有分区器的，非key-value类型RDD分区器的值是none

#### Hash分区(默认分区器)

Hash分区的原理:对于给定的key,计算其hashCode,并除以分区的个数取余,如果余数小于0,则用余数+分区的个数(否则加0),最后返回的值就是这个key所属的分区ID。

HashPartitioner分区弊端:可能导致每个分区中数据量的不均匀,极端情况下会导致某些分区拥有RDD的全部数据

#### Range分区

将一定范围内的数陕射到某一个分区内,尽量保证每个分区中数据量的均匀,而且分区与分区之间是有序的,一个分区中的元素肯定都是比另一个分区内的元素小或者大，但是分区内的元素是不能保证顺序的，简单的说就是将一定范围内的数映射到某一个分区内。

实现过程为:

第一步:先重整个RDD中抽取出样本数据,将样本数据排序,计算出每个分区的最大key值，形成一个Aray[KEY]类型的数组变量rangeBounds;第二步:判断key在rangeBounds中所处的范围,给出该key值在下一个RDD中的分区id下标;该分区器要求RDD中的KEY类型必须是可以排序的

RangePartitioner分区弊端:要求数据可排序

### 那你说下spark的action算子

取数据：first，taken(n)

迭代和回收：foreach,collect

聚合：reduce,aggregate,fold,count,countBykey

保存为文件：saveAsTexFile
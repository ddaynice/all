审批：具体位置在在https://pwaibao.woa.com/  进入系统-个人中心-我的审批-待处理进行审批或手机直接myoa快速审批

## 简单知道

### 主流版本

https://www.wanyiwan.top/game/sgbhsd

Apache Flink 1.10.0 于 2020年02月11日正式发布。Flink 1.10 是一个历时非常长、代码变动非常大的版本，也是 Flink 社区迄今为止规模最大的一次版本升级，Flink 1.10 容纳了超过 200 位贡献者对超过 1200 个 issue 的开发实现，包含对 Flink 作业的整体性能及稳定性的显著优化、对原生 Kubernetes 的初步集成以及对 Python 支持（PyFlink）的重大优化。

**Flink1.10.0 完美整合了阿里的BLink、支持了YARN模式下的跨Task资源共享，并强化了对Hive的支持。随着 Flink 1.10 版本的发布，Blink 合并的正式完成，Flink 作业的整体性能及稳定性有了显著优化，越来越多的企业开始采用 Flink 用于生产环境**

### 版本特点

这个看文档

## flik重要特点

### 有状态和无状态

#### 无状态：

无状态计算观察每个独立的事件，storm就是无状态的计算框架，每条消息来了之后以后和以前都没有关系,来一条是一条。

无状态流处理：来一条处理一条，每一条数据都是独立的

有状态流处理：是维护了一个记录，比如记录最大值是多少，但是spark不是也能记录最大值么，我们说spark记录的最大值是吧所有的计算，所有的数据处理完成之后，比如10个g的数据，是不是要把10个g的数据处理完之后得到一个最大值！-这是和状态没有关系，这是一个最终的结果

我们说有状态，像源源不断的流水一样，我们并不知道这个数据的边界在哪里，那我们怎么计算最大值呢？

所以想流这种其实是没有最大值的一个概念的，它有的只是某一节最大值是多少！

说白了就是说有状态的就是把一个结果给保存下来，然后来的数据和那个结果做比较！类似冒泡排序！

### 流与批的世界观

流：

数据是无界的，实时的，不需要对整个数据集进行一个操作，比如去重

#### 事件驱动型

我们说flink是事件驱动型的

就是说你来了一个最大的值，比上一个最大值还大就是

事件驱动在传统的存算分离

transactional

## Flink运行组件

Flink包括哪些组件？

flink它是一个典型的master - selever 架构 

那么就肯定需要一个master-叫jobmanager

这里有的博客说job其实是位于master节点的，就是他是有一个真实的master节点

那master节点包括三个部分：jobmanger,**Dispatcher**,resourManager，这里是很多博客去说的

但是我们说一定要以官网为依据

那这里官网上是说：**ResourceManager，Dispatcher，JobMaster**

很少有人去说**JobMaster，也有可能是之前的版本**

但是现在已新的版本来说，一定是只有两大节点 1.jobmanger 2.taskmanagers

## Flink分层

Flink可以分未

SQL:这个就是类似关系型SQL查询

Table API:声明式 DSL，以表为中心

DataStream/DataSet API:核心 API，面向流/批数据处理

Stateful Stream Processing:最底层，提供流、状态、事件时间等基础能力

这四个顺序是从下到上

最底层就是 

## 四大基石头

State,time,checkpoint,window

State：

可以看作是基座

主要是有两个点，一致性语义，因为State本身就带有一致性语义

然后还提供了State API`ValueState`（存单值，如计数器）、`ListState`（存列表）、`MapState`（存键值对）、`BroadcastState`（广播状态，常用于"一份规则配置广播给所有算子、和数据流做匹配"的场景）

这个就是翻译的意思状态，流处理是“持续不断的”，所以很多计算是要记住之前发生的事情，

所以说 State 是上层应用的基座、是实现实时的必要条件。

Checkpoint —— 一致性的来源

 Chandy-Lamport 分布式快照算法,解决的是分布式系统里每个节点各自自拍的快照，怎么去保证拼起来的是一个“全局一致”的瞬间？

通过在数据流中插入barrier（屏障）来切分，各算子看到 barrier 就拍快照，最终所有快照对应同一个逻辑时间点

time：这个是解决乱序

Time的核心是Watermark机制，这个是流中携带的一种时间标记，含义是我认为时间时间早于T的数据基本都到齐了。窗口靠它来决定何时触发计算，何时关闭。

Window —— 计算的载体

流计算中一般在对流数据进行操作之前都会先进行开窗，即基于一个什么样的窗口（Window）上做这个计算。Flink 提供了开箱即用的各种窗口，比如滑动窗口、滚动窗口、会话窗口以及非常灵活的自定义的窗口

哪整体来说就是

window按照Time/Watermark划定计算边界 -> 中间结果会存进State-> Checkpoint（Chandy-Lamport 快照）保证 State 故障可恢复、结果精确一次。

**什么是事件驱动？**

其实是一种架构/编程范式：程序不是被动的被调用，被轮询，而是当作某件事发生（事件到达）的时候，主动触发相应的处理逻辑。

就是来了事件->立刻反应。就像烟雾报警器，不是有人每隔1分钟去检查有没有烟（轮询），而是烟雾一出现（事件），报警器立刻响（触发处理）

## 第一章记录：

简介这里要知道flink是个什么框架，我们叫做有状态的实时流框架

国内情况呢国内大厂都在用

主流特点了解下：

阿里巴巴的代码flink是什么时候合到主版本里面的1.10 国内最稳定的是什么版本1.15

比较重要掌握的：

什么叫做事件驱动，什么叫做有状态无状态，什么叫做流批世界观，flink4大基石有哪些啊

应用场景:如果业务室上游变动想及时的在下游体现

常见流框架：介绍技术选型 你为什么要选择flink

## Flink组件

### 这是最重要的

### 组件栈

这里在看flink的组件的时候可以去类比下spark的

Spark core对应的就是flinkcore

那么flink上层应用对应的就是 spark sql ,spark streaming 这些

下层就是各种调度模式 

那么flink的核心就是runtime 也叫flink core

核心的数据结构叫做 分布式流数据 spark的核心叫做rdd

整体的去看Flink的分层架构，每一层的组件都包含了特定的抽象，来服务于是上层组件

最低层：Deployment层 这个就是部署层，和spark类似，只不过spark最底层是存储比如hdfs这些

往上就是Runtime层 这一层 对标的是spark core 这里提供的支持flink计算的全部核心实现，比如支持分布式Stream处理、JobGraph到ExecutionGraph的映射、调度等等，为上层API层提供基础服务

在往上就是API层，这里分为两个部分 流处理和面向Batch的批处理API，面向流处理对应DataStream API，面向批处理对应DataSet API。

最上层就是应用层框架。根据API层的划分，在API层之上构建的满足特定应用的实现计算框架，也分别对应于面向流处理和面向批处理两类。面向流处理支持：CEP（复杂事件处理）、基于SQL-like的操作（基于Table的关系操作）；面向批处理支持： FlinkML（机器学习库）、Gelly（图处理里）

所以这些大数据的框架其实都是类似的，像MR SPARK等等，都是一套从下到上的

其实对于flink最重要的就是Bath和Streaming共同使用同一个处理引擎

Stream API ：datastream 

Bath API: dataset 

Dataset 往下有一个优化执行计划 OptimizedPlan

datastream  往下有个流图结构我们叫做DAG

##### 问题：就是Batch和Streaming是如何使用同一个处理引擎进行处理的？

切换么？通过使用的时候去切换么，还是说是两条路流一条？批一条？他们互不影响？

使用场景不一样，所以？

它这里其实是入口分两条路，然后底下在汇成一条路。

> 

> 

Batch API -> OptimizedPlan   ↘

                               JobGraph → ExecutionGraph → 物理执行（TaskManager 上的 tasks）

Stream API → StreamGraph    ↗

##### Flink程序的执行流程

写代码 -> 

StreamGraph（流）/ OptimizedPlan（批）  客户端生成 ->

JobGraph      客户端生成，提交给 JobManager   ->

ExecutionGraph    JobManager 生成  ->

物理执行图（真正跑在 TaskManager 上）

这个是大致的执行的过程

###### 哪什么是JobGraph？

在写java的时候 会有最后一句env.execute()这个

调用的时候客户端就会把代码转换成一张图，这个图就是JobGraph

哪这个图里包含了：

JobVertex：一个个算子节点（比如你的 map、filter、keyBy+reduce 等）

JobEdge：节点之间的数据传输关系

IntermediateDataSet：中间数据集，表示一个节点产出的数据

其实说人话就是

比如我现在写的代码是要做一个汉堡，薯条什么的

JobGraph 就是我给经理看的一个正式运营流程图 ："A 工位负责煎肉饼→B 工位负责组装汉堡→C 工位负责打包"

###### 哪什么是OptimizedPlan？

这个就是优化后的执行计划，但是这个是批处理才会

你的 DataSet 代码

    ↓

生成一个初步的执行计划（类似 Plan）

    ↓

【优化器介入】← 这里做很多优化

    ↓

生成 OptimizedPlan（优化后的计划）

    ↓

再转换成 JobGraph

    ↓

提交给 JobManager

但是不管是流还是批 在JobGraph做了统一

我们说flink要做到流批一体，就是Stream 和Bath 如何使用同一个处理引擎的

**Batch和Streaming采用的不同的ExecutionEnviroment，对于ExecutionEnviroment来说读到的源数据是一个DataSet,而 StreamExecutionEnviroment的源数据来说则是一个DataStream**

你的批处理和流处理：Batch和streaming会有两个不同的ExecutionEnvironment ，就是我们说的采用不同的**ExecutionEnviroment**

不同的ExecutionEnvironment会将不同的API翻译成不同 的JobGraph，JobGraph上除了 StreamGraph 还有 OptimizedPlan

但是有个问题为什么api不能直接转换成JobGraph，还得中间过一道？

因为Bath 是批我提前知道我整个数据的规模，我知道我的数据大概是一个什么样子的结构，那就可以使用分析的方法优化

但是对于流来说，我不知道数据有多少，那就不存在我对你的sql怎么进行优化

所以这个就是由JobGraph 做一个统一的图，不管你上面是什么到我zhe全都是job图

### 运行时组件

运行时组件时Runtime，可以理解为是一个分布式系统，其实就是和批的分布式一样，接收数据流程序，可以在一台或者多台机器上执行这些数据流程序。

可以单机，也可以放到YARN上运行。

我们说flink是一个典型的mast-slever 架构 

或者用现在的话说叫做master-worker 架构

由一个Flink JobManager和一个或者多个Flink TaskManager组成呢个的

哪这里肯定就要有一个mastrer 这里叫做Jobmanager 作业管理器

右边就是整体的架构图

在左边的AM（application Manager） 它的部分时Master 

它负责管理整个集群中的资源并且处理作业的提交，作业监督

右边的两个TaskExecutor 则是 Slave

这块就是工作进程

哪整个流程

首先通过客户端向集群提交应用程序

哪然后就启动Application Master

Cluster Management 这里就启动JobManager

在YARN模式下先启动的是Application Master

然后就是第三步，进行提交作业

Client会提交到JobManager


接着第四步会生成（JM）JobManager 实例

由Dispatcher创建JobMaster

第五步这里会向ResourceManager申请slot,申请计算资源槽位

第六步申请了，就要进行资源的分配

Cluster Management跟据请求进行资源分配

第7步这里还是Cluster Management 生成TaskManager

第8步这里ResourceManager向TaskManager 请求具体的Slot槽位

第九步这里TaskManager进行slot的提供

第10步这里进行提交任务将task分发到Slot上执行

哪上面这么多名词，我们现在就要清楚这些

#### 作业管理器JobManager 

JobManager 其实就像spark里的Driver的一个功能

我们说JobManager处于master地位那么他就处于一个领导地位 ，就干一些领导该干的活

负责接收任务，负责处理任务，负责拆解任务，负责分配任务

然后把这些任务分配给干活的人 taskmanager 上的一些资源一些Exectur这些

**每个应用都应该被唯一的 JobManager 所控制执行**。

**JobManager会先接收到要执行的应用程序，这个应用程序会包括：**

**作业图（JobGraph）、逻辑数据流图（logical dataflow graph）和打包了所有的类、库和其它资源的JAR包**

JobManager会把JobGraph转换成一个物理层面的数据流图，这个图被叫做“执行图”（ExecutionGraph），包含了所有可以并发执行的任务。

**JobManager会向资源管理器（ResourceManager，这里的是Yarn等上的不是flink内部的）请求执行任务必要的资源，也就是任务管理器（TaskManager）上的插槽（slot）**。

一旦它获取到了足够的资源，就会将执行图分发到真正运行它们的TaskManager上。

而**在运行过程中，JobManager会负责所有需要中央协调的操作，包括任务调度，检查点管理，失败恢复等**。

当然，对于集群HA模式，可以同时多个master进程，其中一个作为leader，其他作为standby。

当leader失败时，会选出一个standby的master作为新的leader（通过zookeeper实现leader选举）。

#### 总结下JobManager 有哪些功能

> 

> 

> 

> 

> 

**资源管理器-ResourceManager**

具体干活的是taskmanager，哪taskmanager是以什么形式给你干活呢？

我们说spark 的manager,就是我们用executer

在flink中资源就是taskmanager 上的slot

##### 什么是slot

就比如我现在这个taskmanager上面有10G内存 

在第taskmanager上设置3个slot 哪每一个sloat就是10/3

**所以在flink中只有内存是可以隔离的，CPU是不隔离的，内存就是以slot形式隔离**

**果ResourceManager没有足够的插槽来满足JobManager的请求，它还可以向资源提供平台发起会话，以提供启动TaskManager进程的容器。**

**另外，ResourceManager还负责终止空闲的TaskManager，释放计算资源。在整个 Flink 集群中只有一个 ResourceManager。**

**这里的ResourceManager和Yarn中的ResourceManager不是一回事儿。**

这里的**ResourceManager是管理slot的**

**Yarn中的ResourceManager是管理的continer 容器**

**这个资源管理器主要是负责插槽的（slot）的资源提供，回收和分配等等**

**分发器-Dispatcher**

分发器就是相当于提供一个接口，提供一个入口，那这个入口就是用来提交flink程序的，**并为每个提交的作业启动一个新的 JobMaster**

我们通过客户端提交的任务会先提交到分发器上，在由分发器决定给哪一个JobManager 去执行

**JobMaster**

JobMaster 负责管理单个JobGraph的执行。

JobGraph返回的值就是由JobMaster 去收集的

Flink 集群中可以同时运行多个作业，**每个作业都有自己的 JobMaster**。 

##### 任务管理器-taskManager

这个是管理集群上有哪些slot

**每一个TaskManager都包含了一定数量的插槽（slots），TaskManger插槽是Flink中定义的处理资源单元**

它其实共享的是内存，CPU还是集群的cpu

slots可以

TaskManager 里面的主要组件有：

> 

> 

> 

#### 总结

这里说了flink内部的一个组件，两个方面

JobManage

这里分三部分**ResourceManager，Dispatcher，JobMaster**

分别是申请资源的，接收任务去分发任务的，然后具体去处理任务的

JobManage的功能就是体现在上面三个角色上面

TaskManage

这个是真的干活的去提供资源的

提供的资源是slot，没一个slot上面运行的是一个任务啊，那有多少slot就是由多少个具体的任务

### 任务提交流程  - flink在提交一个应用流程的时候是什么样子的

首先提交任务的时候会提交到Dispatcher，然后Dispatcher会启动并提交任务到JobMaster

JobMaster 会向**ResourceManager请求Slots**

请求slots之后**ResourceManager就会启动注册相应的TaskManager**

然后发出我要提供多少slots的指令

那么一旦启动好了JobMaster 就会把相应拆解后的任务提交到**TaskManager执行**

然后**TaskManager之间也是去交换数据的**

从这个图上可以看到整个的调度系统是比较宏观的

#### 以YARN为例子

flink提交任务之后 ，client向HDFS上传Flink的jar包和配置

然后就会向YARN的ResourceManager提交任务，这里的

ResourceManager会分配Container资源，并且通知对应的NodeManager启动ApplicationMaster

AM启动之后会加载Flink的Jar包和配置构建环境，然后启动JobManager
这里的Jar包就是一开始上传的

在之后ApplicationMaster向ResourceManager申请资源启动TaskManager，
ResourceManager分配Container资源后

由ApplicationMaster通知资源所在节点的NodeManager启动TaskManager

同样NodeManger也会加载Flink的jar包和配置构建环境并且启动TaskManager

最后TaskManager启动后向JobManager发送心跳包，并等待JobManager向其分配任务。

#### 任务调度原理

这里就是flink写的程序怎么一步一步的放在了具体的taskmanager上去执行

以及taskmanager上面那些东西在执行以及各个节点之间的交互方式

#### 首先看白色的框的内容

其实在白框这里整个都是一个客户端

红色的就是我们的程序写的代码，如果我们写的是一个批作业，要做一个OPtimerizer ,流作业就是StreamGroaph

这里就是做了一些优化，生成的是一个数据流图 jopgraph

然后这个数据流图由客户端通过actor系统提交到 JobManager上

这个任务实际上发送的就是数据流图

那这个节点之间的交互就是actor系统交互的

提交任务之后，这个任务就会进行一个调度，调度拆解完了之后*（这里拆解的就是那个流图）再交给actor系统

然后actor系统就会把这个任务分发到其他的TaskManager上

具体执行的就是TaskManager的slot 然后会定期通过actor系统 把task的一个状态，相关指标的统计，心跳

返回给JobManager

任务完成了之后，JobManager又会通过actor系统把任务的口径，任务返回的结果更新到客户端

#### taskmanager和slot的关系

我们说Flink中每一个worker(TaskManager)都是一个**JVM进程**，**为了控制一个worker能接收多少个task，worker通过task slot来进行控制（一个worker至少有一个task slot）**

简单的理解就是说一个task-slot它就是一定的内存+一个cup可以这样理解

每个task slot表示TaskManager拥有资源的**一个固定大小的子集**

**Task的并行度是由运行在Task Manager中的task slots的数量决定。**

我这个程序同时运行多少个任务就是看**task slots**

**如果一个Task Manager有4个slots，那么JVM的内存将平均分配给每个task slot 25%的TaskManager的可用内存。**

一个Task slot中可以运行1个或多个线程，同一个slot中的线程又可以共享相同的JVM。

将资源 slot 化意味着来自不同job的task不会为了内存而竞争，而是每个task都拥有一定数量的内存储备。

而**在同一个JVM进程中的task将共享TCP连接（基于多路复用）和心跳消息。它们也可能共享数据集和数据结构，因此这减少了每个task的负载。**

所以这里我们说的slot一定是均分的内存

**一个taskmanager上的slot的个数由参数：taskmanager.numberOfTaskSlots决定，仅仅对内存做了隔离，并没有对cpu进行隔离。**

总结：

其实taskmanager就是相当于一个资源池，sloat就是均衡资源池的每一个槽位

我们说slot概念是flink里面独有的，在spark指定任务的时候可以指定executer的内存，核数

所以这个slot作用就是把每一个任务进行隔离但是cpu没有隔离，所以cpu是共享的 心跳机制也是共享的

#### slot和parallelism关系

在执行过程中一个可能包含很多个分区，哪这个分区可能就是逻辑上的分区

那么在分布式环境下，那么一个算子我们称为一个任务

每一个算子（operator）可以包含一个或多个子任务（operator subtask）

这些子任务在不同的线程、不同的物理机或不同的容器中彼此互不依赖地执行

我们说一个特定算子的子任务的个数就称为并行度，那这里的并行度是一个动态的概念

**一般情况下，一个流程序的并行度，可以认为就是其所有算子中最大的并行度。一个程序中，不同的算子可能具有不同的并行度。**

那这里slot和parallelism关系

哪这里就要搞清楚slot和parallelism 是什么

概念

是什么

一句话理解

**Parallelism（并行度）**

一个算子拆成几份

决定"需要几个人干活"

**Subtask**

拆分后的每一份

真正干活的那个人

**Slot**

工位

给 Subtask 坐的地方

**一个 Slot 里可以坐多个 Subtask，但一个 Subtask 只能坐一个 Slot。**

Flink 会尽量把一条完整链路（Source → Map → Sink）的 Subtask 塞进同一个 Slot。

**你需要的 Slot 总数 = 所有算子中最大的并行度**

在spark中师没有程序所谓的最大并行度的概念，因为spark分为各个stage，只能说一个stage里面的并行度是多少，而且stage里面的并行度是一致的没有最大并行度这个说法！

上面的图 在spark中叫做DAG图，在flink中叫做数据流图

从soure开始经过map-keyby这些算子

比如现在的soure的并行度是2 就用两个子任务去读这个数据源

map也是2 之后的也是

那这个根据上面的**一个流程序的并行度，可以认为就是其所有算子中最大的并行度。**

这里的最大并行度就是2

#### **总结：**

**Task Slot是静态的概念，是指TaskManager具有的并发执行能力**，可以通过参数**taskmanager.numberOfTaskSlots**进行配置；

而**并行度parallelism是动态概念，即TaskManager运行程序时实际使用的并发能力**，可以通过参数**parallelism.default**进行配置。

IDEA里运行flink程序默认并行度是运行程序机器的核心数量，这一点和spark是一致的。

#### 这里需要重新看下视频没太懂

## DataStream

spark最核心的概念是RDD

那么flink最核心的概念就是datastream

在spark中一个rdd通过某种转化成另外一个rdd，另外一个rdd在通过某种转换变成其他的rdd，在flink中

有同等的概念。就是一个datastream通过某种操作变成另外一个datastream，这就是典型的链式调用

**哪这里的意思就是说每个DataStream身上都挂着“我是怎么来的”的这个信息**

比如

- [ ] 

### DataStream程序主要组成

**StreamExecutionEnvironment初始化**：这个主要是进行创建和初始化，通过DataStream API构建Flink作业需要的执行环境，包括ExecutionConfig,CheckpointConfig以及StateBackend和TimeCharacteristic等变量

**业务逻辑代码转换**：

那首先，我们不管怎么样肯定要有个数据源，数据从哪里来的，我的第一个datastream是通过数据源去构建数据的

env中提供了创建DataStream的方法，通过env.readTextFile()方法读取文本数据并构建DataStreamSource数据集，之后所有的DataStream操作都会以DataStreamSource为头节点。同时DataStreamAPI 提供了各种转换操作，如map、reduce、keyBy等算子，用于构建完整的计算逻辑。

**程序执行env.execute()：**在execute()方法中基于DataStream之间的转换生成StreamGraph,并将StreamGraph转成成JobGraph,最终将JobGraph提交到集群

这里就是再写代码的时候

初始化 env

然后写业务逻辑

然后再执行**env.execute() 这个要抛出异常**

###  Transformation

这个展示了当前的datastream是通过什么操作变过来的

**Transformation是衔接DataStream API和Flink内核的逻辑结构。**

DataStream的api调用只是表达每个步骤的业务逻辑处理，并不关心各个业务逻辑之间的数据上下游关系。

比如我调用map的话我只需写map的逻辑，我需要flapmap我只写falpmap的逻辑，那么怎么从map到flapmap的转换呢？那就是通过Transformation。

**Flink引入Transformation概念来表达上下游关系，将各个步骤的业务逻辑组织成一个流水线。**

但Transformation不关心数据执行时刻涉及的物理来源、序列化、转发等行为，运行时刻的行为交由Flink算子概念去处理。

**Transformation分成两类：**

**物理Transformation -运算的Transformation **

**虚拟Transformation -路由的Transformation **

物理Transformation在运行时刻会转换为具体的算子，主要包括SourceTransformation、OneInputTransformation、TwoInputTransformation、SinkTransformation等。

虚拟Transformation在运行时刻不会转换为算子，主要包括SideOutputTransformation、PartitionTransformation、UnionTransformation等。

#### **这里物理Transformation我理解就是转换成了干活的人就是具体的算子哪虚拟Transformation我没太理解 它不会转换成具体的算子哪这是什么？**

哪这里物理的Transformation 定义了“点”（谁是上下游）

比如你有 `Source -> Map -> Sink`。 这就是具体的算子

虚拟 Transformation 定义了“线”（数据怎么路由）

不生产数据，也不改造数据

> 

> 

这就是上面说的哪个datastream是通过什么操作变过来的！

每个StreamTransformation都包含相应的StreamOperator，例如执行DataStream.flatMap(new FlatMapFuction(…)) 转换之后，内部生成了StreamFlatMap，**StreamOperator包含了自定义函数的信息**，StreamFlatMap算子包含了FlatMapFuction。

所以，在DataStream转换的过程中,不管是哪种类型的转换操作，都是按照相同的方式：

**首先将用户自定义的函数封装到StreamOperator中，**

**然后将StreamOperator封装到Transformation转换操作中，**

**最后将Transformation添加到StreamExecutionEnviroment提供的Transfromation集合，**

**即env会将DataStream之间的转换操作存储到env中List< Transformation<?>>，**

**transformations集合，**

**然后基于转换操作去构建Pipeline，**

**用于描述作业的总体计算逻辑，流作业具体实现类是StreamGraph，批作业对应的Pipeline实现类为Plan。**

#### DataFlow 数据流图

其实所有的Flink程序都是由三个部分组成Source 、Transformation和Sink

Source ：负责读取数据源

Transformation：利用各种算子进行处理加工

Sink：负责输出

哪在运行的时候程序会被映射成“逻辑数据流”（dataflows）

这个dataflows又包含了上面的哪三个部分

而且每一个dataflow以一个或多个sources开始以一个或多个sinks结束，dataflow类似于任意的有向无环图（DAG）

**在大部分情况下，程序中的转换运算（transformations）跟dataflow中的算子（operator）是一一对应的关系，但有时候，一个transformation可能对应多个operator。一个stream-api主要有 source，operate，sink 这几部分**

### 四张图

这里也叫做逻辑流图

**Flink 中的执行图可以分成四层：StreamGraph -> JobGraph -> ExecutionGraph -> 物理执行图**。

**StreamGraph：**

根据用户通过DataStreamAPI编写的代码生成的最初的DAG图，用来表示程序的拓扑结构。这一步一般在客户端完成。

**当Flink应用业务逻辑算子编写完后会直接调用StreamExecutionEnvironment.execute()方法开始任务的生成、提交及调度，第一阶段就是将Transformation转换为StreamGraph**

**StreamNode是StreamGraph中的节点，由Transformation转换而来，**

这里我们可以理解Transformation就是一个包含了所有算子的详细信息，StreamNode就是把这个详细信息给它转变成为一个具体的计算过程

**可以理解成一个StreamNode就表示一个算子计算过程。**

Transformation分虚拟Transformation和物理Transformation，相应转换（对应的接口TransformationTranslator）成的StreamNode也分为虚拟StreamNode和物理StreamNode。

我们上面说了虚拟的Transformation作用就是做数据的一个分发，搬运，怎么从上游搬到下游他不做数据的改变

同样的虚拟的TransformationTranslator不生成StreamNode、StreamEdge，

仅用来负责连接上游Transformation和下游Transformation。StreamGraph生成结束后UnionTransformation就不存在了。

**UnionTransformation 是合并多个数据流，把多个同类型的流合成一个流，继续下游处理。**

**Union 只是逻辑上把流连起来，不产生实际的计算算子。它只负责告诉 Flink："这多个流的数据都往同一个下游送"。**

**所以在 StreamGraph 生成后，UnionTransformation 就消失了，变成 StreamNode 之间的多条入边。**

物理StreamNode最终会变成物理的算子，虚拟StreamNode会附着在StreamEdge上。StreamNode可以有多个输入，也可以有多个输出。

StreamEdge是StreamGraph中的边，用来连接2个StreamNode。

一个StreamNode可以有多个出边、多个入边。在StreamEdge中包含着OutputTag、StreamPartitioner等必要的边生成信息。

StreamGraph主要由StreamNode、StreamEdge组成，StreamGraph的成员变量决定了StreamGraph所有的功能，比如做checkpoint的位置等。

**JobGraph：**

Stream**Graph 经过优化就是JobGraph（作业图），这块是提交给JobManager 的数据结构**

这里JobGraph做的最大的一件事就是把能够放到一个slot里执行的任务放到一起

**StreamGraph经过优化后生成的就是作业图（JobGraph），这是提交给JobManager 的数据结构**，确定了当前作业中所有任务的划分。

那这里做的优化就是把一些节点可以链到一起的，放到一起就是**JobGraph**

**JobManager 这里拿到也不是flink的程序拿到的而是StreamGraph转成JobGraph，这个是JobManager 拿到的数据结构**

主要的优化为: 将多个符合条件的节点链接在一起合并成一个任务节点，形成算子链，这样可以减少数据交换的消耗。**JobGraph一般也是在客户端生成的，在作业提交时传递给JobMaster。**

1、JobVertex：经算子融合后将1个或多个StreamNode转换为JobVertex，即JobVertex包含一个或多个算子。

JobVertex.results成员变量代表该节点被几个下游节点所消费，JobVertex.inputs代表该节点消费了几个上游节点。

**JobVertex.results        被几个下游消费        Source 的 results=1（只给 FlatMap+Filter）**

**JobVertex.inputs        消费了几个上游        KeyBy+Sink 的 inputs=1（只消费 FlatMap+Filter）**

- [ ] 

2、IntermediateDataSet：JobVertex计算输出结果为中间结果集IntermediateDataSet，它是一种逻辑结构，用来描述JobVertex的输出。

**这里obVertex 输出的逻辑描述，不是真正的数据，而是"我产出了什么、谁能来读"的声明。**

比如上面的

3、JobEdge：用来连接JobVertex和IntermediateDataSet的边，表示JobGraph中的一个数据流转通道。

**JobVertex的IntermediateDataSet个数可以是一个或多个，取决于对应的StreamNode出边数量。**

**StreamGraph类的getJobGraph()方法是JobGraph生成入口方法。**

**哪整体来说这三个的关系就是**

#### 这里明确xiachin是什么？

可以chin就是one-to-one + 并行度相同

source.map(x -> x).filter(x -> x > 0);  // 合成一个 JobVertex

// 不能 Chain：redistributing

source.map(x -> x).keyBy(x -> x).sum(1);  // map 一个 JobVertex，keyBy+sum 另一个

**JobGraph 是 StreamGraph 的"合并优化版"：把能 Chain 的算子捏成 JobVertex，产出用 IntermediateDataSet 描述，传输用 JobEdge 连接。目的是减少网络传输，提高执行效率。**

**ExecutionGraph**：

JobMaster收到JobGraph后，会根据它来生成执行图（ExecutionGraph）。

ExecutionGraph是JobGraph的并行化版本，是调度层最核心的数据结构。 因为调度是**JobManager 上调度的**

把任务并行化之后分发到taskmanger上去执行

生成位置：在jobmanager上生成。JobMaster收到JobGraph后，会根据它来生成执行图（ExecutionGraph）。

这里ExecutionGraph就是obGraph 的"并行展开版"，把每个算子按照并行度拆成多个可执行的实例，是真正用来调度Task的图

这里就是在JobGraph 中的JobVertex  变成了**ExecutionGraph 的一组ExecutionVertex**

相比于StreamGraph、JobGraph，ExecutionGraph加入了并行度的概念，成为真正可调度的图结构ExecutionGraph核心对象包含ExecutionJobVertex、ExecutionVertex、IntermediateResult、IntermediateResultPartition、ExecutionEdge、Execution等。**在较新版本中，ExecutionEdge已被EdgeManager替换。**

1、ExecutionJobVertex：该对象与JobGraph中的JobVertex一一对应。它包含一组ExecutionVertex，数量是该节点所对应的并行度。

比如JobGraph:  FlatMap+Filter(并行度=2)

ExecutionGraph:

ExecutionJobVertex(FlatMap+Filter)

    ├── ExecutionVertex(1/2)  ← 第1个实例

    └── ExecutionVertex(2/2)  ← 第2个实例

这里是和 JobVertex 一一对应，只是把它按并行度展开了。

2、ExecutionVertex：ExecutionJobVertex会对Flink应用中执行节点并行化处理，构造可并行执行的ExecutionVertex实例。

就比如

ExecutionJobVertex(FlatMap+Filter) 并行度2

    ├── ExecutionVertex(1/2)  → 会被调度到某个 Slot 执行

    └── ExecutionVertex(2/2)  → 会被调度到某个 Slot 执行

可以理解为可调度执行的最小单元

3、IntermediateResult：该对象与JobGraph中的IntermediateDataSet一一对应，表示ExecutionJobVertex的输出。一个IntermediateResult包含多个IntermediateResultPartition，数据取决于算子的并行度。

4、IntermediateResultPartition：表示1个ExecutionVertex输出结果，与ExecutionEdge相关联。

ExecutionJobVertex(FlatMap+Filter, 并行度=2)

    ├── ExecutionVertex(1/2) → 输出 → IntermediateResultPartition(1/2)

    └── ExecutionVertex(2/2) → 输出 → IntermediateResultPartition(2/2)

                                ↓

                         IntermediateResult（整体输出）

                                ↓

                    被下游 KeyedAgg+Sink 消费

5、EdgeManager：负责存储ExecutionGraph中所有的tasks并行度之间的关联关系。

6、Execution：ExecutionVertex相当于Task的模板，真正执行的时候Flink系统会从ExecutionVertex封装出一个Execution实例，代表一个实际的运行尝试。一个Execution通过一个ExecutionAttempID来唯一标识。

**DefaultExecutionGraphBuilder.buildGraph()即为ExecutionGraph生成入口**。该方法入参包括之前生成的JobGraph实例及其他一些重要组件，方法实现中首先会生成一些必要信息，然后经过以下几个关键步骤生成一个DefaultExecutionGraph实例并构造以上核心对象，最后返回DefaultExecutionGraph实例。

**物理执行图**：

**JobMaster 生成执行图后，会将它分发给 TaskManager；各个 TaskManager 会根据执行图部署任务，最终的物理执行过程也会形成一张“图”**，一般就叫作物理图（Physical Graph）。这只是具体执行层面的图，并不是一个具体的数据结构。生成位置：在taskmanager上生成。

**Task**：Execution 被调度后在分配的 TaskManager 中启动对应的 Task。Task 包裹了具有用户执行逻辑的 operator。

**ResultPartition**：代表由一个 Task 的生成的数据，和 ExecutionGraph 中的 IntermediateResultPartition 一一对应。

**ResultSubpartition**：是 ResultPartition 的一个子分区。每个 ResultPartition 包含多个 ResultSubpartition，其数目要由下游消费 Task 数和 DistributionPattern 来决定。

**InputGate**：代表 Task 的输入封装和 JobGraph 中 JobEdge 一一对应。**每个 InputGate 消费了一个或多个的 ResultPartition。**

**InputChannel**：每个 InputGate 会包含一个以上的 InputChannel，和 ExecutionGraph 中的 ExecutionEdge 一一对应，也和 ResultSubpartition 一对一地相连，即**一个 InputChannel 接收一个 ResultSubpartition 的输出。**

#### 整体：

我写了一个flink的任务，通过flink run

第一件事就是把我写的代码转换成了**StreamGraph**

**这一步在客户端生成的**

转换我那成lehiho点是能嵌在一起的进行优化生成**JobGraph**

**JobGraph才是我在客户端生成的最终的数据结构，我在实际运行的时候是在JobMaster上调度的所以**

就把**JobGraph发给的JobMaster**

然后**JobMaster又做个各种转换是不是就变成了一张ExecutionGraph**

然后发给了taskmanger,taskmanger拿到这个封装之后先把它给解开，把对应的节点转换成

taskmaner能够识别的

### fink任务链

这里讲解的就是**Chain**

**Flink采用一种称为任务链（Operator Chain）的优化技术，相同并行度的 one to one 操作，Flink 把这样相连的算子链接在一起形成一个 task，原来的算子成为里面的一部分（subtask）。**

**为了满足任务链的要求，必须将两个或多个算子设为相同的并行度，并通过本地转发（local forward）的形式进行链接。**

这里的好处就是数据都是从本地，当前的线程中走不用走机器之前等等速度很快

在一个 DAG 图中不能被 Chain 在一起的 Operator 会被分隔到不同的 Task 中，一般一个Task占用一个slot，也就是说 Task 是 Flink 中资源调度的最小单位。

在StreamGraph转换为JobGraph过程中，关键在于将多个 StreamNode 优化为一个 JobVertex，对应的 StreamEdge 则转化为 JobEdge，并且 JobVertex 和 JobEdge 之间通过 IntermediateDataSet （中间数据集）形成一个生产者和消费者的连接关系。

每个JobVertex就是JobManger的一个任务调度单位（任务Task）。为了避免在这个过程中将关联性很强的几个StreamNode（算子）放到不同JobVertex（Task）中，从而导致因为Task执行产生的效率问题（数据交换（网络传输）、线程上下文切换），Flink会在StreamGraph转换为JobGraph过程中将可以优化的算子合并为一个算子链（也就是形成一个Task）。

这样就可以把这条链上的算子放到一个线程中去执行，这样就提高了任务执行效率。

这里主要就是说Chain的本质

包括上面也说过Chain但是当时知识一知半解

Chain就是把多个算子粘成一个Task，在同一个线程里顺序执行

举个例子：

如果不Chain,这里的算子都要一个一个执行，而且还有取走网络进行IO

每一步都要

- [ ] 

哪进行Chain后多个算子在同一个线程里顺序执行，数据直接方法调用，不走网络，大幅提升效率。

- [ ] 

**但是这里是有条件的**

该方法返回true时两个端点才可以合并到一起，根据源码可以得出形成作业链的规则如下：

i、上下游的并行度一致（槽一致）

相同的并行度：上下游的并行度一致（slot一致，就是槽）

- [ ] 

ii、该节点必须要有上游节点跟下游节点；

该节点必须要有上游节点跟下游节点

这里我一开始理解的是上下游节点

但是其实并不是，他这个是指的比如

- [ ] 

iii、下游StreamNode的输入StreamEdge只能有一个

这里需要回看上面的StreamGraph这个图了 StreamEdge 这个是边 用来链接StreamNode，而物理StreamNode就是一个算子，所以StreamEdge 也可以说是用来链接两个算子的边

哪回到这个规则就是 下游算子的输入边只能有一条

举个例子：

- [ ] 

Filter 如果有两个上游（Map 和另一个流），就不能和 Map Chain。

iv、上下游节点都在同一个 slot group 中

v、下游节点的 chain 策略为 ALWAYS（可以与上下游链接，map、flatmap、filter等默认是ALWAYS）

vi、上游节点的 chain 策略为 ALWAYS 或 HEAD（只能与下游链接，不能与上游链接，Source默认是HEAD）

vii、上下游算子之间没有数据shuffle (数据分区方式是 forward)

viii、用户没有禁用 chain

**link会尽可能地将多个operator链接（chain）在一起形成一个task pipline。每个task pipline在一个线程中执行**

OperatorChain的优点：它能减少线程之间的切换，减少消息的序列化/反序列化，减少数据在缓冲区的交换（即降低本地数据交换成本），减少了延迟的同时提高整体的吞吐量。

OperatorChain的缺点：如果其中某一个算子是一个耗时耗资源等操作，但是符合任务链的条件将其放在一个task中，这种就不适合集群资源的充分利用。

### **重拾作业调度及作业的状态转换**

首先什么时**重拾作业调度及作业的状态转换**

### 复习

运行架构这一章节极其重要

工作用不到，但是面试覆盖面试很大

flink组件这部分和spark比较像以flink core为核心

##### 作业管理器-jobmanager

功能类比spark中的driver，不是完全一样就是类比

它既然是master节点，那么是不是就是处于一个领导地位，负责接收任务，负责处理任务，负责拆解任务，负责分配任务这些任务

那谁干活？是taskmanager上面的资源去执行

JobManager会先接收到要执行的应用程序，这个应用程序会包括：

作业图（JobGraph）

逻辑数据流图（logical dataflow graph）

打包了所有的类、库和其它资源的JAR包。

**JobManager会把JobGraph转换成一个物理层面的数据流图，这个图被叫做“执行图”（ExecutionGraph），包含了所有可以并发执行的任务。**

JobManager会向资源管理器（ResourceManager）请求执行任务必要的资源，也就是任务管理器（TaskManager）上的插槽（slot）。

一旦它获取到了足够的资源，就会将执行图分发到真正运行它们的TaskManager上。

而在运行过程中，JobManager会负责所有需要中央协调的操作，包括任务调度，检查点管理，失败恢复等。

当然，对于集群HA模式，可以同时多个master进程，其中一个作为leader，其他作为standby。当leader失败时，会选出一个standby的master作为新的leader（通过zookeeper实现leader选举）

###### 总结：

JobManager的功能主要有：

> 

> 

> 

> 

> 

补充知识：

flink内部节点用的是Akka,Akka其实就是我们说scala自己是有一套通讯的末班action通讯方式，基于action通讯方式，我们有个框架叫Akka

从上面看jobmanager这么多的功能，从上面拆解下来就是三部分

资源管理器（resourceManager）

分发器（Dispatcher）

Jobmaster

资源管理器（resourceManager）

slot：这个翻译过来就是一个槽位，什么意思呢

比如现在我这个taskmanger有10个g内存，那我现在设置三个slot，每一个slot就是10/3的内存

所以在flink中只有内存是隔离的，cpu不会被隔离，内存就是以slot形式隔离的

但是这里的resourceManager和yarn中的resourceManager不一样

这里的resourceManager是管理slot的

yarn的resourceManager是管里是continer容器

分发器（Dispatcher）

Jobmaster

jobGraph:我是在代码写了很多程序，我的jobgraph就死相当于这个程序的逻辑图

jobmanger和

比如我现在去提交一个任务

以yarn为例

我们先把clinet提交到yarn上面

yarn会启动一个对应的aplactionmaster

在flink中 jobmanger会根据不同的调度系统形式不一样

那么这个jobmanger其实就是逻辑上的一个概念

对不同的调度系统形式不一样，yarn这里就是通过aplaction实现的

也就是说yarn中applactionmanger里面包含了jobmanger

那么jobmanger包含了三个组件：**Dispatcher，RM,JMaster**

那么这里我启动的AM或者说是启动了jobmanger

是不是**Dispatcher就有了**

那么client就可以把作业放到**Dispatcher里了**

**Dispatcher去生成对应的JMaster**

去分配我的JobGraph,那么这里的JobGraph是不是就是类似于spark中的一个DAG

JobGraph 处理完JobGraph告诉RM我需要多少个solat

比如10个，然后再去找yarn分配资源，yarn发现你这个配置文件中，每一个taskmanger只配置了3个sloat

那现在需要10个slot，那我启动三个taskmanger就不够

因为只有9个slot

这个时候就需要启动4个taskmanger,这个时候去找yarn，yarn就会给你生成

那么taskmanger，就告诉了jobmaster说我可以提供给你三个，那么taskmaster就把任务放到了taskmanger上了

这里一定要记住：

JobManger 只是逻辑上的概念 这里把resourmanger和jobmaster放到一起就是jobmanger

那么不同的框架里面，实现的逻辑是不一样的

比如说yarn中 还要加个jiageappalactionmaster

## Flink任务调度原理

调度原理就是一个flink程序怎么一步一步的放到了具体的taskmanger上去执行

首先白色的框

红色的地方是我们程序自己写的代码

如果是批作业是不是要做一个Optimizer

如果做一个流作业要做一个string Graph

然后回生成一个作业流图

这个作业流图会通过akka把任务提交到jobmanger上

那么这里的各个节点就是用actor System进行交互的

## slot和parallelism（并行度）的关系

回顾下，taskmanger类似一个资源池，而slots是去均衡资源池的每一个池位。

我们说slots是flink里面的独有的，在spark里面其实是没有slots这个概念的

先来说spark在指定任务的时候能指定excutor的内存，核数

所以这个slts的作用就是把每一个槽位进行隔离的，但是cpu和spark是一样的没有进行隔离

所以cpu是共享的，包括心跳机制也是共享的

## Flink datastream

在spark中核心的概念就是 RDD-弹性分布式数据集

flink 对等的概念的datastream

一样的，rdd是spark中最重要的数据结构，那么datastream就是Flink中最重要的数据结构

datastream程序包含:

1.StreamExcutionEnvironment初始化:包括执行的设置，检查点的设置，状态后端的设置和时间特征的设置 时间特征这个在flink1.15 版本里面这个东西已经就没有了

2.业务逻辑代码转化:那么首先我们不管怎么样，我们是不是要有个数据源吧，那我的第一个datastream是不是通过数据源去构建数据的

3.程序执行env.execute：

## Flink Transformation

Transformation是衔接DataStream API和Flink内核的逻辑结构

我们在写DataStream的时候只关心我如果调用map的话我只需要去写map的一个逻辑

我调用flapmap，我就写一个flapmap逻辑，那我们怎么通过map 到 flapmap转化呢 那就是通过Transformation

从A到B怎么过来的，那这条线就是Transformation

## Flink里的四张图

首先在前面的时候说过

这里在底层屏蔽了流批一体，在上一层可以写流api，也可以写批api 

## Flink中的类型系统

**Flink **流应⽤程序处理的是以数据对象表⽰的事件流，所以在 Flink 内部，需要能够处理这些对象。它们需要被序列化和反序列化，以便通过⽹络传送它们；

flink其实也可以吧java那一套拿过来，java的序列化接口：Serializable

但是这个接口会带一些对象头相关的，我们说flink是为了提高一个高效，简化，flink为了处理这些结构它自己内部做了一个数据类型，整个数据类型都是有个顶级的类：**TypeInformation**

这个类如果面试问到类型系统是什么 就是**TypeInformation，他是超级类**

它包含

**BasicTypeInfo ：对标的就是java中的基础类**

## slotSharingGroup

slot说了这么久，但是这个slot怎么设置？

使用taskmanger.numberOfTaskSlts 进行设置

但是如果不设置呢，它的默认是怎么样呢？

默认就跟着本地cup的核数，比如我的电脑核数是8个那么slot的个数就是8个。

### Flink包括哪些组件

Flink是一个典型的mast-work架构， 那么就需要一个mask-作业管理器（JobManager）

那么这个在查找信息的时候很多博客会说，这个JOB是唯一mask节点的，就是他是有一个真实的mast节点

那么mast节点包括三个部分比如jobmanger,resoueceManager等这个是很多博客都会去说的

但是以什么为依据？我当时想，然后着了官网

### 整体框架
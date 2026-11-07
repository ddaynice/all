## 避免创建重复的rdd

通常来说，我们在开发⼀个 Spark 作业时，⾸先是基于某个数据源（⽐如 Hive 表或 HDFS ⽂件）创建⼀个初始的 RDD ；

接着对这个 RDD 执⾏某个算⼦操作，然后得到下⼀个 RDD ；

以此类 推，循环往复，直到计算出最终我们需要的结果。

在这个过程中，多个 RDD 会通过不同的算⼦操作（⽐如 map 、 reduce 等）串起来，这个 “RDD 串 ” ，就是 RDD lineage ，也就是 “RDD 的⾎缘关系链 ” 。

我们在开发过程中要注意：对于同⼀份数据，只应该创建⼀个 RDD ，不能创建多个 RDD 来代表同⼀份数据。

- [ ]

## 尽可能复用同⼀个 RDD

除了要避免在开发过程中对⼀份完全相同的数据创建多个 RDD 之外，在对不同的数据执⾏算⼦操作时还要尽可能地复⽤⼀个 RDD 。

⽐如说，有⼀个 RDD 的数据格式是 key-value 类型的， 另⼀个是单 value 类型的，这两个 RDD 的 value 数据是完全⼀样的。

那么此时我们可以只使⽤ key-value 类型的那个 RDD ，因为其中已经包含了另⼀个的数据。

对于类似这种多个 RDD 的数 据有重叠或者包含的情况，我们应该尽量复⽤⼀个 RDD ，这样可以尽可能地减少 RDD 的数量，从⽽尽可能减少算⼦执⾏的次数

这里的意思其实就是说

如果 RDD A 的数据已经完全覆盖了 RDD B 的数据，那就只保留 A，B 通过 A 做一次轻量转换（如 `map`、`keys`、`values`）得到，不要重新读源数据。

Spark 的 每个 RDD 都是一个独立的计算链起点（除非显式依赖）。多一个 RDD，就多一条 lineage，多一份：

>

>

>

## 对多次使用的rdd进行持久化

之前的的复用rdd在这个基础上就是要进行优化

保证对一个rdd执行多次算子操作的时候。这个rdd本身仅仅被计算一次

因为spark对一个rdd执行多次算子默认原理是：

每次对一个rdd进行算子操作的时候，都会重新从源头处计算一次，计算出哪个rdd来，然后在对这个rdd执行你的算子操作

所以这这里，对多次使用的rdd进行持久化

 Spark 就会根据你的持久化策略，将 RDD 中的数据保存到内存或者磁盘中

以后每次对这个 RDD 进⾏算⼦操作 时，都会直接从内存或磁盘中提取持久化的 RDD 数据，然后执⾏算⼦，⽽不会从源头处重新计算⼀遍这个 RDD ，再执⾏算⼦操作

那么这里就要弄清楚持久化怎么做？

比如

- [ ]

针对于手动持久化

persist

持久化级别

MEMORY_ONLY:

这个是将数据存到内存中，如果内存不够放所有的数据，超出可能就不会进行持久化，那这些没有持久化的数据，就需要从头计算一遍，cache就是用的这个方法！

MEMORY_AND_DISK:

这个和上面不同的是如果内存不够放所有的数据，就会往磁盘里写入

MEMORY_ONLY_SER：

和MEMORY_ONLY差不多，但是这个会将rdd中的数据进行序列化，rdd的每个partition会被序列化成一个字节数组

优点就是这种方式会节省内存，避免持久化的数据占用过多的内存导致GC

MEMORY_AND_DISK_SER：

和MEMORY_AND_DISK一样，区别和上面一样

DISK_ONLY：

这个就是写到磁盘里

还有其他的持久化策略！

**从上面的描述也能看到性能最高的其实就是MEMORY_ONLY，因为它的数据都是放到内存里的，但是有个问题就是内存你要足够大，能放下整个rdd的数据。**

**使用上的话可以参考降级，如果MEMORY_ONLY发生了oom可以选择MEMORY_AND_DISK这种降级的操作！**

**其实一般是预估如果rdd的数据量太大，直接带SER 的级别，避免一开始就撑爆内存。**

## 尽量避免使用shuffle类算子

其实在spark整个作业运算的过程中，shuffle算子是最消耗性能的过程

shuffle过程简单的来说就是将分布在集群中多个节点上的同一个key拉到同一个节点进行处理啊，也就是我们说的宽依赖！

这个地方需要使用网络进行拉取数据进行额外的i/o消耗

比如进行聚合或者join等还有reduceBykey等算子都会触发shuffle

shuffle过程中各个节点上相同key都会先写入本地磁盘文件中，然后其他节点就要通过网络拉去各个磁盘的上的相同key

都拉到同一个节点进行聚合操作，那么这个时候就有可能因为某个节点上处理相同的key过多，导致内存不够，进而溢写到磁盘文件中

这些网络传输，大量磁盘读写i/o操作都是shffle性能比较差的原因，所以能避免就避免

案例

- [ ]

## 使用map-side 预聚合的 shuffle 操作

我们上面只是说了避免shuffle操作，如果真的要用的话怎么办？

那就使用map-side预聚合的算子

map-side,是在每个节点本地对相同的key进行一次聚合的操作，类似mr的本地combiner

这里再预聚合之后，每个本地节点就会只有一条相同的的key

那其他节点在拉取所有节点上的相同key的时候，拉取的数量就会少很多，这样就减少了磁盘i/o和网络传输的开销

比如

reduceByKey和aggregateByKey

算子都会使用用户自定义的函数对每个节点本地的相同

key进行预聚合

## 使用高性能的算子

除了shuffle相关的算子由优化原则之外，其他的算子也都有着相应的优化原则

比如使用reduceByKey/aggregateByKey 替代groupByKey

使用mapPartition替代普通的map，

mapPartition这类的算子，一次函数调用会处理一个partition所有的数据，而不是一次函数调用处理一条，性能相对会高一些！

但是把有时候mapPartition 会出现oom

因为单次函数调用就要处理掉一个partition所有的数据，如果内存不太够，垃圾回收无法回收掉太多对象，可能出现oom异常！

使用foreachPartition替代foreach，类似mapPartition 代替map

也是一次函数调用处理一个partition的所有数据，而不是一次函数调用处理一条数据

其实在实践中foreachPartition类的算子，对性能提升是很有帮助的！

比如在foreach函数中，将rdd中所有数据写mysql，那普通的foreach算子就会一条数据一条数据的写，每次调用函数就会创建一个数据库链接！

但是如果是foreachpartition算子一次性就能处理一个partition的数据，对于每个partition，这个时候创建一个数据库链接就可以，然后执行批量插入！

还有就是使用filter之后进行coalesce操作，通常一个rdd执行filter算子过滤掉rdd中比较多的数据之后，使用coalesce算子，手动减少rdd的partition数量，将rdd中的数据压缩到更少的partition中去

因为啥呢，filter之后rdd中的每个partition中都有很多的数据被过滤掉，那么每个task要处理的partition中的数据量其实并不是很多，但是task越多，可能速度越慢，所以用coalesce减少partition的数量，这样用更少的task去处理所有partition！

## 广播大变量

为什么广播大变量会减少性能开销，提高优化呢？

再算子函数中使用到外部变量的时候，默认spark会将这个变量赋值多个副本

通过网路传输到task中，这个时候每个task都有一个变量副本

如果变量本身比较大的话 比如100m甚至到g，那么大量的变量副本再网络传输的性能开销，还有再各个节点的Executor占用过多内存导致的频繁GC，都会影响性能

所以如果使用外部变量比较大，可以用广播功能对变量进行广告，这样会保证每个excutor的内存中只保留一份变量副本，excutor之中的task执行时共享那份变量副本，这样的话就能减少副本的数量从而减少网络传输的性能开销，减少executor内存的占用开销，降低GC

## 使用Kryo优化序列化性能

首先spark有哪些涉及到序列化我们要知道

1.对象，每个java对象都有对象头，引用等额外的信息，所以这个比较占用内存空间

2.字符串，每个字符串内部都有一个字符数组一级长度等额外信息

3.集合类型，比如hashmap linkedKist等，这些集合类型内部会使用一些内部类来封装集合元素，比如map.entry

所以我们去看spark的官方文档里，提过对于算子函数中的代码尽量不要使用上面的三种数据结构，可以使用字符串代替都西昂，使用原始类型比如 int long去代替字符串

使用数据代替几个类型，从而减少内存占用，降低GC频率

**但是要做到该原则其实并不容易，因为我们同时要考虑到代码的可维护性，如果⼀个代码中，完全没有任何对象抽象，全部是字符串拼接的⽅式，那么对于后续的代码维护和修改，⽆ 疑是⼀场巨⼤的灾难。同理，如果所有操作都基于数组实现，⽽不使⽤ HashMap 、 LinkedList 等集合类型，那么对于我们的编码难度以及代码可维护性，也是⼀个极⼤的挑战。因此建 议，在可能以及合适的情况下，使⽤占⽤内存较少的数据结构，但是前提是要保证代码的可维护性。**

## Data Locality 本地化级别

Data Locality（数据本地化） 就是 Spark 在调度任务时，尽量让计算代码在数据所在的节点上执行，而不是把数据通过网络搬到计算节点。

本地化的参数有：

PROCESS_LOCAL：

进程本地化，代码和数据在同一个进程中，也就是在同一个executor中

计算数据的task由executor执行，数据在executor的blockmanager中，性能是最好的

NODE_LOCAL：

节点本地化，代码和数据在同一个节点中，比如说，数据作为一个Hdfs block块，就在节点上行，而task在节点上某个executor中运行，或者是，数据和task在一个节点上的不同executor中

数据需要在进程间碱性传输

NO_PREF：

对于task来说，数据从哪里获取都一样，没有好坏之分

RACK_LOCAL：机架本地化，数据和task再一个机架的两个节点上，需要通过网络再节点之间传输

ANY：数据和 task 可能在集群中的任何地⽅，⽽且不在⼀个机架中，性能最差

**Spark 在 Driver 上，对 Application 的每⼀个 stage 的 task ，进⾏分配之前，都会计算出每个 task 要计算的是哪个分片数据， RDD 的某个 partition ； **

**Spark 的 task 分配算法，优先，会希望 每个 task 正好分配到它要计算的数据所在的节点，这样的话，就不⽤在⽹络间传输数据；**

这里首先第一步就是要将task partition stage这三个的关系

rdd的partition（数据块）

rdd是一个大表格，但是它不会真的存在一张完整的表里，而是被切成了很多小块

比如假设 HDFS上文件有3个block

rdd的逻辑

比如 rdd 10G数据

Partition 0 3gb

Partition 1 3GB

Partition 2 4GB

stage就是把代码切成一段一段的，遇到shuffle的时候 比如reducebykey 就切一刀 前面一段，后面一段

每一段就是一个stage

task任务

一个stage里面每个partition都要有一个task去处理它

比如stage-0 里面有3个partition 所以产生3个task

Task -0 处理partition0

Task -1 处理partition1

Task -2 处理partition2

那么他们的关系就是

Job (一个 Action 触发一个 Job)

 └── Stage (遇到 shuffle 切一刀，产生多个 Stage)

      └── Task (Stage 内每个 Partition 对应一个 Task)

           └── 处理对应的 Partition（数据块）

Stage 包含 Task，Task 处理 Partition

那么

**Spark 在 Driver 上，对 Application 的每⼀个 stage 的 task ，进⾏分配之前，都会计算出每个 task 要计算的是哪个分片数据， RDD 的某个 partition ； **

首先第一步我们要知道 Driver上 谁来做事情

Driver 是spark作业的大脑，它是单独的跑在JVM里，不负责实际的计算，只是负责拆解任务

简单来说就是DAGScheduler 运行在 Driver 上，是面向 Stage 的高层调度器

我们写的比如rdd.map().filter().reduceByKey()

Driver 不会直接拿去算，而是先交给 DAGScheduler 拆解成"任务清单"。

这里的意思就是说diver在派活之前，必须要做查地址的工作，它要知道这个task负责处理rdd的哪一块partition，以及这块数据现在再那台机器上，只有把工单和地址绑定好之后才能把task发到离数据最近的机器，避免跨网络拉数据

**那么这里计算每个 task 要计算的是哪个分片数据**

就是查清楚这个工单对应的数据在哪台机器上！

那上面是Data Locality的概念把算

哪如果task没有机会分配到数据所在的节点，可能是哪个节点的计算能力都满了

所以这个时候Spark回等，通常是3s

如果时间过了，等不了了就会选择一个比较差的本地化级别，比如说将task分配到靠它要计算的数据所在节点比较近的一个节点，然后再进行计算

但是这种情况就会涉及到发生数据传输，task会通过其所在节点的BlockManager来获取数据

BlockManager 发现自己本地没有数据，会通过⼀个 getRemote() 方法， 通过 TransferService （⽹络数据传输组件）从数据所在节点的 BlockManager 中，获取数据，通过⽹络传输回 task 所在节点。

所以这里还是说怎么减少网络传输！

怎么去调节这个参数？

那就去卡门spark的运行日志，可能会显示starting task ， PROCESS LOCAL 、 NODE LOCAL ，观察⼤部分 task 的数据本地化级别

如果大多数都是是 PROCESS_LOCAL ，那就不⽤调节了，如果是发现，好多的级别都是 NODE_LOCAL 、 ANY ，那么最好就去调节⼀下数据本地化的等待时⻓调节完，应该是要反复调节， 每次调节完以后，再来运⾏，观察⽇志   看看⼤部分的 task 的本地化级别有没有提升；看看，整个 spark 作业的运⾏时间有没有缩短

但是注意别本末倒置，本地化级别倒是提升了，但是因为⼤量的等待时⻓， spark 作业的运⾏时间反⽽增加了，那就还是不要调节了

## spark 关于调优最常⻅的参数⼤全（必背）

### 资源相关参数

**Num-executor:**

就是字面意思 设置spark作业时候的executor进程的个数

因为啥呢spark默认只会启动很少的进程，如果不设置这个的话，作业的并行度是不够的，影响执行速度

一般的话每个作业50-100就行，设太大资源也没办法给够

**Executor-memory:**

还是字面意思，executor内存大小，这个比较重要了，很大程度上直接决定了spark作业的性能

，⽽且跟很常⻅的  Java 中的虚拟机内存溢出异常 (oom) 也有关系

一般来说4-8g 参考啊，但是根据我这边的经验最好不要超过资源队列的最大内存的1/3 ~1/2

**Executor-cores**

这个就是设置每个Executor进行的cup 核数据

每个cpu core同时只能执行一个task线程，所以Executor-cores的个数决定了Executor并发能力

这个看了 2~6个我觉得都行

**driver-memory/driver-core**

这个就和上面的类似只不过是设置driver的内存和core

这个用的很少基本没有用过，默认是512m 但是用到collect算子的时候才会往上调2-4g

核数 默认就行1

**Spark.default.parallelism**

这个就是设置stage默认的task数量，他们的关系上面也有说

默认值的时候，spark会根据底层HDFS的block数量设置task，通常一个block对应一个task

但是吧task才是真正执行spark作业的线程，如果task太少，那就有个问题exector资源够但是task不够

没有task执行，哪你针对executor的优化也没啥用了

所以基于上面的问题一般设置为Executor-memory和Executor-cores 的2倍就行 也可以加点3倍

**spark.memory.fraction**

默认 0.6，它控制的是 Executor JVM Heap 中“统一内存区域”的占比。

那什么是Executor JVM Heap？

┌─────────────────────────────────────────┐

│           Executor Heap (4GB)           │

├─────────────────────────────────────────┤

│  统一内存区域 (Unified Memory)  60%      │                              ← spark.memory.fraction = 0.6

│  ┌─────────────────────────────────┐    │

│  │  Storage (缓存)  +  Execution  │    │                            ← 两者共享，可互相挤占

│  │      (shuffle/sort/join/agg)   │    │

│  └─────────────────────────────────┘    │

├─────────────────────────────────────────┤

│  User Memory + Safety Reserved   40%     │          ← 用户对象、Spark 内部元数据、防 OOM 缓冲

└─────────────────────────────────────────┘

统⼀内存模型下 Storage 和 Execution 划分为统⼀共享内存区域，默认是 0.6

也就是说，默认 Executor 60% 的内存⽤来存储和计算。

在 spark 程序⽐较简单，但是处理的逻辑⽐较复杂的 情况下，可以适当调⾼此参数。

**spark.memory.storageFraction**

⽤于设置 RDD 持久化数据在 Executor 内存中能占的⽐例，默认是 0.5 。也就是说，默认 Executor 50% 的内存，可以⽤来保存持久化的  RDD  数据。当 Spark 作业中有较多 RDD 需要进⾏持 久化操作时，可以将该参数值调⾼；当 Spark 作业中有较少 RDD 需要进⾏持久化操作时，可以将该参数值调低

**spark.memory.offHeap.enabled/spark.memory.offHeap.size **

堆外内存默认情况下是不开启的，需要在配置中将 spark.memory.offHeap.enabled 设为 True ，同时配置 spark.memory.offHeap.size 参数设置堆⼤⼩。对于堆外内存的划分，仅包含 Execution( 执⾏内存 ) 和 Storage( 存储内存 ) 两块区域，且被所有 task 线程任务共享。⼀般建议在处理⼤数据级的数据时建议开启

### shuffle相关的

 spark.shuffle.file.buffer

调整 map 端缓冲区⼤⼩，内存资源充⾜时，可适当调⼤ map 端缓冲区的⼤⼩，以减少磁盘溢写次数，提⾼效率。默认 32K

spark.reducer.maxSizeInFlight

调整缓冲区的大小，内存资源足的时候，可以适当调大reduce端缓冲区的大小，这个是为了减少数据拉取次数，减少网络传输次数。默认48M

spark.shuffle.io.maxRetries

调整 reduce 端拉取数据重试次数，⽹络状况不稳定时， reduce 拉取数据的重试次数如果超过阈值，会导致任务失败，为了提⾼任务执⾏的稳定性，可适当调⼤该值。默认 3 次

spark.shuffle.io.retryWait

调整 reduce 端拉取数据等待间隔， reduce 端进⾏拉取重试时，会等待⼀段时间再重试，⽹络状况极不稳定时，可适当增⼤该间隔时⻓，以增加 shuffle 操作的稳定性。默认 5s

### sql相关参数

spark.sql.adaptive.enabled

这个就是AQE 遇到倾斜 直接先打开这个 基本80%的倾斜都能解决

还有几个参数一起使用

比如设置 shuffle分区合并的大小

spark.sql.adaptive.coalescePartitions.minPartitionSize=1MB spark.sql.adaptive.coalescePartitions.initialPartitionNum=200

启⽤动态  Join  策略调整： spark.sql.adaptive.autoBroadcastJoinThreshold

 启⽤数据倾斜优化： spark.sql.adaptive.skewJoin.enabled=true

问题：

为什么会使用shuffle分区合并？

因为aqe再解决倾斜的时候会产生大量碎片化的小分区，所以要合并机制，要不并发度崩了

其实aqe运行过程就是

当检测到某个reduce分区数据量远超平均

比如超过`spark.sql.adaptive.skewJoin.skewedPartitionFactor`倍数且大于`skewedPartitionThresholdInBytes`

它会把那个倾斜的大分区原地拆成多个小分区，分别和对应的小表分区做join。

spark.sql.optimizer.dynamicPartitionPruning.enabled

动态裁剪

但是这里要说的是为什么有时候不生效？

Spark 3.x 中 DPP 也被视为重⼤的优化项之⼀，正常实际的⼯作中都会开启此配置，默认就是 true 。

### spark推测执行

推测执行的参数是默认的

/*  开启推测执⾏后，每隔该值时间会检测是否有需要推测执⾏的  Task */ set spark.speculation.interval=1000ms;

当成功的task占总的task比例超过spark.speculation.quantile

统计成功task运行时间中位数乘以 spark.speculation.multiplier  得到推测执⾏阈值，当在运⾏的任务超过这个阈值就 会启动推测执⾏。当资源充⾜时，可以适当减⼩这两个值

set spark.speculation.quantile=0.99;

set spark.speculation.multiplier=3;

##  Spark  的 OOM 会发⽣在 Spark  那个组件上 ? 对应的解决⽅案是？（背诵理解）

首先oom在driver和executor上都能出现oom

分别讨论

### driver端的OOM

collect 之类的⾏动算⼦拉取了过多数据到 Driver 端引发的 OOM 。

这个没得说单纯是数据量大引起的oom，适当调大driver端的内存分配

或者用其他的算子代替

还有就是广播变量导致的oom

广播变量需要在driver端缓存，广播变量过大也可能造成driver端的oom

解决也是调大dreiver内存或者放弃广播变量

### Executor 端的 OOM

这里的oom比如分区批处理类的算子啊mappartition引发的oom

解决办法：调⼤ Executor 的内存，或者在业务场景允许的情况下放弃分区批处理算⼦的使⽤，改⽤针对单个元素的算⼦。

（ 2 ）可能原因 2 ：分区合并算⼦ coalesce 引发的 OOM

解决办法：尽量不要使⽤ coalesce 算⼦，改⽤ repartition( 主动 shuffle) 代替，防⽌⼤量 Executor 空跑以及个别 Executor 出现 OOM 。

（ 3 ）可能原因 3 ：⼴播变量会在每个 Executor 存储⼀份副本，⼴播变量过⼤时会引发 Executor 端的 OOM 。

解决办法：放弃使⽤该⼴播变量，或者调⼤ Executor 的内存。 （

 4 ）可能原因 4 ： reduce 端⼀次拉取数据量过⼤引发 OOM

解决办法：适当减⼩ reduce 端拉取数据的缓冲区⼤⼩（ spark.reducer.maxSizeInFlight ），尽管这样做会增加 reduce 端拉取数据的⽹络传输次数，⼀定程度上牺牲了运⾏效率，但能 够提⾼运⾏的稳定性。

## Spark SQL 中单 count(distinct) 的理解及优化（重点理解）

这个优化其实问的是比较多的

涉及到count，那么就会涉及到Aggregate

哪spark sql中对应的聚合模式有哪些？

在源码中

- [ ]

简单来说就是spark给每个聚合函数 sum...贴个标签，告诉它 你现在处于哪个阶段

Partial 是局部数据的聚合。会根据读入的原始数据更新对应的聚合缓冲区，当处理完所有的输入数据之后，返回的是局部聚合的结果

PartialMerge 这个是针对Partial返回的聚合缓冲区（局部聚合结果）进行合并，但是这个时候的结果也不是最终的结果，还要经过final才是最终的结果

Final:将聚合缓冲区的数据进行合并，然后返回最终的结果

Complete：用户直接从原始输入行计算此函数，而且无需任何部分聚合，当它处理完所有输入行之后，将直接返回此函数的最终结果。应用在不支持Partial模式的聚合函数上比如求百分比percentile_approx

其实对于非distinct类的聚合函数的路线：partial -> Final

distinct类的聚合就是Partial --> PartialMerge --> Partial --> Final

### 比如只有 count distinct 聚合函数的情况下执⾏原理

select name,count(distinct age) from people group by name

这里的物理执行计划从从下往上的

**FileScan csv [name#0,age#1] Batched: false, DataFilters: [], Format: CSV, Location: InMemoryFileIndex(1 paths)**

csv [name#0,age#1]：从 CSV 文件读取数据，只读 `name` 和 `age` 两列（列裁剪），`#0` `#1` 是 Spark 内部生成的列 ID

Batched: false        CSV 不支持批量列式读取（Parquet 会是 true）

DataFilters: []        没有下推到文件层的过滤条件（比如没有 WHERE age > 20）

Location: InMemoryFileIndex(1 paths)        文件路径信息缓存在内存中，共 1 个路径

整体的意思就是：Spark 去 HDFS/本地目录找到 CSV 文件，逐行读出 `name` 和 `age`，生成第一批 RDD

**HashAggregate(keys=[name#0, age#1], functions=[], output=[name#0, age#1])**

这是第一次：第一次 HashAggregate（Map 端局部去重）

keys=[name#0, age#1]        按 name 和 age 两列做分组键

functions=[]        空数组！ 没有聚合函数，只做分组

output=[name#0, age#1]        输出还是这两列

这里相当第一次去重，在每个Executor本地，用HashMap 按 (name, age) 分组。相同的 (name, age) 只保留一条。

**Exchange hashpartitioning(name#0, age#1, 200), ENSURE_REQUIREMENTS, [id=#20]**

Exchange        Shuffle 操作，数据跨网络重新分发

hashpartitioning(name#0, age#1, 200)        按 name 和 age 的哈希值取模，分发到 200 个分区

ENSURE_REQUIREMENTS        这是 Spark 为了满足"相同 key 必须在同一分区"而自动插入的 Shuffle

[id=#20]        Spark 内部算子 ID，调试用的

把第 2 步输出的 (name, age) 对，按哈希值发到 200 个 Reducer 之一。保证相同 (name, age) 一定落在同一台机器上。

**HashAggregate(keys=[name#0, age#1], functions=[], output=[name#0, age#1])**

第二次 HashAggregate（Reduce 端全局去重）

这里和第二行一样其实，但是阶段不同

shuffle完了之后，每个reducer再次按照`(name, age)` 分组

此时整个集群范围内，相同的 `(name, age)` 已经都在本地了，再次分组就是全局去重。

到这一步，全局范围内 `(name, age)` 绝对唯一。 `DISTINCT` 的活干完了。

**HashAggregate(keys=[name#0], functions=[partial_count(distinct age#1)], output=[name#0, count#12L])**

keys=[name#0]        现在只按 name 分组

functions=[partial_count(distinct age#1)]        聚合函数：partial_count(distinct age)

output=[name#0, count#12L]        输出 name 和局部计数值

输入已经是全局唯一的 (name, age)，现在按 name 分组，数每个 name 有几条。

**Exchange hashpartitioning(name#0, 200), ENSURE_REQUIREMENTS, [id=#24]**

第二次 Exchange（Shuffle）

hashpartitioning(name#0, 200)        这次只按 name 哈希，分发到 200 个分区

把第 5 步的 `(name, count)` 按 `name` 重新 Shuffle。保证相同 `name` 落到同一台机器，才能做最终汇总。

**HashAggregate(keys=[name#0], functions=[count(distinct age#1)], output=[name#0, count(DISTINCT age)#7L])**

functions=[count(distinct age#1)]        这次是 Final 模式的 count(distinct)

output=[name#0, count(DISTINCT age)#7L]        最终输出列

相同 `name` 的局部计数已经碰头，直接加起来。

**AdaptiveSparkPlan isFinalPlan=false**

Spark 先按这个计划启动，跑完 Map 阶段后，AQE 可能会重新优化 Reduce 阶段的计划。

对 hive 的 count(distinct) 做优化，怎么做？   先 group by ，再 count 。然后通过以上分析我们我可以知道，对于 spark sql 的单个 one count(distinct)  的情况，系统已经帮我们做好了上述的优化，即先 group by ，再 count ，不需要我们再去主动优化。
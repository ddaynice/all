### 程序的入口

Flink程序可以在各种上下文环境中运行：可以在本地JVM中执行程序，也可以提交到远程集群上运行。

不同的环境，代码的提交运行的过程会有所不同。

这就要求我们在提交作业执行计算时，首先必须获取当前Flink的运行环境，从而建立起与Flink框架之间的联系。

该环境提供了控制作业执行（如设置并行性或容错/检查点参数）和与外部世界交互（数据访问）的方法。

哪StreamExecutionEnvironment就是

作业开发的入口、数据源接口、生成和转换DataStream的接口、数据Sink的接口、作业配置接口、作业启动执行的入口

但是这里还有一个叫org.apache.flink.runtime.execution.Environment

这个接口是运行时作业级别的概念，他是从上面 **StreamExecutionEnvironment 中的配置信息衍生出来的**

他这里是有作业的名称、并行度、作业编号JobID、监控的Metric、容错的配置信息、IO等相关的配置信息

整体的关系就是

那这里的最下面还有一个RuntimeContext，它是flink运行时Task实例级别的概念

其实就是因为Environment 本身的粒度还是比较粗

对于每一个Task而言，其本身有更细节的配置信息，所以Flink又抽象了RuntimeContext

每一个Task实例有自己的RuntimeContext

所以RuntimeContext是RichFunction运行时的上下文，封装了RichFunction运行时可能需要的所有信息，让RichFunction在运行时能够获取到作业级别的信息，如并行度相关信息、Task名称、执行配置信息(ExecutionConfig)、State等

### 源算子

这个就是字面的意思，Flink可以从各种来源获取数据，然后去构建DataStream进行转换处理

那这个时候将数据的输入来源称为数据源，你读取的数据的算子就是源算子

所以，source就是我们整个处理程序的输入端。

#### 从文件/文件夹读取数据

readTextFile这个就是从文件里读取

用法就是

- [ ] 

这里的readTextFile去看源码其实底层调用的就是readFile

而且这个readFile最终调用的还是addSource

**readTextFile方法默认是使用批处理的方式，如果要想使用流处理需要采用底层他的readFile方法**

- [ ] 

上面就是流处理的方式

这里

inputFormat表示的是文件读取的格式，一般使用的flink里的TextInputFormat,即一行数据是流中的一个元素

// filePath表示文件/文件夹的路径

// watchType表示文件处理的模式，有两个可选项：PROCESS_ONCE表示一次性读，即批；PROCESS_CONTINUOUSLY表示持续性读，即流

// interval表示流每次读取的时间间隔，默认是-1，表示批。如果设置了watchType，那么interval也要做相应的改动，单位是毫秒，最小是1

在实际的体现过程中PROCESS_CONTINUOUSLY他不是实时增量的读取，他是如果数据源改动了，他会把最新的所有的数据全都取出来的

不是一个extractly-once

#### 递归读取

- [ ] 

#### Pojo的使用

- [ ] 

TypeExtractor.createTypeInfo(...) Flink 的"类型侦探"——自动分析这个类的结构
(PojoTypeInfo<UserBehavior>) 强制类型转换，告诉编译器"我确定这是 POJO 类型"

**POJO 的判定条件（Flink 官方要求）**

你的 `UserBehavior` 完全符合：

#### 新的api

在flink 1.12正式环境中，我们读取文件，建议使用新类FileSource

File Source 是基于 Source API 同时支持批模式和流模式文件读取的统一 Source，File Source 分为以下两个部分：SplitEnumerator 和 SourceReader

**i、SplitEnumerator 负责发现和识别需要读取的文件，并将这些文件分配给 SourceReader 进行读取。**

**ii、SourceReader 请求需要处理的文件，并从文件系统中读取该文件**

那这里有界和无界又不一样

有界： File Source（通过 SplitEnumerator）列出所有文件（一个过滤出隐藏文件的递归目录列表）并读取。

无界：

无界的 File Source 由配置定期扫描文件的 enumerator 创建

在无界的情况下，SplitEnumerator 将像有界的 File Source 一样列出所有文件，但是不同的是，经过一个时间间隔之后，重复上述操作；

对于每一次列举操作，SplitEnumerator 会过滤掉之前已经检测过的文件，将新扫描到的文件发送给 SourceReader

- [ ] 

#### DataGen 连接器

这个是模拟数据主要是用于生成一些随机数，用于在没有数据源的时候，进行流任务的测试以及性能测试等

案例：

- [ ] 

#### 自定义反序列化

从kafka中消费数据的过程是需要将kafka中的数据进行反序列化的

哪KafkaSourceBuilder  提供了**setDeserializer和setValueOnlyDeserializer**这两个方法来反序列化

前面是反序列化完整的ConsumerRecord，后者是反序列化ConsumerRecord 的value

哪回答这个反序列化这里，反的是谁的消息 Kafka的消息

##### 核心问题：Kafka 消息长什么样？

**ConsumerRecord {**

**    topic: "my-topic",           // 主题**

**    partition: 0,                // 分区号**

**    offset: 12345,               // 偏移量**

**    timestamp: 1694000000,       // 时间戳**

**    key: "user_001",             // 消息的 key**

**    value: "1,100,3,click,..."   // 消息的真正内容（value）**

**    headers: {...}               // 消息头**

**}**

哪在看两个方法的参数

**setDeserializer 这个方法的参数是KafkaRecordDeserializationSchema **

但是setValueOnlyDeserializer  方法参数是DeserializationSchema

这两个方法返回的都是KafkaRecordDeserializationSchema 

那这里`DeserializationSchema` 只处理裸字节

public interface DeserializationSchema<T> {

    T deserialize(byte[] message) throws IOException;

}

可以看到源码这里输入只有 byte[]纯字节数组

`KafkaRecordDeserializationSchema` 处理完整的 Kafka 消息

public interface KafkaRecordDeserializationSchema<T> {

    void deserialize(ConsumerRecord<byte[], byte[]> record, Collector<T> out) throws IOException;

}

> 

哪这两个方法的关系：

- [ ] 

但是你看就能发现 `setValueOnlyDeserializer` 内部调用了 `KafkaRecordDeserializationSchema.valueOnly()`，把只处理 value 的接口包装成了能处理完整 record 的接口。

那这里的关系就是

- [ ] 

### 基本转换算子

#### map（映射）

map这个我是挺熟悉的但是吧我一直不清楚这个干什么用的，这个是用于数据流中的数据进行转换，形成新的数据流

简单来说就是一个**一一映射，一进一出，读取一条处理后输出一条数据**

但是这里因为数据是流式的，没有办法对整个分区进行map，所以DataStream里没有mapPartition算子，而在DataSet中就有

案例：

- [ ] 

#### 扁平映射（flatMap

这个式将数据流中的整体拆分成一个一个的个体使用

一进多出，消费一个元素，可以产生 0 到多个元素。

flatMap 可以认为是“扁平化”（flatten）和“映射”（map）两步操作的结合，

也就是先按照某种规则对数据进行打散拆分，再对拆分后的元素做转换处理。

- [ ] 

#### 过滤filter

对数据流执行一个过滤，通过一个布尔条件表达式设置过滤条件，对于每一个流内元素进行判断，若为 true 则元素正常输出，若为 false 则元素被过滤掉。进行 filter 转换之后的新数据流的数据类型与原数据流是相同的

- [ ] 

###  聚合算子

#### keyBy

Flink的DataStream里是没有直接进行聚合的API的。因为对海量数据做聚合肯定要进行分区并行处理，这样才能提高效率。所以在Flink中，要做聚合，需要先进行分区；

是通过keyBy来完成的

keyBy是聚合前必须要用到的一个算子。

keyBy通过指定键（key），可以将一条流从逻辑上划分成不同的分区（partitions）。

这里所说的分区，其实就是并行处理的子任务。

基于不同的key，流中的数据将被分配到不同的分区中去；

这样一来，所有具有相同的key的数据，都将被发往同一个分区。类似于Spark中的groupByKey，在flink dataStream中没有类似于groupBy的算子，在DataSet中有

**keyBy得到的结果将不再是DataStream，而是会将DataStream转换为KeyedStream，**

**KeyedStream可以认为是“分区流”或者“键控流”，它是对DataStream按照key的一个逻辑分区，类似于spark中的RDD的概念**

#### 简单聚合（sum/min/max/minBy/maxBy）

- [ ] 

#### 归约聚合（reduce）

- [ ] 

### 用戶自定义函数（UDF）

#### 富函数类（Rich Function Classes）

#### 什么是富函数？

"所有 Flink 函数类都有其 Rich 版本"

普通函数

富函数

`MapFunction`

`RichMapFunction`

`FlatMapFunction`

`RichFlatMapFunction`

`FilterFunction`

`RichFilterFunction`

富函数可以获取运行时上下文，拥有生命周期方法。

#### 2. 三个生命周期方法

方法

触发时机

调用次数

`open()`

算子被调用前

**每个并行实例只调一次**

`close()`

生命周期最后

**每个并行实例只调一次**

`getRuntimeContext()`

运行时随时

按需调用

##### RuntimeContext 能拿到什么？

> 

> 

> 

> 

> 

#### 核心设计思想

普通函数：来一条数据 → 处理一条 → 结束

         （没有准备阶段，没有清理阶段）

富函数：  open() 初始化 → 来一条处理一条 → close() 清理

         （有完整的生命周期）

"生命周期方法，对于一个并行子任务来说只会调用一次；而对应的实际的业务逻辑，例如 RichMapFunction 中的 map()，在每条数据到来后都会触发一次调用。"

并行度 = 2 时：

实例 0:  open() [1次] → map() [N次，每条数据] → close() [1次]

实例 1:  open() [1次] → map() [N次，每条数据] → close() [1次]

富函数 = 普通函数 + 生命周期（open/close）+ 运行时上下文（RuntimeContext）

- [ ] 

#### 物理分区算子

在flink中每个算子都可以设置并行度，比如上游的Map算子的并行度为3，下游的filter算子的并行度为4

哪这种上下游算子并行度不一致的情况下，flink怎么传递数据？

**这里就要涉及到flink的分区策略**

数据分区在Flink中叫做Partition，本质上，分布式计算就是把一个作业切分成子任务task，将不同的数据交给不同的Task计算

那么在partition分区概念就是把数据集切分成块，每一块数据存储到不同的机器上

**核心就是这里对于flink流处理来说，算子之间的数据流动要靠分区器，也就是StreamPartitioner**

##### 分区策略

###### GlobalPartitioner（对应的算子：global()

数据会被分发到下游算子的第一个实例中进行处理，即算子的第一个subtask。通过调用.global()方法，会将所有的输入流数据都发送到下游算子的第一个并行子任务中去。这就相当于强行让下游任务并行度变成了1，所以使用这个操作需要非常谨慎，可能对程序造成很大的压力。

###### ForwardPartitioner -forward

在API层面上ForwardPartitioner应用在 DataStream上，生成一个新的 DataStream。该Partitioner 比较特殊，用于在同一个OperatorChain中上下游算子之间的数据转发，实际上数据是直接传递给下游的，要求上下游并行度一样。上游算子与下游算子是1:1的关系。根据作业图对流图的优化，同一个OperatorChain的不同算子将在同一个slot中执行，即数据直接在本地传递给下游的算子

###### ShufflePartitioner（对应的算子：shuffle()）

将数据随机地分配到下游算子的并行任务中去。把流中的数据随机打乱，然后传递到下游任务分区。因为是完全随机的，所以对于同样的输入数据, 每次执行得到的结果也不会相同。需要注意的是不是均匀分布，而是随机分布

###### RebalancePartitioner（对应的算子：rebalance()）

以Round-robin（循环）的方式为每个元素分配分区，确保下游的 Task 可以均匀地获得数据，避免数据倾斜

###### BroadcastPartitioner（对应的算子：broadcast()

将记录广播给所有分区，即有N个分区，就把数据复制N份，所以这种方式其实不应该叫做“重分区”，因为经过广播之后，数据会在不同的分区都保留一份

###### CustomPartitionerWrapper

当 Flink 提供的所有分区策略都不能满足用戶的需求时，我们可以通过使用partitionCustom()方法来自定义分区策略。在调用时，方法需要传入两个参数，第一个是自定义分区器（Partitioner）对象，第二个是应用分区器的字段，它的指定方式与 keyBy 指定 key 基本一样：可以通过字段名称指定，也可以通过字段位置索引来指定，还可以实现一个KeySelector。

#### 分流

这里就是将一条数据流拆分成完全独立的两条，甚至多条流

也就是基于一个DataStream定义一些筛选条件，将符合条件的数据拣选出来放到对应的流里

- [ ] 

#### 测输出流

侧输出流就是将数据流进行分割

在DataStream API这里大部分的算子都是单一输出，也就是某种数据类型的流。

除了split算子可以将一条流分成多条流

**那这里process function 的 side outputs 功能可以产生多条流，并且这些流的数据类型可以不一样。一个 side output 可以定义为 OutputTag[T]对象，T 是输出流的数据类型。**

- [ ] 

#### 基本合流操作

##### 联合（Union）

联合操作要求必须流中的数据类型必须相同，合并之后的新流会包括所有流中的元素，数据类型不变

和sql一样其实也都是要转类型的

- [ ] 

#### 链接Connect

##### 连接流（ConnectedStreams）

一个DataStream中的数据只能有唯一的类型

所以连接得到的并不是DataStream，而是一个“连接流”

**连接流可以看成是两条流形式上的“统一”，被放在了一个流中；事实上内部仍保持各自的数据形式不变，彼此之间是相互独立的。**

**所以整体上来，两条流的连接就像是“一国两制”，两条流可以保持各自的数据类型、处理方式也可以不同，不过最终还是会统一到同一个DataStream中。**

需要分为两步：

首先基于一条 DataStream 调用.connect()方法，传入另外一条DataStream作为参数，将两条流连接起来，得到一个ConnectedStreams；

然后再调用协同处理方法得到 DataStream。这里可以的调用的协同处理方法有.map()/.flatMap()，以及.process()方法。

- [ ] 

#### 输出到文件

添加的依赖flink-connector-files同时实现了Source和Sink，其中sink是FileSink，为批处理和流处理提供了一个统一的Sink，它可以将分区文件写入Flink支持的文件系统

特点：

缓冲和批处理：Flinksink会将接收到的数据进行缓冲，直到缓冲区达到一定大小或者一定的时间间隔后，才会将数据批量的写入到文件，和shuffl差不多，这里对应的就是滚动策略，行模式默认60s滚动，如果不设，小文件会很多

分桶：FlinkSink可以将数据分为多个不同的文件桶进行处理，默认是按照系统时间分目录，如果按事件事件，需要自己实现BucketAssigner

#### 滚动策略：

这里滚动策略其实就是一个文件从"正在写"到"写完可见"的生命周期，以及谁来控制这个过程

文件的三个状态

- [ ] 

滚动策略只负责把文件从"正在写"变成"写完"，但文件要对下游可见，还得等 checkpoint 成功。这就是为什么必须开 checkpoint——不开的话文件永远卡在中间状态，下游看不到数据。

哪滚动策略这里有两个实现类

DefaultRollingPolicy（行模式用）：

这个是满足任意一条就关文件

DefaultRollingPolicy.builder()

    .withRolloverInterval(Duration.ofMinutes(15))      // 文件写了15分钟了，关

    .withMaxPartSize(MemorySize.ofMebiBytes(128))      // 文件到128MB了，关

    .withInactivityInterval(Duration.ofMinutes(5))     // 5分钟没来新数据，关

    .build();

CheckpointRollingPolicy（列模式/Parquet 专用）：

三个判断条件全返回 false，只有 checkpoint 来了才关文件。

但是为什么CheckpointRollingPolicy（列模式/Parquet 专用）只能按照checkpoint 滚动？

> 

> 

所以 Flink 干脆规定：列模式不允许按时间/大小滚动，跟着 checkpoint 节奏走，checkpoint 一次 finalize 一个文件，刚好和两阶段提交天然契合。

**滚动策略 = 决定"什么时候停止往当前文件写、开一个新文件"；**

**checkpoint = 决定"写完的文件什么时候对下游生效"。**

**行模式可以按时间/大小滚动，列模式（Parquet）只能跟着 checkpoint 滚动。**

#### 压缩策略

forRowFormat 行模式下：自定义内容限定于文件内部，想对文件进行压缩等操作，则很难办到；

forBulkFormat 列模式下：不仅可以对文件内部操作，也可以轻松做到对文件压缩等操作

##### 为什么行模式没法压缩

Gzip 压缩：FileSink支持使用Gzip算法对输出文件进行压缩。然后这里需要重新实现BulkWriter。
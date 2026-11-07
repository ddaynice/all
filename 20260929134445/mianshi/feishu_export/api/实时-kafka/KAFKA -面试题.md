红色是必背

黄色是理解但是尽量也背

## auto.offset.reset参数

这个是当消费者没有有效偏移量（offset）或偏移量失效时，从哪个位置开始消费消息

这里的话有三个参数

Earliest:当各分区下有已经提交offset的时候，从最近一次提交的offset开始消费，如果没有提交的话就从头开始消费

Latest:当各分区下有已经提交offset的时候，从最近一次提交的offset开始消费，没有提交的话，消费新产生的该分区下的数据，就是从最新数据开始消费

None:当各分区下有已经提交offset的时候，从最近一次提交的offset后开始消费，但是这里只要有一个分区没有提交offset就抛出异常

其实从这里就能看出来，对于已经提交过的offset，none，latest合earlist是没有区别的

但是如果没有提交offset，使用latest旧的数据就没办法读取到

因此只要不更改group.id，每次重新消费kafka，都是从上次消费结束的地方继续开始，不论"auto.offset.reset”属性设置的是什么

这里的`latest` 参数要注意是无书签时默认

准确来说只要有offset提交，goup_id不改就是从上个结束地方开始不会用参数

举个例子

- [ ] 

## Kafka 中的 ISR、AR 又代表什么？ISR 的伸缩又指什么

整体关系是

分区中的所有副本统称为AR

那所有和leader副本保持一定程度同步的副本包括leader 组成ISR

ISR就是AR集合中的一个子集

接着Follower和leader副本同步的时候，延迟过多的副本就放到OSR

整体就是AR=ISR+OSR

哪这里的ISR的伸缩：

leader副本是负责维护和ISR集合中所有的follower副本的滞后状态

如果follower副本落后太多了，甚至是失效了

leader副本会把他从ISR集合中剔除掉

如果OSR集合中有follower副本进度追上了follower,那么leader副本会把它从OSR集合转移到ISR集合

其实再默认情况下，当leader副本发生故障的时候，只有再ISR集合中的副本才有资格被选举为新的leader

哪你这个机会在OSR集合中是没有的

其实说白了

ISR 的"伸缩" = 动态维护一个"足够新、足够快"的副本白名单。

核心目的：在"数据不丢"（一致性）和"服务不挂"（可用性）之间做动态平衡。

这里的话replica.lag.time.max.ms 这个参数 是Follower副本能够落后Leader副本的最长时间间隔，默认是10秒

还有unclean.leader.election.enable 这个是 是否允许Unclean领导的选举。

这个参数的话开启可能导致数据丢失，但是好处就是他会使得分区leader副本一直存在

## Kafka 中的HW、LEO、LSO、LW 等分别代表什么？

HW 这个是High Watermark 的缩写，俗称高水位，它标识了一个特定的消息消费偏移量offset，消费者只能拉取到这个 offset 之前的消息

LSO是LogStartOffset  就是日志起始处，一般情况下 日志文件的起始偏移量LogStartOffset是等于第一个日志分段的baseOffset的

LEO是Log End Offset  这个虽然和上面对立，按道理来说因该是日志的结束，但是这个结束时动态的

他表示当前日志中下一条待写入消息的offset，这个时生产偏移量

下面这个图例的虚线9就是下一条消息也就是LEO

LEO在当前的日志分区中最后的一条消息的offset的值加一

并且分区ISR集合中的每个副本都会维护自身的LEO，那这里要注意在ISR集合中最小的LEO就是这个分区的HW

LW 这个和HW对立  Low Watermark 的缩写，俗称“低水位”

这个代表的是AR集合中最小的LSO的值

## 了解Kafka里的Controller吗？Controller的选举？职责？还有脑裂？

集群一般是主从或者主备模式 

像spark Standlone Master + Worker

yarn的 ResourceManager + NodeManager    

还有hdfs     NameNode（Master）+DataNode（Slave）

但是在kafka集群中各个broker之间是不存在主从 主备关系

为了能更好的管理broker上下线，topic分区的工作，这个时候旧会选举出一个contuoller的角色协调管理

这块Controller一般是与Zookeeper协助管理整个Kafka集群

**Controller选举流程：**

就是每个broker启动的时候都会和zookeeper交互，第一个在zookeeper建了controller目录的broker节点即被选举为Controller

**Controller的作用：**

集群内Broker节点的管理，包括新增，下线

副本leader选举，分区重分配

**脑裂**：

就是一个身体有了两个脑子

因为集群式属于分布式环境，所以可能会有很多因素造成broker和zookeeper之间的绘画失效

比如网络波动，长时间的GC无响应

这些问题造成了旧的Controller无法收到新的Controller选举结果，那么当网络或者GC恢复了之后，由于缺少了部分的记忆，旧的Controller还以为自己式**Controller角色，那么这里旧出现了两个Controller，这就是脑裂**

哪脑裂带来的影响就是数据不一致。所以kafka引用了epoch number来解决这个问题

epoch number就是一个单调递增的数据，每次**Controller角色的选举都会增加1**

同时Zookeeper回调会讲当前的epoch number通知到其他的Broker节点

如果在Controller发布的命令中，包含了比当前epoch number更小的值，那么broker会忽略这条命令，不做任何操作

## **Kafka 中的分区器、序列化器、拦截器是否了解？它们之间的处理顺序是什么？**

序列化器：这个就是发送和接收的意思，生产者需要使用序列化器吧对象转成字节数组才能通过网络发给kafka，反过来消费就需要使用反序列化器把从kafka中收到的字节数组转换成相应的对象

分区器：这个就是为消息分配分区，如果ProducerRecord 中没有指定 partition 字段，那么就需要依赖分区器，根据 key 这个字段来计算 partition的值

拦截器：主要在消费到消息或在提交消费位移时进行一些定制化的操作

处理顺序：拦截器->序列化器->分区器

整体来说：KafkaProducer 在将消息序列化和计算分区之前会调用生产者拦截器的 onSend() 方法来对消息进行相应的定制化操作。然后生产者需要用序列化器（Serializer）把对象转换成字节数组才能通过网络发送给Kafka。最后可能会被发往分区器为消息分配分区。

## kafka的Partition分配策略有哪些（背诵）

理想状态下Group内的Consumer实例因该等于该Group订阅topic的分区总数

所以partition的分配问题核心就是确定

哪个Partition由哪个Consumer来消费的问题

如果分区数量大于消费者

**部分消费者要消费多个分区，并行度受限**

过载（活儿干不完）

分区数量小于消费者 那就是资源有一部分浪费

**分配策略**

通过partition.assignment.strategy属性配置分区分配策略

可以同时配置多个分区分配策略

在2.0~2.8版本中，默认的分区策略是 RangeAssignor

在3.0之后默认分区策略是 [RangeAssignor,CooperativeStickyAssignor]

这个意思就是当消费者组启动以后默认使用 RangeAssignor 策略，但是当触发一次 Rebalance 之后，就会移除 RangeAssignor 协议，转而使用 CooperativeStickyAssignor

> 

这个是kafka的默认分区分配算法

它这个是按照topic维度进行的分配，对于每个Topic

> 

## Kafka 生产者客戶端的整体结构是什么样子的？

从整体上来说分为两个线程协调 主线程和 Sender 线程（发送线程）

但是中间还有个消息累加器，这个也是属于主线程

所以整体就是：主线程-消息累加器-sender线程

在主线程中由kafkaProduce创建消息，然后通过（可选）拦截器，序列化器和分区器 

然后再到消息累加器中

哪Sender线程负责从消息累加器里获取消息然后发送到Kafka中

**累加器主要用来缓存消息以便 Sender 线程可以批量发送，进而减少网络传输的资源消耗以提升性能**

**整体的图**

## 有哪些情形会造成重复消费？

**Rebalance**

一个consumer正在消费一个分区的一条消息，还没有消费完，发生了rebalance(加入了一个consumer)，从而导致这条消息没有消费成功，rebalance后，另一个consumer又把这条消息消费一遍。

Rebalance这个是再平衡

### 什么情况下会触发？

但是为什么**Rebalance会导致重复消费？**

首先offset的提交时异步的，Rebalance是突发的

- [ ] 

从上面来看其实Rebalance是Kafka为了保证每个分区有且只有一个Consumer消费而做的重新分配机制

但是这个机制会暂停所有的Consumer，如果某个Consumer正在处理消息并且offset没有提交，那条消息就会被下一个接手的Consumer重复消费。

消费者端手动提交如果先消费消息，再更新offset位置，导致消息重复消费。

消费者端自动提交设置offset为自动提交，关闭kafka时，如果在close之前，调用 consumer.unsubscribe() 则有可能部分offset没提交，下次重启会重复消费。

生产者端生产者因为业务问题导致的宕机，在重启之后可能数据会重发

## 哪些情景下会造成消息漏消费？（背诵

1.自动提交

设置offset为自动定时提交，当offset被自动定时提交时，

数据还在内存中未处理，此时刚好把线程kill掉，那么offset已经提交，

但是数据未处理，导致这部分内存中的数据丢失。

2. 生产者发送消息发送消息设置的是fire-and-forget（发后即忘）

它只管往 Kafka 中发送消息而并不关心消息是否正确到达。

不过在某些时候（比如发生不可重试异常时）会造成消息的丢失。这种发送方式的性能最高，可靠性也最差。

3. 消费者端先提交位移，但是消息还没消费完就宕机了，造成了消息没有被消费。

自动位移提交同理

4. acks没有设置为all如果在broker还没把消息同步到其他broker的时候宕机了，那么消息将会丢失

## 简述消费者与消费组之间的关系（理解）

首先consumer Group下是可以有一个或者多个Consumer实例的，实例就hi是一个单独的进程
然后Group id 是一个字符串，他是一个Consumer Group 的唯一标识

Consumer Group 下所有实例订阅的主题的单个分区，只能分配给组内的某个Consumer的实例消费

这个分区也能被其他的Group消费，就是说这个分区可以被不同的组消费

## 创建topic时如何选择合适的分区数？（背诵）

这个就得去测试了可以用Kafka提供的

用于生产测试的kafka-producer- perf-test.sh 

和用于消费者测试的kafka-consumer-perf-test.sh

这俩来测试选择

其实增加分区数在一定程度上可以提升整体的吞吐量，但是如果超过对应的阈值之后

吞吐量会不升反而下降

因为你分区过多->协调的开销就大 -> 网络的开销也增加 ->反馈到吞吐量上就是会被拉下来

而且分区多每个分区都要加载/关闭日志文件，分区越多越慢

每个分区独立清理，分区越多清理周期越长

**删除 Topic 更慢，**删除时要清理大量分区目录，耗时显著增加

### 测试出来

这里的花就要测试

比如

## 生产者性能测试

bin/kafka-producer-perf-test.sh \

--topic test-topic \

--num-records 1000000 \

--record-size 1024 \

--throughput -1 \

--producer-props bootstrap.servers=localhost:9092

## 消费者性能测试

bin/kafka-consumer-perf-test.sh \

--topic test-topic \

--messages 1000000 \

--bootstrap-server localhost:9092

逐步增加分区的数量，记录吞吐量的变化，找到合适的分区数阈值区间

分区数的多少还会影响系统的可用性。如果分区数非常多，如果集群中的某个 broker 节点宕机，那么就会有大量的分区需要同时进行 leader ⻆色切换，这个切换的过程会耗费一笔可观的时间，并且在这个时间窗口内这些分区也会变得不可用。

分区数越多也会让 Kafka 的正常启动和关闭的耗时变得越⻓，与此同时，主题的分区数越多不仅会增加日志清理的耗时，而且在被删除时也会耗费更多的时间

## Kafka目前有哪些内部topic，它们都有什么特征？各自的作用又是什么？（必背）

__consumer_offsets：作用是保存 Kafka 消费者的位移信息,替代早期版本存储在 ZooKeeper 中的设计

__transaction_state：用来存储事务日志消息

**__cluster_metadata KRaft 模式下存储集群元数据**

## 优先副本是什么？它有什么特殊的作用？（理解）

优先副本就是AR集合列表中的第一个副本

在理想的情况之下，优先副本就是这个分区的leader副本，所以也可以称为preferred leader

他的特殊作用就是为了解决leader不均衡的问题

比如

Broker 1 2 3 都有三个leader

broker 1宕机之后：Broker-1: 0 个 Leader（宕机）

Broker-2: 5 个 Leader ← 压力暴增

Broker-3: 4 个 Leader ← 压力增加

**Broker-1 恢复后：**
Broker-1: 0 个 Leader ← 闲着！
Broker-2: 5 个 Leader ← 还在扛
Broker-3: 4 个 Leader ← 还在扛

宕机的leader被分给其他的broker上，会负载不均衡

在开启优先副本之后

**Broker-1 恢复后，执行 Preferred Leader Election：**

Broker-1: 3 个 Leader ← 恢复！
Broker-2: 3 个 Leader ← 减负
Broker-3: 3 个 Leader ← 减负

哪优先副本这一行为也可以称为“分区平衡”

通过自动：`auto.leader.rebalance.enable=true`（默认开启）

其实优先副本是 Kafka 的"理想 Leader 蓝图"，通过优先副本选举实现**Leader 均匀分布**，从而**促进集群负载均衡**。

## Kafka有哪几处地方有分区分配的概念？简述大致的过程及原理（理解

1.生产者的分区分配

这个是指的为每条消息指定其所要发往的分区

可以编写一个具体的类实现org.apache.kafka.clients.producer.Partitioner接口

过程：Producer 发送一条消息，该发到 Topic 的哪个分区？

消息由key ->通过hash取余分匹配 ->相同的key进同一个分区

消息没有key ->Sticky Partitioner -》批量发同一个分区里

还有就是通过自定义分区器

- [ ] 

2.消费者中的分区分配

这个是为消费者指定可以消费消息的分区

Kafka 提供了消费者客戶端参数 partition.assignment.strategy 来设置消费者与订阅topic之间的分区分配策略

这里是有分配策略

**四种分配策略对比：**

**RangeAssignor（默认）**

按 Topic 维度分配，先排序再按范围切分。多 Topic 场景下负载不均。

**RoundRobinAssignor**

全局轮询分配，所有 Topic 的分区打平后轮流分。多 Topic 场景更均衡。

**StickyAssignor**

尽量保持现有分配不变，Rebalance 时最小化分区移动。适合有状态消费。

**CooperativeStickyAssignor**

增量 Rebalance，只移动受影响的分区。Kafka 2.4+ 推荐生产环境使用。

3.分区副本的分配

这个是为集群制定创建topic时的分区副本分配方案， 创建 Topic 时决定副本放在哪些 Broker。默认自动均匀分配，也可通过 `--replica-assignment` 手动指定。

kafka-topics.sh 脚本中提供了一个 replica-assignment 参数来手动指定分区副本的分配方案。

## 简述Kafka的日志目录结构（理解背诵

首先kafka中的消息都是以Topic为基本的单位进行归类的

各个topic在逻辑上是相互独立的

每个topic可以分成一个或者多个分区

哪这里的分区对应的就是日志log

为了防止Log过大，Kafka又引入了日志分段LogSegment，可以切成多个，类似blok块

Log 和 LogSegment 也不是纯粹物理意义上的概念，

Log 在物理上只以文件夹的形式存储，而每个 LogSegment 对应于磁盘上的一个日志文件和两个索引文件，以及可能的其他文件（比如以“.txnindex”为后缀的事务索引文件

哪整体的目录结构就是

topic主题-> partitions分区 ->分区有副本 replica ->每个分区副本对应一个log

log日志下又会分为LogSegment日志分段这样 -> 每个 LogSegment 对应于磁盘上的一个日志文件和两个索引文件，以及可能的其他文件（比如以“.txnindex”为后缀的事务索引文件）

### 延申问题：kafka有哪些所索引文件？

每个日志分段对应两个索引文件

.index的偏移量索引 他的作用是文件用来建立消息偏移量到物理地址之间的映射关系，目就是提高查找消息效率

.timeindex时间戳索引文件 

## 聊一聊你对Kafka的Log Retention的理解（理解背诵）

Log Retention：这个是日志删除，这个会按照一定的保留策略来进行删除，就是阈值其实

可以通过log.cleanup.policy 这个参数来设置策略 默认是delete 采用日志删除的清理策略

然后策略是由

基于时间的：

日志再删除的时候会检查保留的时间有没有超过设定的阈值，类似表的生命周期一样

可以通过log.retention.hours、log.retention.minutes 和 log.retention.ms

这三个来定，这里ms的优先级最高，最低的是hours

删除日志分段的流程：

首先会从Log对象中维度的日志分段跳跃表移除待删除的分段

然后讲日志分段对应的文件添加上.deleted后缀

最后会有一个deletefile 的延迟任务来删除这个被打上.deleted后缀 的文件

基于日志大小

通过 broker 端参数log.retention.bytes来配置，默认值为-1，表示无穷大。

但是这个配置的是Log中所有日志文件的总大小，不是单个的日志文件

单个的日志文件由 broker 端参数 log.segment.bytes 来限制，默认值为1073741824，即 1GB

基于日志起始偏移量

基于日志起始偏移量的保留策略的判断依据是某日志分段的下一个日志分段的起始偏移量 baseOffset 是否小于等于logStartOffset，若是，则可以删除此日志分段

首先要搞清楚什么是logStartOffset 这个是整个分区中目前最小有效消息的offset

换句话说，logStartOffset 左边的消息，对消费者来说已经不可见了。

也就是小于logStartOffset 这个的就都会被删除
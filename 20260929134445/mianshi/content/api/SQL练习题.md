## 有一张表ids记录了id，id不重复，但是会存在间断，求出**连续段的最后一个数**及**每个连续段的个数**。

---

WITH ids AS (

    SELECT 1 AS id UNION ALL

    SELECT 2 AS id UNION ALL

    SELECT 3 AS id UNION ALL

    SELECT 5 AS id UNION ALL

    SELECT 7 AS id UNION ALL

    SELECT 9 AS id UNION ALL

    SELECT 10 AS id UNION ALL

    SELECT 11 AS id UNION ALL

    SELECT 13 AS id UNION ALL

    SELECT 14 AS id UNION ALL

    SELECT 17 AS id UNION ALL

    SELECT 18 AS id UNION ALL

    SELECT 19 AS id

)

--连续的最后一个个数

--再把连续的id个数输出

就是连续登录问题，连续登录是日期相减，这个就是id相减就行

- [ ]

## 求**连续3天及以上**减少碳排放量不低于100的用户，输出**用户id和最大连续减排天数**。

1.连续三天

2.减少碳排放量>=100

3.

- [ ]

- [ ]

## 假设我们有一张订单表**order**，字段有：shop_id,order_time,order_amt，题目需要**计算【出现过连续10天及以上】销售金额连续增长的商户shop_id**

1.连续10天

2.

- [ ]

## 本题目为某自动驾驶汽车大厂**SQL面试真题**

考察的是相对比较罕见的题目类型：**交叉开窗**，没接触过的同学可以好好挑战一下！

- [ ]

---

**业务背景：**

**vin** 可以理解为车辆的 id，整个表记录的是一个车辆自动变道的过程：整个过程是**先亮起转向灯**，也就是 **indicator** 字段，然后是开始上报准备变道的信号 **auto_change**，也就是 **ACTIVE_LEFT**，表示激活了向左变道，没激活之前是 **AVL **

**lane** 就是当前道路，变道激活后，具备变道条件后开始变道，lane 从1 变成 0 表示变道完成，左边第一条道路是0，完成变道后关闭转向灯，然后停止上报激活信号。

**【有点绕，好好理解一下】**

**题目要求：**

计算**每辆车的每一次转向灯的时间间隔**，以及对应的这次**变道信号的时间间隔【如果在某一种转向灯状态的持续时间内，有多种变道信号，则取最长的那个作为变道信号的时间间隔】**

**结果示例：**

**解释：**

**indicator_window含义：**

>

>

**auto_window含义：**

>

>

>

>

**indicator_duration含义：**

>

>

>

>

**auto_duration含义：**

>

>

>

>

>

>

## **某平台在双 11 大促期间（2024-10-15 至 2024-11-11）开展抽奖活动，规则如下：**

>

>

>

##### 需求：请使用 Hive SQL 编写代码，完成以下任务：

>

>

>

**已知数据表：promotion_consumption_di（用户推广消耗记录表），包含字段：**

>

>

>

>

- [ ]
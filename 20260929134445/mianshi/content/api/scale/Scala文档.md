## 1 导学

### 1.1 课程概述

>

>

>

### 1.2 Scala 我们该如何学习呢？ ☆☆

>

[https://docs.scala-lang.org](https://docs.scala-lang.org/tutorials.html)

>

https://docs.scala-lang.org/overviews/scala-book/introduction.html

<快学 Scala>、<Scala 实用指南>、<Scala 编程>

>

[https://www.scala-lang.org/api/current/](https://www.scala-lang.org/api/current/)

### 1.3 编程语言概述☆

#### 1.3.1 编程语言之分

>

语言是个进化的过程，所谓的机器语言就是只有机器能够识别的一系列的0和1，而对于汇编语言用英文字母或符号串来替代机器语言，把不易理解和记忆的机器语言按照对应关系转换成汇编指令。

由于汇编语言依赖于硬件，使得程序的可移植性极差，而且编程人员在使用新的计算机时还需要学习新的汇编指令，大大增加了编程人员的工作量，为此计算机高级语言诞生了（人类所有技术的进步都是为了提高生产效率）。高级语言不是一门语言，而是一类语言的统称，它比汇编语言更贴近于人类使用的语言，易于理解、记忆和使用。由于高级语言和计算机的架构、指令集无关，因此它具有良好的可移植性。

>

（1）动态类型语言指是在运行期间才检查数据的类型的语言。使用这类语言编程时，不用给任何变量指定数据类型。该语言会在第一次赋值给变量时，在内部将数据类型记录下来。

常见的动态类型语言有：Python、JS、Scala

（2）静态类型语言是会在编译期间做检查数据类型的语言，即写程序时要声明所有变量的数据类型，是固定的。使用数据之前，必须先声明数据类型（int，float，double 等）。相当于使用之前，首先要为它们分配好内存空间。

常见的静态类型语言有：C、C++、Java

>

1）编译型语言是指程序在执行之前需要一个专门的编译过程，把程序源文件编译为机器语言的文件，运行时不需要重新编译，执行效率高。但缺点是编译型语言依赖编译器，跨平台性差。

常见的编译型语言有：C、C++、Java、Scala

（2）解释型语言是指在运行时，要先进行翻译再运行（每执行一次都要翻译一次）。解释型语言执行效率低，但跨平台性好

常见的解释性语言有：Python、JS、Java、Scala

总结：Scala 是一种优美的、富有表现力的编程语言。它具有简洁、现代的语法，支持函数式编程（FP）和面向对象编程（OOP），并提供安全的静态类型系统

### 1.4 Scala 概述 ☆

#### 1.4.1 Scala 是怎么诞生的？

Scala 的创始人是联邦理工学院洛桑（EPFL）的 **Martin Odersky**（马丁·奥德斯基），Odersky

>

>

>

>

>

#### 1.4.2 有哪些公司在用 Scala?

>

>

>

>

>

#### 1.4.2 大数据从业人员为什么要学 Scala 呢？

### 大数据组件中核心计算引擎 Spark 核心部分使用 Scala 开发

>

>

而以上这三种框架也是我们大数据工程师走向更远处所必备的基础技能，有兴趣的同学可以持续关注我们后续的相关课程，我们都会持续的进行课程迭代。

### 1.5 Java和Scala的区别 ☆☆

从上图可以看出来，Java和Scala都是构建于JVM之上的高级语言，而Scala在设计之处作者就参考了Java大量的设计思想，因此Scala本身的语法特性又有很多和Java的相似之处，所以可以理解为Scala源于Java，是Java的便捷版本，很多语法都是为了简化Java过于冗余的写法，所以Scala是一门可以大大提高工作效率的大数据工程师必备的语言之一。

### 1.6 面试题&思考题

>

>

>

## 2环境

### 2.1 Scala 环境安装☆☆

#### 2.1.1 概述

Scala是构建在JVM之上的一门编程语言，它的设计目标就是与Java的无缝对接，所以安装Scala环境首先得先安装JDK

操作步骤：

#### 2.1.2 安装JDK

安装JDK，相信同学们已经在学习Java的过程中，已经安装好了，此操作略过

#### 2.1.3 安装Scala

操作步骤：

i、下载Scala安装包

官方的下载地址： [https://www.scala-lang.org/download/2.12.17.html](https://www.scala-lang.org/download/2.12.17.html)

说明：mac版本和wins版本2下载后是需要需配置环境变量，才可以使用

ii、点击安装Scala

下载完成后，点击scala-2.12.17.msi ，然后一路无脑点击下一步直至完成。iii、打开控制台，输入scala -verison检查是否安装成功

### 2.2 Scala初体验☆☆

按住window+r，输入scala，然后我们就进入了一个黑色小框，这就是Scala的命令行界面

### 2.3 Scala关联IDEA☆☆

见实操

### 2.4 练习

i、scala环境的安装

ii、idea关联scala

## 3 Scala变量、操作符及输入输出

### 3.1 常见的类型☆☆

Scala中的类型和Java中的类型大多是一样的，包括类型的描述和数值区间，下面是Scala中所有的类型，其中有些类型我们会放在后面详细的描述

从上图中我们可以发现

>

>

>

>

>

>

>

### 3.2关于val和var☆☆

>

>

>

备注：一般情况下，我们如果可以使用val，我们就尽量使用val。

### 3.3变量语法格式☆☆

val/var 变量名：变量类型 = 初始值

其中Scala基于语法的简洁性，变量类型可以不用写，Scala可以通过初始值的类型自动推断出变量的类型

### 3.4 案例及注意事项☆☆

object Demo {
  def main(args: Array[String]): Unit = {
    //val 类型的声明,表示一个常量，是不可变的
    val aa:Int = 10 // 在scala中，尾部的分号可以不写，但是写也没有问题
    // aa = 100

    // var 类型的声明，是一个变量，可以改变值
    var bb:String = "abc"
    bb = "ecf"

    //（1）声明变量时，类型可以省略，编译器自动推导，即类型推导
    var cc = 1
    *println*(cc.getClass) //int
    cc = 2

    //（2）但是一旦确定类型之后，就不能修改，说明 Scala 是强数据类型语言。
    // age = "tom" // 错误

    //（3）变量声明时，必须要有初始值
    // var name //错误

// 但是如果在声明的时候确实没有想好该赋什么值，可以使用_表示，_表示一个占位符，编译器会根据你变量的类型赋予相应的初始值

var name = _

        // (4)Scala还可以将多个变量放在一起进行声明，将一个数值同时赋给多个变量
val a,b,c = 100

    // p1 是 var 修饰的，p1 的属性可以变，而且 p1 本身也可以变
    var p1 = new Student()
    p1.*name *= "lisi"
    p1 = null
    // p2 是 val 修饰的，那么 p2 本身就不可变（即 p2 的内存地址不能变），但是，p2 的属性是可以变，因为属性并没有用 val 修饰。
    val p2 = new Student()
    p2.*name*="zhangsan"
    // p2 = null // 错误的，因为 p2 是 val 修饰的
  }
}
class Student{
  var *name *: String = "zhangsan"
}

### 3.5 Scala 算数与操作符☆☆

#### 3.5.1算数与操作符概述

>

>

>

#### 3.5.2 基本语法

**a 操作符 b  **等价于** a.操作符方法(b)**

**备注：在 Scala 中其实是没有运算符的，所有运算符都是方法。**

#### 3.5.3 示例代码

def main(args: Array[String]): Unit = {
  val a = 1 + 1
  val b = 1.+(1)
  *println*( a == b )
}

Ps：上述代码中，a.+(b)中的符号+表示的是方法名;

Scala 中的方法命名没有 Java 那么严格，我们几乎可以使用任何符号为 Scala 方法命名；与 Java 中的操作符相比，Scala 有一个明显的不同之处，那就是 Scala 没有提供操作符++和- -；如果我们想实现递增或者递减的效果，可以使用 “+ =1”或者“- =1”这种方式来实现。

其内幕是这些数值类型都是类，并且 **Scala 通过****隐式转换****为这些类型提供了很多常用方法**。

备注：隐式转换属于scala中的高阶部分，这里有个印象即可，后面会着重讲解。

比如说 Scala 提供了 RichInt，RichChar，RichDouble 等，分别为 Int，Char，Double 提供其所不具备的方法

比如表达式：1.to(10)，Int 值1首先被隐式转换为 RichInt，然后应用 RichInt 类的方法。

**注：****在 Scala 中，建议使用方法而不是强制类型转换来做数值类型之间的转换**，比如说 1.4.toInt得到 1, 99.toChar 得到 c

### 3.6 键盘输入☆☆

在编程中，需要接收用户输入的数据，就可以使用键盘输入语句来获取：**StdIn.readLine()**、StdIn.readInt()、StdIn.readDouble()

def main(args: Array[String]): Unit = {
  *println*("input name:")
  val name = StdIn.readLine()
  *println*("input age:")
  val age = StdIn.readInt()
  *println*("my name is " + name + ", my age is " + age)
}

### 3.7 格式化输出☆☆

**（1）println的用法**：常规的字符串的输出。

**备注：**字符串可以通过+号连接，这点和java类似，但是需要注意的是在scala中可以使用*将一个字符串复制多次拼接，如：name*3

**（2）printf 用法**：字符串，通过%传值，类似与C语言中的，常见的类型表示如下表，了解即可，在需要用的时候查询

def main(args: Array[String]): Unit = {
  val name = "zhangsan"
  val age = 12
  //%d表示Int类型的引用,%s表示字符串类型的引用,\n表示换行
  *printf*("%d岁的%s\n", age, name)
}

**（3）字符串模板（s""）**：通过$获取变量值

def main(args: Array[String]): Unit = {
  val name = "zhangsan"
  val age = 12
  //s""表示字符串模板,使用${}引用变量
  *println*(s"**$**{age}岁的**$**{name}")

*println*(s"**$**{age+3}岁的**$**{name*3}")

}

**（4）字符串模板（f""）**：可以理解是printf和s字符串模板的结合

def main(args: Array[String]): Unit = {
  val name = "zhangsan"
  val age = 2.3456
  //s""表示字符串模板,使用${}引用变量
  *println*(f"**$**{age}%2.2f岁的**$**{name}")
}

**（5）三引号换行输出**：可以结合$一起使用

多行字符串，在 Scala中，利用三个双引号包围多行字符串就可以实现输入的内容带有空格、\t 之类。但是存在一个问题就是三引号的写法会将内容**原封不动**的输出，可能会导致每一行的开始位置不能整洁对齐。应用 scala 的 stripMargin 方法，**在 scala 中 stripMargin(表示忽略|的左边界，右边界原样输出) 默认是“|”作为连接符，**在多行换行的行头前面加一个“|”符号即可（一般情况换行自动生成“|”）。

**备注：**以上是这部分内容中最重要的，也是企业中用的最多输出字符串的方法。

def main(args: Array[String]): Unit = {
  // 这里顺带说一句，scala中的所有注释的方法和java中一模一样
 /*
  select *
    from
  student
  where
  name = 'Tom'
  */
  val name = "Tom"
  val testSql: String =
    s"""
       |select *
       |from
       |   student
       | where
       |   name = '**$**{name}'
       |""".stripMargin
  *println*(testSql)
}

### 3.8 练习题及面试题

1、将文档里的代码多敲一敲，多动动手，不能只动眼

2、面试：scala中val和var的区别及注意点

3、面试：scala中类型体系的大致架构（看图说话）

4、面试：重点理解三引号和stripMargin

## 4 流程控制

### 4.1 if else☆☆

语法和java中一样，不花时间说，但是需要注意的是，因为**在scala中任何表达式都是有返回值的**，因此在Scala中if else也是有返回值。

def main(args: Array[String]): Unit = {
  *println*("input age")
  val age = StdIn.readInt()
  val res :String = if (age < 12){
    "童年"
  }else if(age>=12 && age<40){
    "青年"
  }else{
    "中老年"
  }
  *println*(res)
}

另外需要注意的是，scala中没有java中的三元运算符的语法，但是可以使用if else替代，如下：

def main(args: Array[String]): Unit = {
  *println*("input age")
  val age = StdIn.readInt()
  //java中的写法是：String str = age < 10 ? "童年" : "成年"
  val res = if (age < 12) "童年" else "成年"
  *println*(res)
}

### 4.2 switch☆☆

Scala中没有switch语法，可以用模式匹配代替，具体什么是模式匹配，后面重点说。

### 4.3 while和do while循环☆☆

Scala 中的while和do while循环和java中的用法完全一致。while 语句没有返回值，即整个 while 语句的结果是 Unit 类型，值为()。因为 while 中没有返回值，所以当要用该语句来计算并返回结果时，就不可避免的使用变量，而变量需要声明在 while 循环的外部，那么就等同于循环的内部对外部的变量造成了影响，所以不推荐使用，而是**推荐使用 for 循环**。

说一个while关于死循环的问题：需求是读一个文本中的数据

先看看java中是如何实现的：

public static void main(String[] args) throws Exception{
    String path = "C:\\Users\\14553\\Desktop\\scala集合.txt";
    BufferedReader br = new BufferedReader(new FileReader(path));
    String len = "";
    while ((len=br.readLine()) != null) {
        System.*out*.println(len);
    }
}

以上是可以正确输出，并且程序可以正常退出，再来看看scala的写法：

def main(args: Array[String]): Unit = {
  val path = "C:\\Users\\14553\\Desktop\\scala集合.txt"
  val br = new BufferedReader(new FileReader(path))
  var len = ""
  while ((len = br.readLine) != null){
    System.*out*.println(len)
  }
}

但是可以发现以上程序并不是输出一个正确的结果，并且程序一直在死循环中无法退出，究其原因就是(len = br.readLine)这个表达式在scala中是有返回值的，且返回值的结果为()，而这个结果永远是满足() != null，因此while会一直循环。

**打死都要记住：在scala中任何表达式都是有值的**

因此为了解决以上的问题，可以采用标志位的形式解决死循环的问题：

def main(args: Array[String]): Unit = {
  val path = "C:\\Users\\14553\\Desktop\\scala集合.txt"
  //读取文件
  val br = new BufferedReader(new FileReader(path))
  //设一个标记
  var flag = true
  while (flag) {
    val len = br.readLine()
    //if判断,满足条件,改变标记值,下回跳出循环
    if (len == null) {
      flag = false
    }else{
      *println*(len)
    }
  }
}

### 4.4 for循环（重点掌握）☆☆

#### 4.4.1 scala中的基本for语法

语法：for(循环变量 <- 数据集)

For (int i=0;i<100;i++)

解释：1、循环变量不需要写类型，也不需要使用val或者var来修饰

          2、**<-** 可以理解为循环的标志，是一个整体，不可以分开写，本质上<-也是一个方法，知道即可，直接理解成循环标志就行。

          3、数据集常见的有：

               i、集合，如字符串、数组、List，Set等

               ii、由to方法表示的左右闭合的序列

               iii、由until方法表示的左闭右开的序列

                 备注：上述两个按步长1递增的，可以使用by方法指定步长

               iv、可以方法reverse表示倒序

实战案例：

def main(args: Array[String]): Unit = {
  val list = *List*(1,2,3,4,5)
  for(i <- list){
   *println*(i)
  }

  // 其实scala中还有一个关于方法的写法，对于一个方法有参数，有调用者时
  // 可以写成 调用者 方法 参数 的形式，等价于 调用者.方法(参数)
  for(i <- 1 to 10){
    *println*(i)
  }

  for(i <- 1 until 10){
    *println*(i)
  }

  for(i <- 1 to 10 by 2){
    *println*(i)
  }

  for(i <- 1 to 10 reverse){
    *println*(i)
  }
}

#### 4.4.2 循环防卫

所谓循环防卫听起来很高端，但是实质就是for和if的语法上的一种结合，可以理解为便捷开发的一种方式。所谓防卫就是符合条件的放行，不符合条件的跳过，而这个和java中continue关键字的功能相吻合，而scala的语法中又没有continue关键字，因此可以用此种语法代替循continue的功能。

实战案例：取偶数

def main(args: Array[String]): Unit = {

//常规在for循环中添加if判断
  for (i <- 1 to 10){
    if(i % 2 == 0){
      *println*(i)
    }
  }

// 使用循环防卫
  for(i <- 1 to 10 if i % 2 == 0){
    *println*(i)
  }
}

#### 4.4.3 嵌套循环

和循环防卫一样，也是一种便捷开发的方式，是多重for循环的简化写法，大大的提高了开发效率。

语法：

def main(args: Array[String]): Unit = {
  // 常规嵌套
  for (i <- 1 to 10){
    for(j <- 1 to 10){
      *println*(i+j)
    }
  }

  // scala风格的嵌套，多层循环使用分号（;）分割
  for(i <- 1 to 10; j <- 1 to 10){
    *println*(i+j)
  }
}

项目实战：九九乘法表

object First {
  def main(args: Array[String]): Unit = {

    *println*("***********************************九 九 乘 法 表***************************************")
    for(i <- 1 to 9; j <- 1 to 9){
      *print*(s"**$**{i} x **$**{j} = **$**{i*j}")
      *print*("\t")
      if( j == 9){
        *println*()
      }
    }

    *println*("\n\n")

    *println*("****************************************九 九 乘 法 表***************************************")
    for(i <- 1 to 9; j <- 1 to 9 if i >= j ){
      *print*(s"**$**{i} x **$**{j} = **$**{i*j}")
      *print*("\t")
      if( i == j){
        *println*()
      }
    }
  }
}

#### 4.4.4 引入变量

def main(args: Array[String]): Unit = {
  for( i <- 1 to 10; j = i * i){
    *println*(s"i的值是**$**{i},j的值是**$**{j}")
  }
}

说明：

（1）for 推导式一行中有多个表达式时，所以要加 ; 来隔断逻辑

（2）for 推导式有一个不成文的约定：当 for 仅包含单一表达式时使用圆括号，当包含多个表达式时，一般每行一个表达式，并用花括号代替圆括号，这样就可以不用使用分号进行表达式的分割，如下：

def main(args: Array[String]): Unit = {
  for{
    i <- 1 to 10
    j = i * i
  }{
    *println*(s"i的值是**$**{i},j的值是**$**{j}")
  }
}

#### 4.4.5 for表达式的返回值

一般情况下for返回的是一个类型为Unit的值，为(),如下

def main(args: Array[String]): Unit = {
  val res = for( i <- 1 to 10){}
  *println*(res) // 返回的结果是()
}

但是如果想要收集for循环的结果，可以借助yield关键字，返回的是一个Vector的集合类型，这里暂且可以把这个类型理解为List，后面课程会详细讲解。

def main(args: Array[String]): Unit = {
  val res = for( i <- 1 to 10) yield i
  *println*(res) // Vector(0, 1, 2, 3, 4, 5, 6, 7,  8, 9, 10)
}

项目案例：偶数不变，奇数变成原来的五倍

def main(args: Array[String]): Unit = {
  val res = for (i <- 0 to 10) yield {
    if (i % 2 == 1)
      i * 5
    else
      i
  }
  *println*(res) // Vector(0, 5, 2, 15, 4, 25, 6, 35, 8, 45, 10)
}

#### 4.4.6 控制中断☆☆☆

我们知道在java中有continue和break两个关键字可以跳过或者是跳出循环，但是我们却发现在scala中没有这两个关键字，原因是scala在设计的时候推荐使用函数式编程，用最少的关键字实现最全的功能。但是如果想在scala中实现这两个功能怎么办呢？上面已经说过了可以使用循环防卫实现continue的功能，下面重点说一下break的功能在scala中是如何实现的

方法一：采用异常的方式推出循环

def main(args: Array[String]): Unit = {
  try {
    for (elem <- 1 to 10) {
      *println*(elem)
      if (elem == 3)
        throw new RuntimeException
    }
  }catch {
    case e =>
  }
  *println*("跳出循环")
}

方法二：采用scala自带的方法退出

import scala.util.control.Breaks

object First {
  def main(args: Array[String]): Unit = {
    Breaks.breakable(
      for (elem <- 1 to 10) {
        *println*(elem)
        if (elem == 3)
          Breaks.break()
      }
    )
    *println*("跳出循环")
  }
}

### 4.5 练习题及面试题

1、自己实现逆输出九九乘法表

2、面试：理解scala中的表达式都是有返回值的

3、面试：必须要深刻把握for循环的所有的形式

4、面试：拔高题，scala中怎么实现break和continue

## 5 方法和函数

### 5.1方法的声明（定义）☆☆

在前面我们其实已经学过了很多的方法，比如我们说的操作符，stripMargin都是方法，首先我们要明白方法是什么意思，方法的定义是给定一个或者是多个（甚至是零个）输入，通过某种规则，将输入转化成输出，而这种规则我们就称之为方法，因为**方法可以理解是对规则的封装。**

在此之前我们学过java的中方法的定义，如下：

public static int func(int aa){

        // 某种规则

        return bb

}

抽象出来就是：

**方法描述符 返回值类型 方法名(输入参数类型 输入参数名称){**

**// 规则**

**return 返回值**

**}**

而在scala在声明方法也类似，只是语法结构不同，但是应该抓住本质的东西。Scala中的方法声明如下：

**修饰符** **def 方法名(输入参数名称：输入参数类型): 返回值类型 = {**

**// 某种规则**

**return 返回值**

**}**

其中：

备注：在scala中，所有表达式的返回值都是表达式中逻辑的最后一行代码的返回值。

object First {
  def main(args: Array[String]): Unit = {

    // 定义一个sum方法，该方法有两个参数，返回值为int类型
    def sum1(a:Int, b: Int): Int = {
      return a + b
    }

    def sum2(a:Int, b: Int): Int = {
       a + b // return不写，默认之后一行实际执行到的地方，并不是代码的最后一行
    }

    def sum3(a:Int, b: Int): Int = {
      if(a < 0)
        -a + b
      else
        a + b
    }

    // 当返回类型不写时，就不能写return，如果需要在代码中写return，那么就要在方法声明的地方指出返回值类型
    def sum4(a:Int, b: Int) = {
       a + b
    }
  }
}

Scala 允许指明方法的最后一个参数可以是重复的，即不需要指定函数参数的个数，可以向函数传入可变长度的参数列表。

**注意：**Scala 通过在参数的类型之后放一个星号来设置可变参数(可重复的参数)，而在Java中是使用三个英文的点号“…”表示可变参数的。

**“可变参数”就是：你可以传任意个数（包括0个）的某个类型参数，编译器会自动把它们打包成一个数组或序列。**

object First {
  def main(args: Array[String]) {
    *printStrings*("Runoob", "Scala", "Python");
  }

  def printStrings( args:String* ) = {
    var i : Int = 0;
    for( arg <- args ){
      *println*("Arg value[" + i + "] = " + arg );
      i = i + 1;
    }
  }
}

需要注意的是如果参数列表中存在多个参数，那么可变参数一般放置在最后

def test2( name : String, s: String* ): Unit = {

println(name + "," + s)

}

test2("wang", "hu", "jian")

**参数默认值****，一般将有默认值的参数放置在参数列表的后面**，因为Scala 函数中参数传递是，从左到右。如果参数传递了值，那么会覆盖默认值，如果参数有默认值，在调用的时候，可以省略这个参数

def test3( name : String, age : Int = 30 ): Unit = {

println(s"$name, $age")

}

test3("hujian")

但是**如果将参数默认值放在前面，则可以通过指定****带名参数**。

def test4( sex : String = "男", name : String ): Unit = {

println(s"$name, $sex")

}

// test4("wusong")  //报错

test4(name="ximenqing")

}

### 5.2函数的声明（定义）☆☆

在java中没有区别方法与函数的区别，有些人称作方法，有些人称作函数，其实都是一个意思，而**在scala中，大部分的情况下也不必区分方法和函数**，比如5.1中方法的定义也使用与函数，而在实际的工作中一般人也没有加以区别，而一些特殊的场景中我们可以去区别方法和函数，我们将在后续学完特质（trait）之后再详细的解释方法和函数区别的场景，因此以后在工作或者在面试中，除非特殊说明，否则我们都可以认为方法===函数。

Scala是一门便捷开发的语言，而便捷的特性在函数中体现的尤为明显，所谓便捷即在开发的过程中能省则省，就是所谓的函数的至简原则，有以下几点，要求所有人必须掌握。

**（1）第一点就是我们之前提到的，return 可以省略**，Scala 会使用函数体的**逻辑****上的最后一行代码作为返回值**

def f1( s : String ): String = {

s

}

**（2）如果函数体只有一行代码，可以省略花括号**

def f2(s: String): String = s

（3）返回值类型如果能够推断出来，那么可以省略:和返回值类型一起省略

def f3( s : String ) = s

（4）如果有 return，则不能省略返回值类型，**必须指定**

def f4(): String = {

return "ximenqing4"

}

（5）如果函数明确声明 **Unit**，那么即使函数体中使用 return 关键字也不起作用

**（6）Scala 如果函数是没有返回值类型，可以省略等号，将无返回值的函数称之为过程**

def f6() {

"dalang6"

}

（7）如果**函数无参**，但是声明了参数列表，那么**调用时，小括号可加可不加**

def f7() = "dalang7"

f7

**（8）如果函数没有参数列表，那么小括号可以省略，****调用时小括号必须省略**

def f8 = "dalang"

println(f8)

### 5.3 匿名函数（lambda函数）☆☆

**如果函数不关心名称，****只关心逻辑处理****，那么函数标识符（def）可以省略，称之为匿名函数**

语法结构：**(x:Int)=>{函数体}**

其中：

x：表示输入参数类型；

Int：表示输入参数类型；

**=>：匿名函数的标志**

函数体：表示具体代码逻辑

案例：(x:String)=>{println("wusong")}

因为匿名函数没有名字，所有没有办法提供给别人使用，所以一般会有两种用法：

1、为函数也是个表达式，所以也可以赋值给一个变量，如下：

def main(args: Array[String]): Unit = {
  val res = (x:String)=>{*println*("wusong")}
  *println*(res.getClass()))
}

2、作为一个参数传递给另外一个函数，这里就涉及到scala中的函数高级特性，函数本身也可以作为一个参数传递给另外一个函数的参数，因为函数本身也是一个表达式。

### 5.4 scala函数中的高级特性☆☆

在 Scala 中，函数是一等公民。**所谓一等公民，即对于一个函数不仅可以，定义函数、调用函数，但是还有更高阶的用法**

**在scala中，所有的函数的背后其实都会有一个对应函数类型。**

因此函数本身就像scala中的Int一样也是一种数据类型，只不过Int类型的祖先类是AnyValue，函数的类型的祖先类是AnyRef

函数类型的格式：**函数类型名 : (输入参数类型) =>输出参数类型**

类比：

var name ：String // String类型变量声明

var func : (String，Int) => Int// 函数类型变量声明

当我们知道函数类型的声明之后，我们就可以进一步去研究函数更多的高阶用法：

**1）函数可以作为值进行传递**

def main(args: Array[String]): Unit = {
  //（1）调用 foo 函数，把返回值给变量 f
  //val f = foo() // ()可以省略
  val f = *foo*
*  println*(f)
  //（2）在被调用函数 foo 后面加上 _，相当于把函数 foo 当成一个整体，传递给变量 f1
  val f1 = *foo *_
  *foo*()
  f1()
  //（3）如果明确变量类型，那么不使用下划线也可以将函数作为整体传递给变量
  var f2:()=>Int = *foo*
*  println*(f2) // 这里在调用的时候必须要加(),否则返回的是f2的类型。
}

def foo():Int = {
  *println*("foo...")
  1
}

**2）函数可以作为参数进行传递**

def main(args: Array[String]): Unit = {
  // （1）定义一个函数，函数参数还是一个函数签名；f 表示函数名称;(Int,Int)表示输入两个 Int 参数；Int 表示函数返回值
  def f1(f: (Int, Int) => Int): Int = {
    f(2, 4)
  }
  // （2）定义一个函数，参数和返回值类型和 f1 的输入参数和返回值类型一致
  def add(a: Int, b: Int): Int = a + b
  // （3）则 add 函数作为参数传递给 f1 函数，只传函数名。如果能够推断出来不是调用，_可以省略
  *println*(f1(add _))
  *println*(f1(add))
}

而对于传递匿名函数也有很多简化的原则，而这些原则才是在实际工作中或者源码中用的最多的地方。以一下这个标准调用为例说明问题。

f((name: String) => {

      println(name)

    })

**i、参数的类型可以省略，会根据形参进行自动的推导**

f((name) => {

      println(name)

    })

**ii、类型省略之后，如果只有一个参数，则圆括号可以省略；其他情况：****没有参数和参数超过 1 的永远不能省略圆括号****。**

f( name => {

      println(name)

    })

**iii、匿名函数如果只有一行，则大括号也可以省略**

f( name => println(name) )

**iv、如果****参数只出现一次****，则参数可以省略且后面的参数可以用_代替**

f( println(_) )

推导：对于多个参数，但是**参数只出现一次**，那么每个参数可以使用_代替，但是下划线的顺序和参数的顺序是一一对应的。

def main(args: Array[String]): Unit ={

  dualFunctionOneAndTwo((a: Int, b: Int) => a + b)  // 标准调用
  dualFunctionOneAndTwo( _ + _) // 使用_代替调用，第一个下划线就是第一个参数等等

  def dualFunctionOneAndTwo(fun: (Int, Int)=>Int): Int = {
    fun(1, 2)
  }
}

v、如果可以推断出当前传入的表达式是一个函数体，而不是调用语句，可以直接省略下划线

f( println )

**3）局部函数和偏函数**

在 Scala中，可以**在函数内定义函数**，定义在函数内的函数称之为局部函数。

def main(args: Array[String]) {
  //输出各个数的阶乘
  *println*( *factorial*(0) )
  *println*( *factorial*(1) )
  *println*( *factorial*(2) )
  *println*( *factorial*(3) )
}

def factorial(i: Int): Int = {
  def fact(i: Int, accumulator: Int): Int = {
    if (i <= 1)
      accumulator
    else
      fact(i - 1, i * accumulator)
  }
  fact(i, 1)
}

Scala 偏应用函数是一种表达式，不必提供函数需要的所有参数，只需要提供部分，或不提供所需参数。

def main(args: Array[String]){
  val date = new Date
  // 把不固定的使用_:Type的形式写出来，得到的是一个关于其他参数的方法
  val logWithDateBound = *log*(date, _ : String)

  logWithDateBound("message1" )
  Thread.*sleep*(1000)
  logWithDateBound("message2" )
  Thread.*sleep*(1000)
  logWithDateBound("message3" )
}

def log(date: Date, message: String)  = {
  *println*(date + "----" + message)
}

**4）可以作为函数返回值返回**

def main(args: Array[String]): Unit = {
  def f1() = {
    def f2() = {}

    f2 _
  }

  val f = f1()
  // 因为 f1 函数的返回值依然为函数，所以变量 f 可以作为函数继续调用
  f()va
  // 上面的代码可以简化为
  f1()()

  // 如果返回值是函数类型，那么函数定义处的返回值就应该写成返回函数的输入和输出参数的类型
  def func(i: Int): String => (Char => Boolean) = { // 最后一个是整个函数的最终返回类型
    def f1(s: String): Char => Boolean = {
      def f2(c: Char): Boolean = {
        if (i == 0 && s == "" && c == '0') false else true
      }

      f2
    }

    f1
  }
}

**5）柯里化（currying）**

柯里化指的是将原来接受两个参数的函数变成新的接受一个参数的函数的过程。新的函数返回一个以原有第二个参数为参数的函数。可推导至多参数形式。

def main(args: Array[String]): Unit = {
  //定义了一个求和函数
  def add1(a:Int,b:Int) = a+b
  // 那么我们在调用的时候，应该是add(1,2)
  // 现在我们将这个函数变形
  def add2(a:Int)(b:Int)=a+b
  // 那么我们在调用的是后应该是add(1)(2),其结果还是等于3，这种方式（或过程）就叫做柯里化，
  // 经过柯里化之后函数通用性降低，但是适用性有所提高
  //分析下其演变过程
  def add3(a:Int): Int => Int={
    (b:Int)=>a+b
  }
  //(b:Int)=>a+b 为一个匿名函数，也就意味着add方法的返回值为一个匿名函数，
  // 那么现在的调用过程为
  var result=add3(1)
  var sum1=result(2)
}

**6）闭包（closure）**

**闭包是一个函数，返回值依赖于声明在函数外部的一个或多个变量**。闭包通常来讲可以简单的认为是可以访问一个函数里面局部变量的另外一个函数。

其实闭包就是一个函数 + 外部变量捕获。

闭包是一个函数对象，它记住了创建时的词法作用域中的变量，即使在其作用域之外执行，仍能访问这些变量。

def main(args: Array[String]): Unit = {
  def minusXY(x: Int) = (y: Int) => x - y
  //f函数就是闭包.
  val f = minusXY(20)
  *println*("f(1)=" + f(1)) // 19
  *println*("f(2)=" + f(2)) // 18
}

分析：

i、(y: Int) => x – y

返回的是一个匿名函数 ，因为该匿名函数引用了函数外的 x，那么该函数和x整体形成 一个闭包。如：这里 val f = minusxy(20) 的f函数就是闭包

ii、可以这样理解，返回函数是一个对象，而x就是该对象的一个字段，他们共同形成一个闭包

iii、当多次调用f时（可以理解多次调用闭包），发现使用的是同一个x, 所以x不变。

iv、在使用闭包时，主要搞清楚返回函数引用了函数外的哪些变量，因为它们会组合成一个整体(实体)，形成一个闭包

**备注：**闭包的知识点要求必须要掌握，因为当我们学习spark的时候，可以发现spark的源码里有大量的关于闭包的内容，这些内容在我们之后说到spark的时候再进行更深入的讲解。

### 5.5 惰性加载☆☆

在scala中有一个独有的关键字：**lazy，该关键字的作用是可以延迟计算，延迟计算的概念在spark中用的相当的多，可以理解为被lazy声明的类型不会立即发生计算过，而是在调用的时候才发生计算**，比如当函数返回值被声明为 lazy 时，函数的执行将被推迟，直到我们首次对此取值，该函

数才会执行。这种函数我们称之为惰性函数。

def main(args: Array[String]): Unit = {
  lazy val res = *sum*(10, 20)
  *println*("#############")
  *println*("res=" + res)
}

def sum(n1: Int, n2: Int): Int = {
  *println*("sum 被执行。。。")
  n1 + n2
}

输出结果：

#############

sum 被执行。。。

res=30

**注意：**lazy 不能修饰 var 类型的变量

### 5.6 scala中传名函数和传值函数☆☆☆

在java中没有所谓的传值函数还是传名函数，而在scala中分的比较明确，

**传值函数：**表示在函数调用之前参数表达式**会被求值**，例如Int，Long等数值参数类型

**传名函数**在函数调用前表达式**不会被求值**，而是会被包裹成一个匿名函数作为函数参数传递下去，例如参数类型为无参函数的参数就是传名参数

Scala的解释器在解析函数参数(function arguments)时有两种方式：

（i）先计算参数表达式的值(reduce the arguments)，再应用到函数内部，称为传值调用（call-by-value）

（ii）将未计算的参数表达式直接应用到函数内部，称为传名调用（call-by-name）。

  Call-by-Value避免了参数的重复求值，效率相对较高；

       而Call-by-Name避免了在函数调用时刻的参数求值，而将求值推延至实际调用点，但有可能造成重复的表达式求值。

object Add {

  def addByName(a: Int, b: **=>** Int) = a + b

  def addByValue(a: Int, b: Int) = a + b

}

addByName是传名调用，addByValue是传值调用。

**语法上可以看出，使用传名调用时，在参数名称和参数类型中间有一个****=>****符号。**

以a为2，b为2 + 2为例，在Scala解释器进行参数规约（reduction）时的顺序分别是这样的：

  addByValue(2, 2 + 2)

->addByValue(2, 4)

->2 + 4

->6

  addByName(2, 2 + 2)

->2 + (2 + 2)

->2 + 4

->6

可以看出，在进入函数内部前，传值调用方式就已经将参数表达式的值计算完毕，而传名调用是在函数内部进行参数表达式的值计算的。

这就造成了一种现象，每次使用传名调用时，解释器都会计算一次表达式的值。对于有副作用(side-effect)的参数来说，这无疑造成了两种调用方式结果的不同。

#### 5.6.1简单类型的传递示例

##### 5.6.1.1传值参数(by-value parameter)示例

在下面的示例中，编译器检测到strToInt接受一个传值参数，所以先对传入的参数表达式{println("eval va"); "123"}，然后再将求值结果传递给strToInt。

def strToInt(s: String) = {
  *println*("call strToInt")
  s.toInt
}

def main(args: Array[String]) {
  //被{}包围的是一个表达式，而一把表达式的最后一个返回值就是这个表达的值，最后是String类型的即可
  // val res = {println("eval va"); "123"}
  // println(res)
  *strToInt*({*println*("eval va"); "123"})
}

输出:

eval va

call strToInt

##### 5.6.1.2传名参数(by-name parameter)示例

在strToInt函数声明的参数列表中添加一个=>（即正常的函数的调用都是by-value，但是**如果在输入参数的:后面加一个=>，那么就是by-name**），参数传递就按照传名传递了。

def strToInt(s: => String) = {
  *println*("call strToInt")
  s.toInt
}

def main(args: Array[String]) {
  *strToInt*({*println*("eval va"); "123"})
}

输出:

call strToInt

eval va

从上面的输出可以看出，参数表达式在strToInt函数调用之后才被求值。其实此处编译器自动将参数表达式{println("eval va"); "123"}转换成匿名的无参函数，并传递给s。

#### 5.6.2复杂类型的传递示例

##### 5.6.2.1 传值参数(by-value parameter)示例

invode函数的参数f的类型为柯里化函数String => Int => Long（实质就是（String,Int）=>Long，即最后一个为返回值类型）, 此处为按值传递。

def invode(f: String => Int => Long) = {
  *println*("call invoke")
  f("1")(2)
}

def curry(s: String)(i: Int): Long = {
  s.toLong + i.toLong
}

def main(args: Array[String]) {
  *invode*{*println*("eval va"); *curry*}
}

输出:

eval va

call invoke

##### 5.6.2.2 传名参数(by-name parameter)示例

invode函数的参数f的类型为柯里化函数String => Int => Long，但是因为在:后面有=>，所以此处为按名传递。

def invode(f: => String => Int => Long) = {
  *println*("call invoke")
  f("1")(2)
}

def curry(s: String)(i: Int): Long = {
  s.toLong + i.toLong
}

def main(args: Array[String]) {
  *invode*{*println*("eval va"); *curry*}
}

输出:

call invoke

eval va

#### 5.6.3 小结

传值调用在进入函数体之前就对参数表达式进行了计算，这避免了函数内部多次使用参数时重复计算其值，在一定程度上提高了效率。

但是传名调用的一个优势在于，**如果参数在函数体内部没有被使用到，那么它就不用计算参数表达式的值了。在这种情况下，传名调用的效率会高一点。**

那么函数体内部不使用参数，干嘛还要传进去？这里有一个例子：

var *flag*: Boolean = true

def useOrNotUse(x: Int, y: => Int) = {
  *flag *match{
    case true => x
    case false => x + y
  }
}

def main(args: Array[String]) = {
  *println*(*useOrNotUse*(1, 2))
  *flag *= false
  *println*(*useOrNotUse*(1, 2))
}

实操案例：自定义实现while功能(递归实现)

object First {
  def main(args: Array[String]): Unit = {

    // 1. 用闭包实现一个函数，将代码块作为参数传入，递归调用。外层函数表示需要一个执行结果为Boolean型的表达式，因为需要每次都要判断不同的condition，所以只能by-name，内层函数表示需要一个执行结果为Unit的表达式
    def myWhile(condition: =>Boolean): (=>Unit)=>Unit = {
      // 内层函数需要递归调用，参数就是循环体
      def doLoop(op: =>Unit): Unit = {
        if (condition){
          op
          myWhile(condition)(op)
        }
      }
      doLoop _
    }

    // 2. 用匿名函数实现，上面过程的函数简化而来。
    def myWhile2(condition: =>Boolean): (=>Unit)=>Unit = {
      // 内层函数需要递归调用，参数就是循环体
      op => {
        if (condition){
          op
          myWhile2(condition)(op)
        }
      }
    }

    // 3. 用柯里化实现，最简化的实现，也是开发中用的最多的
    def myWhile3(condition: =>Boolean)(op: =>Unit): Unit = {
      if (condition){
        op
        myWhile3(condition)(op)
      }
    }

    var n = 10
    // 柯里化中如果某个参数有多行，可以使用{}代替()，方便书写阅读。
    /*
    // 赋值语句的表达式的值是()
    var res = {
      // op
      println(n)
      n -= 1
    }
    println(res.getClass)
    println(res)
    */

    myWhile3(n >= 1){
      // op
      *println*(n)
      n -= 1
    }
  }

}

### 5.7 练习题及面试题

1、本章节的内容较多，文档中涉及到的代码也！比较多，同学们可以参照文档中的代码多练习练习，一定要做到文档中的代码都能自己完全主动的不差分毫的写出来，得多练习

2、面试题：方法/函数的定义，与java中方法定义的区别

3、面试题：scala中函数简化写法的原则有哪些？

4、面试题：常见的关于函数的概念如匿名函数、闭包、柯里化、懒加载等

5、面试题：拔高题，scala中函数中的传值调用和传名调用

## 6 面向对象

### 6.1 类☆☆

scala和java都是面向对象的编程语言，因此在对类的概念上是一致的，scala延续了java中的类的三大特征，即封装、继承和多态。Scala中的类是用于创建对象的蓝图，其中包含了方法、常量、变量、类型、对象、特质、类，这些统称为成员。

#### 6.1.1 类的定义

一个最简的类的定义就是关键字class+标识符，类名首字母应大写。

class User

val user1 = new User

关键字new被用于创建类的实例。scala中，类并不用声明为public，**如果没有定义构造器，类会有一个默认的空参构造器**。User由于没有定义任何构造器，因而只有一个不带任何参数的默认构造器。通过创建可以发现，对于不带任何参数的构造器，类后的()可以直接省略不写。因为构造器也是函数，而对于无参函数的调用可以直接省略()。然而，通常需要一个构造器和类体。

#### 6.1.2 构造器

在scala中类的构造器分为两种，一种称为主构造器，还有一种称为辅助构造器。**一个类只能有一个主构造器，但是可以很多个辅助构造器。**主构造器是直接声明在类名后的，结构如下：**class A(a:Int, b: String)**

而辅助构造器允许用户通过多种方式去构建对象, 定义辅助构造器与定义方法一样，也使用def关键字来定义，而**这个方法的名字必须为为this，**辅助构造的结构如下：**def this(参数名:类型, 参数名:类型)。而单独写一个this就是表示当前类的主构造器。**

object First {
  def main(args: Array[String]): Unit = {
    new Teacher("tom").showInfo()
    new Teacher("jack",18).showInfo()
    new Teacher("mary",20,"woman").showInfo()
  }
}

class Teacher{
  var *name *: String = _
  var *age *: Int = _
  var *sex *: String = _
  def this(inName : String){
    // 在scala中所有辅助构造器的内部最终要顶要落实到主构造器中，否则会报错。
    this
    this.*name *= inName
  }

  def this(inName : String,inAge : Int){
    this(inName) //调用的时前面的辅助构造器this(inName : String)
//    this
//    this.name = inName
    this.*age *= inAge
  }

  def this(inName : String,inAge : Int,inSex : String){
    this(inName,inAge)
    this.*sex *= inSex
  }

  def showInfo(): Unit ={
    *println*("name：" + *name *+ " age:" + *age *+ " sex: " + *sex*)
  }

}

而关于构造器，以下几点需要特别的注意：

1、主构造器直接跟在类名后面， **主构造器中的参数，最后会被编译成字段**

2、主构造器执行的时候， 会执行类中的所有语句

3、附属构造器名称为this，可以有多个，**编译器通过参数的个数及类型来区分**。每一个辅助属构造器必须**首行**调用已经存在的主构造器或者其他已经声明的附属构造器

4、辅助构造方法不能直接构建对象，**必须直接或者间接调用主构造方法。**

5、构造器调用其他另外的构造器，要求被调用构造器必须提前声明。

class Person2(var name: String, val age: Int) {

  println("this is the primary constructor!")

  var gender: String = _

  val school: String = "ZJU"

  def this(name: String, age: Int, gender: String){

    this(name, age) // 参数的类型和主构造器一致，所以这里调用的是主构造器

    this.gender = gender

  }

}

#### 6.1.3 getter和setter方法

**在class里面定义的var，会同时****默认生成****getter函数和setter函数**，比如 var y = 2，会有 def **y**:Int 和 def **y_=** (y:Int):Unit 两个函数其中，前者相当于getter方法（无参方法，()默认不写），后者相当于setter方法。所以**属性名_=**作为一个整体作为方法名动态生成。所以a.money_=(200)，其中a是类对象，money_=是方法名，200是参数，这个是在编译器中处理的，简写为：a.money=200，money为字段，相当于字段赋值。

同时，我们也可以使用scala自带的Bean 属性（@BeanPropetry），可以自动生成规范的 setXxx/getXxx 方法

object First {
  class Person {
    var *name*: String = "bobo" //定义属性
    var *age*: Int = _ // _表示给一个默认值
    @BeanProperty var *sex*: String = "男"
  }

  def main(args: Array[String]): Unit = {
    val person = new Person()
    *println*(person.*name*)
    person.setSex("女")
    *println*(person.getSex)
  }
}

**Scala 中的 public 属性，底层实际为 private**，并通过 get 方法（obj.field()）和 set 方法（obj.field_=(value)）对其进行操作。所以 **Scala 并不推荐将属性设为 private，并为其显示的设置public 的 get 和 set 方法的做法。**但由于很多 Java 框架都利用反射调用 getXXX 和 setXXX 方法，有时候为了和这些框架兼容，也会为 Scala 的属性设置 getXXX 和 setXXX 方法（通过@BeanProperty 注解实现）。

**getter方法和setter方法的意义在于控制类中私有对象的数据**。在类中可以通过重新定义getter和setter方法用来获取或者有限制的修改私有字段

object First {
  val *hello *= new Hello
//  println(hello.privateValue1)
  *println*(*hello*.value1)   // Hello
  *hello*.add  //HelloWorld
  *hello*.value1_("HelloHello")
  *hello*.add //HelloHelloWorld
}

class Hello{
  private var *privateValue1 *= "Hello"
  var *value2 *= "World"

  def add(){
    *println*(value1 + *value2*)
  }

  def plus(m: Char) = *value2 *+ m

  def value1 = *privateValue1  *//重新定义getter方法

  def value1_ = (newValue1: String) =>{  // 从新定义getter方法
    if(newValue1.length > *privateValue1*.length)
      *privateValue1 *= newValue1
  }
}

而在Scala 类的主构造器函数的形参包括三种类型：没有任何修饰、var 修饰、val 修饰

（1）**未用任何修饰符修饰，这个参数就是一个局部变量**，等价于被private[this] var修饰（无set和get）

（2）var 修饰参数，作为类的成员属性使用，可以修改（有get、set）

（3）val 修饰参数，作为类只读属性使用，不能修改（有get，无set）

#### 6.1.4 关于scala中的访问修饰符

Scala访问修饰符基本和Java的一样，分别有：private，protected，如果没有指定访问修饰符，默认情况下，Scala 对象的访问级别都是 public。

1、私有(private)成员：用 private 关键字修饰，带有此标记的成员**仅在包含了成员定义的类或对象内部可见，同样的规则还适用内部类。**

2、保护(Protected)成员：它只允许保护成员在定义了该成员的类，内部类，其**子类中被访问**，同一个包里的其他类不可以进行访问。

3、公共(Public)成员：Scala 中，没有public这个关键字，但是如果没有指定任何的修饰符，则默认为 public,这样的成员在任何地方都可以被访问。

**访问修饰符可以通过使用限定词强调。格式为: ****private[x]**

其中：

1、这里的x指代某个所属的包、类或单例对象，如果是表示当前类的访问权限，即private[this]，可以简化为private，因此scala中的private修饰符实质上是private[this]的意思。

2、如果写成private[x]，读作"这个成员除了对[x]中的类或[x]中的包中的类及它们的伴生对象可见外，对其它所有类都是private。

3、私有构造器，关于私有构造器有一下两种写法：

**class A private(){....}**：私有的主构造器，只能通过辅助调用

**class A private[b]{....}**：私有的主构造器，只能通过辅助调用或者包b下可以调用A的主构造器

4、私有类

private[this] class放在类声明最前面，是修饰类的访问权限，也就是说类在某些包下可见或不能访问，比如：private [sheep] class代表该类在sheep包及其子包下可见，同级包不能访问

### 6.2 单例对象☆☆

在 Scala 中，是没有 static 这个东西的，但是它也为我们提供了**单例模式**的实现方法，那就是使用**关键字 object（区别java中顶级类Object）**，object 对象的声明不能带参数。object对象的声明方式除了不能带参数，其他完全和类声明一致，包括变量、函数的声明等。**object中声明的默认都是static**

object ScalaSingleton{
  def saySomeThing(msg:String): Unit ={
    *println*(msg)
  }
}

object First {
  def main(args: Array[String]): Unit = {
    ScalaSingleton.*saySomeThing*("hello")
    *println*(ScalaSingleton)
    *println*(ScalaSingleton)
    // output:
    // hello
    //ScalaSingleton$@ea4a92b
    //ScalaSingleton$@ea4a92b
  }
}

**关于object对象我们只需要知道一点即可，即由它为模板创建的对象是一个单列**，不用再像java那种各种饿汉模式、懒汉模式，还要考虑到线程安全的问题，而在scala中创建一个单列对象十分的方便。

**备注：**这里的对象注意和class的实例对象做区别。一个是单例对象object，scala中独有的；一个是实例对象，面向对象编程中的通俗的概念，注意区别理解。

### 6.3伴生类和伴生对象☆☆

当声明的类和对象（object）的名字一样时，这种现象我们称为伴生，其中类称为**伴生类**，对象称为**伴生对象**。**伴生对象中的private属性和方法都可以通过伴生对象名（类名）直接调用访问**

object Student {//伴生对象
  private val *occupation*:String="student"
  def main(args: Array[String]): Unit = {
    *println*('s')
  }
}

class Student(Id:Int,Name: String) {//伴生类

  def printInfo():Unit={
    *println*("学号:"+this.Id +" 姓名:" + this.Name +" 职业:" + Student.*occupation*)
  }
}

### 6.4 伴生的底层分析☆☆☆

首先我们来声明一个对象，

object HelloWorld {

  def main(args: Array[String]): Unit = {

    println("hello world")

  }

}

Class文件反编译的方法：https://blog.csdn.net/zhangeer/article/details/127604580

**该object对象编译之后会生成两个类：HelloWorld（入口类）和HelloWorld$（辅助类）**

public final class HelloWorld{

  public static void main(String[] paramArrayOfString){

    HelloWorld$.MODULE$.main(paramArrayOfString);

  }

}

public final class HelloWorld${

  // 会生成一个默认的静态对象

  public static MODULE$;

  // 构造方法私有化，且是静态代码块调用私有构造，因此是单例，即object有单例效果

  static{

    new ();

  }

  public void main(String[] args){

    Predef$.MODULE$.println("hello world");

  }

  private HelloWorld$() {

    MODULE$ = this;

  }

}

通过实验，我们可以看出来：

我们继续探索，首先我们来看看再java中是如何使用static：

public class Student {

    private String name;

    private Integer age;

    private static String school = "ds";

    public Student(String name, Integer age) {

        this.name = name;

        this.age = age;

    }

    public void printInfo(){

        System.out.println(this.name + " " + this.age + " " + Student.school);

    }

    public static void main(String[] args) {

        Student alice = new Student("alice", 19);

        Student bob = new Student("bob", 20);

        alice.printInfo();

        bob.printInfo();

    }

}

而在scala中：

class Student(name: String, var age: Int) {

  def printInfo(): Unit = {

    println(name + " " + age + " " + Student.school)

  }

}

object Student{

  // object中的隐式声明为static

  val school: String = "ds"

  def main(args: Array[String]): Unit = {

    val alice = new Student("alice", 19)

    val bob = new Student("bob", 20)

    alice.printInfo()

    bob.printInfo()

  }

}

scala代码编译后（一对伴生共用两个编译后的文件）：

public class Student{

  **// scala中val在编译之后会生成final**

  private final String name;

  **// scala中声明的var，说明是个变量，变量会生成对应的setter/getter方法**

  private int age;

  public static void main(String[] paramArrayOfString){

    Student$.MODULE$.main(paramArrayOfString);

  }

  // scala会生成一个调用object属性的方法

  public static String school(){

    return Student$.MODULE$.school();

  }

  //scala 为每一个私有变量提供了getter、setter方法，不用显性的定义

  // scala会将属性生成一个对应的getter方法，所以在代码中直接写属性名字，就是调用相应的getter方法

  public int age(){

    return this.age;

  }

  // scala会将属性生成一个对应的setter方法，直接代码中写属性名_=属性值就是调用对应的setter方法，如age_=10，编译之后就是调用age(10)

  public void age_$eq(int x$1) {

     this.age = x$1;

  }

  // Unit返回值编译之后就是void

  public void printInfo() {

    Predef$.MODULE$.println(2 + this.name + " " + age() + " " + Student$.MODULE$.school());

  }

  // 生成一个默认的全参数构造方法

  public Student(String name, int age){

  }

}

//object中的属性都都在这里

public final class Student${

  public static  MODULE$;

  private final String school;

  static{

    new ();

  }

  // 静态变量的getter方法

  public String school(){

    return this.school;

  }

  public void main(String[] args) {

    Student alice = new Student("alice", 19);

    Student bob = new Student("bob", 20);

    alice.printInfo();

    bob.printInfo();

  }

  // 静态变量在私有构造方法中赋值

  private Student$() {

    MODULE$ = this;

    this.school = "ds";

  }

}

**Scala 中没有静态方法，不过它有个类似的特性，叫做单例对象，通常一个类对应一个伴生对象, 伴生对象中定义的方法和 Java 中的静态方法一样。**

总结：

1、scala中没有public关键字，如果不声明访问权限，默认就是public

2、scala中没有静态语法，所以没有static关键字。**由object实现类似静态方法的功能（类名.方法名）。**

3、void表示空返回值，但是不遵循面向对象语法，所以**scala中没有void关键字，但有Unit关键字，表示没有返回值，编译之后就是void**，Unit作为返回值打印出来是()

4、scala中函数必须使用def关键字声明

5、class关键字和Java中的class关键字作用相同，用来定义一个类

object类型在编译之后构造方法是private，无法在外部生成实例对象，而其中的方法/变量编译之后变为static的静态方法/变量，可以通过类名直接调用。在对object进行编译的时候会同时生成一个XXXX$.class的文件，该类是一个单例类，内部会构造一个public static XXXX$ MODULE$;  单例对象，所以**object类型在编译的时候生成两个class文件**

### 6.5 scala中第一个重要的方法（注入方法）☆☆

我们先来引入一个案例，通过案例的现象我看看能得出什么结论：

先创建一对伴生：

class Foo(foo: String) {
  def apply(foo: String) : Unit = {
    *println*(foo)
  }
}

object Foo {

  var *aa*: Int = 10

  def apply(foo: String) : Foo = {
    *println*(foo)
    new Foo(foo)
  }
}

定义了一个Foo类，并且在这个类中，有一个伴生对象Foo，里面定义了apply方法。有了这个apply方法以后，在调用这个Foo类的时候，用函数的方式来调用：

object First {
  def main(args: Array[String]): Unit = {
    *println*(Foo.*aa*)

    val foo = *Foo*("Hello")  //object加()表示调用object里对应参数的apply方法
    foo("world")    // 实例对象加()表示调用class里对应参数的apply方法
  }
}

输出：

10

Hello

world

通过输出我们可以看出以下三点：
1、obj中的变量或者方法可以被其他的类或者obj调用

2、触发了obj中的apply方法的执行

3、触发了class中的apply方法的执行

用Foo("Hello")的方式，就得到了一个Foo类型的对象，这一切就是apply方法的功劳。如果没有apply方法，将需要使用new关键字来得到Foo对象。

因此，一般在伴生对象中声明apply方法，然后在其中实现内容，那么**伴生对象()****和伴生对象.apply是等价的（()中参数的个数和apply中声明的****参数个数要保持一致****方可）**，实例对象加括号相当于调用类中声明的apply方法。如：theArray(0)，取数组的第一个元素的操作会转换成 theArray.apply(0) 操作，这也能解释为什么 Scala 数组取值不用中括号括下标的方式，因为它也是一次方法调用

通过分析我们可以得到两个结论：

### 6.6 抽象类☆☆

和java中一样，在 Scala 中, 使用 **abstract** 修饰的类称为抽象类，在抽象类中可以定义属性、未实现的方法和具体实现的方法。Scala中的抽象类和java中的抽象类一样，都是**不能实例化**。

Scala中抽象类的需要主要的地方是：

abstract class Animal(val age: Int) {
  // 抽象字段
  var aa:Int
  val bb :Int

  // 抽象方法
  def eat()

  // 普通的方法
  def sleep(sound: String) = {
    *println*(s"sleep with **$**sound")
  }
}

object First{

  def main(args: Array[String]): Unit = {

    // 实现类 一把关于scala中的抽象类的实现都是使用匿名内部类
    val a1 = new Animal(2) {

      override var *aa*: Int = 4
      override val *bb*: Int = 5

      override def eat(): Unit = *println*("eat")
    }

    a1.eat()

    a1.sleep("huhuhu...")
    *println*(a1.*aa*)
  }
}

### 6.7 继承☆☆

作为面向对象编程语言，继承是必不可少的特性，scala中的继承和java中一样，也是使用**extends关键字**实现继承，也是**单继承**。但需要注意以下几点：

**1、重写一个非抽象方法必须使用override修饰符。 **

2、只有主构造函数才可以往父类的构造函数里直接写参数。

//父类直接写变量名，不需要再声明类型

class Student(name: String, age: Int) extends Person2(name){

3、在子类中重写超类的抽象方法时，可以不使用override关键字。

重写规则：

**重写 def：**

子类用val重写 ：利用val能重写超类中没有参数的方法(getter)

子类用var重写：同时重写getter、setter方法，只重写getter方法报错

子类用def重写：子类的方法与超类方法重名

**重写val：**

子类用val重写 ：子类的一个私有字段与超类的字段重名，getter方法重写超类的getter方法

**重写var：**

子类用var重写：且当超类的var是抽象的才能被重写，否则超类的var都会被继承

abstract class A {

    val a = 25// 可在子类中用val重写

    var b = 15// 不可在子类中用var重写，因为不是抽象的

    var c: Int   // 可在子类中用var重写

    def fun1     // 可在子类中用val重写

    def fun      // fun的getter方法，可在子类中用var重写

    def fun_     // fun的setter方法，用var重写setter后，还要用var重写此方法

    def fun3(m:Char)  // 可在子类中用def重写

  }

**综上可得，子类中，def只能重写超类的def，val能重写超类的val或不带参数的def，var只能重写超类中抽象的var或者超类的getter/setter**

**注：**1、当一个类不希望被继承时，可在类声明前加上**final保留字**：final class A {...}

2、当一个类的某些成员不希望被重写时，可以在成员声明前加上final保留字  class A { final def sign{...} }

3、当超类中的某些成员需要被子类继承，又不想对子类以外成员可见时，在成员声明前加上**protected保留字**  class A { protected def sign{...} }

另外需要注意的是，**object也可以继承类，和类的继承语法相同，但是object和类都不能继承其他的object**

### 6.8 特质☆☆

Scala中没有Java中的接口，而产生一个新的概念：**Trait**(特质)，**特质相当于 Java 的接口**，但是它比java中的接口的功能要强大很多。 与接口不同的是，**它还可以定义属性和方法的实现**。特质是Scala里代码复用的基础单元，封装了方法和字段的定义

一般情况下Scala的类只能够继承单一的父类，但是如果是 Trait的话就可以继承多个，从结果来看就是实现了多重继承。

**备注：**所有 Java 接口都可以当做 Scala 特质来使用

特质的定义的方式与类相似，除了不能拥有构造参数，但它使用的关键字是 trait。

trait Equal {

  def isEqual(x: Any): Boolean

  def isNotEqual(x: Any): Boolean = !isEqual(x)

}

一旦特质被定义了，就可以由类来“实现（implements）“，但是在scala中不称为实现，称为”**混入（mixin）**“，并且依旧使用关键字extends，即scala中是没有implements这个关键字，混入格式可类继承格式一致： class B extends A {...}

当要混入多个特质时，利用**with关键字**：class D extends A with B with C {...}

通过查看字节码，我们可以得到一个大概的概念，即可以**将特质理解为抽象类+接口**

**特质的成员可以是抽象的，而且不需要使用abstract声明**，并且重写特质的抽象方法无需override，但是**多个特质重写同一个特质的抽象方法需override**

**备注：**当特质继承抽象类时，重写的方法要用abstract override修饰。

除了在类定义中混入特质以外，还可以在特质定义中混入特质，以及**构造对象时混入特质**

// 定义特质时混入

trait B extends A {...}

// 构造对象时混入

Val obj = new C with B

注：如果在构造对象时混入特质时，如果需要覆写特质的写法，可以使用匿名内部类写法：

// Feline 猫科动物
abstract class Feline {
  def say()
}

trait Tiger extends Feline {
  // 在特质中重写抽象方法, 需要在方法前添加 abstract override 2个关键字
  abstract override def say() = *println*("嗷嗷嗷")
  def king() = *println*("I'm king of here")
}

class Cat extends Feline {
  override def say() = *println*("喵喵喵")
}

object First extends App {
  val *cat *= new Cat with Tiger
  *cat*.say // Cat 和 Tiger 都有 say 方法，但是调用时是从右往左调用，所以是 Tiger 在叫
  *cat*.king // 可以看到即使cat 中没有 king 方法, Tiger 特质也能将自己的方法混入 Cat 中
}

**备注：**在构造单个对象时，也可以为混入特质，特质可以将对象原本没有的方法与字段加入对象中

特质继承另一特质是一种常见的用法，而特质继承类却不常见。**特质继承类，这个类会自动成为所有混入该特质的类的超类**

trait Logger extends Exception { }

class Mylogger extends Logger { } // Exception 自动成为 Mylogger 的超类

如果类已经继承了另一个类怎么办？只要这个类是特质超类的子类就好了;

//IOException 是 Exception 的子类

class Mylogger extends IOException with Logger { }

不过**如果类继承了一个和特质超类不相关的类, 那么这个类就没法混入这个特质了**

特质中的字段可以是具体的也可以是抽象的。如果给出了初始值那么字段就是具体的

trait  Ability {

  val swim: String

  val run = "running" // 具体字段

  def ability(msg: String) = println(msg + swim)  // 方法用了swim字段

}

class Cat extends Ability {

    val name = "cat"

    val swim = "swimming" // 不需要 override

}

混入Ability特质的Cat类自动获得一个run字段。通常对于特质中每一个具体字段，使用该特质的类都会获得一个字段与之对应，这些字段不是被继承的, 而是自动生成一个字段与之对应。

### 6.9 关于特质相关的super的问题详解☆☆

在 Java 或者 Scala 的一般类/抽象类中，super.foo() 这样的方法调用是**静态绑定**的，也就是说当在代码中写下 super.foo() 的时候就能明确是调用它的父类的 foo() 方法。然而，**如果是在****特质****中写下了 super.foo() 时，它的调用是动态绑定的，调用的实现将在每一次特质被混入到具体类的时候才被决定**。因此需要对特质中相应的方法加上abstract 声明（虽然加上了abstract 声明，但方法仍可以被具体定义，但该方法仍然是抽象方法，这种用法只有在特质中有效）以告诉编译器特质中的该方法只有在特质被混入某个具体定义的类中才有效。

需要非常注意特质被混入的次序：**特质在构造时顺序是从左到右，但由于多态性，子类的方法最先起作用，因此越靠近右侧的特质越先起作用**，如果最右侧特质调用了super，它调用左侧的特质的方法，依此类推。确切的讲，特质的 super 调用与混入的次序很重要，越靠近后面的特质越优先起作用

**备注：**对于特质而言，super不是代指父类特质，而是指的**上一级特质，即加载顺序，**从右到左，不一定调用父类的，而是调用左边的混入特质，左边没有了，才调用父类的

object First {
  def main(args: Array[String]): Unit = {
    val queue1 = new BasicIntQueue with Incrementing with Doubling
    queue1.put(2)  //Doubling.put(2*2)->Incrementing.put(4+1)
    *println*(queue1.get()) //result is 5

    */***
*    当调用带混入的类的方法是，最右侧特质的该方法首先被调用。如果有些混入的特质没有该方法，则从有该方法的特质开始。*
*    如果那个方法调用了 super，它调用其左侧特质的方法。可以这么认为，Doubling 的 super 指向了  Incrementing，*
*    Incrementing 的 super 指向了 BasicIntQueue。*
*     */*
*    *val queue2 = new BasicIntQueue with Doubling with Incrementing
    queue2.put(2)  //Incrementing.put(2+1)->Doubling.put(2*3)
    *println*(queue2.get()) //result is 6
  }
}

abstract class IntQueue {
  def get(): Int
  def put(x: Int)
}

class BasicIntQueue extends IntQueue {
  private val *buf *= new ArrayBuffer[Int]
  def get() : Int = *buf*.remove(0)
  def put(x: Int) { *buf *+= x }
}

trait Incrementing extends IntQueue {
  abstract override def put(x: Int) {
    super.put(x + 1)
  }
}

trait Doubling extends IntQueue {
  abstract override def put(x: Int) {
    super.put(2 * x)
  }
}

上面每一个put方法都将修改过的消息传递给 super.put，对于特质来说，super.put 调用的是特质层级的下一个特质，**具体是哪一个根据特质添加的顺序来决定。**

**在特质中，由于继承的是抽象类，super调用是非法的**。这里必须使用abstract override 这两个关键字，在这里表示特质要求它们混入的对象(或者实现它们的类)具备 put 的具体实现，**这种定义仅在特质定义中使用。**

混入的顺序很重要，越靠近右侧的特质越先起作用。**当调用带混入的类的方法时，最右侧特质的方法首先被调用**。如果那个方法调用了super，它调用其左侧特质的方法，以此类推。

**备注：**如果要控制具体哪个特质的方法被调用, 则可以在方括号中给出名称**super[]**，这样如果想要调用某个指定的混入特质中的方法，可以增加约束。super[Category].describe()。

trait A {

def hello(): String = "Hello, I am trait A!"

}

trait B {

def hello(): String = "Hello, I am trait B!"

}

class C extends A with B {

override def hello(): String = super[A].hello()

}

这里的super[A]就指定了调用哪一个父类的方法，很神奇的东西

### 6.10 scala中的包管理☆

Scala中引入一个包也是使用import关键字，但是Scala中关于包的管理和java中的区别比较大，先来看看常见的scala包管理的知识。

**1、默认引入的几个包（隐式引用）**

**import java.lang._// java.lang包下的内所有东西**

**import scala._// scala包下的所有东西**

**import Predef._// Predef object下的所有东西**

**备注：**通常，假设import进来两个包都有某个类型的定义的话，比方说，同一段程序既引用了’scala.collection.mutable.Set’，又引用了’import scala.collection.immutable.Set’，则编译器会提示无法确定用哪一个Set。这里的隐式引用则不同，**假设有同样的类型，后面的包的类型会将前一个隐藏掉**。比方：java.lang和scala两个包里都有StringBuilder，这样的情况下会使用scala包里定义的那个，java.lang里的定义就被隐藏掉了，除非显示的使用java.lang.StringBuilder。

**2、为避免命名冲突，可修改别名来命名**

import java.util.{HashMap **=>** JavaHashMap}

**3、如果不想用包内某个类，可将其指向下划线(_)屏蔽该类**

import scala.{StringBuilder => **_**}

**4、引入指定的包下的多个类，可以使用{}包裹，用逗号分隔**

import java.awt.{Color, Font}

**备注：**1、scala可以在代码中直接使用import动态引用包中的指定类，这样只有在用的时候才会加载

2、包的引用是有作用域的，**只包括包下面的第一层（不存在递归包）**，如scala._指定的是包含scala包下的所以的相关的类，但不包括scala包下的包，如scala.collection._就不包括

package spark{

abstract class A{//spark.A

def aa

}

package scala{//spark.scala.Test

class Test

}

}

指定spark包，会包含A，但不会包含Test，因为Test属于spark.scala包

3、包可以相互嵌套，如：

package scala.collection.mutable

等价于：

package scala

package collection

package mutable

4、Scala 有两种包的管理风格，一种方式和 Java 的包管理风格相同，每个源文件一个包（包名和源文件所在路径不要求必须一致），包名用“.”进行分隔以表示包的层级关系，如com.ds.scala。另一种风格，通过嵌套的风格表示层级关系，如下：

package com{

package ds{

package scala{

…..

}

}

}

第二种风格有以下特点：

（1）一个源文件中可以声明多个 package

（2）子包中的类可以直接访问父包中的内容，而无需导包

package com {

import com.ds.Inner // 父包访问子包需要导包

object Outer {

val out: String = "out"

def main(args: Array[String]): Unit = {

println(Inner.in)

}

}

package ds {

object Inner {

val in: String = "in"

def main(args: Array[String]): Unit = {

println(Outer.out) //子包访问父包无需导包

}

}

}

}

package other {}

**5、包对象（package object）**

**在 Scala 中可以为每个包定义一个同名的包对象（文件名显示为：****package****）**，包中的所有类都可以直接访问包对象中的所有的成员和方法，类似C中定义的宏

package object people{ val a = "scala"}

package people{

class Student{

var name = a

}

}

（1）若使用 Java 的包管理风格，则包对象一般定义在其对应包下的 **package.scala**文件中，包对象名与包名保持一致。

（2）如采用嵌套方式管理包，则包对象可与包定义在同一文件中，但是要保证包对象与包声明在同一作用域中。

package com {

object Outer {

val out: String = "out"

def main(args: Array[String]): Unit = {

println(name)

}

}

}

package object com {

val name: String = "com"

}

**备注：**1、包对象的名字要和所在包层级的名字保持一致

2、定义包对象跟定义一个普通的伴随对象(companion object)在写法上的唯一区别就是在关键字object 前加上 package。可以像使用伴随对象那样使用包对象，**可以把包对象看作是包的伴生（伴随包）**

### 6.11 类型检测和转换☆☆

在scala中关于类型的检测的api一共有以下三个：

（1）obj.isInstanceOf[T]：判断 obj 是不是 T 类型。

（2）obj.asInstanceOf[T]：将 obj 强转成 T 类型。

（3）classOf[T]：获取类的信息

需要注意的是：**scala中的classOf[T]等价于java中的T.class**

object Third {
  def main(args: Array[String]): Unit = {
    val person = new Person
    //（1）判断对象是否为某个类型的实例
    val bool: Boolean = person.isInstanceOf[Person]

    if ( bool ) {
      //（2）将对象转换为某个类型的实例
      val p1: Person = person.asInstanceOf[Person]
      *println*(p1)
    }
    //（3）获取类的信息
    val pClass: Class[Person] = *classOf*[Person]
    *println*(pClass)
  }
}

class Person

### 6.12 Type关键字声明自定义类型☆

使用 **type 关键字**可以定义新的数据类型名称，**本质上就是****类型的一个别名**

object Test {

def main(args: Array[String]): Unit = {

type S = String

var v: S = "abc"

def test(): S = "xyz"

}

}

### 6.13 方法与函数的区别☆☆☆

这个问题也是我们之前的留的坑之一，我们之前说方法和函数可以混为一谈，但是其实际上还是有区别的，今天我们就把这个问题好好的说一说，看看他们的区别究竟在哪里。

**（i）方法名不能作为单独的表达式而存在（参数为空的方法除外，scala中参数为空的方法调用，方法名后的（）可以不写），而函数可以**。即方法名不能作为最终的表达式出现，只有方法调用的时候才能作为最终的表达式，而函数可以。函数名单独存在输出的是函数的类型说明。

（ii）函数必须要有参数列表，而方法可以没有参数列表，即方法如果是空参数，可以（）可以省略不写，而函数不可以。

（iii）针对空白参数：方法名可以表示方法的调用，而函数名只是代表函数对象本身，而要调用必须要加参数列表，即使是空白参数。

**备注**：（ii）（iii）主要是针对空白参数的声明和调用的情况，即方法可以省略空白列表，而方法不可以。均属特例。

（iv）方法可以进行eta展开，即自动转换为函数。**如果期望出现函数的地方提供了一个方法，该方法就会自动被转换成函数。该行为被称为****ETA expansion**

**如果直接把一个方法赋值给变量会报错**。但如果指定变量的类型就是函数，那么就可以通过编译，如下：

方法不是值，函数是值，所以方法不能绑定给一个val变量，函数可以，但是**可以使用“_”强制把一个方法转换给函数**，这就用到了scala中的部分应用函数：

利用这种自动转换，可以写出很简洁的代码，如下面这样

val myList = List(3,56,1,4,72)

myList.filter(12.<)  //或者写成myList.filter(12<)

上述的12.<被解释成obj.method，即整形的<的方法，所以该表达式是一个方法，在此处会被解释成函数，等价于12.<(_)或者12 < _。即这里的表达式所代表的方法调用自动转换成函数。

### 6.14 练习题和面试题

1、这章涉及的概念比较多，所以这章重点把握相关的知识点，以及这些知识点和java的区别

2、面试题：类的构造器（主辅）、getter和setter方法

3、面试题：单例对象、伴生现象

4、面试题：抽象类、特质、super

5、面试题：scala中的包管理

6、面试题：拔高题，方法和函数的区别

## 7 泛型

### 7.1 概念☆☆

Scala中的泛型的概念和java中对的基本一致，只是声明方式有所区别，java中的泛型使用<T, K>的形式，而Scala中的泛型的形式则是[T, K]的形式。因为scala是便捷式的开发语言，对很多东西都是高度抽象的，因为在scala或者spark的源码中随处可见的是大量的使用泛型，因为要想学好scala并且熟练的上手，泛型是必须要掌握的。

其实我们可以简单的理解泛型T就是某个容器中的元素是T类型的，比如我们声明一个泛型类：class Person[T](var name: T)，这里的Person就相当于一个容器，里面装了一个name，然后这个name的类型就是T，比如说这个是人是中国人，那么T类型可以理解是China，同理，如果是美国人，则可以理解为T类型是America。这样的话，我们在定义Person之初并不知道他是哪国人，因为我们就把这个类型给抽象出来，当我们在使用的时候，再具体指定，比如：val zhagnsan = new Person[China](“zhangzan”)

### 7.2 泛型类和泛型方法的声明☆☆

#### 7.2.1 泛型类

class Animals**[A, B]**(var name: A, var age: B) {

    println(s"Name is $name, Age is $age")

}



object GenericClient extends App {

    val cat = new Animals[String, Int]("小花", 2)

    val dog = new Animals[String, String]("阿黄", "5")

}

#### 7.2.2 泛型方法

def asList**[T]**(pSrc: Array[T]): List[T] = {

    if (pSrc == null || pSrc.isEmpty) {

        List[T]()

    } else {

        pSrc.toList

    }

}

val friends = Array("小白", "琪琪", "乐乐")

val friendList = cat.asList(friends)

println(friendList.isInstanceOf[List[String]])

备注：scala中不能给object添加参数化类型

### 7.3 变形及协变逆变☆

#### 7.3.1 变形

变型（variance）是指如何根据组成类型之间的子类型关系，来确定更复杂的类型之间的子类型关系，当用类型构造出更复杂的类型，原本类型的子类型性质可能被**保持、反转、或忽略**───取决于类型构造器的变型性质。比如说类型A是类型B的子类型，那么组合出来一个新的类型C[A]类型和C[B]类型之间是什么关系呢？C[A]还保持是C[B]的子类？或者C[A]反转成了C[B]的父类？亦或是二者没有关系了呢？

#### 7.3.2 协变

如果类型A是类型B的子类型，那么组合出来一个新的类型C[A]类型依旧保持是C[B]的子类，我们就说类型A是支持协变的(covariant)，在scala中用**[+A]**表示。在scala中常见的协变类型比如：List[+A]

#### 7.3.2 逆变

如果类型A是类型B的子类型，那么组合出来一个新的类型C[A]类型反转成了C[B]的父类，我们就说类型A是支持逆变的(covariant)，在scala中用**[-A]**表示。

**备注：**默认类型是不变的，写成[A]，即不用写加减号

一般来说，当在类方法里碰到协变和逆变的故障时，通常的解决方法是引入一个新的类型参数，即在方法签名里用新引入的类型参数.

object Third {
  def main(args: Array[String]): Unit = {
    var s1 = new S[Any, String]{
      override def apply(arg: Any): String = "Hello \t" +arg
    }
    var s2: S[Any, String] = s1
    var s3: S[String, Any] = s1
    var value: Any = s3.apply("Spark")
  }
}

trait S[-F, +S]{
  // 函数的参数类型是逆变的，函数的返回值类型是协变的
  def apply(arg: F): S
}

### 7.4 泛型的界☆

在Scala当中，类型变量的限定(约束)分为两种类型：类型变量的上界与类型变量的下界。通过类型变量的限定，可以方便的表达出类型变量具有某些需要的特征和方法，声明方法如下：

上界用"**<:**"来表示，例如：A <: B，表示B为A的上界，即**A继承B**。

下界用"**>:**"来表示，例如：A >: B，表示B为A的下界，此时B继承A。

在Scala当中，所有类型的最大上界是Any，最大下界是Nothing

多重界定

T <: A with BT是A**或者**B的子类

T >: A with BT是A或者B的父类

T >: A <: BT的父类是B，子类是A（位置不能倒，A一定是B的子类） String >: Nothing <: Any

A =:= B表示A类型等同于B类型

A <:< B表示A类型是B类型的子类型

### 7.5 上下文界定(Context Bound)☆☆☆

进阶的学员可以参照第八章第五小结，隐式对象，而对于小白可以直接跳过。

## 8 隐式转换

### 8.1 隐式转换的概念☆☆☆

**所谓隐式转换就是将A转换成B，但并不是A真的就成了B，而是A本来的属性仍存在的同时又拥有了B的属性**，这使得了A本身不发生变化的同时，扩大了功能，此属于蒙面设计模式。又因为A直接使用了B的功能而不需要对A进行修改，因此转换是隐式的，使用**关键字implicit**修饰。所以简单的说隐式转换就是增强类型，扩展功能

当编译器第一次编译失败的时候，会在当前的环境中查找能让代码编译通过的方法，用于将类型进行转换，实现**二次编译**。即当想调用对象功能时，如果编译错误，那么编译器会尝试在当前作用域范围内查找能调用对应功能的转换规则，**这个调用过程是由编译器(scalac)完成的，所以称之为隐式转换，或称之为自动转换**

### 8.2 隐式转换的作用域☆☆☆

**scala编译器仅考虑作用域之内的隐式转换**，要使用某种隐式操作，必须以单一标识符的形式（一种情况例外）将其带入作用域之内。

object TestImplicit {
  implicit def doubleToInt(x: Double) = x.toInt
}

object Third {
  def main(args: Array[String]): Unit = {
    import TestImplicit._      //以单一标识符引进doubleToInt的隐式转换
    val i: Int = 2.3
  }
}

**单一标识符有一个例外，编译器还将在源类型和目标类型的伴生对象中寻找隐式定义。**

### 8.3隐式转换函数☆☆☆

1、格式

**implicit** def 函数名(参数)：返回值类型={

     //函数体

     //返回值

}

2、例子

class RichFile(file : File){
  def read = Source.*fromFile*(file.getPath()).mkString
}

object Context{
  implicit def fileToRich(file:File) = new RichFile(file)
}

object Third {
  def main(args: Array[String]): Unit = {
    import Context.*fileToRich     *//使用隐式住转换
    *println*(new File("d://aaaaa.txt").read)
  }
}

流程大概是这样的：new File().read-->发现File类中没有read方法-->然后找隐式转换，找到某个方法的参数正好File类型，然后便执行这个隐式函数，得到RichFile类型，该类型中read方法，便继续执行即可，否则运行不通过。再例如：

object Third {
  object MyImplicitTypeConversion {
    implicit def strToInt(str: String) = str.toInt
  }

  def main(args: Array[String]) {
    //compile error!
    //val max = math.max("1", 2);
    import MyImplicitTypeConversion.*strToInt*
*    *val max = math.*max*("1", 2);//遇到不符合的先检查是否在隐式转换的作用域内
    *println*(max)
  }
}

3、注意事项

1） 隐式转换函数的**函数名可以是任意的**，与函数名称无关，只与**函数签名（函数参数和返回值类型）有关**，即隐式函数的入参要是编译不通过的类型，返回值要是能正确编译的类型

2）如果当前作用域中存在函数签名相同但函数名称不同的两个隐式转换函数，则在进行隐式转换时会报错。

### 8.4 隐式类☆☆☆

在 Scala2.10 后提供了隐式类，可以使用 implicit 声明类，隐式类的非常强大，同样可以扩展类的功能，在集合中隐式类会发挥重要的作用

       1、格式：

**implicit** class 类名（参数）{

    //类主体

}

2、例子

String中没有bark方法，通过隐式转换，调用对应的方法转换

object Context{
  implicit class BA(val name : String){
    def bark=*println*(s"**$**name is barking")
  }
}
object Third {
  def main(args: Array[String]): Unit = {
    import Context._
    *println*("dog".bark)//"dog"和BA的参数类型相同，便可扩展BA的功能。
  }
}

3、注意事项

隐式类的运作方式是：**隐式类的主构造函数****只能****有一个参数**（有两个以上并不会报错，但是这个隐式类永远不会被编译器作为隐式类在隐式转化中使用），且**这个参数的类型就是将要被转换的目标类型**。从语义上这很自然：这个隐式转换类将包裹目标类型，隐式类的所有方法都会自动“附加”到目标类型上。所以：

1）隐式类的主构造函数参数有且仅有一个！**之所以只能有一个参数，是因为隐式转换是将一种类型转换为另外一种类型，源类型与目标类型是一一对应的**

2)implicit修饰符修饰类时只能存在于“类”或“伴生对象”或“包对象”或“特质”之内，即**隐式类不能是顶级的**

3）在同一作用域内，不能有任何方法、成员或对象与隐式类同名

4）隐式类不能是case class

5）Scala源码中存在的大部分隐式转换都是存在于Predef之中，比如：String->StringOps，Array->ArrayOps等，而Scala.Predef 自动引入到当前作用域

### 8.5 隐式对象☆☆☆

1、格式

**implicit** object 对象名{

    //类主体

}

2、例子

object ImplicitTest{
  def main(args: Array[String]): Unit = {
    //定义一个乘法接口
    trait Multiplicable[T]{
      def multiply(x: T):T
    }

    //定义一个隐式对象，用于整型数据相乘
    implicit object MultiplicableInt extends Multiplicable[Int]{
      def multiply(x: Int): Int = x*x
    }

    //定义一个隐式对象，用于字符串相乘
    implicit object MultiplicableString extends Multiplicable[String]{
      def multiply(x: String): String = x*2
    }

    //定义一个函数，函数具有泛型参数
    def multiply[T: Multiplicable](x: T): T ={
      //implicitly方法，访问隐式对象
      val ev = *implicitly*[Multiplicable[T]]  // 会检索作用域内类型为Multiplicable[T]的隐式
      //根据具体的类型调用相应的隐式对象中的方法
      ev.multiply(x)  //固定写法
    }

    //调用隐式对象 MultiplicableInt 中的方法
    *println*(multiply(5))  // 因为5是Int类型，就会找到Multiplicable[Int]，继而就能找到MultiplicableInt extends Multiplicable[Int]，然后就能找到这个类中定义的multiply方法
    //调用隐式对象 MultiplicableString 中的方法
    *println*(multiply("5"))
  }
}

3、注意事项

1）def multiply**[T: Multiplicable]**(x: T): T = {  //等价于def multiply[T](x:T)**(implicit mc:Multiplicable[T])**:T={

而T: Multiplicable就是所谓的**上下文界定(Context Bounds)**，类型参数声明 T : Comparator 就表示存在一个 Comparator[T]类型的隐式值。

2）def **implicitly**[T](implicit e: T) = e   是Predef中的方法，**用于返回隐式对象**。编译器会记录当前上下文里的隐式值，**而该方法则可以获得某种类型的隐式值。**

3）implicit修饰符修饰对象时**不能处于顶层对象级别**

### 8.6 隐式参数☆☆☆

1、格式：

def 函数名(**implicit** 参数名：类型) : 返回值 = {

       //函数体

}

2、例子

//修改上面的一个方法

//定义一个函数，函数具有泛型参数

 def multiply[T](x: T)(implicit ev: Multiplicable[T]): T ={

   //根据具体的类型调用相应的隐式对象中的方法

   ev.multiply(x)

 }

 3、隐式参数使用的常见问题：

**非柯里化**

      1）当函数没有柯里化时，implicit关键字会作用于函数列表中的所有参数。

      2）隐式参数使用时要么**全部不指定，要么全部指定**，不能只指定部分。

      3）在指定隐式参数时，implicit 关键字只能出现在参数开头。

**柯里化**

      4）如果想要实现参数的**部分隐式参数，只能使用函数的柯里化**，

例如：要实现这种形式的函数，def test(x:Int, implicit  y: Double)的形式，必须使用柯里化实现：def test(x: Int)(implicit y: Double).

       5) 柯里化的函数，** ****implicit 关键字只能作用于最后一个参数**。否则，不合法。

       6）implicit 关键字在隐式参数中**只能出现一次**，柯里化的函数也不例外！

7）匿名函数不能使用隐式参数

如： val prodeuct = (implicit x: Double, y: Double) => x*y  会报错

8）柯里化的函数如果有隐式参数，则不能使用其偏函数

如：scala> def product(x: Double)(implicit y: Double) = x*y

product: (x: Double)(implicit y: Double) Double

//定义隐式参数后，便不能使用其偏应用函数

scala> val p1 = product _

<console>:13: error: could not find implicit value for parameter y: Double

       val p1=product _

              ^

### 8.7 隐式值（相当于隐式参数的默认值）☆☆☆

1、格式

**implicit** val 变量名: 类型 = 值

2、例子

//定义一个带隐式参数的函数

scala> def sqrt(implicit x: Double) = Math.sqrt(x)

sqrt: (implicit x: Double)Double

//定义一个隐式值

scala> implicit val x:Double = 2.55

x: Double = 2.55

//调用定义的sqrt函数，它将自行调用定义好的隐式值

scala> sqrt

res1: Double = 1.5968719422671311

3、注意事项

1）**同类型****的隐式值只能在作用域内出现一次**，即不能在同一个作用域中定义多个相同类型的隐式值。但是不同类型的可以出现多次

2）编译器按照隐式参数的**类型去寻找对应类型的隐式值，与隐式值的名称无关**

3）implicitly[T]可以检索作用域内的类型为T的隐式值

     implicit val str: String = "alice"

     implicit val num: Int = 18

    def sayHello()(implicit name: String): Unit = {

      println("hello, " + name)

    }

     //如果参数有默认值，隐式值有衔接高于默认值

    def sayHi(implicit name: String = "ds"): Unit = {

      println("hi, " + name)

    }

    sayHello

    sayHi

    // 简便写法

    def hiAge(): Unit = {

      println("hi, " + **implicitly[Int]**)  //会检索上作用域内类型为T的隐式值

    }

·    hiAge()

  }

## 9 集合

### 9.1 相关概念☆

相比java的集合系统，scala的集合系统相当的复杂。**scala的集合系统的区分了可变（ mutable  ）和不可变（immutable ）集合。**一个mutable  集合能够更新甚至扩展空间，这意味着能改变、增加、删除一个集合的元素。 一个immutable集合，刚好相反，不能改变。虽然仍然可以做一些类似的增加，删除，或者更新，但是实际上（跟java的String一样）返回了一个新的对象，这里面就是指**返回了一个新的集合，而老的集合没有改变。**

**备注：**可变与否表明的是**内存中开辟出来的这块空间里的内容能否被修改**，如果针对 immutable 变量进行修改，其实是开辟了一块新的内存空间，产生了一个新的变量，而原来的变量依然没有改变

### 9.2 集合包的划分☆☆

所有的集合类在scala.collection 包中，或者它的子包中，分为mutable，immutable以及generic。大部分集合在scala.collection，scala.collection.immutable和scala.collection.mutable有**三个同名的类**(导包的时候一定要注意，不要导错了)，每个同名类有不同的特征：

i、scala.collection.immutable包中元素不可变，可以保证在任何时间访问时元素值都是相同的

ii、scala.collection.mutable 包中的元素可变，所以你要知道它在何时何地变化了

有一些集合类不在上述两个包下，如collection.IndexedSeq[T] 是collection.immutable.IndexedSeq[T] 和collection.mutable.IndexedSeq[T] 的父类。**一般情况下会在collection包下定义接口，由mutable和immutable两个包实现。**

**scala默认的集合包是不可变的 ，即scala.collection.immutable**。 比如，Set 如果没有导入其他的包，默认collection.immutable.Set，如果想用一个可变的Set，需要显示的导入collection.mutable.Set

如果想两个都引用，又想简单写，有个办法：import scala.collection.mutable，那么直接用Set则仍是默认不可变的，如果想Set是mutable的，写成mutable.Set

还有一个包  collection.generic，该包包含了实现集合的构建块。典型的generic里classes推迟实现一些函数。另一方面，集合framework的用户需要在一些特殊环境中用到generic中的类。

**scala.collection包下的集合的结构如下：**

**备注：**Seq是列表，适合存有序重复数据，进行快速插入/删除元素等场景，Set是集合，适合存无序非重复数据，进行快速查找海量元素的等场景

trait **Traversable**[+A] extends TraversableLike[A, Traversable[A]]

                         with GenTraversable[A]

                         with TraversableOnce[A]

                         with GenericTraversableTemplate[A, Traversable]

这些混入的trait丰富了整个集合的功能，比如TraversableOnce里的mkString，该api表示将字符串按照某种形式分割，有以下两种形式：

**mkString(seq:String)**：方法是将原字符串使用特定的字符串seq分割。

**mkString(statrt:String,seq:String,end:String)**：方法是将原字符串使用特定的字符串seq分割的同时，在原字符串之前添加字符串start，在其后添加字符串end。

object Third {
  def main(args: Array[String]): Unit = {
    var name : String = "Hello LittleLawson"
    var age :Int = 2
    *println*(name.mkString)
    *println*(name.mkString(" "))//separate string with space

    var str0 = "scala"
    *println*(str0.mkString(","))//separate string with comma

    *println*(str0.mkString("begin",",","end"))

    /*
    1.mkString is used in the inner List,That is say ,Elements in the list is applied.
     */
    val a = *List*(1,2,3,4)
    val b = new StringBuilder()
    *println*(a.mkString("List(" , ", " , ")"))

  }
}

scala.collection.immutable包下的集合的结构如下：

**备注：**Scala的Seq类似Java的List，Scala的List类似Java的LinkedList，然后Seq分为IndexedSeq 和 LinearSeq，我们来看二者的区别：

（1）IndexedSeq 是通过索引来查找和定位，因此速度快，比如 String 就是一个索引集合，通过索引即可定位

（2）LinearSeq 是线型的，即有头尾的概念，这种数据结构一般是通过遍历来查找

scala.collection.mutable包下的集合的结构如下：

所有集合类都支持Traversable提供的API，但只有一些特殊类有意义。如Traversable 类中的 map 方法返回另一个Traversable ，但结果类型会在子类中被重写。例如，在List中调用map，会返回一个List结果，在Set中调用返回Set.

scala> List(1, 2, 3) map (_ + 1)

res0: List[Int] = List(2, 3, 4)

scala> Set(1, 2, 3) map (_ * 2)

res0: Set[Int] = Set(2, 4, 6)

**备注：**集合中的大部分都存在（指名字相同的类分别存在）三个包中：collection、mutable、immutable，只有trait Buffer只存在mutable集合中

### 9.3 不可变数组Array☆☆

与Java中不同的是，Scala中没有数组这一种类型。在Scala中，Array类的功能就与数组类似。与所有数组一样，Array的长度不可变，里面的数据可以按索引位置访问

**备注****：Array是在scala包下，而不是在scala.collection包下**

def main(args: Array[String]): Unit = {
  //第一种构造：指定泛型，指定长度
  val array1 = new Array[Int](5)
  array1(1) = 1  // 实际上调用的是实例对象update方法，等价arr1.update(1,1)
  *println*(array1(1))

  //第二种构造：初始化元素，可以是任意类型，实质是隐式调用apply方法
  val array2 = *Array*(0, 1, 2, 3, 4)
  *println*(array2(3))

  //增加元素（由于创建的是不可变数组，增加元素，其实是产生新的数组）
  val ints: Array[Int] = array1 :+ 5  //元素加在数组最后面 巧记：:写在集合的那一侧
  val newArr3 =  15 +: array2   //元素加在数组最前面
  val newArr4 = 19 +: 29 +: newArr3 :+ 26 :+ 73

  // 数组的遍历
  // 第一种方式
  for (i <- 0 until array1.length){
    *println*(array1(i))
  }

  // 第二种方式
  for (i <- array1.indices) *println*(array1(i))

  // 第三种方式
  for (elem <- array1) *println*(elem)

  // 第四种方式
  array1.foreach( *println *)

  // 第五种方式
  val iter = array1.iterator
  while (iter.hasNext)
    *println*(iter.next())
}

### 9.4 scala中第二个重要方法（更新方法）☆☆

当对带有括号并包括一到若干参数的对象进行赋值时，编译器将使用对象的 update 方法对括号里的参数和等号右边的对象执行调用。

object Third {
  def main(args: Array[String]): Unit = {
    val obj = new SomeClass
    val result = (obj(1, "key1") = "Hello")
    *println*(result)
  }
}

class SomeClass {
  def update(arg1: Int, arg2: String, arg3: String): String = {
    *println*("update method called")
    arg1 + "|" + arg2 + "|" + arg3
  }
}

      ** 在应用 update 时，等号右边的值会作为 update 方法的最后一个参数。**因此，我们可以看到，update方法被默认调用，这个也是scala这门语言的便捷之处，往往通过隐式的方法，实际上调用的确实背后真的方法。

### 9.5 可变数组ArrayBuffer☆☆

ArrayBuffer混入了mutable下Seq的两个子trait：IndexedSeq、Buffer，因此。而ArrayList在Java中是用得非常多的一种集合类。与Array一样，元素有先后之分，可以重复，可以随机访问，但是插入的效率不高。

object Third {
  def main(args: Array[String]): Unit = {
    val arr = new mutable.ArrayBuffer[Int]()
    arr.append(1)  //等价于+=，但可添加多个
    // :+不会在arr1 上添加元素，而是新生成一个ArrayBuffer
    val newArr1 = arr :+ 2
    *println*(arr == newArr1)  //false
    val newArr2 = arr += 3 //元素加在数组最后面
    *println*(arr == newArr2)  //true
    newArr2 += 4
    *println*(arr)  //ArrayBuff(1, 3, 4)，因为是引用类型，所以对于可变集合，不建议添加元素后赋值给一个新变量
    5 +=: arr  //元素加在数组最后面
    arr.prepend(6) //等价于+=:，但可添加多个
    arr.insert(1, 13, 59)  //在指定的位置开始添加
    arr.insertAll(2, newArr1)
    arr.prependAll(newArr2)
    arr.remove(3, 10) // 删除指定的位置开始后10个元素
    arr -= 13  //删除数组中的元素，如果存在则删除，不存在不做操作
    val newArr= arr.toArray
    val buff = newArr.toBuffer
    // 创建二维数组
    val array: Array[Array[Int]] = Array.*ofDim*[Int](2, 3)  //两行三列
    array.foreach(_.foreach(*println*))
  }
}

### 9.6 IndexedSeq☆☆

这种类型的主要访问方式是通过索引，**默认的实现方式为Vector**

**备注：**这里的IndexedSeq是immutable包下的，相关联的还有Array和String

object Third {
  def main(args: Array[String]): Unit = {
    val x = *IndexedSeq*(1,2,3)
    *println*(x.getClass)
    *println*(x(0))

    val y = *Range*(1, 5)
    *println*(y)

  }
}

### 9.7 LinearSeq☆☆

主要的区别在于其被分为头与尾两部分。其中，**头是容器内的第一个元素，尾是除了头元素以外剩余的其他所有元素**。LinearSeq默认的实现是List，是不可变列表

object Third {
  def main(args: Array[String]): Unit = {
    val x = collection.immutable.LinearSeq("a", "b", "c")
    val head = x.head
    *println*(s"head is: **$**head")

    val y = x.tail
    *println*(s"tail of y is: **$**y")

    // 1. 创建一个List
    val list1 = *List*(23, 65, 87)

    // 2. 访问和遍历元素
    *println*(list1(1))
    //    list1(1) = 12  //immutable包下的List没有update方法，即不能更改列表中的数据
    list1.foreach(*println*)

    // 3. 添加元素
    val list2 = 10 +: list1
    val list3 = list1 :+ 23

    // 写成方法调用就是添加在前面，写成操作符的形式就添加在后面
    val list4 = list2.::(51) //生成一个新的List，然后会把元素添加到list2开头，等价51 :: list2
    *println*(list4)

    val list5 = *Nil*.::(13)
    *println*(list5)

    val list7 = 17 :: 28 :: 59 :: 16 :: *Nil *// 常见创建列表的方法
    *println*(list7)

    // 4. 合并列表
    val list9 = list5 ::: list7 // 等价于list7.:::(list5)
    *println*(list9)

    val list10 = list5 ++ list7 // 源码可以发现就是调用:::
    *println*(list10)

  }
}

### 9.8 ListBuff☆☆

     相比于List，ListBuffer是可变的集合，可以添加，删除元素，属于scala.collection.mutable包下。

object Third {
  def main(args: Array[String]): Unit = {
    // 1. 创建可变列表
    val list1: ListBuffer[Int] = new ListBuffer[Int]()
    val list2 = ListBuffer(12, 53, 75) //scala中推荐使用的构建方法，使用伴生对象的方式

    // 2. 添加元素
    list1.append(15, 62)
    list2.prepend(20)
    list1.insert(1, 19, 22)
    31 +=: 96 +=: list1 += 25 += 11

    // 3. 合并list
    val list3 = list1 ++ list2 // 返回新的对象，list1和list2不变
    list1 ++= list2  // 在list1后添加list2的元素，list2不变，如果反过来就是list1 ++=: list2

    // 4. 修改元素
    list2(3) = 30 // 等价于 list2.update(3, 30)

    // 5. 删除元素
    list2.remove(2)
    list2 -= 25
  }
}

### 9.9 Set☆☆

与其他任何一种编程语言一样，Scala中的Set集合类具有如下特点：

i、不存在有重复的元素。

ii、集合中的元素是无序的。换句话说，不能以索引的方式访问集合中的元素。

iii、判断某一个元素是否在Set集合中比Seq类型的集合要快。

#### 9.9.1 不可变的HashSet

object Third {
  def main(args: Array[String]): Unit = {
    val x = immutable.HashSet[String]("a","c","b")
    //x.add("d")无法使用，因为是不可变集合，没有add方法。没有类似+=这样的操作
    val y = x + "d" + "f"  // 增加新的元素，生成一个新的集合
    val z = y - "a"  // 删除一个元素，生成一个新的集合
    val a = *Set*(1,2,3)
    val b = *Set*(1,4,5)
    val c = a ++ b  //合并集合
    val d = a -- b  // a中剔除b中的元素
    val e = a & b // 与操作，交集
    val f = a | b // 或操作，并集
  }
}

#### 9.9.2 可变的HashSet

object Third {
  def main(args: Array[String]): Unit = {
    val x = new mutable.HashSet[String]()
    x += "a"  // 添加一个新的元素。注意此时没有生成一个新的集合
    x.add("d") //因为是可变集合，所以有add方法，返回值是boolean类型
    x ++= *Set*("b", "c")  // 添加一个新的集合，改变的是x，参照listBuffer
    x.foreach(each => *println*(each))
    x -= "b"  // 删除一个元素，remove返回值也是boolean类型
    val flag = x.contains("a") // 是否包含元素
    *println*(flag)
  }
}

### 9.10 Map☆☆

Map这种数据结构是日常开发中使用非常频繁的一种数据结构。Map作为一个存储键值对的容器（key－value），其中key值必须是唯一的。 默认情况下，可以通过Map直接创建一个不可变的Map容器对象，这时候容器中的内容是不能改变的，在scala中，可以使用java相同的方式即(key,value)来标识键值对，但是这符合scala的风格，**scala建议使用(key -> value)的形式来标识是一个key-value对**。

def im() = {
  // 两种创建map的方式
  val peoples = *Map*("john" -> 19, "Tracy" -> 18, "Lily" -> 20) //不可变
  val peopless = *Map*(("john", 19), ("Tracy", 18), ("Lily", 20))
  // people.put("lucy",15) 会出错，因为是不可变集合。
  //遍历方式1
  for(p <- peoples) {
    *print*(p + "  ") // (john,19)  (Tracy,18)  (Lily,20)
  }
  //遍历方式2
  peoples.foreach(x => {val (k, v) = x; *print*(k + ":" + v + "  ")}) //john:19  Tracy:18  Lily:20
  //遍历方式3
  peoples.foreach ({ case(k, v) => *print*(s"key: **$**k, value: **$**v  ")})
  //遍历方式4
  for (key <- peoples.keys){
    *println*(s"**$**key ---> **$**{peoples.get(key)}") //scala中的map.get返回的是一个Optional类型
  }
  *println*("a: " + peoples.get("a").get)
  *println*("c: " + peoples.get("c"))
  *println*("c: " + peoples.getOrElse("c", 0))
  *println*(peoples("a")) //等价于get
}

def mm() = {
  val map = new mutable.HashMap[String, Int]()
  map.put("john", 19) // 因为是可变集合，所以可以put
  map += (("Tracy", 18))
  map -= "john"  // remove
  map.contains("Lily") //false
}

### 9.11 元组（元素组合）☆☆

**元组也是可以理解为一个容器，可以存放各种相同或不同类型的数据**。说的简单点，就是将多个无关的数据封装为一个整体，称为元组。Map 中的键值对其实就是元组,只不过元组的元素个数为 2，称之为对偶，二元元组

**注意：**元组中最大只能有 22 个元素。

object Third {
  def main(args: Array[String]): Unit = {
    // 1. 创建元组
    val tuple: (String, Int, Char, Boolean) = ("hello", 100, 'a', true)
    *println*(tuple)

    // 2. 访问数据
    *println*(tuple._1)
    *println*(tuple._2)
    *println*(tuple._3)
    *println*(tuple._4)

    *println*(tuple.productElement(1))// 等价于_2，下标从零开始。

    // 3. 遍历元组数据
    for (elem <- tuple.productIterator)
      *println*(elem)

    // 4. 嵌套元组
    val mulTuple = (12, 0.3, "hello", (23, "scala"), 29)
    *println*(mulTuple._4._2)

    // 对偶
    val map = *Map*("a"->1, "b"->2, "c"->3)
    map.foreach(tuple => { *println*(tuple._1 + "=" + tuple._2)})

  }
}

### 9.12 队列☆☆

Scala 也提供了队列（Queue）的数据结构，队列的特点就是先进先出。进队和出队的方法分别为 enqueue 和 dequeue。

object Third {
  def main(args: Array[String]): Unit = {
    val que = new mutable.Queue[String]()
    que.enqueue("a", "b", "c")
    *println*(que.dequeue())
    *println*(que.dequeue())
    *println*(que.dequeue())
  }
}

### 9.13 集合常用函数☆☆

1、基本属性和常用操作

val list: List[Int] = List(1, 2, 3, 4, 5, 6, 7)

**（1）获取集合长度**

println(list.length)

通过源码分析可得，

def length: Int = {

  var these = self

  var len = 0

  while (!these.isEmpty) {

    len += 1

    these = these.tail

  }

  len

}

从源码中可以看到length内部是不管递归tail，说明此方法适合LinearSeq

**（2）获取集合大小**，有些集合（比如Set）可能没有length方法，在LinearSeq中等同于 length

在SeqLike中：override def size = length

而**Set调用的是TraverableOnce中的size，可以看出它是遍历集合中的元素，**源码分析如下：

def size: Int = {

  var result = 0

  for (x <- self) result += 1

  result

}

（3）循环遍历

list.foreach(println)

（4）迭代器

for (elem <- list.iterator) {

println(elem)

}

（5）生成字符串

println(list.mkString(","))

（6）是否包含

println(list.contains(3))

2、衍生集合

object Third {
  def main(args: Array[String]): Unit = {
    val list1: List[Int] = *List*(1, 2, 3, 4, 5, 6, 7)
    val list2: List[Int] = *List*(4, 5, 6, 7, 8, 9, 10)
    //（1）获取集合的头
    *println*(list1.head)
    //（2）获取集合的尾（不是头的就是尾）
    *println*(list1.tail)
    //（3）集合最后一个数据
    *println*(list1.last)
    //（4）集合初始数据（不包含最后一个）
    *println*(list1.init)
    //（5）反转
    *println*(list1.reverse)
    //（6）取前（后）n 个元素
    *println*(list1.take(3))
    *println*(list1.takeRight(3))
    //（7）去掉前（后）n 个元素
    *println*(list1.drop(3))
    *println*(list1.dropRight(3))
    //（8）并集
    *println*(list1.union(list2)) // 等价于：++
    //（9）交集
    *println*(list1.intersect(list2))
    //（10）差集
    *println*(list1.diff(list2))
    //（11）拉链操作：如果两个集合的元素个数不相等，那么会将同等数量的数据进行拉链，多余的数据省略不用，返回一个List，其组成元素是二元组
    *println*(list1.zip(list2))
    //（12）滑窗
    list1.sliding(3, 3).foreach(*println*)  // 返回值类型：Iterator[List[Int]]
    // sliding的第一个参数定义窗口的长度，第二个参数定义滑动的步长，当窗口长度和步长相等时称为滚动，如果窗口长度小于步长将造成数据丢失
  }
}

3、集合计算简单函数

object Third {
  def main(args: Array[String]): Unit = {
    val list: List[Int] = *List*(1, 5, -3, 4, 2, -7, 6)
    val map = *Map*(("john", 19), ("Tracy", 18), ("Lily", 20))
    //（1）求和
    *println*(list.sum)
    //（2）求乘积
    *println*(list.product)
    //（3）最大值
    *println*(list.max)
    //以后看到actionBy名字的方法，同时通过某种自定义函数的结果去执行action方法。
    *println*(map.maxBy(_._2))  //("Lily", 20)
    //（4）最小值
    *println*(list.min)
    *println*(map.maxBy(_._2))  //("Tracy", 18)
    //（5）排序
    // （5.1）按照元素大小排序
    *println*(list.sortBy(x => x))
    *println*(list.sorted.reverse)  //倒序，list里的reverse
    *println*(list.sorted(*Ordering*[Int].reverse)) //倒序，Ordering里的reverse
    // （5.2）按照元素的绝对值大小排序
    *println*(list.sortBy(x => x.abs))
    // （5.3）按元素大小升序排序
    *println*(list.sortWith((x, y) => x < y))
    // （5.4）按元素大小降序排序
    *println*(list.sortWith((x, y) => x > y))
    *println*(list.sortWith(_ > _)

  }
}

备注：

（1）sorted：对一个集合进行自然排序，可以传递隐式的 Ordering

（2）sortBy：通过指定的属性进行排序，通过它的类型。可以传递隐式的 Ordering

def sortBy[B](f: A => B)(implicit ord: Ordering[B]): Repr = sorted(ord on f)

（3）sortWith：基于函数的排序，通过一个 comparator 函数，实现自定义排序的逻辑。

def sortWith(lt: (A, A) => Boolean): Repr = sorted(Ordering fromLessThan lt)

4、集合计算高级函数

object Third {
  def main(args: Array[String]): Unit = {
    val list: List[Int] = *List*(1, 2, 3, 4, 5, 6, 7, 8, 9)
    val nestedList: List[List[Int]] = *List*(*List*(1, 2, 3), *List*(4,5, 6), *List*(7, 8, 9))
    val wordList: List[String] = *List*("hello world", "hello spark", "hello scala")

    //（1）过滤
    *println*(list.filter(x => x % 2 == 0)) // list.filter(_ % 2 == 0)

    //（2）转化/映射
    *println*(list.map(x => x + 1))  // list.map(_ + 1)

    //（3）扁平化
    *println*(nestedList.flatten) //List(1, 2, 3, 4, 5, 6, 7, 8, 9)

    //（4）扁平化+映射 注：flatMap 相当于先进行 map 操作，在进行 flatten操作，集合中的每个元素的子元素映射到某个函数并返回新集合
    *println*(wordList.flatMap(x => x.split(" "))) // List(hello, world, hello, spark, hello, scala)

    //（5）分组：按照指定的规则对集合的元素进行分组
    *println*(list.groupBy(x => x % 2))  //Map(1 -> List(1, 3, 5, 7, 9), 0 -> List(2, 4, 6, 8))
    // Map(奇数 -> List(1, 3, 5, 7, 9), 偶数 -> List(2, 4, 6, 8))
    *println*(list.groupBy(data => if (data % 2 == 0) "偶数" else "奇数"))

    //（6）Reduce 简化（归约） ：通过指定的逻辑将集合中的数据进行聚合，从而减少数据，最终获取结果。
    // 将数据两两结合，实现运算规则
    val ii: Int = list.reduce( (x, y) => x-y )  //list.reduce(_ - _ )
    *println*("ii = " + ii)
    // 从源码的角度，reduce 底层调用的其实就是 reduceLeft
    // 1-2=-1  -1-3=-4 -4-4=-8.....
    val i1 = list.reduceLeft((x,y) => x-y)
    // 9-8=1 1-7=-6 -6-6=-12....
    val i2 = list.reduceRight((x,y) => x-y)
    *println*(i2)

    //（7）Fold 折叠：化简的一种特殊情况。
    // fold 方法使用了函数柯里化，存在两个参数列表，第一个参数列表为 ： 零值（初始值），第二个参数列表为： 简化规则。fold 底层其实为 foldLeft
    val i = list.foldLeft(1)((x, y) => x - y)
    val i1 = list.foldRight(10)((x, y) => x - y)
    // 两个 Map 的数据合并
    val map1 = mutable.Map("a"->1, "b"->2, "c"->3)
    val map2 = mutable.Map("a"->4, "b"->5, "d"->6)
    val map3: mutable.Map[String, Int] = map2.foldLeft(map1){
      (map, kv) => {
        val k = kv._1
        val v = kv._2
        map(k) = map.getOrElse(k, 0) + v
        map
      }
    }
    *println*(map3)  // Map(b -> 7, d -> 6, a -> 5, c -> 3)
  }
}

### 9.14 典型案例：WordCount☆☆

object Third {
  def main(args: Array[String]): Unit = {
      // 单词计数：将集合中出现的相同的单词，进行计数，取计数排名前三的结果
      val stringList = *List*("Hello Scala", "Hello Scala Hbase", "Hello HBase")

      // 1) 将每一个字符串转换成一个一个单词
      val wordList: List[String] = stringList.flatMap(_.split(" "))
      //println(wordList)

      // 2) 将相同的单词放置在一起
      val wordToWordsMap: Map[String, List[String]] = wordList.groupBy(word => word)
      *println*(wordToWordsMap) //Map(Hello -> List(Hello, Hello, Hello), Hbase -> List(Hbase), HBase -> List(HBase), Scala -> List(Scala, Scala))

      // 3) 对相同的单词进行计数(word, list) => (word, count)
      val wordToCountMap: Map[String, Int] = wordToWordsMap.map(tuple => (tuple._1, tuple._2.size))

      // 4) 对计数完成后的结果进行排序（降序）
      val sortList: List[(String, Int)] = wordToCountMap.toList.sortWith(_._2 > _._2)

      // 5) 对排序后的结果取前 3 名
      val resultList: List[(String, Int)] = sortList.take(3)
      *println*(resultList) //List((Hello,3), (Scala,2), (Hbase,1))
    }
}

### 9.15 java与scala集合的相互转换☆☆☆

Scala中提供了如下的object：**JavaConverters** extends DecorateAsJava with DecorateAsScala，里面包含了各种各样的装饰器，可以在java和scala之间进行转换，提供两个扩展方法，**asScala 和asJava**。扩展方法返回相应API的适配器。

下面的转换是通过asScala和asJava支持的，可以实现**自动转换**，即需要左边的地方完全可以使用右边的代替，同理也是一样：

备注：自动转换一般用在函数传参的地方，如果强行转换，需要显示调用asJava或者asScala

scala.collection.Iterable   <=> java.lang.Iterable

scala.collection.Iterator  <=> java.util.Iterator

scala.collection.mutable.Buffer<=> java.util.List

scala.collection.mutable.Set  <=>java.util.Set

scala.collection.mutable.Map  <=> java.util.Map

scala.collection.concurrent.Map  <=> java.util.concurrent.ConcurrentMap

以下转换必须通过指定的方法转换为Java集合，如下所示:

scala.collection.Iterable  <=> java.util.Collection(通过 asJavaCollection)

scala.collection.Iterator  <=> java.util.Enumeration(通过 asJavaEnumeration)

scala.collection.mutable.Map  <=> java.util.Dictionary(通过 asJavaDictionary)

此外，通过类似' xxxAsJavaXxxx '提供了以下单向转换，也可以自动转换（如果需要左边的类型可以使用右边的类型替代）

scala.collection.Seq=> java.util.List

scala.collection.mutable.Seq=> java.util.List

scala.collection.Set => java.util.Set

scala.collection.Map=> java.util.Map

下面的一种方式转换是通过类似' asScala '提供的:

java.util.Properties=>scala.collection.mutable.Map

**在所有情况下，从源类型转换到目标类型再转换回来都将返回原始源对象**。例如:

import scala.collection.JavaConverters._



val source = new scala.collection.mutable.ListBuffer[Int]

val target: java.util.List[Int] = source.asJava

val other: scala.collection.mutable.Buffer[Int] = target.asScala

println(source eq other) // true

或者，转换方法具有描述性名称，可以显式调用。

scala> val vs = java.util.Arrays.asList("hi", "bye")

vs: java.util.List[String] = [hi, bye]



scala> val ss = asScalaIterator(vs.iterator)

ss: Iterator[String] = non-empty iterator



scala> .toList

res0: List[String] = List(hi, bye)



scala> val ss = asScalaBuffer(vs)

ss: scala.collection.mutable.Buffer[String] = Buffer(hi, bye)

**scala最大的优势之一就是可以使用JDK上面的海量类库**。实际项目中，经常需要在java集合类与scala集合类之间做转化。具体的转换对应关系如下： **在使用这些转换的时候，只需要scala文件中引入scala.collection.JavaConversions._ 即可**。

如：Java List转Scala Seq

List<String> tmpList = new ArrayList<>()

tmpList.add("abc")

Seq<String> tmpSeq = JavaConverters.asScalaIteratorConverter(tmpList.iterator()).asScala().toSeq()

Scala Seq转Java List

List<String> tmpList = scala.collection.JavaConversions.seqAsJavaList(tmpSeq)

### 9.16 练习题和面试题

1、练习题：手写wordcount程序

2、练习题：该部分重点是对操作的熟悉，本篇涉及众多操作，凡是文档中涉及到的操作，希望大家都能手动敲敲

3、面试：scala集合包的结构以及和java中的区别

4、面试题list、set、map、元组及常见的数据结构

## 10 模式匹配

Scala 中的模式匹配类似于 Java 中的 switch 语法，这个我们在说到scala中的流程控制的时候提到过，但是scala中的模式匹配的功能远远大于switch的功能，并且在scala中使用的相当的广泛。

### 10.1基本语法☆☆

所谓的模式匹配就是给定多条路径，然后选择一条匹配的路径。在模式匹配语法中，采用**match** 关键字声明，每个分支采用依旧 case 关键字进行声明，当需要匹配时，会从第一个 case分支开始，如果匹配成功，那么执行对应的逻辑代码，其他case将不再进行比较，如果匹配不成功，继续执行下一个分支进行判断。**如果所有 case 都不匹配，那么会执行默认 ****case _**** 分支，类似于 Java 中 default 语句。若此时没有 case _ 分支，那么会抛出MatchError。**

同样，模式匹配也是有返回值结果的，而这个结果就是匹配到的case对应的值。

**备注：**_下划线可以用其他有效名称代替，只是不需要写出类型。

object Third {
  def main(args: Array[String]): Unit = {
    var a: Int = 1
    var b: Int = 2
    var operator: Char = '+'
    var result = operator match {
      case '+' => a + b
      case '-' => a - b
      case '*' => a * b
      case '/' => a / b
      case _ => "illegal"
    }

println(result)
  }
}

**match case 语句可以匹配任何类型，而不只是字面量**。=> 后面的代码块，直到下一个 case 语句之前的代码是作为一个整体执行，可以使用{}括起来，也可以不使用大括弧。

### 10.2模式守卫☆☆

如果想要表达匹配某个范围的数据，就需要在模式匹配中增加条件守卫

def main(args: Array[String]): Unit = {
  val age:Int = 18
  age match {
    case a if a < 12 => *println*("青年")
    case b if b>=12 && b < 50 => *println*("中年")
    case _ => *println*("未知")
  }
}

### 10.3匹配常量☆☆

Scala 中，模式匹配可以匹配所有的字面量，包括字符串，字符，数字，布尔值等等。

def describe(x: Any) = x match {
  case 1 => "one"
  case "hello" => "hello"
  case true => "true"
  case '+' => "+"
  case _ => "Else"
}

### 10.4 匹配类型☆☆

需要进行类型判断时，可以使用 isInstanceOf[T]和 asInstanceOf[T]，也可使用模式匹配实现同样的功能

object Third {

  def describe(x: Any) = x match {
    case i: Int => "Int"
    case s: String => "String hello"
    case m: List[_] => "List"
    case c: Array[Int] => "Array[Int]"
    case someThing => "something else " + someThing // 这里使用something代替_
  }

  def main(args: Array[String]): Unit = {
    //泛型擦除，即JVM中只能看到List，看不到例如List[Int]、List[String]等泛型
    *println*(*describe*(*List*(1, 2, 3, 4, 5)))
    //数组例外，可保留泛型
    *println*(*describe*(*Array*(1, 2, 3, 4, 5, 6)))
    *println*(*describe*(*Array*("abc")))
  }
}

### 10.5 匹配数组☆☆

scala 模式匹配可以对集合进行**精确的匹配**，例如匹配只有两个元素的且第一个元素为 0 的数组

def main(args: Array[String]): Unit = {
  for (arr <- *Array*(*Array*(0), *Array*(1, 0), *Array*(0, 1, 0), *Array*(1, 1, 0), *Array*(1, 1, 0, 1), *Array*("hello", 90))) { // 对一个数组集合进行遍历
    val result = arr match {
      case *Array*(0) => "0" //匹配 Array(0) 这个数组
      case *Array*(x, y) => x + "," + y //匹配有两个元素的数组，然后将将元素值赋给对应的 x,y
      case *Array*(0, _*) => "以 0 开头的数组" //匹配以 0 开头和数组
      case _ => "something else"
    }
    *println*("result = " + result)
  }
}

### 10.6 匹配列表☆☆

和匹配数组大致相似。

object Third {
  def main(args: Array[String]): Unit = {
    for (list <- *Array*(*List*(0), *List*(1, 0), *List*(0, 0, 0), *List*(1,0, 0), *List*(88))) {
      val result = list match {
        case List(0) => "0" //匹配 List(0)
        case List(x, y) => x + "," + y //匹配有两个元素的 List
        case List(0, _*) => "0 ..." //匹配第一个元素是0的List
        case _ => "something else"
      }
      *println*(result)
    }

    val list: List[Int] = *List*(1, 2, 5, 6, 7)
    list match {
      // first=1 second=2 rest=List(5, 6, 7)
      case first :: second :: rest => *println*(first + "-" + second + "-" + rest)
      case _ => *println*("something else")
    }
  }
}

### 10.7匹配元组☆☆

和数组，list的匹配规则也是相似的。

object Third {
  def main(args: Array[String]): Unit = {
    //对一个元组集合进行遍历
    for (tuple <- *Array*((0, 1), (1, 0), (1, 1), (1, 0, 2))) {
      val result = tuple match {
        case (0, _) => "0 ..." //是第一个元素是 0 的元组
        case (y, 0) => "" + y + "0" // 匹配后一个元素是 0 的对偶元组
        case (a, b) => "" + a + " " + b
        case _ => "something else" //默认
      }
      *println*(result)
    }
  }
}

元组其他的模式匹配（也可以用于List、Array等）

object Third{
  def main(args: Array[String]): Unit = {
    // 一般的for循环
    for (elem <- *Array*(("a", 1), ("b", 2), ("c", 3))) {
      *println*(elem._1)
    }

    // 指定元组的for循环
    for ((word,count) <- *Array*(("a", 1), ("b", 2), ("c", 3))) {
      *println*(word)
    }

    // 只留下想要的部分，剩下的用_，如果是连续多个，用_*
    for ((word, _) <- *Array*(("a", 1), ("b", 2), ("c", 3))) {
      *println*(word)
    }

    // 只留下第一个元素是"a"的元组，相当于守卫
    for (("a",count) <- *Array*(("a", 1), ("b", 2), ("c", 3))) {
      *println*(count)
    }

    //给元组元素命名
    var (id, name, age): (Int, String, Int) = (100, "zs", 20) // 一一对应
    *println*((id, name, age))

    // 元组map中的case
    var list: List[(String, Int)] = *List*(("a", 1), ("b", 2), ("c", 3))
    //println(list.map(t => (t._1, t._2 * 2)))
    list.map(
      tuple => tuple match {
        case (word, count)=>(word, count*2)
      }
    )

    // 对上述的过程的简写即为如下：
    list.map{
      case (word, count)=>(word, count*2)
    }

    var list1 = *List*(("a", ("a", 1)), ("b", ("b", 2)), ("c", ("c", 3)))
    *println*(
      list1.map{
        case (groupkey, (word, count))=>(word, count*2)
      }
    )
  }
}

### 10.8 变量声明中的模式匹配☆☆

object Third {
  def main(args: Array[String]): Unit = {
    val (x, y) = (1, 2)
    *println*(s"x=**$**x,y=**$**y")

    //这里_*不能用其他代替，否则会出现不匹配的情况，如果向匹配可以用::
    val *Array*(aaa, bbb, _*) = *Array*(1, 7, 2, 9)
    *println*(s"aaa=**$**aaa,bbb=**$**bbb")
  }
}

### 10.9 for 表达式中的模式匹配☆☆

object Third {
  def main(args: Array[String]): Unit = {
    val map = *Map*("A" -> 1, "B" -> 0, "C" -> 3)
    for ((k, v) <- map) { //直接将 map 中的 k-v 遍历出来
      *println*(k + " -> " + v) //3 个
    }

    //遍历 value=0 的 k-v ,如果 v 不是 0,过滤
    for ((k, 0) <- map) {  //等价于：for ((k, v) <- map if v == 0)
      *println*(k + " --> " + 0) // B->0
    }

    //if v == 0 是一个过滤的条件
    for ((k, v) <- map if v >= 1) {
      *println*(k + " ---> " + v) // A->1 和 c->33
    }
  }
}

### 10.10匹配样例类或者样例对象☆☆

#### 10.10.1 Scala中第三个重要的方法（抽取方法）

说这个方法之前，首先我们来看一个案例：

class Money(val value: Double, val country: String) {}

object Money {
  def apply(value: Double, country: String) : Money = new Money(value, country)

  def unapply(money: Money): Option[(Double, String)] = {
    if(money == null) {
      None
    } else {
      Some(money.value, money.country)
    }
  }
}

object Third{
  def main(args: Array[String]): Unit = {
    *testUnapply*()
  }

  def testUnapply() = {
    val money = *Money*(10.1, "RMB")
    money match { // 在Money类中是否找到unapply方法
      case *Money*(num, "RMB") =>  *println*("RMB: " + num)
             case _ => *println*("Not RMB!")
    }
  }
}

在match之前，Scala首先会查找有没有对应的unapply方法，如果有让对象调用伴生对象的unapply方法（即对象是unapply方法里的参数，unapply方法的返回类型是case里的类型），然后**把对象的中的值取出来，然后让Optional对象和对应的case中类中提取出来的值进行比较**

再比如：

class UnapplyTest (var x :String ,var y :Int) {}

object UnapplyTest {
  def apply(x:String): UnapplyTest ={
    val array =  x.split(":")
    *require*(array.length==2)
    new UnapplyTest(array(0).toString, array(1).toInt)
  }

  def unapply(unapplyTest: String): Option[(String, Int)]={
    val array =  unapplyTest.split(":")
    Some(array(0).toString, array(1).toInt)
  }

  def main(args: Array[String]): Unit = {
    val unapplyTest = *UnapplyTest*("localhost:8080")
    *println*(unapplyTest.x + ":" + unapplyTest.y)
    var test  = "localhost:8080"

// 1.case 匹配到一个Object的时候，那我们看看这个object里有没有unapply
// 2、看unapply方法的参数类型和match之前的类型是否一致，如果一致的话，那么默认调用该unapply方法
// 3、unapply返回值得Some类型的参数个数和case后面的object的参数个数是否一致，如果一致，成功匹配
    test match { // 在当前类中是否可以找到unapply方法
      case *UnapplyTest*("localhost",8080) => *print*("I am here")
    }
  }
}

test 是String类型，本身是无法匹配UnapplyTest 类型的。因为在unapply里面定义，在这里会先将test调用unapply 然后与输出的Option 比较。

#### 10.10.2 case class

**case class被称为样例类，定义方法和class没有区别，**构造器中的每一个参数都成为 val，除非它被显式地声明为 var（不建议这样做），一般不需要方法体。

首先我们定义一个简单的样例类：Person.scala

case class Person(name: String, age: Int)

通过终端中编译该文件后生成两个class文件，Person.class和Person$.class（和object编译的结果一样，生成两个类：主类和辅助类）

接下来再通过jad命令反编译Person.class，结果结果如下：

Compiled from "Person.scala"

public class com.scala.whj.Person implements scala.Product, scala.Serializable {

public static scala.Function1<scala.Tuple2<java.lang.String, java.lang.Object>, com.scala.whj.Person> tupled();

public static scala.Function1<java.lang.String, scala.Function1<java.lang.Object, com.scala.whj.Person>> curried();

public java.lang.String name();

public int age();

public com.scala.whj.Person copy(java.lang.String, int);

public java.lang.String copy$default$1();

public int copy$default$2();

public java.lang.String productPrefix();

public int productArity();

public java.lang.Object productElement(int);

public scala.collection.Iterator<java.lang.Object> productIterator();

public boolean canEqual(java.lang.Object);

public int hashCode();

public java.lang.String toString();

public boolean equals(java.lang.Object);

public com.scala.whj.Person(java.lang.String, int);

}

再反编译Person$.class

Compiled from "Person.scala"

public final class com.scala.whj.Person$ extends scala.runtime.AbstractFunction2<java.lang.String, java.lang.Object, com.scala.whj.Person> implements scala.Serializable {

public static final com.scala.whj.Person$ MODULE$;

public static {};

public final java.lang.String toString();

public com.scala.whj.Person apply(java.lang.String, int);

public scala.Option<scala.Tuple2<java.lang.String, java.lang.Object>> unapply(com.scala.whj.Person);

public java.lang.Object apply(java.lang.Object, java.lang.Object);

}

可见，当声明样例类时， Scala 会自动实现：

1、构造器中的每个参数都成为 val （除非它被显式的声明为var ，不建议）；age和name字段都是由final 修饰，也就是说是不可改变的，那么用scala的语言来阐述，那么就是** case class 的参数默认是 immutable类型的**

**2、在伴生对象中提供的apply方法；**

**3、默认提供unapply 方法让模式匹配可以工作；**

4、将自动生成 toString、equals、hashCode 和 copy方法 (除非显式的给出这些方法的定义。 除上述之外， 样例类和其他类完全一样。可以添加字段和方法，扩展它们等。)

5、默认是可以序列化的

6、自动从scala.Product中继承一些函数

7、case class构造函数的参数是public级别的，可以直接访问

#### 10.10.3 case object

case object 称为样例对象，和case class用法基本类似，还是以case object Person和case class Person(age:Int, name:String)为例，查看二者的主要区别在于：

1、case object Person相比于case class Person(age:Int, name:String)缺少了apply、unapply方法，因为case object是没有参数输入的，所以对于apply 和unapply的方法也自然失去。

2、**case object 不再像object那样仅仅是一个单列对象，而是有像类（class）一样的特性。**

**备注：**case class Person，此刻是不带参数的。发现和case object Person 编译的结果一模一样，因此总结一句话，**当Person有参数的时候，用case class ，当Person没有参数的时候那么用case object。意义在于区分有参和无参**

#### 10.10.4 样例类/对象的模式匹配

**样例类/对象是为模式匹配而优化的类，因为其默认提供了 unapply 方法，因此，样例类可以直接使用模式匹配，而无需自己实现 unapply 方法**。

// case class不需要new来创建对象

case class User(name: String, age: Int)

object Third {
  def main(args: Array[String]): Unit = {
    val user: User = *User*("zhangsan", 11)
    val result = user match {
      case *User*("zhangsan", 11) => "yes"
      case _ => "no"
    }
    *println*(result)
  }
}

### 10.11 练习题及面试题

1、练习题：将该 List(1, 2, 3, 4, 5, 6, "test")中的 Int 类型的元素加一，并去掉字符串

2、面试：各种模式匹配都要知道原理以及实操的方法

3、面试：case class和case object，工作中用的非常的多

4、面试：unapply方法的理解

## 11 异常

Scala关于异常处理的语法上大体和java相同，但是又有些语法上的区别，只需要记住这些区别即可

### 11.1 java中的异常处理☆

首先我们来看看Java的 异常处理

public class ExceptionDemo {

public static void main(String[] args) {

try {

int a = 1;

int b = 0;

int c = a / b;

}catch (ArithmeticException e){

// catch 时可以写多个异常，但是需要将范围小的写到前面

e.printStackTrace();

}catch (Exception e){

e.printStackTrace();

}finally {

System.out.println("finally");

}

}

}

注意事项：

（1）Java 语言按照 try-catch-finally 的方式来处理异常，不管有没有异常捕获，都会执行 finally，因此通常可以选择在 finally 代码块中释放资源。

（2）可以有多个 catch，分别捕获对应的异常，这时需要把范围小的异常类写在前面，把范围大的异常类写在后面，否则编译错误。

### 11.2 Scala 异常处理☆

def main(args: Array[String]): Unit = {

try {

var n= 10 / 0

}catch {

   // 在scala中使用模式匹配的方式去匹配异常

case ex: ArithmeticException => {

// 发生算术异常

println("发生算术异常")

}

case ex: Exception => {

// 对异常处理

println("发生了异常 1")

println("发生了异常 2")

}

}finally {

println("finally")

}

}

1）将可疑代码封装在 try 块中。在 try 块之后使用了一个 catch 处理程序来捕获异常。如果发生任何异常，catch 处理程序将处理它，程序将不会异常终止。

2）Scala 的异常的工作机制和 Java 一样，但是 Scala 没有“checked（编译期）”异常，即 **Scala 没有编译异常这个概念，异常都是在运行的时候捕获处理。**

**3）异常捕捉的机制与其他语言中一样，如果有异常发生，catch 子句是按次序捕捉的**。因此，在 catch 子句中，越具体的异常越要靠前，越普遍的异常越靠后，如果把越普遍的异常写在前，把具体的异常写在后，在 Scala 中也不会报错，但这样是非常不好的编程风格。

4）finally 子句用于执行不管是正常处理还是有异常发生时都需要执行的步骤，一般用于对象的清理工作，这点和 Java 一样。

5）用 throw 关键字，抛出一个异常对象。所有异常都是 Throwable 的子类型。**在scala中throw 表达式是有类型的，就是 Nothing**，因为 Nothing 是所有类型的子类型，所以 throw 表达式可以用在任何需要类型的地方

def test():Nothing = {

**throw** new Exception("不对")

}

6）java 提供了 throws 关键字来声明异常。可以使用方法定义声明异常。它向调用者函数提供了此方法可能引发此异常的信息。它有助于调用函数处理并将该代码包含在 try-catch块中，以避免程序异常终止。**在 Scala 中，可以使用 ****throws 注解****来声明异常**

class ExceptionExample{
  @throws[NumberFormatException] // 或者写成：@throws(classOf[NumberFormatException])
  def validate()={
    "abc".toInt
  }
}

object First{
  def main(args:Array[String]){
    var e = new ExceptionExample()
    try{
      e.validate()
    }catch{
      case ex : NumberFormatException => *println*("Exception handeled here")
    }
    *println*("Rest of the code executing...")
  }
}

## 12 实操

1、假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

object First {
  def main(args: Array[String]): Unit = {
    *println*(*climbStairs*(12))
  }

  def climbStairs(n: Int): Int = {
    *ex*(n)
  }

  def ex(n: Int): Int = {
    if (n > 2) {
      *ex*(n - 1) + *ex*(n - 2)
    } else if (n == 2) {
      2
    } else if (n == 1) {
      1
    } else {
      0
    }
  }
}

2、给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

object First {
  def main(args: Array[String]): Unit = {
    val arr = ArrayBuffer(2,3,0,9,0,1)
    *moveZeroes*(arr)
    arr.foreach(*println*)
  }

  def moveZeroes(nums: ArrayBuffer[Int]): Unit = {
    var zeroIndex:Int = 0
    for(index <- 0 until nums.length){
      if(nums(index) !=0){
        nums(zeroIndex) = nums(index)
        if(index != zeroIndex) {
          nums(index) =0
        }
        zeroIndex += 1
      }
    }
  }
}

3、scala练习连接mysql

object First {

  // 访问本地MySQL服务器，通过3306端口访问mysql数据库
  val *url *= "jdbc:mysql://127.0.0.1:3306/scala_demo"
  //驱动名称
  val *driver *= "com.mysql.cj.jdbc.Driver"

  //用户名
  val (*username*, *password*) = ("root", "123456")

  //初始化数据连接
  var *connection*: Connection = _

  def main(args: Array[String]): Unit = {

    try {
      //注册Driver
      Class.*forName*(*driver*)
      //得到连接
      *connection *= DriverManager.*getConnection*(*url*, *username*, *password*)
      val statement = *connection*.createStatement
      //执行查询语句，并返回结果
      val rs = statement.executeQuery("SELECT * FROM lang")

      //打印返回结果
      while (rs.next) {
        val age = rs.getString("age")
        *println*(s"age is **$**{age}")
      }

      *println*("查询数据完成！")

      //    执行插入操作
      val rs2 = statement.executeUpdate("INSERT INTO `lang` (`age`) VALUES (22)")
      *println*("插入数据完成")

    } catch {
      case e: Exception => e.printStackTrace
    }
    //关闭连接，释放资源
    *connection*.close
  }
}

4、scala练习hdfs的连接

object First {

  val *conf*: Configuration = null
  var *fs*: FileSystem = null

  @throws[Exception]
  def main(args: Array[String]): Unit = {
    *fs *= FileSystem.*get*(new URI("hdfs://ds-bigdata-001:8020"), new Configuration, "hdfs")
    *travelFile*()
    //            可递归创建目录
    //            hdfsDemo.mkdir("/data1/data2");
    //            只能删除最后一层目录，并不能递归删除目录
    //            hdfsDemo.delete_dir("/data1/data2");
    *close*()
  }

  @throws[IOException]
  def mkdir(str: String): Unit = {
    val dir = new Path(str)
    System.*out*.println("执行创建文件夹目录")
    if (*fs*.exists(dir)) {
      System.*out*.println("目录已存在！")
      *fs*.delete(dir, true)
    }
    *fs*.mkdirs(dir)
    System.*out*.println("创建成功")
  }

  @throws[IOException]
  def delete_dir(str: String): Unit = {
    val dir = new Path(str)
    System.*out*.println("执行删除程序")
    if (*fs*.exists(dir)) {
      *fs*.delete(dir, true)
      System.*out*.println("删除成功！")
    }
    else System.*out*.println("地址不存在")
  }

  @throws[IOException]
  def upload(): Unit = {
    System.*out*.println("执行上传程序")
    val input = new BufferedInputStream(new FileInputStream(new File("./data/book.docx")))
    val outfile = new Path("/data/test/out.txt")
    val output: FSDataOutputStream = *fs*.create(outfile)
    IOUtils.*copyBytes*(input, output, *conf*, true) //链接输入流和输出流文件

  }

  @throws[Exception]
  def travelFile(): Unit = {
    val fileStatuses: Array[FileStatus] = *fs*.listStatus(new Path("/"))
    for (fileStatus <- fileStatuses) {
      if (fileStatus.isDirectory) {
        val path: Path = fileStatus.getPath
        *listAllFiles*(*fs*, path)
      }
      else System.*out*.println("文件路径为: " + fileStatus.getPath.toString)
    }
  }

  @throws[Exception]
  def listAllFiles(fileSystem: FileSystem, path: Path): Unit = {
    val fileStatuses: Array[FileStatus] = fileSystem.listStatus(path)
    for (fileStatus <- fileStatuses) {
      if (fileStatus.isDirectory) *listAllFiles*(fileSystem, fileStatus.getPath)
      else {
        val path1: Path = fileStatus.getPath
        System.*out*.println("文件路径为" + path1)
      }
    }
  }

  @throws[IOException]
  def close(): Unit = {
    *fs*.close()
  }
}
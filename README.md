# 人生苦短之Objective-C与Python交互简介

![share_python](http://onmw6wg88.bkt.clouddn.com/share_python.png)

## 写在前面

随着编程界语言的飞速发展，Python已占据编程语言排行榜单的第5名，并且近几年来更是愈发火热，不管是做运维、网络爬虫，还是服务端开发，Python似乎越来越被开发者所青睐，更是有**“人生苦短，我用Python。”**之说，由此，Python的重要性还是显而易见的。

![share_sort](http://onmw6wg88.bkt.clouddn.com/share_sort.png)

## 1. Python 简介

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。

Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色的语法结构。

* **Python 是一种解释型语言：**这意味着Python在开发过程中不存在编译这个环节。

* **Python是交互式语言：**这意味着，您可以在一个Python提示符，直接互动执行写你的程序。

* **Python是面向对象语言：**这意味着，Python支持面向对象的特性或代码封装在对象的编程技术。

* **Python是初学者的语言：**Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

Python 的特点可以简单的概括如下：

* **1.易于学习：**Python有相对较少的关键字，结构简单，和一个明确定义的语法，学习起来相对简单。
* **2.易于阅读：**Python 代码定义的更清晰，有严格的代码结构要求。
* **3.易于维护：**Python 的成功在于它的源代码是相当容易维护的。
* **4.广泛的标准库：**Python 的最大的优势之一是拥有丰富的库，跨平台的，在 UNIX，Windows 和 Mac OS 上都兼容很好。
* **5.互动模式：**互动模式的支持，您可以从终端输入执行代码并获得结果的语言，互动的测试和调试代码片断。
* **6.可移植：**基于其开放源代码的特性，Python 已经被移植到许多平台。
* **7.可扩展：**如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。<font color=red>（本次要说的就是基于这一特点。）</font>
* **8.数据库：**Python 提供所有主要的商业数据库的接口，SQLite、MySQL等等。
* **9.GUI编程：**Python 也支持GUI可以创建和移植到许多系统调用。
* **10.可嵌入：**你可以将 Python 嵌入到 C/C++ 程序，让你的程序获得"脚本化"的能力。

## 2. Python 基础语法

***Python 语法格式是要严格缩进的，所以一旦代码中的缩进不正确，执行时是会报错的。这一点很重要！***

### 2.1 Python 变量类型

Python 有5个标准的数据类型：

* Numbers （数字）
* String （字符串）
* List （列表）
* Tuple （元祖）
* Dictionary （字典）

同时，Python 还支持4种不同的数字类型：

* int (整型)
* long （长整型）
* float （浮点型）
* complex （复数）

```
count = 100 #整型变量
miles = 100.5 #浮点型变量
name = 'John' #字符串
list = ['runoob', 786, 2.23] #列表
tuple = ('runoob', 786, 2.23) #元祖(相当于只读list)
dict = {'name': 'john', 'code': 6734, 'dept': 'sales'} #字典
```

Python 变量定义不需要指定变量类型，直接写变量名即可。

### 2.2 Python 运算符

Python 算术运算符：

以下假设变量：a=10, b=20

<table align="center">
		<tr>
			<th>运算符</th>
			<th>描述</th>
			<th>实例</th>
		</tr>
		<tr>
			<td align="center">+</td>
			<td>加——两个对象相加</td>
			<td>a+b 输出结果 30</td>
		</tr>
		<tr>
			<td align="center">-</td>
			<td>减——得到负数或是一个数减去另一个数</td>
			<td>a-b 输出结果 -10</td>
		</tr>
		<tr>
			<td align="center">*</td>
			<td>乘——两个数相乘或是返回一个被重复若干次的字符串</td>
			<td>a * b 输出结果 200</td>
		</tr>
		<tr>
			<td align="center">/</td>
			<td>除——x除以y</td>
			<td>b/a 输出结果 2</td>
		</tr>
		<tr>
			<td align="center">%</td>
			<td>取模——返回除法的余数</td>
			<td>b%a 输出结果 0</td>
		</tr>
		<tr>
			<td align="center"> ** </td>
			<td>幂——返回x的y次幂</td>
			<td>a ** b 输出结果 10的20次幂</td>
		</tr>
		<tr>
			<td align="center">//</td>
			<td>取整——返回商的整数部分</td>
			<td>9//2 输出结果 4, 9.0//2.0 输出结果 4.0</td>
		</tr>
	</table>
	
Python 逻辑运算符：

<table align="center">
		<tr>
			<th>运算符</th>
			<th>逻辑表达式</th>
			<th>描述</th>
			<th>实例</th>
		</tr>
		<tr>
			<td align="center">and</td>
			<td>x and y</td>
			<td>布尔"与"——如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。</td>
			<td>(a and b) 返回 20</td>
		</tr>
		<tr>
			<td align="center">or</td>
			<td>x or y</td>
			<td>布尔"或"——如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。</td>
			<td>(a or b) 返回 10</td>
		</tr>
		<tr>
			<td align="center">not</td>
			<td>not x</td>
			<td>布尔"非"——如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。</td>
			<td>not(a and b) 返回 False</td>
		</tr>
	</table>

	a = 10
	b = 20

	if ( a and b ):
   		print "1 - 变量 a 和 b 都为 true"
	else:
   		print "1 - 变量 a 和 b 有一个不为 true"

	if ( a or b ):
   		print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
	else:
  		print "2 - 变量 a 和 b 都不为 true"

	# 修改变量 a 的值
	a = 0
	if ( a and b ):
   		print "3 - 变量 a 和 b 都为 true"
	else:
   		print "3 - 变量 a 和 b 有一个不为 true"

	if ( a or b ):
   		print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
	else:
   		print "4 - 变量 a 和 b 都不为 true"

	if not( a and b ):
   		print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
	else:
   		print "5 - 变量 a 和 b 都为 true"
   		
Python 成员运算符

除了以上一些运算符之外，Python 还支持成员运算符：

<table align="center">
		<tr>
			<th>运算符</th>
			<th>描述</th>
			<th>实例</th>
		</tr>
		<tr>
			<td align="center">in</td>
			<td>如果在指定的序列中找到值返回 True，否则返回 False。</td>
			<td>x 在 y 序列中 , 如果 x 在 y 序列中返回 True。</td>
		</tr>
		<tr>
			<td align="center">not in</td>
			<td>如果在指定的序列中没有找到值返回 True，否则返回 False。</td>
			<td>x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。</td>
		</tr>
	</table>
	
	a = 10
	b = 20
	list = [1, 2, 3, 4, 5 ];

	if ( a in list ):
   		print "1 - 变量 a 在给定的列表中 list 中"
	else:
   		print "1 - 变量 a 不在给定的列表中 list 中"

	if ( b not in list ):
   		print "2 - 变量 b 不在给定的列表中 list 中"
	else:
   		print "2 - 变量 b 在给定的列表中 list 中"

	# 修改变量 a 的值
	a = 2
	if ( a in list ):
   		print "3 - 变量 a 在给定的列表中 list 中"
	else:
  		print "3 - 变量 a 不在给定的列表中 list 中"
	
Python 身份运算符

身份运算符用于比较两个对象的存储单元。

<table align="center">
		<tr>
			<th>运算符</th>
			<th>描述</th>
			<th>实例</th>
		</tr>
		<tr>
			<td align="center">is</td>
			<td>is是判断两个标识符是不是引用自一个对象</td>
			<td>x is y, 如果 id(x) 等于 id(y) , is 返回结果 1</td>
		</tr>
		<tr>
			<td align="center">is not</td>
			<td>is not是判断两个标识符是不是引用自不同对象</td>
			<td>x is not y, 如果 id(x) 不等于 id(y). is not 返回结果 1</td>
		</tr>
	</table>
	
	a = 20
	b = 20

	if ( a is b ):
   		print "1 - a 和 b 有相同的标识"
	else:
   		print "1 - a 和 b 没有相同的标识"

	if ( id(a) is not id(b) ):
   		print "2 - a 和 b 有相同的标识"
	else:
   		print "2 - a 和 b 没有相同的标识"

	# 修改变量 b 的值
	b = 30
	if ( a is b ):
   		print "3 - a 和 b 有相同的标识"
	else:
   		print "3 - a 和 b 没有相同的标识"

	if ( a is not b ):
   		print "4 - a 和 b 没有相同的标识"
	else:
   		print "4 - a 和 b 有相同的标识"
   		
***这里只是列举了部分运算符，例如比较运算符、赋值运算符、位运算符等与其他语言基本相同，故没做解释。***

### 2.3 Python 条件语句

Python 程序语言指定任何非0和非空（null）值为true，0或者null为false。

Python 中if条件语句基本形式为：

```
if 判断条件:
	执行语句...
else:
	执行语句...
```

其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句，具体例子如下：

```
flag = False
name = 'luren'
if name == 'python':        # 判断变量否为'python'
    flag = True          	 # 条件成立时设置标志为真
    print 'welcome boss'    # 并输出欢迎信息
else:
    print name              # 条件不成立时输出变量名称
```

if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系。当判断条件为多个值时，可以使用以下形式：

```
if 判断条件1:
	执行语句1...
elif 判断条件2:
	执行语句2...
elif 判断条件3:
	执行语句3...
else:
	执行语句4...
```

示例如下：

```
num = 5     
if num == 3:            # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出
```

***由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。***

### 2.4 Python 循环语句

Python 提供了for循环和while循环，**<font color=red>但是在Python中没有do..while循环。</font>**

Python 的while循环基本形式为：

```
while 循环条件:
	执行语句...
```

示例如下：

```
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"
```

Python 的for循环基本形式为：

```
for interating_var in sequence:
	statements(s)
```

示例如下：

```
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit
 
print "Good bye!"
```

### 2.5 Python 函数

Python 定义一个函数的简单规则：

* 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
* 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
* 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
* 函数内容以冒号起始，并且缩进。
* return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

基本形式为：

```
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

示例如下：

```
# 定义函数
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;
 
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
```

### 2.6 Python 面向对象

Python 从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。

**创建类**

使用class语句来创建一个新类，class之后为类的名称并以冒号结尾，基本形式如下:

```
class ClassName:
   '类的帮助信息' #类文档字符串
   class_suite  #类体
```

类的帮助信息可以通过ClassName.__doc__查看。

class_suite 由类成员，方法，数据属性组成。

示例如下：

```
class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
```

* empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问；
* 第一个方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法；
* self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数；

***<font color=red>类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。</font>***

**创建实例对象**

要创建一个类的实例，你可以使用类的名称，并通过__init__方法接受参数。示例如下：

```
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
```

**访问属性**

您可以使用点(.)来访问对象的属性。使用如下类的名称访问类变量:

```
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
```

你可以添加，删除，修改类的属性，如下所示：

```
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性
```

你也可以使用以下函数的方式来访问属性：

* getattr(obj, name[, default]) : 访问对象的属性。
* hasattr(obj,name) : 检查是否存在一个属性。
* setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
* delattr(obj, name) : 删除属性。

```
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(empl, 'age')    # 删除属性 'age'
```

**Python 内置类属性**

* __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
* __doc__ :类的文档字符串
* __name__: 类名
* __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
* __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

**类的继承**

派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，基本形式如下：

```
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
```

```
class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print "调用父类构造函数"

   def parentMethod(self):
      print '调用父类方法'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "父类属性 :", Parent.parentAttr

class Child(Parent): # 定义子类
   def __init__(self):
      print "调用子类构造方法"

   def childMethod(self):
      print '调用子类方法 child method'

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法
```

**私有属性与方法**

类的私有属性：

\_\_private\_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.\_\_private\_attrs。

类的私有方法:

\_\_private\_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.\_\_private\_methods

示例如下：

```
class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter.__secretCount  # 报错，实例不能访问私有变量
```

## 3. OC 调用 Python 函数

鉴于 Python 的优势所在，而我们又主要以OC开发为主，故这里简单介绍一下OC与Python的交互实现方式。***需要声明的是：由于iOS系统暂时并没有引入Python库所以本次交互实现只针对Mac OS系统。***


### 3.1 项目配置

新建好一个Mac OS的项目之后，需要添加依赖库，即Python.framework，如下图：

<center> ![share_lib](http://onmw6wg88.bkt.clouddn.com/share_lib.png) </center>

为了能够更好的管理项目，同时，采用面向对象的思维方式，我们新建一个继承自NSObject的类，专门负责做与 Python 交互相关的事情。那么有了这么一个类就能够与 Python 联系上了，但是为了我们金字塔顶层调用的方便，我们选择创建一个管理类来管理这个负责与 Python 交互的类。当然，这里的两个类都是采用单例模式的设计，创建完成后项目结构如下图：

![share_class](http://onmw6wg88.bkt.clouddn.com/share_class.png)

### 3.2 通过 OC 初始化 Python

在 [Python 官网](https://docs.python.org/2/c-api/index.html) 我们可以看到其实官方是给出了 Python 与 C 语言的API，这里的函数相当之多，后面会说到一些我们使用到的相关函数，那么我也是简单阅读了之后，关于在 OC 中初始化 Python 总结了以下步骤：

> 1、设置 Python 环境变量。这里我们要用的实际上就是设置我们编写的 Python 文件所在的路径；
> 
> 2、设置 Python 解释器的启动路径。可以在终端使用命令：where python 查看电脑上 Python 解释器的路径；
> 
> 3、系统初始化。直接调用系统初始化函数即可；
> 
> 4、设置参数。需要时设置，不需要时可以不做这一步，但是需要注意的是：***<font color=red>这一步必须在系统初始化之后执行；</font>***
> 
> 5、OC 模块初始化。因为是 OC 与 Python 交互，所以不仅要采用 OC 的方式去初始化 Python，也要用 Python 的方式去初始化一个 OC 模块，用于建立两者之间的联系；
> 
> 6、导入 Python 模块。Python 中一个模块即是指一个文件，这里就是调用函数导入一个 Python 文件中的所有方法，类似于 Python 中的 from module import *；
> 
> 7、调用运行简单文件函数。这里是为了检测 Python 环境是否初始化成功；
> 
> 8、完成初始化。直接调用系统完成初始化函数；
> 

**下面对关键步骤及容易出错的地方做解释说明：**

1、设置 Python 环境变量。这里涉及到一个函数的调用，函数原型如下：

　　**int setenv(const char * name,const char * value,int overwrite);**
　　
　　<table align="center">
		<tr>
			<th>参数名称</th>
			<th>描述</th>
		</tr>
		<tr>
			<td align="center">name</td>
			<td>要设置的环境变量名称</td>
		</tr>
		<tr>
			<td align="center">value</td>
			<td>变量内容</td>
		</tr>
		<tr>
			<td align="center">overwrite</td>
			<td>决定是否要改变已存在的环境变量。如果此环境变量不存在则无论overwrite为何值均添加此环境变量，如果此环境变量存在，则当overwrite不为0时，原内容会被改为参数value所指的变量内容；否则参数value会被忽略。</td>
		</tr>
		<tr>
			<th>返回值</th>
			<th>描述</th>
		</tr>
		<tr>
			<td align="center">int</td>
			<td>执行成功则返回0，有错误发生时返回-1。</td>
		</tr>
	</table>
	
　　这个函数的功能主要是指定我们写的 Python 文件所在的位置，让 Python 解释器能够找得到。

2、OC模块初始化。这个模块初始化可以理解成向 Python 声明一个Module，同时注册了一些方法，当在 Python 中调用到这些方法的时候会反射到 OC 中去执行。具体初始化方法如下：

```
/**
 模块初始化,即是在第一次使用import语句导入模块时会执行
 这是 Python 2.x 的写法：
    函数名必须为initmodule_name这样的格式,例如我们的module名为oc_python_module,所以函数名就是initoc_python_module.
 */
PyMODINIT_FUNC
initoc_python_module(void)
{
    Py_InitModule("oc_python_module", oc_python_module_methods);
}
```

　　这里用到了一个 Python 提供的初始化模块的函数，该函数原型如下：

　　**PyObject* Py_InitModule(char *name, PyMethodDef *methods);**
　　
　　<table align="center">
		<tr>
			<th>参数名称</th>
			<th>描述</th>
		</tr>
		<tr>
			<td align="center">name</td>
			<td>模块名称</td>
		</tr>
		<tr>
			<td align="center">methods</td>
			<td>PyMethodDef * 定义的一个函数列表，也就是上文提到的向 Python 注册的供 Python 调用时反射到 OC 中执行的方法列表，具体定义方法详见下文。</td>
		</tr>
		<tr>
			<th>返回值</th>
			<th>描述</th>
		</tr>
		<tr>
			<td align="center">PyObject*</td>
			<td>Python 模块对象</td>
		</tr>
	</table>
	
　　PyMethodDef* 定义函数列表的方式如下：

```
/**
 声明该模块具有哪些方法,即在Python中执行到这些函数时都会回调这里对应的方法
 PyMethodDef结构体有四个字段:
 第一个是一个字符串，表示在 Python 中对应的方法的名称；
 第二个是对应的 OC 代码的方法名称；
 第三个是一个标识位，表示该 Python 方法是否需要参数，METH_NOARGS表示不需要参数，METH_VARARGS表示需要参数；
 第四个是一个字符串，它是该方法的__doc__属性，这个不是必须的，可以为NULL。
 */
static PyMethodDef oc_python_module_methods[] = {
    {"myLog", myLog, METH_VARARGS, NULL},
    {"myAlert", myAlert, METH_NOARGS, NULL}
};
```

　　实现 OC 方法的方式如下：

```
/**
 打印日志

 @param self 模块对象
 @param args 参数
 @return PyObject对象
 */
static PyObject *myLog(PyObject *self, PyObject *args)
{
    const char *command;
    if (!PyArg_ParseTuple(args, "z", &command))
    {
        return NULL;
    }
    
    NSString *pyStr = [NSString stringWithUTF8String:command];
    NSLog(@"%@", pyStr);
    
    Py_IncRef(Py_None);
    return Py_None;
}
```

　　这里用到了一个分析方法参数的函数，其函数原型如下：

　　**int PyArg_ParseTuple(PyObject *args, const char *format, ...)**
　　
　　<table align="center">
		<tr>
			<th>参数名称</th>
			<th>描述</th>
		</tr>
		<tr>
			<td align="center">args</td>
			<td>一个 PyObject* 类型的参数</td>
		</tr>
		<tr>
			<td align="center">format</td>
			<td>解析结果格式化参数。具体格式可以参考 [Pyhtho 与其他语言结合的参数转换函数说明](http://www.cnblogs.com/DxSoft/archive/2011/04/01/2002676.html)</td>
		</tr>
		<tr>
			<th>返回值</th>
			<th>描述</th>
		</tr>
		<tr>
			<td align="center">int</td>
			<td>解析成功返回true，否则返回false并抛出相关异常信息</td>
		</tr>
	</table>

> 模块初始化的时候还有 Python 3.x 的写法与上述方法稍有不同，这里不作详细说明，初始化示例如下：
> 

```
/**
 模块初始化,即是在第一次使用import语句导入模块时会执行
 这是 Python 3.x 的写法：
    函数名必须为PyInit_module_name这样的格式,例如我们的module名为oc_python_module,所以函数名就是PyInit_oc_python_module.
 */
PyMODINIT_FUNC
PyInit_oc_python_module(void)
{
    return PyModule_Create(&oc_python_module);
}
```

### 3.3 通过 OC 调用 Python

经过上述一系列配置与初始化，OC 与 Python交互的基本条件就已经有了，下面介绍一下在 OC 中调用 Python 的基本流程。

> 1、初始化 Python 解释器；
> 
> 2、初始化 OC 模块；
> 
> 3、加载 Python 文件、模块以及模块中的相关函数；
> 
> 4、判断并执行相关函数；
> 
> 5、释放对象、完成解释器；
> 
> 6、结果处理；
> 

示例代码如下：

```
/**
 OC 调用 Python

 @param funcKey 函数名称
 @param args 函数参数
 @return 返回值
 */
- (NSString *)pyCallWithFunctionKey:(NSString *)funcKey Args:(NSString *)args
{
    PyObject *pName, *pModule, *pFunc, *pValue = NULL, *pResult=NULL;
    //初始化Python解释器
    Py_Initialize();
    
    //模块初始化
    initoc_python_module();
    
    //获取内置在Python的名称对象
    pName = PyString_FromString((char *)"Functions");
    
    //加载模块对象
    pModule = PyImport_Import(pName);
    
    //获取模块中的函数
    pFunc = PyObject_GetAttrString(pModule, [funcKey UTF8String]);
    
    //判断能否被执行
    if (PyCallable_Check(pFunc))
    {
        if (args.length > 0) {
            //设置函数参数
            pValue = Py_BuildValue("(z)", [args UTF8String]);
            PyErr_Print();
            
            //调用函数
            pResult = PyObject_CallObject(pFunc, pValue);
            PyErr_Print();
        }
        else
        {
            pResult = PyObject_CallObject(pFunc, NULL);
            PyErr_Print();
        }
    }
    else
    {
        PyErr_Print();
    }
    
    //释放对象
    if (pValue)
    {
        Py_DECREF(pValue);
    }
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
    Py_DECREF(pName);
    
    //Python解释器完成
    Py_Finalize();
    
    //结果处理
    if (PyString_Check(pResult))
    {
        //如果是PyString就转成NSString返回
        return [NSString stringWithUTF8String:PyString_AsString(pResult)];
    }
    else if (PyInt_Check(pResult))
    {
        //否则就认为是Pyint转成long之后再转为NSString返回
        return [NSString stringWithFormat:@"%ld", PyInt_AsLong(pResult)];
    }
    else
    {
        NSDictionary *paramsDic = @{@"success":@"yes", @"msg":@"Python return value type unknown."};
        NSError *dataError = nil;
        NSData *data = [NSJSONSerialization dataWithJSONObject:paramsDic options:NSJSONWritingPrettyPrinted error:&dataError];
        NSString *paramsStr = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
        return paramsStr;
    }
}
```

到此为止，OC 中负责与 Python 交互的这个类就已经完成了，接下来只要编写好我们的 Python 脚本代码就可以通过上述方式去调用了。

## 4. Python 调用 OC 方法

在 Python 中去调用 OC 的方法非常简单，只需要两步即可：

* 导入 OC 中定义的 Python 交互模块***（注意模块名称）；***
* 使用 Module.func 的方式来调用 OC 的方法***（注意方法名和参数必须正确）；***

1、导入模块

　　这里类似于 OC 中导入头文件一样，具体形式为：

　　**import Module_Name**

　　示例代码如下:

```
import oc_python_module  #这里的模块名称一定要跟 OC 中初始化的模块名称一致
```

2、调用 OC 方法

　　调用 OC 方法时跟 Python 正常调用函数的形式一样，实际上，上述导入的模块就可以理解为一个 Python 模块是一样的，所以把它当成标准的 Python 模块来用就好了。示例代码如下：

```
# Python Call OC
def python_OCLog(self):
	return oc_python_module.myLog("I'm from Python.")

# Python Call OC
def python_OCAlert(self):
	return oc_python_module.myAlert()
```

> 在上述示例代码中，当调用到oc_python_module这个模块的myLog和myAler方法时就会自动反射到我们的 OC 代码中去执行我们提前声明好的方法。
> 

## 5. 结果展示

**在经过上面一番设置与代码编写之后，我们就可以看到 OC 与 Python 交互的结果了，下面请看 Demo 演示。**


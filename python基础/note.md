# python基础

## Anaconda



## for循环

```python
#增强for循环
example_list=[1,2,3,4,5,6,7,8,9]
for i in example_list:
    print(i)
```

```python
#range
for i in range(10):
    print(i)
    
for i in range(0,10):
    print(i)
    
```

## 函数

```python
def
```

## 局部变量和全局变量

python允许在函数中设置全局变量

`global`标记的变量不能赋初值

```python
apple=100
#函数外部定义的是全局变量
def func():
    #在函数内部也可以定义全局变量，global保留字
    global a 
    a=10
    return a+100
apple=func()
print(apple)
print(a)

#110
#10
```

## 读写文件

### 写文件

open()参数表示允许进行的操作

`w`:写覆盖

`a`:继续写

```python
text='dasjdas'
my_file=open('./readme.txt','w')
my_file.write(text)
my_file.close()
```

### 读文件

```python
file=open('./readme.txt','r',encoding='UTF-8')
contents=file.readlines()
print(contents)
```

## 类

```python
class Calculator:
    name='Good calculator'
    price=18
    # 类中定义的方法需要将自己作为参数传递
    def _init_(self,name,price,hight,width):
        self.name=name
        self.price=price
        self.hight=hight
    def add(self, x,y):
        print(self.name)
        result=x+y
        print(result)
    def sub(self, x,y):
        print(self.name)
        result=x-y
        print(result)

c=Calculator()
print(c.name)
print(c.price)
c.add(1,2)
c.sub(3,2)
```

`_init_`功能相当于构造函数

## 输入

```python
a=input()
b=int(input())
```

## 元组



## 列表



## 字典



## 包机制

### import

```python
#直接import
import time
print(time.localtime())
```

```python
#import xxx as xx
import time as t
print(t.localtime())
```

```python
#from xxx import xxx
from time import time,localtime
from time import *
print(localtime())
print(time())
```

### 自己的模块

**1、使用同一目录下的模块**




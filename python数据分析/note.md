

# Python数据分析

## Numpy

### 数据类型

### 数组属性

#### 秩

`ndarrary.ndim`:数组的秩，可以理解为维度数量，中括号的深度

return `int`

```python
import numpy as np
a=np.arange(24);
print(a)
b=a.reshape(2,3,4)
print(b)
#a的秩
print('a的秩为'+str(a.ndim))
#b的秩
print('b的秩为'+str(b.ndim))

'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
a的秩为1
b的秩为3
'''
```

#### 维度

`ndarrary.shape`:数组维度，返回一个元组，元组长度为维数

返回值： `tuple[int,...]`

```python
print(a.shape)
print(b.shape)

'''
(24,)
(2, 3, 4)
'''
```

允许直接调整`shape`属性来调整数组的维度

```python
a = np.array([[1,2,3],[4,5,6]]) 
a.shape =  (3,2)  
print (a)

'''
[[1 2]
 [3 4]
 [5 6]]
'''
```

`ndarrary.reshape()` 

返回值：`ndarrary`

同样可以调用该方法来改变数组的维度

==注意==：`reshape`通常返回非拷贝副本



```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(2,3,1)
print(b)

'''
[[[1]
  [2]
  [3]]

 [[4]
  [5]
  [6]]]
'''
```

#### 单位大小

`ndarrary.itemsize`：返回数组中单个元素的字节数

返回值：`int`

```python
a=np.array([1,2,3],dtype=np.int64)
print(a.itemsize)
b=np.array([1,2,3],dtype=np.float16)
print(b.itemsize)

'''
8
2
'''
```

#### 内存信息

`ndarrary.flags`:返回ndarrary的内存信息

| 属性             | 描述                                                         |
| :--------------- | ------------------------------------------------------------ |
| C_CONTIGUOUS (C) | 数据是在一个单一的C风格的连续段中                            |
| F_CONTIGUOUS (F) | 数据是在一个单一的Fortran风格的连续段中                      |
| OWNDATA (O)      | 数组拥有它所使用的内存或从另一个对象中借用它                 |
| WRITEABLE (W)    | 数据区域可以被写入，将该值设置为 False，则数据为只读         |
| ALIGNED (A)      | 数据和所有元素都适当地对齐到硬件上                           |
| UPDATEIFCOPY (U) | 这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新 |

```python
a=np.array([1,2,3],dtype=np.int64)
print(a.flags)

'''
 C_CONTIGUOUS : True
  F_CONTIGUOUS : True
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False
'''
```

### 创建数组

#### ndarrary构造器

#### 特殊方法创建

`numpy.empty(shape,dtype,order)`

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| shape | 数组形状                                                     |
| dtype | 数据类型，可选                                               |
| order | 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

数组元素未初始化，为随机值

```python
import numpy as np
a=np.empty([3,3],dtype=np.int32)
print(a)

'''
[[7536727 6225970 3276851]
 [7340115 7209065 7274563]
 [7209077     116 6488161]]
'''
```

`numpy.zeros(shape,dtype,order)`

生成单位元素全为0的数组

`numpy.ones(shape,dtype,order)`

生成单位元素全为1的数组

```python
a=np.zeros((3,3),dtype=np.int16)
print(a)
b=np.ones((3,3),dtype=np.int16)
print(b)

'''
[[0 0 0]
 [0 0 0]
 [0 0 0]]
[[1 1 1]
 [1 1 1]
 [1 1 1]]
'''
```

`numpy.random.random(shape)`

单位元素为0~1的随机数

```python
a=np.random.random((3,4))
print(a)

'''
[[0.47888442 0.12357127 0.02905793 0.22678333]
 [0.37318862 0.50214953 0.71957351 0.18123715]
 [0.54800823 0.1786296  0.60228272 0.62622128]]
'''
```



#### 数值范围创建

`numpy.arange(start,stop,step,dtype)`

生成一维数组，==列向量==

```python
a=np.arange(1,10,2)
print(a)

'''
[1 3 5 7 9]
'''
```

`numpy.linspace(start,stop,num,endpoint,retstep,dtype)`

创建一个一维数组，是一个等差数列

| 参数       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| `num`      | 要生成的等步长的样本数量，默认为`50`                         |
| `endpoint` | 该值为 `true` 时，数列中包含`stop`值，反之不包含，默认是True。 |
| `retstep`  | 如果为 True 时，生成的数组中会显示间距，反之不显示。         |

```python
a=np.linspace(0,10,21,dtype=np.float64)
print(a)

'''
[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4.   4.5  5.   5.5  6.   6.5
  7.   7.5  8.   8.5  9.   9.5 10. ]
'''
```

`numpy.logspace(start,stop,num,endpoint,base,dtype)`

| 参数    | 描述                      |
| ------- | ------------------------- |
| `start` | 序列起始值为`base**start` |
| `stop`  | 序列结束值为`base**stop`  |
| `base`  | 对数log的底数             |

#### 从已有的数组创建数组

### 基础运算

#### 算术运算

`+`:维度相同的数组

`-`:维度相同的数组

`*`:整形或者维度相同的数组

`\`:整形或者维度相同的数组

```python
a=np.array([10,20,40,100])
b=np.array([2,3,4,5])
print(a+b)
print(a-b)
print(a*2)
print(a*b)
```

#### 矩阵运算

`numpy.dot(ndarray)`

矩阵乘法

```python
a=np.array([[1,3],
            [4,7]])
b=np.array([[2,3],
            [4,2]])
print(a.dot(b))

'''
[[14  9]
 [36 26]]
'''
```

#### 矩阵操作

#### 矩阵统计

#### 广播机制

### 矩阵迭代

### 切片索引

#### 单位索引

#### 高级索引

索引的返回值仍然是`ndarray`类型

```python
# 4*3的数组
x = np.array([[  0,  1,  2],
              [  3,  4,  5],
              [  6,  7,  8],
              [  9,  10,  11]])
#[0,1]为行索引
#[1,2]为行索引
y=x[[0,1],[1,2]]
print(y)
x_axis=np.array([[0,0],
                 [3,3]])
y_axis=np.array([[0,2],
                 [0,2]])
#此时x_axis为行索引,y_axis为列索引
y=x[x_axis,y_axis]
print(y)

'''
[1 5]
[[ 0  2]
 [ 9 11]]
'''
```



## Pandas

### Series

`pandas.Series(data,index,dtype,name,copy,fastpath)`

**Series类似于一维数组或列表，但具有索引，数据在处理和分析时更具灵活性**

- `data`：Series 的数据部分，可以是列表、数组、字典、标量值等。如果不提供此参数，则创建一个空的 Series。
- `index`：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `name`：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
- `copy`：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
- `fastpath`：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。

![img](https://www.runoob.com/wp-content/uploads/2023/12/628084-20201205212241597-1156923446.png)

```python
```

### DataFrame

## Matplotlib

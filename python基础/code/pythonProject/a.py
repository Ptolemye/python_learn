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


print(c.name)
print(c.price)
c.add(1,2)
c.sub(3,2)
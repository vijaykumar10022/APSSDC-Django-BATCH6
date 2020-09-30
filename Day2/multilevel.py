class A:
         def myfun1(self):
                  print(" i am from A Class")
class B(A):
         def myfun2(self):
                  print("i am from B class")
class C(B):
         def myfun3(self):
                  print("i am from C class")
class D(C):
         def myfun4(self):
                  print("i am from D class ")

obj=D()
obj.myfun1()
obj.myfun2()
obj.myfun3()
obj.myfun4()

class A:
         def fun1(self):
                  print("i am from fun1")
class B(A):
         def fun2(self):
                  print("i am from fun2")
                  
class C(A):
         def fun3(self):
                  print(" i am from fun3")
class D:
         def fun4(self):
                  print("i am from fun4")
class E(C,A,D):
         def fun5(self):
                  print(" i am from fun5")
                  

class A:
         # reverse of string
         def myfun1(self,name):
                  print(name[::-1])
class B:
         # char coutnt
         def myfun2(self,name):
                  print(len(name))
class C(A,B):
         # lower to uppercase
         def myfun3(self,name):
                  print(name.upper())
                  
obj=C()
obj.myfun1("vijay")#yajiv
obj.myfun2("vijay")#5
obj.myfun3("vijay")#VIJAY

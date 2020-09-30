# single level inheritance
class parent:
         myvar1="i variable from parent class"
         def myfun1(self):
                  print("i am method from parent class")
class child(parent):
         myvar2="i am varaible from child class"
         def myfun2(self):
                  print(" i am method2 from child class")
                  

obj=child()
print(obj.myvar1)
print(obj.myvar2)
obj.myfun1()
obj.myfun2()
         

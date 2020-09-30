class A:
         def mylen(self,name):
                  return len(name)
class B(A):
         def duplicates(self,l,name):
                  print(l,name)
                  # built logic here to find duplicates
                           #input:abcsavcs
                           #output:abcsv

class C(A):
         def charcount(self,l,name):
                  name=name[:le]
                  #built logic to find individual character count
                  # input:ababcabcdf
                  #output:a-->3
                               #b-->3
                               #c-->2
                               #d-->1
                               #f-->1
                  print(l,name)

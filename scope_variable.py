def function():
     print(c)#1 #not local variable
if __name__=="__main__":
     a=9
     c=0
     function()#2
     print(a)  



a=6
def function():
    a=7
    print(a)#3
if __name__=="__main__":
    print(a)#1
    function()
    print(a)#4
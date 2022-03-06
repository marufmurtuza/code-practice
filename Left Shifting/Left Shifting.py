source = [10,20,30,40,50,60]
n = 3
   
def shiftLeft(source,n):
    sliced_value = source[n:] 

    for i in range(len(source)-len(sliced_value)):
        sliced_value.append(0)
      
    print(sliced_value)
    
    
shiftLeft(source,n)
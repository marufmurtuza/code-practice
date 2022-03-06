source = [10,20,30,40,50,0,0]
n = 2 
   
def remove(source, size, n):
    element = source[n] 

    source.remove(element) 
    source.append(0) 
    
    print(source) 
    
remove(source, 7, n)
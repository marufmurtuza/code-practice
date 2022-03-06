source = [10,20,30,40,50,60]
n = 3
   
def roateLeft(source,n): 
    
      
    for i in range(0, n):  
          
        first = source[0]  
          
        for j in range(0, len(source)-1):  
              
            source[j] = source[j+1]  
              
          
        source[len(source)-1] = first;  
    print(source)


roateLeft(source,n)
source = [10,2,30,2,50,2,2,0,0]

value = 2 # value to be removed

def removeAll(source, size, n):
    count = 0 
    try:
        while True:
            source.remove(n) 
            count += 1
            
    except ValueError:
        pass 
    
    for i in range(count):
        source.append(0) 
        
    print(source)
    

removeAll(source, 9, value)
def arraySeries(n):
    array=[0]*(n*n)
    index=1
    while(index<=n):
        value=1
        value_index=(n*index)-1 #2,5,8
        while(value<=index): #divide by group of n
            array[value_index]=value
            value+=1
            value_index-=1
        index+=1
    return array
output=arraySeries(int(input()))
print(output)
def splittingArray(source):
    pointer=0
    pointer_one=1
    pointer_two=len(source)-1
    val=False
    while pointer_one<pointer_two:
        sum_one=0
        index=0
        while index<=pointer_one:
            sum_one+=source[index]
            index+=1
        sum_two=0
        index=pointer_one+1
        while index<=pointer_two:
            sum_two+=source[index]
            index+=1
        if sum_one==sum_two:
            val=True
            break
        pointer_one+=1
    if val:
        print("true")
    else:
        print("false")
        
source=  [10, 4,1, 1, 2, 10] 
splittingArray(source)
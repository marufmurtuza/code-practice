def repitation(source):
    index=0
    unique_list=[0]*len(source)
    repitation_counter=[0]*len(source)
    while index<len(source):
        check =source[index]
        pointer_one=0
        counter=0
        while pointer_one <len(source):
            if source[pointer_one]==check:
                counter+=1
                pointer_one+=1
            else:
                pointer_one+=1
        val=False
        i=0
        while i<len(source):
            if unique_list[i]==check:
                val=True
                break
            i+=1
        index+=1   
        if val:
            continue
        else:
            unique_list[index-1]=check
            if counter >1:
                repitation_counter[index-1]=counter
            else:
                repitation_counter[index-1]=0
                
    ##check repitation array same time of repitation or not
    index_of_check=0
    val=False
    while index_of_check<len(repitation_counter):
        checker=repitation_counter[index_of_check]
        index_of_match=0
        counter=0
        index_of_check+=1
        while index_of_match<len(repitation_counter):
            if repitation_counter[index_of_match] ==checker and checker!=0:
                counter+=1
            index_of_match+=1
        if counter>1:
            val=True
            break
    if val:
        return("true")
    else:
        return("false")
result=repitation([3,4,6,3,4,7,4,6,8,6,6])
print(result)

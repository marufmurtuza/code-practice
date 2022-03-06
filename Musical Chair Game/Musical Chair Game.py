import random 
def musicalChair(source):
    index=0
    ran=0
    while ran!=1:
        ran=random.randint(0, 3) 
        if ran==1:
            index=len(source)//2
            temp=[0]*(len(source)-1)
        else:
            temp=source[len(source)-1] 
            index=len(source)-1
            pointer=0
            while(index>pointer):
                source[index]=source[index-1] 
                index-=1
            source[0]=temp 
        print("Rotate",source)
    pointer_one=0
    idx=0
    while pointer_one< len(source):
        
        if pointer_one!=index:
            temp[idx]=source[pointer_one]
            idx+=1
        pointer_one+=1
    print("A person got Eliminated")
    print("Remaining Players:",temp)
    if len(temp)==1:
        print("\nCongratulation to our Winner: \n")
        print(temp[0])
    else:
        musicalChair(temp)
musicalChair(["Person1","Person2","Person3","Person4","Person5","Person6","Person7"])
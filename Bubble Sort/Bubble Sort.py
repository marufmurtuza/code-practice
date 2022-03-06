def bubbleSort(Arr):

    for i in range(len(Arr)-1):

        cnt = 0

        for j in range(len(Arr)-i-1):

            if(Arr[j] > Arr[j+1]):

                Arr[j+1], Arr[j] = Arr[j], Arr[j+1]

                cnt += 1

        if cnt == 0: break

read_inputs = open("input.txt", "r")

write_result = open("output.txt", "w")

lines = read_inputs.read().split("\n")

x = int(lines[0])

Arr = list(map(int, lines[1].split()))

bubbleSort(Arr)

result = ""

for i in range(len(Arr)): result += str(Arr[i])+" "

write_result.write(result)

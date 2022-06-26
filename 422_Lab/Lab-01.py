from math import inf

solution = 0

def BFS(x, y, vstd, Matrix, cost, rel, N, M):

    que = []

    que.append((x, y))

    vstd[x][y] = 1

    cost[x][y] = 0

    while(len(que) != 0):

        x, y = que[0][0], que[0][1]

        que.pop(0)

        for l in rel:

            u = x+l[0]

            v = y+l[1]

            if(u < 0 or u >= N or v < 0 or v >= M or Matrix[u][v] == -1 or Matrix[u][v] == 1):continue

            if(not vstd[u][v] and not Matrix[u][v]):

                que.append((u, v))

                vstd[u][v] = 1

                cost[u][v] = min(cost[u][v], cost[x][y]+1)

def DFS(x, y, co, vstd, Matrix, rel, N, M):

    global solution

    vstd[x][y] = 1

    for l in rel:

        r = x+l[0]
        
        c = y+l[1]

        if(r >= 0 and r < N and c >= 0 and c < M and Matrix[r][c] and not vstd[r][c]):
          
            co += 1

            solution = max(solution, co)

            DFS(r, c, co, vstd, Matrix, rel, N, M)


def INFECTED_TRACKER():

    global solution

    solution = 0

    take_input = open("input1.txt", "r")

    write_output = open("output1.txt", "w")

    read_lines = take_input.read().split("\n")

    Matrix = []

    def conv(c): return 0 if c == 'N' else 1

    for line in read_lines:Matrix.append(list(map(conv, line.split())))

    N = len(Matrix)

    M = len(Matrix[0])

    vstd = [[0]*M for x in range(N)]

    rel = [(-1, -1), (0, -1), (1, -1),
            (-1, 0),         (1, 0),
            (-1, 1), (0, 1), (1, 1)]

    for x in range(N):

        for y in range(M):

            if(Matrix[x][y] and not vstd[x][y]):DFS(x, y, 1, vstd, Matrix, rel, N, M)

    write_output.write(str(solution))

    write_output.close()

    take_input.close()

def SURVIVOR_TRACKER():

    take_input = open("input2.txt", "r")

    write_output = open("output2.txt", "w")

    read_lines = take_input.read().split("\n")

    def conv(c): return -1 if c == 'T' else 1 if c == 'A' else 0

    N = int(read_lines[0])

    M = int(read_lines[1])

    Matrix = []

    for k in range(2, len(read_lines)): Matrix.append(list(map(conv, read_lines[k].split())))

    vstd = [[0]*M for x in range(N)]

    cost = [[inf]*M for x in range(N)]
    
    rel = [        (0, -1),
            (-1, 0),        (1, 0),
                    (0, 1)]

    for x in range(N):

        for y in range(M):

            if(not vstd[x][y] and Matrix[x][y] == 1):BFS(x, y, vstd, Matrix, cost, rel, N, M)

    t = 0

    s = 0

    for x in range(N):

        for y in range(M):

            if(cost[x][y] != inf):t = max(t, cost[x][y])

            if(not vstd[x][y] and not Matrix[x][y]):s += 1

    result = "Time: " +str(t)+ " Minutes\n"

    if(s == 0):result += "No one Survived"

    else:result += str(s)+" survived"

    write_output.write(result)


INFECTED_TRACKER()

SURVIVOR_TRACKER()

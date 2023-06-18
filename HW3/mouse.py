import random

my_mapx = 5
my_mapy = 10

my_map = []
road=[]
move= [[-1, 0], [1, 0], [0, -1], [0, 1]]
n_count=[0,0,0,0]
count=0
for i in range(my_mapx + 1):
    row = []
    for j in range(my_mapy + 1):
        row.append(random.choice(['0', '.']))
    my_map.append(row)

i = random.randint(0, my_mapx)
j = random.randint(0, my_mapy)
my_map[0][0] = 'S'
my_map[my_mapx][my_mapy]='.'

for x in range(my_mapx + 1):
    for y in range(my_mapy + 1):
        if my_map[x][y] == 'S':
            s_row = x
            s_col = y
inside=True
while inside:
    count=count+1
    for x in range(my_mapx + 1):
        for y in range(my_mapy + 1):
            if my_map[x][y] == 'S':
                s_row = x
                s_col = y
    for i in range(0,len(move)):
        if my_map[s_row][s_col]+move[i]=='.':
            n_count[i]=1
    for x in range(my_mapx + 1):
        for y in range(my_mapy + 1):
            for i in range(0,len(move)+1):
                if n_count[i]==1:
                    my_map[s_row][s_col]=count
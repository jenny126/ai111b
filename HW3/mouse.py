import random

my_mapx = 5
my_mapy = 10
roadx=[]
my_map = []
road=[]
# 前後左右
move= [[0, 1], [0, -1], [-1, 0], [1, 0]]
n_count=[0,0,0,0]
count=0
for i in range(my_mapx + 1):
    row = []
    for j in range(my_mapy + 1):
        row.append(random.choice(['0', '.']))
    my_map.append(row)

i = random.randint(0, my_mapx)
j = random.randint(0, my_mapy)
my_map[0][0] = 'M'
my_map[my_mapx][my_mapy]='.'

for x in range(my_mapx + 1):
    for y in range(my_mapy + 1):
        if my_map[x][y] == 'M':
            M_row = x
            M_col = y
inside=True

for x in range(0,my_mapx):
    for y in range(0,my_mapy):
        for i in range(0,len(move)):
            if my_map[M_row+move[i][0]][M_col+move[i][1]]=='.':
                n_count[i]=1
            roadx.append(n_count)
        road.append(roadx)
        roadx=[]
print(road)
"""
while inside:
    count=count+1
    for x in range(my_mapx + 1):
        for y in range(my_mapy + 1):
            if my_map[x][y] == 'M':
                M_row = x
                M_col = y
                now=[M_row,M_col]
#    for i in range(0,len(move)):
#        if my_map[M_row][M_col]+move[i]=='.':    
#            n_count[i]=1

    for x in range(my_mapx + 1):
        for y in range(my_mapy + 1):
            for i in range(0,len(move)):
                if n_count[i]==1:

                    my_map[M_row][M_col]="a"
                    my_map[M_row][M_col]=my_map[M_row+move[i][0]][M_col+move[i][1]]
                    my_map[M_row][M_col]="M"
"""
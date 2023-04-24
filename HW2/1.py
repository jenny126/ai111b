#import numpy as np
import random
xy = [(0,0), (1,0), (2,0), 
      (3,0), (3,1), (3,2), 
      (3,3), (2,3), (1,3), 
      (0,3), (0,2), (0,1)]
#sroad=[1,2,3,4,5,6,7,8,9,10,11,0]
froad=[0,1,2,3,4,5,6,7,8,9,10,11]

def distance(a,b): # 計算2點距離 
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    return (dx*dx+dy*dy)**0.5
def circle_length(s): # 計算環狀路徑長
    d = 0.0
    for i in range(len(s)):
        d += distance(xy[i], xy[s[i]])
    return d
# def neighborfind0(s): #隨機選一個交換相鄰鄰居
#     a = random.randrange(0, 11)#12會超出
#     s[a],s[a+1]=s[a+1],s[a]
#     return s
def neighborfind(s): #隨機選一個交換相鄰鄰居
    a = random.randrange(0, len(s))#12會超出
    if a==len(s)-1:
        s[a],s[0]=s[0],s[a]
    else:  
        s[a],s[a+1]=s[a+1],s[a]
    return s
def hillClimbing(s):
    max_loops=10000
    fails=0
    random.shuffle(s)
    print("shuffle:",s)
    print("初始距離:",circle_length(s))
    best=s.copy()
    #print(s)
    #print(best)
    while True:
        s2 = neighborfind(s)
        #print(s)
        #print(circle_length(s2))
        if circle_length(s2) < circle_length(best):
            best=s2.copy()
            #print(best)
            fails=0
        else:
            fails+=1
            #print(fails)
        if fails >= max_loops:
            break
    print("路徑:", best)
    print("路徑長度：", circle_length(best))
    return best

hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")
# hillClimbing(froad)
# print("-------------------")

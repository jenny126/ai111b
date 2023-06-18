import random
from collections import deque

rows = 10
columns = 10

def generateRandomMap(rows, columns):
    # 生成一個隨機地圖
    # 地圖以二維列表的形式表示，列表的每個元素代表一個格子
    # 在生成地圖時，有20%的機率生成VV，其餘80%的機率生成..
    map = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            if random.random() < 0.2:
                row.append('VV')
            else:
                row.append('..')
        map.append(row)
    return map

def formatStepNumber(step):
    # 格式化步數，如果步數小於10，則在前面加上0
    if step < 10:
        return '0' + str(step)
    else:
        return str(step)

def bfs(m, x, y):
    # 廣度優先搜索，用於尋找從起點到終點的路徑
    # m: 地圖
    # x, y: 當前位置的座標
    visited = set()  # 記錄已訪問的座標
    queue = deque([(x, y, 1)])  # 使用雙端隊列作為搜索的工具，同時記錄步數
    while queue:
        cur_x, cur_y, step = queue.popleft()
        if cur_x < 0 or cur_x >= len(m) or cur_y < 0 or cur_y >= len(m[0]):
            # 如果座標超出地圖範圍，繼續搜索下一個節點
            continue
        if (cur_x, cur_y) in visited:
            # 如果當前座標已經訪問過，繼續搜索下一個節點
            continue
        if m[cur_x][cur_y] == 'VV':
            # 如果遇到VV（障礙物），繼續搜索下一個節點
            continue
        m[cur_x][cur_y] = formatStepNumber(step)  # 將步數標記在當前位置上
        visited.add((cur_x, cur_y))  # 將當前座標標記為已訪問
        if cur_x == len(m) - 1 and cur_y == len(m[0]) - 1:
            # 如果已經到達終點，表示找到路徑，結束搜索
            return True
        # 將當前節點的相鄰節點加入隊列中
        queue.append((cur_x, cur_y + 1, step + 1))  # 向右移動
        queue.append((cur_x + 1, cur_y, step + 1))  # 向下移動
        queue.append((cur_x, cur_y - 1, step + 1))  # 向左移動
        queue.append((cur_x - 1, cur_y, step + 1))  # 向上移動
    return False

randomMap = generateRandomMap(rows, columns)  # 生成隨機地圖
if bfs(randomMap, 0, 0):
    # 如果找到路徑，印出地圖
    for row in randomMap:
        print(' '.join(row))
else:
    # 如果找不到路徑，印出地圖並顯示錯誤訊息
    for row in randomMap:
        print(' '.join(row))
    print("找不到路徑")

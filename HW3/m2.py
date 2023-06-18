import random

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

def dfs(m, x, y, step):
    # 深度優先搜索，用於尋找從起點到終點的路徑
    # m: 地圖
    # x, y: 當前位置的座標
    # step: 當前步數
    if x < 0 or x >= len(m) or y < 0 or y >= len(m[0]):
        # 如果座標超出地圖範圍，返回False
        return False
    if m[x][y] == 'VV':
        # 如果遇到VV（障礙物），返回False
        return False
    if m[x][y] != '..':
        # 如果當前位置不是..，表示已經訪問過，返回False
        return False
    m[x][y] = formatStepNumber(step)  # 將步數標記在當前位置上
    if x == len(m) - 1 and y == len(m[0]) - 1:
        # 如果已經到達終點，返回True，表示找到路徑
        return True
    # 嘗試向右、向下、向左、向上四個方向進行搜索
    if dfs(m, x, y + 1, step + 1):
        return True
    if dfs(m, x + 1, y, step + 1):
        return True
    if dfs(m, x, y - 1, step + 1):
        return True
    if dfs(m, x - 1, y, step + 1):
        return True
    m[x][y] = '..'  # 如果在該位置找不到路徑，將步數標記還原
    return False

randomMap = generateRandomMap(rows, columns)  # 生成隨機地圖
if dfs(randomMap, 0, 0, 1):
    # 如果找到路徑，印出地圖
    for row in randomMap:
        print(' '.join(row))
else:
    # 如果找不到路徑，印出地圖並顯示錯誤訊息
    for row in randomMap:
        print(' '.join(row))
    print("找不到路徑")

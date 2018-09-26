import heapq

h_list = []
# 来个乱序的二叉树
for i in [3, 5, 6, 8, 2, 4, 7, 1, 9]:
    heapq.heappush(h_list, i)  # 构建最小二叉堆

data = heapq.heappop(h_list)  # 弹出最小值
print(data)

import heapq

h_list = []
# 堆元素可以是元组，可以拓展优先级的概念
heapq.heappush(h_list, (9,"小明"))
heapq.heappush(h_list, (5,"小张"))
heapq.heappush(h_list, (7,"小周"))
heapq.heappush(h_list, (3,"小潘"))

data = heapq.heappop(h_list)  # 弹出优先级最低的
print(data)

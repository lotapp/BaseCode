# from web.json import get_json

# get_json()

# 或者
# import web.json as json

# json.get_json()

# import web.data as data

# data.get_data()

# ####################

# from web import *

# json.get_json()

# data.get_data()

# # 你这样调就不行了
# import web

# web.data.get_data()

# 同样的，你硬是要调，python也拿你没办法
import web.data as data

data.get_data()

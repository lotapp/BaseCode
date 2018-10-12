from modulefinder import ModuleFinder

# 有时候很多人导入直接用*，这时候就可以使用ModuleFinder来分析了
finder = ModuleFinder()
finder.run_script('模块名.py')

print('加载的模块:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))

print('-'*50)
print('未导入模块:')
print('\n'.join(finder.badmodules.keys()))

# https://docs.python.org/3.7/library/modulefinder.html
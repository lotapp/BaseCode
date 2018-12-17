from distutils.core import setup, Extension

mod_name = "dnt" # 模块名
setup(
    name=mod_name,
    ext_modules=[Extension(mod_name, sources=["dnt.c", "pack.c"])]
)
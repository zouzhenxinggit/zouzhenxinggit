一、发布模块
setup.py-------------------------------------->
from distutils.core import setup

setup(name="dongGe", version="1.0", description="dongGe's module", author="dongGe", py_modules=['suba.aa', 'suba.bb', 'subb.cc', 'subb.dd'])

构建模块
python setup.py build
生成发布压缩包
python setup.py sdist






二、模块安装、使用
1.安装的方式
解压压缩包
进入文件夹
执行命令python setup.py install

如果在install的时候，执行目录安装，可以使用python setup.py install --prefix=安装路径

模块的引入
在程序中，使用from import 即可完成对安装的模块使用

from 包名 import 模块名或者*






安装包的位置（可删除）
/usr/local/lib/python2.7/dist-packages
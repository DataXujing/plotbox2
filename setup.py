import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup



def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname),encoding='utf-8').read()

long_des = read("README.rst")
    
platforms = ['Windows']
classifiers = [
    'Development Status :: 3 - Alpha',
    'Topic :: Text Processing',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
]

install_requires = [
    "opencv-python",
    "pillow",
    "numpy"
]

    
setup(name='plotbox2',
      version='0.1.0',
      description='Plot Bounding Box in CV object detection.',
      long_description=long_des,
      py_modules=['plotbox2'],
      author = "DataXujing",  
      author_email = "274762204@qq.com" ,
      url = "https://github.com/DataXujing/plotbox2" ,
      license="Apache License, Version 2.0",
      platforms=platforms,
      classifiers=classifiers,
      install_requires=install_requires,
      # include_package_data=True,
      #  package_data={
      #   'plotbox': ['font/*.ttf'],
      #   'plotbox': ['font/*.TTF'],
      #   'plotbox': ['font/*.ttc'],}
      data_files=[
        ('Lib/site-packages/plotbox/font', ['font/AvantGarGotItcTEE.ttf']),
        ('Lib/site-packages/plotbox/font', ['font/Futura Lt BT.ttf']),
        ('Lib/site-packages/plotbox/font', ['font/HomeStoreRegular.ttf']),
        ('Lib/site-packages/plotbox/font', ['font/kaitiGB2312.ttf']),
        ('Lib/site-packages/plotbox/font', ['font/Microsoft-Yahei-UI-Light.ttc']),
        ('Lib/site-packages/plotbox/font', ['font/youyuan.TTF'])
               ]
      
      )   
      
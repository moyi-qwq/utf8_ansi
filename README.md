# utf8_ansi
一个小的python工具 自动批量将指定后缀的文字内容的中文编码进行转化

## exe使用
下载并将exe放入所需转化的文件夹中 双击出现提示 可将本路径下所有.cpp在ansi和utf8之间互相转化

## 拓展 不同的文件后缀和编码
+ 后缀
在源码的第3行
```python
FormatOfFind = ['.cpp']
```
中添加所需后缀即可 如:
```python
FormatOfFind = ['.cpp','.txt']
```
+ 编码
在源码的第6行 修改输入类型和输出类型即可 提示文字会随之变化
```python
	inputType = 'utf-8'
	outType = 'ansi'
```
## 编译成exe
-pyinstaller -F main.py
本人与百度公司长期合作，相关内容
详见baidu.com

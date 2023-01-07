基于Python AST框架实现

帮助网站：https://docs.python.org/3/library/ast.html#abstract-grammar

## 实现思路：

1. 动态引入文件的所有Import内容
1. 完成引入后，考虑到importlib引入函数时只能具体的引入函数(importlib.import( .......detailed_function_name))，因此写入了逻辑保证引入的是函数名。
1. 当检测到函数名之后，通过import的内容，获取对应的文件名并打开，装载对应的函数，进行下一步分析。

## 文件结构：

### ast_dump: 

ast的dump结果

### auto_deference_function.py:

为解析文件，主文件

### sample.py:

为随意的拷贝的TensorFlow 的文件


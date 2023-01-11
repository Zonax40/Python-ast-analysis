import shutil
import inspect
import sys
import getopt
import ast
import tensorflow 
import xmlrpc	
import zoneinfo
import urllib	
import abc	
import aifc	
import argparse	
import array	
import ast	
import asynchat
import asyncio
import asyncore	
import atexit
import audioop
import base64
import bdb
import binascii
import bisect
import builtins
import bz2
import calendar
import cgi
import cgitb
import chunk
import cmath
import cmd
import code
import codecs
import codeop
import collections
import colorsys
import compileall
import concurrent
import configparser
import contextlib
import contextvars
import copy
import copyreg
import cProfile
import crypt
import csv
import ctypes
import curses
import dataclasses
import datetime
import dbm
import decimal
import difflib
import dis
import distutils
import doctest
import email
import encodings
import enum
import errno
import faulthandler
import fcntl
import filecmp
import fileinput
import fnmatch
import fractions
import ftplib
import functools
import gc
import getopt
import getpass
import gettext
import glob
import graphlib
import grp
import gzip
import hashlib
import heapq
import hmac
import html
import http
import imaplib
import imghdr
import imp
import importlib
import inspect
import io
import ipaddress
import itertools
import json
import keyword
import lib2to3
import linecache
import locale
import logging
import lzma
import mailbox
import mailcap
import marshal
import math
import mimetypes
import mmap
import modulefinder
import multiprocessing
import netrc
import nis
import nntplib
import numbers
import operator
import optparse
import os
import ossaudiodev
import pathlib
import pdb
import pickle
import pickletools
import pipes
import pkgutil
import platform
import plistlib
import poplib
import posix
import pprint
import profile
import pstats
import pty
import pwd
import py_compile
import pyclbr
import pydoc
import queue
import quopri
import random
import re
import readline
import reprlib
import resource
import rlcompleter
import runpy
import sched
import secrets
import select
import selectors
import shelve
import shlex
import signal
import site
import smtpd
import smtplib
import sndhdr
import socket
import socketserver
import spwd
import sqlite3
import ssl
import stat
import statistics
import string
import stringprep
import struct
import subprocess
import sunau
import symtable
import sys
import sysconfig
import syslog
import tarfile
import telnetlib
import tempfile
import termios
import test
import textwrap
import threading
import time
import timeit
import token
import tokenize
import trace
import traceback
import tracemalloc
import tty
import types
import typing
import unicodedata
import unittest
import uuid
import uu
import venv
import warnings
import wave
import weakref
import webbrowser
import wsgiref
import xdrlib
import xml
import zipapp
import zipfile
import zipimport
import zlib



import collections
from typing import TypeVar


# global import's alias:
import_alias = {}
# global from's alias:
from_not_module_alias = {}
# global from's module alias:
from_module_alias = {}
# module dict:
modules = {}
global_call_type = ''
# 包括需要递归的函数
visit_stack = []
# judge if the function has been visited, if so return or exxplore x....x
# attention, the list contains the last method.
visited_function_list = []
raw_api_output = []

# 停止列表
stop_list = ["gen_array_ops", "gen_audio_ops", "gen_batch_ops", "gen_bitwise_ops", "gen_boosted_trees_ops", "gen_candidate_sampling_ops", "gen_collective_ops", "gen_composite_tensor_ops", "gen_control_flow_ops", "gen_count_ops","gen_ctc_ops",  "gen_cudnn_rnn_ops", "gen_data_flow_ops", "gen_dataset_ops", "gen_debug_ops", "gen_decode_proto_ops", "gen_encode_proto_ops", "gen_experimental_dataset_ops", "gen_functional_ops", "gen_image_ops", "gen_io_ops", "gen_linalg_ops", "gen_list_ops", "gen_logging_ops", "gen_lookup_ops", "gen_manip_ops", "gen_math_ops", "gen_nccl_ops", "gen_nn_ops", "gen_parsing_ops", "gen_ragged_array_ops", "gen_ragged_conversion_ops", "gen_ragged_math_ops", "gen_random_index_shuffle_ops", "gen_random_ops", "gen_resource_variable_ops", "gen_rnn_ops", "gen_script_ops", "gen_sdca_ops", "gen_sendrecv_ops", "gen_set_ops", "gen_sparse_ops", "gen_special_math_ops", "gen_spectral_ops", "gen_state_ops", "gen_stateful_random_ops", "gen_stateless_random_ops", "gen_stateless_random_ops_v2", "gen_string_ops", "gen_summary_ops", "gen_tpu_ops", "gen_tpu_partition_ops", "gen_training_ops", "gen_sparse_csr_matrix_ops", "gen_user_ops"]




# input: a tensorflow function sample
class Analyzer_former(ast.NodeVisitor):
    def visit_Call(self, node):
        # use to record the type of call type
        global_call_type = type(node)
        # attriute = node.func
        # method = ''
        # while True:
        #     # 首先判断是不是Call嵌套, just do cycle. 
        #     if type(attriute) == type(node):
        #         break
        #     try: # 读取Attribute的东西
        #         # 在这里首先判断是不是Attribute, 通过能否读取attribute.attr看出来
        #         last_method = attriute.attr
        #         method = '.' + last_method  + method
        #         attriute = attriute.value
        #         continue
        #     except: # 处理Name的情况，这里一定是会遍历的情况！
        #         try:
        #             last_method = attriute.id
        #             method = last_method + method
        #             break
        #         except:
        #             # 这里遇到了可能是常量的情况，不关心()
        #             # Error Maker
        #             break
        # if not method.startswith("."):
        #     final_method = method.split('.')[-1]
        #     visit_stack.append(final_method)

class Analyzer(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        # 首先判断自己位于检索队列中
        # print("Start FunctionDef")
        name = node.name
        # just jump
        if name not in visit_stack:
            # print("Finish FunctionDef")
            self.generic_visit(node)
            return
        body = node.body
        for element in body:
            try:
                # 这里就是用于判断是否为call,通过不断获取内容判断
                attriute = element.value.func
                # if sucessfully executing here, just means element is equal to Call
                method = ''
                while True:
                    # 首先判断是不是Call嵌套
                    if type(attriute) == type(global_call_type):
                        break
                    try: # 读取Attribute的东西
                        # 在这里首先判断是不是Attribute, 通过能否读取attribute.attr看出来
                        last_method = attriute.attr
                        method = '.' + last_method  + method
                        attriute = attriute.value
                        continue
                    except: # 处理Name的情况，这里一定是会遍历的情况！
                        try:
                            last_method = attriute.id
                            method = last_method + method
                            break
                        except:
                            # 这里遇到了可能是常量的情况，不关心()
                            # Error Maker
                            break
                # 获得method
                if not method.startswith("."):
                    last_method = method.split(".")[-1]
                    visit_stack.append(last_method)
                    # print(last_method+":"+method)
            except:
                pass
        # print("Finish FunctionDef")
        self.generic_visit(node)
    # used to deal with call
    def visit_Call(self, node):
        # debug
        # self.generic_visit(node)
        # return
        # Call(expr func, expr* args, keyword* keywords)
        # 如此处理，由于python对于函数的ast的划分是这样子的((a,b),c)，从这里可以看出性质！
        # A()的第一个参数为Name
        # A.B.C的第一个参数func一定是Attribute!, 最后一个为Name
        # Attribute(expr value, identifier attr, expr_context ctx)
        # Name(identifier id, expr_context ctx)
        # 获取函数名,需要完整
        # print("Start call")
        
        attriute = node.func
        method = ''
        while True:
            # 首先判断是不是Call嵌套
            if type(attriute) == type(node):
                break
            try: # 读取Attribute的东西
                # 在这里首先判断是不是Attribute, 通过能否读取attribute.attr看出来
                last_method = attriute.attr
                method = '.' + last_method  + method
                attriute = attriute.value
                continue
            except: # 处理Name的情况，这里一定是会遍历的情况！
                try:
                    last_method = attriute.id
                    method = last_method + method
                    break
                except:
                    # 这里遇到了可能是常量的情况，不关心()
                    # Error Maker
                    # print(method + ":")
                    break
        # print("Checker 1")
        # print(method)
        if not method.startswith("."):
            final_method = method.split('.')[-1]
            # print(method+":"+final_method)
            if final_method in visit_stack:
                pass
            else:
                # print("Finishing Call")
                # if(final_method == "reshape"):
                #     print(visit_stack)
                self.generic_visit(node)
                return
        # 在此获得了函数名
        # 使用inspect进行检索，优先 递归
        # 跳过一些空method，实际上就是call递归的情况
        # 有一些内联的，这些直接跳过
        # 使用另类做法处理: a.b.c
        # print(method)
        try:    
            if method:
                # 获取method的第一个元素
                # 总是正确工作
                # 首先检测是否到达底部
                for element in stop_list:
                    if method.find(element) >= 0 :
                        # print(method)
                        # print("Finishing Call")
                        if method not in raw_api_output:
                            raw_api_output.append(method)
                        self.generic_visit(node)
                        return
                first_method = method.split(".", 1)[0]
                # print(method)
                if not first_method:
                    # print("Finishing Call")
                    # print("skip:" + method)
                    self.generic_visit(node)
                    return
                complete_functions  = ''
                try:
                    _checker = method.split(".")[2]
                    # 暂时停止这一部分的内容
                    # 
                    _last_method = method.split(".")[-1]
                    # print("Chekcer")
                    record = ''
                    # 这里开始处理a.b.c诸如情况
                    # print(first_method)
                    if first_method in import_alias:
                        # 如此拼凑
                        complete_functions = import_alias[first_method][1] + '.' +method.split(".", 1)[1]
                        record = import_alias[first_method][1]
                        # print("chekcer:"+complete_functions)
                    elif first_method in from_not_module_alias:
                        # complete_functions = import_alias[first_method][1] + '.' +method.split(".", 1)[1]
                        # here, few possibility of excuting here
                        pass 
                    elif first_method in from_module_alias:
                        complete_functions = from_module_alias[first_method][1] + '.' +method.split(".", 1)[1]
                        record = import_alias[first_method][1]
                    else:
                        pass
                    # 这里对于的是对于类的，可以直接忽视
                    # sys.exit(-1)

                except:
                    pass
                # 判断是否在imort_alits和from_not_module_alias中
                # global from's module alias:
                # 判断是否在imort_alits和from_not_module_alias中 = {        if 
                # 开始判断在哪一个字典里
                # 
                
                new_file_path = "" 
                # here, attention must give a alias marker or error
                if_alias = 0
                module_name = ''
                # 检验位， checker
                tensorflow_path_checker = 1
                if first_method in import_alias:
                    new_file_path = inspect.getfile(import_alias[first_method][0])
                    # need to change the new_file_path
                    # print(new_file_path.endswith("__init__.py"))
                    # print(complete_functions)
                    if new_file_path.endswith("__init__.py"):
                        if complete_functions:
                            new_file_path = inspect.getfile(eval(complete_functions))
                            print("update new_file_path:"+complete_functions+":"+new_file_path)
                        else:
                            print("new file path errors:"+method+":"+first_method)
                            new_file_path = ""
                elif first_method in from_not_module_alias:
                    new_file_path = inspect.getfile(from_not_module_alias[first_method][0])
                    if_alias = from_not_module_alias[first_method][2]
                    module_name = from_not_module_alias[first_method][1]
                    if new_file_path.endswith("__init__.py"):
                        print("new path errors 2:" + method + ":" + first_method)
                        new_file_path = ""
                    # print(from_not_module_alias[first_method][1])
                elif first_method in from_module_alias:
                    new_file_path = inspect.getfile(from_module_alias[first_method][0])
                    if_alias = from_module_alias[first_method][2]
                    module_name = from_module_alias[first_method][1]
                    if new_file_path.endswith("__init__.py"):
                        print("new path errors 2:" + method + ":" + first_method)
                        new_file_path = ""
                else:
                    tensorflow_path_checker = 0 
                if new_file_path:
                    if "tensorflow" in new_file_path:
                        if tensorflow_path_checker == 0:
                            print("Error1"+ new_file_path)
                        # when excuting here, obviously, the process is going to explore the function
                        # first, check out if the function is visited
                        if not if_alias:
                            tmp_last_method = method.split(".")[-1]
                        else:
                            tmp_last_method = module_name.split(".")[-1]
                            # print(tmp_last_method)
                        # once visted, just jump
                        if tmp_last_method in visited_function_list:
                            # exit
                            self.generic_visit(node)
                            return
                        # no former visit, now time to deal
                        # add into visited_function_list:
                        visited_function_list.append(tmp_last_method) 
                        with open(new_file_path, "r") as f:
                            tree = ast.parse(f.read())
                            # string
                            parse_result = ast.dump(tree)
                            # print(parse_result)
                        # for less bug, first try to find the key words "FunctionDef"
                        # index used to recursively find the key word
                        # print("Entering new file:" + new_file_path)
                        index = 0
                        # if_located used to refer if successfully find the specific function
                        while True:
                            if_located = False
                            # here, update the index
                            # here, wrong handle way
                            search_result = parse_result[index:].find("FunctionDef(name='")
                            if search_result == -1:
                                # used to represent finished
                                break
                            # then check the name
                            if parse_result[search_result + index: search_result  + index + len("FunctionDef(name='") ] != "FunctionDef(name='":
                                # something goes wrong
                                print("In recursive, something goes wrong.")
                                print(parse_result[search_result + index: search_result  + index + len("FunctionDef(name='")])
                            # get the name
                            tmp = parse_result[search_result + index+ len("FunctionDef(name='"):].find("'")
                            # print(tmp)
                            # with successful repair
                            name = parse_result[search_result +index +len("FunctionDef(name='") : search_result +index +len("FunctionDef(name='") + tmp ]
                            # successfully validate
                            # compare the name 
                            # print(name+":"+tmp_last_method)
                            if name == tmp_last_method:
                                # print(name+":"+tmp_last_method)
                                # if the name matches, then store this parts, and then store this part into a file stored in /tmp
                                # first locate such pattern: FunctionDef(.......)
                                # use the simplest way to finish traversing
                                # when bracket_count goes to 0, then finish
                                bracket_count = 1
                                # temp_index is used to account the length of traversing length
                                # The actual index is search_result + leng("FunctionDef(" + temp_index)
                                temp_index = 0
                                for letter in parse_result[search_result + index + len("FunctionDef("):]:
                                    if letter == "(":
                                        bracket_count = bracket_count + 1
                                    elif letter == ")":
                                        bracket_count = bracket_count - 1
                                    # check out if it is time to finish
                                    if bracket_count == 0:
                                        # if_located works 
                                        if_located = True
                                        break
                                    temp_index = temp_index + 1
                                # now get the successful substring, it is time.
                                
                                if if_located:
                                    # if_located is true, means find the defination of the function , recording the inner called functions
                                    check_string = parse_result[search_result + index+ len("FunctionDef"):search_result+index + len("FunctionDef(")+temp_index+1]
                                    # print("+++"+check_string)
                                    # now it is time to deal with the call function
                                    # here is the furthur trace of the function, obtain the contained function and just add it to visit_stack
                                    # similarity, deal with the string result 
                                    new_index = 0
                                    while True:
                                        temp_search_result = check_string[new_index:].find("Call(func=")
                                        if temp_search_result == -1:
                                            break
                                        # to make the program more stable use some fool methods
                                        bracket_count = 1
                                        # temp_index is used to account the length of traversing length
                                        temp_index = 0
                                        for letter in check_string[temp_search_result + new_index + len("Call(func="):]:
                                            if letter == "(":
                                                bracket_count = bracket_count + 1
                                            elif letter == ")":
                                                bracket_count = bracket_count - 1
                                            # check out if it is time to finish
                                            if bracket_count == 0:
                                                # if_located works 
                                                break
                                            temp_index = temp_index + 1
                                        # call_string validate, it is complete
                                        call_string = check_string[temp_search_result+new_index:temp_search_result+new_index+temp_index+len("Call(func=")+1]
                                        # first, check out the first few characters if they are Call(func=Name, if so just get id
                                        # work properly
                                        if check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Name")] == "Call(func=Name":
                                            # just compare the first few chars if it is Call(func=Name(id=
                                            if check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Name(id='")] == "Call(func=Name(id='":
                                                symbol_index = check_string[temp_search_result+new_index+len("Call(func=Name(id='"):].find("'")
                                                # validate
                                                id_name = check_string[temp_search_result+new_index+len("Call(func=Name(id='"):temp_search_result+new_index+len("Call(func=Name(id='")+symbol_index]
                                                visit_stack.append(id_name)
                                        elif check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Attribute")] == "Call(func=Attribute":
                                            bracket_count = 1
                                            temp_index = 0
                                            for letter in check_string[temp_search_result + new_index + len("Call(func=Attribute("):]:
                                                if letter == "(":
                                                    bracket_count = bracket_count + 1
                                                elif letter == ")":
                                                    bracket_count = bracket_count - 1
                                                # check out if it is time to finish
                                                if bracket_count == 0:
                                                    # if_located works 
                                                    break
                                                temp_index = temp_index + 1
                                            func_string = check_string[temp_search_result + new_index+ len("Call("):temp_search_result + new_index + len("Call(func=Attribute(")+temp_index+1]
                                            # call_string is the correct array, just get the last attr
                                            # print(call_string)
                                            symbol_index =  func_string.rfind("attr='")
                                            if symbol_index == -1:
                                                print("Attribute: error:"+func_string)
                                                new_index = new_index + temp_search_result + len("Call(func=")
                                                continue
                                                
                                            temp_index = 0
                                            for letter in func_string[symbol_index + len("attr='"):]:
                                                if letter != "'":
                                                    temp_index = temp_index + 1
                                                else:
                                                    break
                                            attriute_name = func_string[symbol_index + len("attr='"): symbol_index + len("attr='") + temp_index]
                                            # print(attriute_name)
                                            # print(attriute_name)
                                            visit_stack.append(attriute_name)
                                        else:
                                            # print("Call(func= appears error:"+check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Attribute")])
                                            # here just Call and call 
                                            pass
                                        # print(call_string)
                                        new_index = new_index + temp_search_result + len("Call(func=")

                                    pass
                                else:
                                    # pass
                                    # stop tracing
                                    index = search_result + index + len("FunctionDef(name='") - 1
                                    continue
                                break
                            else:
                                # change index to fit the next coming cycle
                                index = search_result + index + len("FunctionDef(name='") - 1
                                pass
                        # when excuting here, judge according to if_located
                        # print(ast.dump(tree))
                        analyzer = Analyzer()
                        analyzer.visit(tree)
                # print(new_file_path)
        except: # 这里考虑一种情况. 类成员.类方法(暂时不考虑)
            try:
                # method = [method.find('.')+1:]
                pass
            except:
                pass
            # print(method)
            # sys.exit(-1)
        # print("Finishing Call")
        self.generic_visit(node)
        # 将所有的
    def visit_Import(self, node):
        # 现在编程一定需要考虑something wrong的情况 
        # import ... as
        # print("import error occurs!\n")
        try:
            name = node.names[0].name
            # print(name)
            if_asname = 0
            try:
                asname = node.names[0].asname
                if_asname = 1
            except:
                # 没有asname
                pass
                # print("import error2!")
            # 
            # print(name)
            # print(asname)
            if not asname:
                # 检查是否存在import a.b的情况
                if name.find(".") >= 0:
                    print(name)
                    print("import error3")
                    sys.exit(-1)
                # 引入
                module_import = importlib.import_module(name)
                import_alias[name] = [module_import, name]
            else: # 存在别名
                # 直接引入
                # print(asname)
                module_import = importlib.import_module(name)
                import_alias[asname] = [module_import, name]
        except:
            print("import error1!")
            pass
        self.generic_visit(node)
    def visit_ImportFrom(self, node):
        # from .... import ... as ...
        # print("Entering import from")
        module = node.module
        # 类似于import方法
        if_asname = 0
        name = node.names[0].name
        asname = ''
        try:
            asname = node.names[0].asname
            # 视乎这里的asname直接为空
            # 放弃原本做法
            # if_asname = 1
        except:
            pass
            # print("importfrom error1")
        # 考虑到from ... import ...的特殊性，不使用统一方式处理
        # 对于模块和非模块引入进行划分
        if_module = 0

        # print("TIMES")
        try: # 首先尝试，整体作为模块进行引入
            long_module = module + "." + name
            # print(long_module)
            # 如果报错，则表示这里的name对应的不是模块
            module_import = importlib.import_module(long_module)
            # 如果执行到这里表示，是模块
            if_module = 1
        except:
            # 在这里只表示只引入了函数
            # error occurs
            try:
                module_import = importlib.import_module(module)
            except:
                self.generic_visit(node)
                return

        # 第二步保存
        # expand the store information with a asname tag.
        if asname:
            if if_module:
                from_module_alias[asname] = [module_import, long_module, 1]
            else:
                # abondon the origninal thoughts
                # from_not_module_alias[asname] = [module_import, module, 1]
                 from_not_module_alias[asname] = [module_import, long_module, 1]
            # considering somethinig error
            # 我不清楚是否应该启用这个
            # Error Maker
            # module[name] = module
        else:
            # print(name)
            if if_module:
                from_module_alias[name] = [module_import, long_module, 0]
            else:
                from_not_module_alias[name] = [module_import, module, 0]
        # still now contains everty module
        self.generic_visit(node)
# with open("./sample.py", "r") as f:
#     tree = ast.parse(f.read())

# print((ast.dump(tree)))




def strip_function(function_name, file_path, parse_result):
    # clear the visit_stack
    visit_stack.clear()
    index = 0
    # if_located used to refer if successfully find the specific function
    while True:
        if_located = False
        # here, update the index
        # here, wrong handle way
        search_result = parse_result[index:].find("FunctionDef(name='")
        if search_result == -1:
            # used to represent finished
            break
        # then check the name
        if parse_result[search_result + index: search_result  + index + len("FunctionDef(name='") ] != "FunctionDef(name='":
            # something goes wrong
            print("In recursive, something goes wrong.")
            print(parse_result[search_result + index: search_result  + index + len("FunctionDef(name='")])
        # get the name
        tmp = parse_result[search_result + index+ len("FunctionDef(name='"):].find("'")
        # print(tmp)
        # with successful repair
        name = parse_result[search_result +index +len("FunctionDef(name='") : search_result +index +len("FunctionDef(name='") + tmp ]
        # successfully validate
        # compare the name 
        # print(name+":"+function_name)
        if name == function_name:
            # print(name+":"+function_name)
            # if the name matches, then store this parts, and then store this part into a file stored in /tmp
            # first locate such pattern: FunctionDef(.......)
            # use the simplest way to finish traversing
            # when bracket_count goes to 0, then finish
            bracket_count = 1
            # temp_index is used to account the length of traversing length
            # The actual index is search_result + leng("FunctionDef(" + temp_index)
            temp_index = 0
            for letter in parse_result[search_result + index + len("FunctionDef("):]:
                if letter == "(":
                    bracket_count = bracket_count + 1
                elif letter == ")":
                    bracket_count = bracket_count - 1
                # check out if it is time to finish
                if bracket_count == 0:
                    # if_located works 
                    if_located = True
                    break
                temp_index = temp_index + 1
            # now get the successful substring, it is time.
            
            if if_located:
                # if_located is true, means find the defination of the function , recording the inner called functions
                check_string = parse_result[search_result + index+ len("FunctionDef"):search_result+index + len("FunctionDef(")+temp_index+1]
                # print("+++"+check_string)
                # now it is time to deal with the call function
                # here is the furthur trace of the function, obtain the contained function and just add it to visit_stack
                # similarity, deal with the string result 
                new_index = 0
                while True:
                    temp_search_result = check_string[new_index:].find("Call(func=")
                    if temp_search_result == -1:
                        break
                    # to make the program more stable use some fool methods
                    bracket_count = 1
                    # temp_index is used to account the length of traversing length
                    temp_index = 0
                    for letter in check_string[temp_search_result + new_index + len("Call(func="):]:
                        if letter == "(":
                            bracket_count = bracket_count + 1
                        elif letter == ")":
                            bracket_count = bracket_count - 1
                        # check out if it is time to finish
                        if bracket_count == 0:
                            # if_located works 
                            break
                        temp_index = temp_index + 1
                    # call_string validate, it is complete
                    call_string = check_string[temp_search_result+new_index:temp_search_result+new_index+temp_index+len("Call(func=")+1]
                    # first, check out the first few characters if they are Call(func=Name, if so just get id
                    # work properly
                    if check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Name")] == "Call(func=Name":
                        # just compare the first few chars if it is Call(func=Name(id=
                        if check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Name(id='")] == "Call(func=Name(id='":
                            symbol_index = check_string[temp_search_result+new_index+len("Call(func=Name(id='"):].find("'")
                            # validate
                            id_name = check_string[temp_search_result+new_index+len("Call(func=Name(id='"):temp_search_result+new_index+len("Call(func=Name(id='")+symbol_index]
                            visit_stack.append(id_name)
                    elif check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Attribute")] == "Call(func=Attribute":
                        bracket_count = 1
                        temp_index = 0
                        for letter in check_string[temp_search_result + new_index + len("Call(func=Attribute("):]:
                            if letter == "(":
                                bracket_count = bracket_count + 1
                            elif letter == ")":
                                bracket_count = bracket_count - 1
                            # check out if it is time to finish
                            if bracket_count == 0:
                                # if_located works 
                                break
                            temp_index = temp_index + 1
                        func_string = check_string[temp_search_result + new_index+ len("Call("):temp_search_result + new_index + len("Call(func=Attribute(")+temp_index+1]
                        # call_string is the correct array, just get the last attr
                        # print(call_string)
                        symbol_index =  func_string.rfind("attr='")
                        if symbol_index == -1:
                            print("Attribute: error:"+func_string)
                            new_index = new_index + temp_search_result + len("Call(func=")
                            continue
                            
                        temp_index = 0
                        for letter in func_string[symbol_index + len("attr='"):]:
                            if letter != "'":
                                temp_index = temp_index + 1
                            else:
                                break
                        attriute_name = func_string[symbol_index + len("attr='"): symbol_index + len("attr='") + temp_index]
                        # print(attriute_name)
                        # print(attriute_name)
                        visit_stack.append(attriute_name)
                    else:
                        # print("Call(func= appears error:"+check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Attribute")])
                        # here just Call and call 
                        pass
                    # print(call_string)
                    new_index = new_index + temp_search_result + len("Call(func=")

                pass
            else:
                # pass
                # stop tracing
                index = search_result + index + len("FunctionDef(name='") - 1
                continue
            break
        else:
            # change index to fit the next coming cycle
            index = search_result + index + len("FunctionDef(name='") - 1
            pass


# the basic idea is: use the inspect.getfile() to check out the file as getfile() might return error results ,which need extra handle
getfile_error=[]
if __name__ == "__main__":
    # first, checkout the cointain folder
    if not os.path.exists("./container"):
        os.mkdir("./container")
    else:
        shutil.rmtree("./container")
        os.mkdir("./container")
    # create the folder "ast" which contains the ast.dump() result of the file
    # create the folder "api" which contains the raw_op of the corrosponding function
    os.mkdir("./container/ast")
    os.mkdir("./container/api")

    log = open("./log", "w+")
    empty_raw_op = 0
    # try to read the file
    with open("./tf_APIdef.txt", "r") as f:
        for line in f.readlines():
            function_call = "tensorflow" + line[2:-1]
            # 
            bracket_index = function_call.find("(")
            if bracket_index == -1:
                print("Error in bracket_index")
                continue
            function_call = function_call[:bracket_index]
            function_call_last_name =  function_call.split(".")[-1]
            # print(function_call)
            try:
                file_path = inspect.getfile(eval(function_call))
            except:
                # actually, this is a quite small set, therefore, just skip it without great influence
                getfile_error.append(function_call)
                continue    
            # by ast tree, it is easy to judge if file_path file contains the function.
            with open(file_path, "r") as f:
                tree = ast.parse(f.read())
                # string
                parse_result = ast.dump(tree)
            if parse_result.find("FunctionDef(name='" + function_call_last_name + "'") >= 0:
                # 561 / 1442
                # print(function_call)
                # global import's alias:
                # import_alias = {}
                # # global from's alias:
                # from_not_module_alias = {}
                # # global from's module alias:
                # from_module_alias = {}
                # # module dict:
                # modules = {}
                # global_call_type = ''
                # # 包括需要递归的函数
                # visit_stack = []
                # # judge if the function has been visited, if so return or exxplore x....x
                # # attention, the list contains the last method.
                # visited_function_list = []
                # raw_api_output = []
                visit_stack.clear()
                visited_function_list.clear()
                raw_api_output.clear()
                from_module_alias.clear()
                from_not_module_alias.clear()
                import_alias.clear()
                strip_function(function_call_last_name, file_path, parse_result)
                
                log.write("::::::::::::::::::::::"+"\n")
                log.write(file_path+"\n")
                log.write(function_call+"\n")
                log.write(" ".join(visit_stack) + "\n")
                # now get the file_path and function_call_last_name and visit_stack
                former_analyzer = Analyzer_former()
                former_analyzer.visit(tree)
                # print(visit_stack)
                analyzer = Analyzer()
                analyzer.visit(tree)

                with open("./container/api/"+function_call, "w+") as f:
                    if len(raw_api_output) == 0:
                        empty_raw_op = empty_raw_op + 1
                        continue
                    for ele in raw_api_output:
                        f.write(ele+"\n")
            else:
                # extra_handle()
                pass
    print("***************************************")
    print("empty:{}".format(empty_raw_op) )
    # print(getfile_error)
    log.close()


























# if __name__=="__main__":
#     try:
#         opts, args = getopt.getopt(sys.argv[1:], "i:")
#     except: 
#         print("./auto_deference_function.py -i file_path")
#         sys.exit(-1)
#     for opt, arg in opts:
#         if opt == "-i":
#             input_file = arg

#     # 获取解析文件路径
#     with open(input_file, "r") as f:
#         for line in f.readlines():
#             try:
#                 if(line[0].isalpha()expm(input)): # 表明是正常
#                     index = line.find("(")
#                     if index > 0:
#                         function_name = line[:index-1]
#                     else:
#                         print(line)
#                         sys.exit(-1)
                    
#             except:
#                 print(line)
#                 sys.exit(-1)


    

from ctypes import *

calc = cdll.LoadLibrary("calc.so")
print(calc.add(1,3))

# 0x02. Python - import & modules
simple python codes

## Purpose
To learn how to import a module and how to write a module

## Coding style
- All python files are interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3) and use the [PEP 8 style (version 1.7.*)](https://github.com/PyC\QA/pycodestyle) for checking coding style.

## Getting started
To use, first download  this repository into your local machine by issuing the following command in your local terminal. 
```
git clone https://github.com/sumin3/holbertonschool-higher_level_programming.git
```
#### Change Directory
```
cd 0x02-python-import_modules
```
Change directory into the **0x02-python-import_modules** directory and issue the following command to compile. (Make sure the .py file is executable before you run it. If it is not a executable file, use this command `chmod u+x <filename.py>` in your terminal to make it executable.

* Run .py file
```
python3 <filename.py>
```
or

```
./<filename.py>
```

## Usage Examples
```
$ ./0-add.py
1 + 2 = 3
```

## Files
Task number | File | Desc
---|--|---
0  | 0-add.py *add_0.py* |  imports the function def add(a, b): from the file add_0.py and prints the result of the addition
1  | 1-calculation.py *calculator_1.py* | imports functions from the file calculator_1.py, does some Maths, and prints the result.
2  | 2-args.py | prints the number of and the list of its arguments.
3  | 3-infinite_add.py | prints the result of the addition of all arguments
4  | 4-hidden_discovery.py [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc) | prints all the names defined by the compiled module hidden_4.pyc
5  | 5-variable_load.py *variable_load_5.py* | imports the variable a from the file variable_load_5.py and prints its value.
6  | 100-my_calculator.py | imports all functions from the file calculator_1.py and handles basics operations.
7  | 101-easy_print.py |  prints #pythoniscool within 2 lines and without using `eval`, `print`, `open`, `import sys`
8  | 102-magic_calculation.py  | Write the Python function def magic_calculation(a, b): that does exactly the same as the Python bytecode (see bytecode section below)
9  |103-fast_alphabet.py  | prints the alphabet in uppercase, followed by a new line. not allow use loops, conditional statement, `str.join()`, any string literal, any system calls 
* All files in *Italic characters* are provided by [Holberton School](https://www.holbertonschool.com/) 
## Python Bytecode
```
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```

## Authors
Sumin Yu  
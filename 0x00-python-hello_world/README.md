# 0x00. Python - Hello, World
Simple python codes

## Purpose
learn how to compile python file, how to runs python code, and how to write simple python codes

## Getting started
To use, first download  this repository into your local machine by issuing the following command in your local terminal. 
```
git clone https://github.com/sumin3/holbertonschool-higher_level_programming.git
```
Change directory into the **0x00-python-hello_world** directory and issue the following command to compile the code

* Run .py file
```
./<filename.py>
```
* Run text file
```
./<filename>
```
* Run .c file
```
gcc -Wall -Werror -Wextra -pedantic 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
```
Once the .c files are compiled you can run the program by issuing the command
```
./cycle
```

## Usage Examples
```
$ ./0-run
Holberton School
```
```
$ ./2-print.py 
"Programming is like building a multilingual puzzle
```
```
$./cycle
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
```

## Files
Task number | File | Desc
---|---|---
0  | 0-run main.py | Shell script that runs a Python script.
1  | 1-run_inline  | Shell script that runs Python code.
2  | 2-print.py  | print a string
3  | 3-print_number.py | print the integer stored in the variable number, followed by a string
4  | 4-print_float.py  | print the float stored in the variable number with a precision of 2 digits
5  | 5-print_string.py | print 3 times a string stored in the variable str, followed by its first 9 characters.
6  | 6-concat.py | print Welcome to Holberton School!
7  | 7-edges.py  | copy-cut-paste a string
8  | 8-concat_edges.py  | print a new string from the given string
9  | 9-easter_egg.py  | prints “The Zen of Python”, by TimPeters
10 | 10-check_cycle.c, lists.h, 10-main.c, 10-linked_lists.c | checks if a singly linked list has a cycle in it
11 | 100-write.py | Use the function write from the sys module to write a string

## Authors
Sumin Yu  
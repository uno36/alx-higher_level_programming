# 0x01. Python - if/else, loops, functions
simple python codes

## Purpose
To learn how to use if/else, loops, functions in python.

## Getting started
To use, first download  this repository into your local machine by issuing the following command in your local terminal. 
```
git clone https://github.com/sumin3/holbertonschool-higher_level_programming.git
```
Change current working directory to **0x01-python-if_else_loops_functions** directory and issue the following command to compile the code
* Run .py file
```
python3 <filename.py>
```
* Run .c file
```
gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-insert_number.c -o insert
```
Once the .c files are compiled you can run the program by issuing the command
```
./insert
```
## Usage Examples
```
$ python3 0-positive_or_negative.py
-5 is negative
```
```
$ ./insert
1
-----------------
-2
1
```
## Files
Task number | File | Desc
---|---|---
0 | 0-positive_or_negative.py | determine positive or negative number
1 | 1-last_digit.py | print last digit of a random number
2 | 2-print_alphabet.py |  prints the alphabet, in lowercase
3 | 3-print_alphabt.py | prints the alphabet, in lowercase except q and e
4 | 4-print_hexa.py | prints all numbers from 0 to 98 in decimal and in hexadecimal
5 | 5-print_comb2.py | prints numbers from 0 to 99
6 | 6-print_comb3.py | prints all possible different combinations of two digits.
7 | 7-islower.py 7-main.py| checks for lowercase character
8 | 8-uppercase.py  8-main.py| prints a string in uppercase followed by a new line
9 | 9-print_last_digit.py  9-main.py| prints the last digit of a number.
10 | 10-add.py  10-main.py| adds two integers and returns the result.
11 | 11-pow.py  11-main.py| computes a to the power of b and return the value
12 | 12-fizzbuzz.py  12-main.py| prints the numbers from 1 to 100 separated by a space
13 | 13-insert_number.c  lists.h  13-main.c  linked_lists.c | inserts a number into a sorted singly linked list
14 | 100-print_tebahpla.py | prints the alphabet, in reverse order, alternating lowercase and uppercase
15 | 101-remove_char_at.py 101-main.py |  creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”)")
16 | 102-magic_calculation.py | write python function that does exactly the same as the Python bytecode (see below)

## Python bytecode
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
## Authors
Sumin Yu  
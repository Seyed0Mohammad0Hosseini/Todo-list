# --------------------
# |        Cli       |
# --------------------
# type(variable) --> to understand the type of variable like string or list or int or ...
# len(variable) --> to calculate the length of string or variable
# capitalize vs title vs upper vs lower for string variable

# get help in python console:
# dir(str) or dir("mohammad") / help(str.upper) -> to get description

# match-case : similar to switch-case
# string.replace() string.strip for removing white spaces

# case _: == case whatever: == finally in java or cpp in switch case
#  'hello' | 'hi' equals to case "hello" || "hi" in java or cpp

# replace("." , "-" , 1) -> only replace the first one

# tuple is an immutable version of list -> you cannot change the value of each index in tuple

# enumerated(List) --> using when you want to number the values in list --> ["a.txt" ,"b","c"] -> enumerate -> (0,"a.txt") , (1,"b"), (2,"c")
# list.sort() -> return a.txt None type and sort the main list and doesn't save to another list

# using file = open(r"folder\directory\text.txt") using r before string because we have special character like \n or \t

# using zip(list1 , list2) function when you want to use values in 2 list in the same index :
# a [ 1,2,3] , b = [10,20,30] , c=zip(a,b) -> c =[(1,10),(2,20),(3,30)]

# open("../") -> it goes to parent directory

# if we don't recognize th file mode -> open("doc.txt") -> to set to read mode by default
# file.read() --> this move the pointer first character to last character in line
# shift +tab --> it move the whole code that you selected to previous indentation
# the way to use not in if condition: if "user" not in variable: some code

# exit(command) ->use when you want to do s.th and stop executing the program like exit("Bye!")
# sum() -> function

# default arguments --> def my_fun(path ="my_pc.txt")
# documentation: """ S.th """ --> we use this format for multiple lines too
# return multiple variables in functions

# use local modules :
# import pythonfile or
# from pythonfile import * -> import all functions which exist in this file
# from modules import functions -> if you want to import a file inside of dir

# time:
# time.strftime("%Y") -> give you current year -> 2023
# time.strftime("%m - %Y") ->give you current month and year -> 05 - 2023
# time.strftime("%b") -> "June" -> give you current month
# time.strftime("%d") -> to give current day
# time.strftime("%b %d %Y %H:%M:%S") -> for instance: June 20 2023 23:20:47

# important modules:
# glob
# import glob
#
# myfiles = glob.glob("*.txt")
# print(myfiles) --> the output will be Data.txt

# csv
# create csv files to define column --> each parameter should be in ""
# csv.reader(csvfile)-> this line read csvfile

# shutil
# you can create your own file with your own format

# webbrowser

# Json:
# json.load and json.dump()

# break vs exit()

# --------------------
# |  Gui(S.th else)  |
# --------------------
# pip install -r requirements.txt -> to install all packages which needed for project when you want to clone the
# project into your device -> this this for web programs

# streamlit run web.py -> to run the web program which you write
# toolConcept in Day17 related to work with git in pycharm

# PySimpleGUI themes

# image_source -> inside buttons you can use this to show an icon

# tooltip -> to show hint when user click on it or etc

# import os
# os.path.exist(filename) -> to check if file exist or not


# get exe file in python:
# first : you should be in (venv) mode in terminal otherwise use this:
# pyinstaller --onefile --windowed --clean gui.py


# ----------------
# |     web      |
# ----------------

# st.title()
# st.subheader()
# st.checkbox()
# st.write()

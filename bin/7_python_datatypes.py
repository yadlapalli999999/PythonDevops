# integer and float Data types

Course_id =100
Score = 9.8

print("Type of Course_id", type(Course_id))
print("Type of Score", type(Score))

print("#" * 50)

# They are two types of 1. Function (obj)
#                        2. obj.method

print("Def of Integer:", dir(Course_id))
#dir() -> combination of variables and objects or methods.


print("Course_id", Course_id)
print("Address of Course_id", hex(id(Course_id)))

print("Def of float:", dir(Score))

print("Score", Score)
print("Address of Score", hex(id(Score)))

print("#" * 50)

# Sequence Data types

#String
Course_name = 'Py4Devops'
print("Types of Course_name:", type(Course_name))
print("Course_name:", Course_name)
print("Address of Course_name:", hex(id(Course_name)))
print("Def of str:", dir(Course_name))

print("#" * 50)

# List Data Type
Course_list = ["Python", "PDMA","Py4Devops"]
print("Types of Course_list:", type(Course_list))
print("Course_list:", Course_list)
print("Address of Course_list:", hex(id(Course_list)))

print("Def of list:", dir(Course_list))
print("#" * 50)


# Tuple Data types
Course_tuple = ("Python", "PDMA","Py4Devops")
print("Types of Course_tuple:", type(Course_tuple))
print("Course_tuple:", Course_tuple)
print("Address of Course_tuple:", hex(id(Course_tuple)))

print("Def of Tuple:", dir(Course_tuple))
print("#" * 50)

Course_tuple1 = ("PDMA")
print("Types of Course_tuple1:", type(Course_tuple1))
print("Course_tuple1:", Course_tuple1)
print("Address of Course_tuple1:", hex(id(Course_tuple1)))

print("Def of Tuple1:", dir(Course_tuple1))
print("#" * 50)

# Boolean Data type
is_enrolled = True
print("Type of is_enrolled:", type(is_enrolled))
print("is_enrolled:", is_enrolled)

print("Address of is_enrolled:", hex(id(is_enrolled)))
print("Def of bool:", dir(is_enrolled))

print("#" * 50)

# Set Data Type
Course_set = {"PDWA", "Python", "Py4Devops"}

print("Types of Course_set:", type(Course_set))
print("Course_set:", Course_set)
print("Address of Course_set:", hex(id(Course_set)))

print("Def of Set:", dir(Course_set))
print("#" * 50)

# Dictionary Data types
Course_dict = {
    "C1":"PDMA",
    "C2":"Python",
    "C3":"Py4Devops"
}
print("Type of Course_dict:", type(Course_dict))
print("Course_dict:",Course_dict )
print("Address of Course_dict:", hex(id(Course_dict)))
print("Def of dict:", dir(Course_dict))

print("#" * 50)

#
__builtins__ = dir()
print("#" * 50)

'''Duplicacy'''

Course_id = 1001

Is_enrolled = False
Score = 95.5

Course_name_duplicacy = 'PDMA'
Course_list_duplicacy = ['PDMA', 'AWS', 'Azure', 'Devops']

Batch_set = {"Batch_A", "Batch_B", "Batch_C"}

Course_dict_duplicacy = {"Course_name":"PMDB", "Duration":"6 Months", "Level":"Begineer"}

Course_name_duplicacy = "PDMAPDMA"
print("Course_name_duplicacy:", Course_name_duplicacy)

Course_list_duplicacy = ['PDMA', 'AWS', 'Azure', 'Devops', 'PDMA', 'AWS']

print("Course_list_duplicacy:", Course_list_duplicacy)

Batch_set = {"Batch_A", "Batch_B", "Batch_C", "Batch_A", "Batch_B"}
print("Batch_set:", Batch_set)

#indexing
# strings, List, Tuple - Support indexing
# Dictionary, set - do not support indexing
Course_name_1 = "Py4Devops"
#                0 1 2 3 4 5 6 7 8 9
#                -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print("Course_name[0]:", Course_name_1[0]) # positive indexing to fetch first character
print("Course_name[9]:", Course_name_1[8]) # positive indexing to fetch last character


print("Course_name[-9]:", Course_name_1[-8]) # negative indexing to fetch first character
print("Course_name[-9]:", Course_name_1[-1]) # negative indexing to fetch last character
print("#" * 50)

# List
Course_list_1 = ["PDWA", "PDMA", "Py4Devops"]
#                  0       1       2
#                  -3       -2     -1
print("Course_list[0]:", Course_list_1[0]) # positive indexing to fetch first character
print("Course_list[9]:", Course_list_1[2]) # positive indexing to fetch last character


print("Course_name[-9]:", Course_list_1[-3]) # negative indexing to fetch first character
print("Course_name[-9]:", Course_list_1[-1]) # negative indexing to fetch last character
print("#" * 50)

# Slicing
# forward slicing
print("Course_name[0:5]:", Course_name_1[0:5]) # forward slicing to fetch 'Py4De'
print("Course_name[5:10]:", Course_name_1[5:10]) # forward slicing to fetch 'vops'

print("Course_name[-10:-5]:", Course_name_1[-10:-5]) # forward slicing to fetch 'Py4De'
print("Course_name[-5:-1]:", Course_name_1[-5:-1]) # forward slicing to fetch 'vops'

print("#" *50)
# reverse slicing
print("Course_name[0:4:-1]:", Course_name_1[0:4:-1]) # reverse slicing to fetch 'sopveD'
print("Course_name[0:4:-1]:", Course_name_1[4:0:-1]) # reverse slicing to fetch 'sopveD'

print("#" * 50)

# Reverse list listing
Course_list_2 = ["PDMA", "PDWA", "Py4Devops", "AWS","JS"]
reserved_Course_list_2 = Course_list_2[:: -1]
print("Reverse Course_list_1:", reserved_Course_list_2)

# INT TO FLOAT
Course_id_float = float(Course_id)
print("Course_id_float:", Course_id_float, type(Course_id_float))
 
# INT TO STR
Course_id_str = str(Course_id)
print("Course_id_str:", Course_id_str, type(Course_id_str))

# INT TO BOOL
Course_id_bool = bool(Course_id)
print("Course_id_bool:", Course_id_bool, type(Course_id_bool))

Course_id_4 = -1001
Course_id_bool_1 = bool(Course_id_4)
print("Course_id_bool_1:", Course_id_bool_1, type(Course_id_bool_1))
print("#" * 50)

#INT TO LIST
Course_id_list = list(str(Course_id))
print("Course_id_list:", Course_id_list, type(Course_id_list))

print("#" * 50)
# string formattings

# f string
Course_id_5 = 1001
Course_name_str ="Py4Devops"

print(f"Course ID is {Course_id_5} and Course name is {Course_name_str}")

#format() method
print("Course ID is {} and Course name is{}".format(Course_id_5, Course_name_str))

# % operator 
print("Course ID is %d and Course Name is %s" %(Course_id_5,Course_name_str))

print("#" * 50)

print(dir(Course_name_str))
print("#" * 50)
# calling string methods
#object.method() # syntax

print("Upper Case Course name str:", Course_name_str.upper())

print("#" * 50)

print("Lower Case Course name str:", Course_name_str.lower())
print("#"*50)

print("Title Case Course Name:", Course_name_str.title())
print("#" * 50)

print("Count of 'o' in Course Name:", Course_name_str.capitalize())
print("#"*50)

Course_name_Str = "  Py4Devops  "
print("Original Course Name with spaces:", Course_name_Str.strip())
print("Original Course Name with spaces:", Course_name_Str.strip('s '))

print("#"*50)

# split method
print("Course name after split():", Course_name_str.split(sep='4'))
Course_name2 = "Py4Devops:Python for Devops"
print("Course name after split():",Course_name2.split(sep=':'))
print("#"*50)

#replace method
print("Course name after replace():", Course_name2.replace('Devops','Development Operations'))
print("#"*50)

#join methods
Course_list_join = ["PDMA", "PDWA","Py4Devops"]
print("Course list after join()", ' | '.join(Course_list_join))
print("Course list after join():", '-'.join(Course_list_join))
print("#"*50)

#starsWith and endwith()
print("Course name startswith 'py':", Course_name2.startswith('Py'))
print("Course name endwith 'ops':", Course_name2.endswith('ops'))
print("#"*50)

#find() and index()
print("index of 'o' in Course name using find():", Course_name2.find('D',0,len(Course_name2)))
print("index of 'D' in Course name Using index:", Course_name2.index('D',0,len(Course_name2)))
print("# " * 50)

#isalpha(), isdigit(), isalnum()
Course_name= "Py4Devops"
Course_id_str = "1001"
print("Course name isalpha():", Course_name.isalpha())
print("Course_id_str isdigit():", Course_id_str.isdigit())

Course_name_alnum="Py4Devops1001"
print("Course_name_alnum isalumn():", Course_name_alnum.isalnum())
print("#"*50)

#zfill()
print("Course_id_str after zfill():", Course_id_str.zfill(8))
print("#"*50)
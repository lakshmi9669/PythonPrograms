# 1) What is <Yield> Keyword in Python ?
#
# The <yield> keyword in Python can turn any function into a generator. Yields work like a standard return keyword.
# But it’ll always return a generator object. Also, a function can have multiple calls to the <yield> keyword.

# 2) How do you debug a Python program?
#
# By using this command we can debug a python program
#
# ex: python -m pdb python-script.py

# 3) convert list into tuple:
# weekdays = ['sun','mon','tue','wed','thu','fri','sat']
# listAsTuple = tuple(weekdays)
# print(listAsTuple)

# num = [1, 2, 3, 4]
# listAsTuple = tuple(num)
# print(listAsTuple)
#
# 4)convert tuple into list:
# num = (1, 2, 3, 4)
# TupleAslist = list(num)
# print(TupleAslist)

# 5) How to convert a list into a set:
# Example:
# weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
# listAsSet = set(weekdays)
# print(listAsSet)
# output: set(['wed', 'sun', 'thu', 'tue', 'mon', 'fri', 'sat'])


# 6) How to count the occurrences of a particular element in the list?
#
# Example # 1:
#
# weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon'
# ]
# print(weekdays.count('mon'))#......Output: 3
#
# Example # 2:
#
# weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
# print([[x,weekdays.count(x)] for x in set(weekdays)])
# output: [['wed', 1], ['sun', 2], ['thu', 1], ['tue', 1], ['mon', 3], ['fri', 1]]

# 7) What is NumPy array?
# NumPy arrays are more flexible then lists in Python.
# By using NumPy arrays reading and writing items is faster and more efficient.

# 8)What is Enumerate() Function in Python?
#The Python enumerate() function adds a counter to an iterable object.
# enumerate() function can accept sequential indexes starting from zero.
#
# Python Enumerate Example:

# subjects = ('Python', 'Interview', 'Questions')
# for i, subject in enumerate(subjects):
#     print(i, subject)

# Output:
# 0 Python
# 1 Interview
# 2 Questions


#
# import re
#
# def find_m(word):
#     if re.match("[^aeiou]*?[aeiou]*?",word):
#         print("PASS")
#     else:
#         print("FAIL")
#
#
# find_m("tr")
# find_m("ee")
# find_m("tree")
# find_m("y")
# find_m("by")
# find_m("trouble")
# find_m("oats")
# find_m("trees")
# find_m("ivy")
# find_m("aaabbbbaaa")


# regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
#
#
# # Define a function for
# # validate an Ip address
# def check(Ip):
#     # pass the regular expression
#     # and the string in search() method
#     if (re.search(regex, Ip)):
#         print("Valid Ip address")
#
#     else:
#         print("Invalid Ip address")

#
# # Driver Code
# if __name__ == '__main__':
#     # Enter the Ip address
#     Ip = "192.168.0.1"

# test_list = [1, 3, 5, 6, 3, 5, 6, 1,4,9]
# print ("The original list is : " ,test_list)
# # using naive method to remove duplicated from list
# res = []
# res1 = []
# for i in test_list:
#    if i not in res:
#       res.append(i)
#    else:
#       res1.append(i)

# using list comprehension to remove duplicated from list
# res = []
# [res.append(x) for x in test_list if x not in res]
# printing list after removal
# print ("The list after removing duplicates : " , res)
# print("duplicates only: " ,res1)



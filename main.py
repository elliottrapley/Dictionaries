# Dict items are key value pairs enclosed in curly brackets
# Dict is ordered as of python 3.7
# Dict is mutable
# Dict keys are unique, cannot have duplicates
# Elements can be of different data types

'''
Dict Attributes
'''
print(dir(dict))
print(help(dict.popitem))


'''
Creating Python Dictionary
'''

dict = {}
# dictionary with key and value
dict = {'name': 'Kingsley', 'age': 37}
# list of tuples into dictionary
# output => {1: 'car', 2: 'bicycle'}
dict = dict([(1,'car'), (2,'bicycle')])

'''
Access Dictionary Values
'''

student = {'name': 'Kingsley', 'age': 37}
# access with []
# output => 'Kingsley'
student['name']
# access using get()
# output => 37
student.get('age')
# get a list of keys
# output => dict_keys(['name', 'age'])
print(student.keys())
# get all values
# output => dict_values(['Kingsley', 37])
print(student.values())

# store a list of dict items
students = [{'name': 'Kingsley', 'age': 37}, {'name': 'Lisa', 'age': 34}]
# access using list index
print(students[0]['name'])
print(students[1]['name'])
# access using for in loop
for i in range(len(students)):
  print(students[i]['name'])

'''
Changing Dictionary elements
'''

student = {'name': 'Kingsley', 'age': 37}
# update value
student['age'] = 26
print(student) # => {'name': 'Kingsley', 'age': 26}
# updating with key and value
student = {'name': 'Kingsley', 'age': 37}
# update student
student.update({'name': 'Jennifer'})
# output => {'name': 'Jennifer', 'age': 37}
print(student)
student = {'name': 'Kingsley', 'age': 37}
# key 'age' exists so 35 is ignored
student.setdefault("age", 35)
# subject is new so it is set
student.setdefault("subject", 'Python')
# output => {'name': 'Kingsley', 'age': 37, 'subject': 'Python'}
print(student)



'''
Remove Element From Dictionary
'''

student = {'name': 'Kingsley', 'age': 37}
# remove the item with key 'name'
student.pop('name')
# => {'age': 37}
print(student)
# remove item from end of dict
student = {'name': 'Kingsley', 'age': 37}
print(student.popitem())
print(student)
# clear all items
student = {'name': 'Kingsley', 'age': 37}
student.clear()
print(student)
# delete the dictionary itself
# NameError: name 'student' is not defined
student = {'name': 'Kingsley', 'age': 37}
del student
print(student)

'''
Dictionary Membership Test
'''

student = {'name': 'Kingsley', 'age': 37}
# output => True
print('name' in student)
# output => False
print('name' not in student)


# clear()	      - Remove all items from dictionary
# copy()	      - Returns a shallow copy of dictionary
# fromkeys()	  - Returns a dictionary with the specified keys and value
# get()	        - Returns the value of the specified key
# items()	      - Returns a list containing a tuple for each key value pair
# keys()	      - Returns a list containing the dictionary's keys
# pop()	        - Removes the element with the specified key
# popitem()	    - Removes the last inserted key-value pair
# setdefault()	- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    - Updates the dictionary with the specified key-value pairs
# values()	    - Returns a list of all the values in the dictionary
def display_list(items):
    print("list contents :",items)
    
def display_tuple(iems):
    print("dictionary contents:",items)
    
#A.operations
n=int(input("how many integers?"))
numbers=[int(input(f"enter an elements{i+1}:")) for i in range(n)]
value=int(input("enter a value to insert="))
position=int(input("enter a position (0-based):"))
if 0<= position <=len(numbers):
    numbers.insert(position,value)
else:
    print("invalid position")
    
value=int(input("enter a element to delete="))
if value in numbers:
    numbers.remove(value)
else:
    print("element not found")
    
numbers.sort()
print("sorted list :",numbers)
numbers.reverse()
print("reversed list:",numbers)

#B.tuple operations
names=input("enter student names separated by space;")
print("tuple:",names)
search_name=input("enter a name to count:")
print("count:",names.count(search_name))
index_name=input("enter a name to find a index:")
if index_name in names:
    print("index:",names.index(index_name))
else:
    print("name not found")
    
#C.dictionary operations
students={"MT26AE001":"gangadhar","4MT26CS001":"bhuvan"}
new_usn=input("enter a new usn=")
new_name=input("enter a new student name=")
students[new_usn]=new_name

update_usn=input("enter usn to update:")
if update_usn in students:
    students[update_usn]=input("enter a updated names=")
else:
    print("usn not found")
    
delete_usn=input("enter usn to delete=")
if delete_usn in students:
    del students [delete_usn]
else:
    print("usn not found")
    
print("keys :",list(students.keys()))
print("values:",list(students.values()))

#D.pass collections to functions
display_list(numbers)
display_tuple(names)
display_dictionary(students)
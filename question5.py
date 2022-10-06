'''5. Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}'''
set_1={"Java", "Python", "SQL"}
set_2= {"C", "Cpp", "NoSQL"}
print(set_1,"\n"),print(set_2,"\n"),set_1.update(set_2),print(type(set_1),":",set_1)

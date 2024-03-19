#multiple dictionariy in python


p1 ={
    "name":"jayesh",
    "education":{"digree": ["btech","diploma","many more things"]}
}

for i in p1:
    print(i)
    
    
    
array_of_dict= [{
    "name":"jayesh"},
    {"name":"savan"},
    {"name":"viral"}
    ]


print(array_of_dict)

enter = input("enter the name: ")
key = input("Enter the key: ")
def add(name,subname):
    new_dict = {}
    new_name = name
    new_subname = subname
    array_of_dict.append(new_dict)

add(enter,key)
print(array_of_dict)
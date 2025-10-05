# Type annotation is use only for indicating Data type

x: int = 10
print(x)

arr: list[int] = {1, 2, 3}
print(arr)

# print if different data type
arr1: list[int] = {"hello", "world"}
print(arr1)

dictionary: dict[str, int] = {'a': 1, 'b': 2}
print(dictionary)

# Function without parameter

def returnString() -> str:
    return "Hello World"

print(returnString())

# Function with parameter

def fun(arr: list[int]) -> None:
    for i in arr:
        print(i,end="--->")
    print("None")
fun([1,2,3,4,5])

# oops

class Node:
    def __init__(self,name:str):
        self.name = name
    def Printname(self)->None:
        print(self.name)    

n1:Node = Node("Tree")
n1.Printname()
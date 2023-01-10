File Access Modes
Read only ('r')
Read and Write ('r+')
Write Only ('w')
Write and Read ('w+')
Append only ('a')
Append and Read ('a+')
1. Text Files
Opening a| file
file =open("random.txt","w")
file.write("blah blah blah blah")
19
file.write("\n new line")
10
file.close()
Writing to a File
write
writelines
file = open("random.txt","w")
file.write("Joey Tribbiani")
14
a=["Joey","Doesn't","Share","Food!!!"]
file.writelines(a)
 file.close()
Reading from a File
read
readline
readlines
file = open("sample.txt","r")
file.read()
'Joey\nPheobe\nChandler\nRoss\nMonica\nRachel\n'
print(file.read())
file.close()
Streams
Iterables which can be iterated in a single direction
They dont have starting and ending point
Moving the Cursor
seek(n): takes the file handle to the nth byte from the beginning.
Smart way of Opening files
With the "with" statement, you get better syntax and execptions handling. "The with statement simplifies exception handling by encapsulation common preparation and cleanup tasks." In addition, it will automatically close the file. The way statement provides a way for ensuring that a clean-up is always used.

Context Programming
with open("random.txt","r") as file:
    print(file.read())
Joey TribbianiJoeyDoesn'tShareFood!!!
class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self, *args):
        print("Exitted")
        print(args)
        return True
with A() as x:
    print(x)
    print("inside Context")
print("Outside Context")
Entered
1
inside Context
Exitted
(None, None, None)
Outside Context
JSON Files
JavaScript Object Notation

json.dump(obj,fileObj)
json.dumps(obj)
json.load(JSONfile)
json.loads(JSONfile)
JSON is like a dictionaries

JSON Rules
keys can only be strings and numbers
values can only be array, json, strings, numbers, boolean, null
a = {
    "name":"joey",
    "marks":100,
    "language": [
        "c++","python","go","rust"
    ]
}
import json
s = json.dumps(a)
type(s)
str
print(s)
{"name": "joey", "marks": 100, "language": ["c++", "python", "go", "rust"]}

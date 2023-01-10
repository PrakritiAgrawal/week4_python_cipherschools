# File Access Mode
# Read Only => r
# Read and Write => r+
# Write Only => w 
# Write and Read  => w+
# Append Only => a
# Append and Read => a+

"""TEXT FILES"""
file=open("random.txt","w")
file.write("hello hello hello")
file.write("\n new line")
file.close() #Closing a file is important because when you open a file in write mode you are blocking the operations from the processes. You have allocated a resource/blocked a resource so you should release that resource once you are done with it.

'''Writing a file'''
file=open("random.txt","w")
file.write("Prakriti Agrawal")
a=["Prakriti","Agrawal","sanchita","nivedita"]
file.writelines(a)
file.close()

'''Reading a file'''
# read
# readline
# readlines

file=open("sample.txt","r")
a=file.read()
print(a)
print(file.read()) #The cursor goes in the end, so didn't read the things before the cursor.



"""Smarter Way Of Opening Files"""

#Context Programming

with open("random.txt","r") as file:
    print(file.read())

#print(file.read())

#Using with ---> Once the context starts it opens the file and once the context ends it closes the file.

class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self,*args):
        print("Exitted")
        print(args)
        return True

with A() as x:
    print(x)
    print("inside context")
    raise Exception

print("outside context")

#Whatever happens in a context remains in a context


"""JSON FILES"""
#Text representaion of data.
#JSON RULE => In json your keys cn onl;y be strings and numbers and value can only be array,json,numbers,boolean,null.

'''
<html>
    <body>
        Hi
    </body>
</html>
{
    "html":{
        "body":"Hi"
    }
}
'''

a={
    "name":"Prakriti Agrawal",
    "marks":100,
    "languages":[
        "c++",
        "python",
        "go",
        "rust"
        ]
}

import json
s=json.dumps(a)
type(a)
print(s)

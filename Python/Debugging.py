import pdb   #import pdb module

#module-pytho file contains useful classes and function wrote by developer.

#According to wikipedia- Debugging is the process of finding and resolving
#defects or problems within a computer program that prevent correct operations
#of computer software or a system.

#Why debugging
#1.) our program is not running and causing unexpected errors.
#2.) our program is working fine but not working the same way we want.

#step for debugging
#1.) set trace
#2.) execute code line by line

pdb.set_trace()
name=input("please type your name:")
age=int(input("please type your age:"))
print(f"hello {name} your age is {age}.")
age2=age+5
print(f"{name} you will be {age2} in next five year.")

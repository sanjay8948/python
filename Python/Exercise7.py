# fun return any dictionary of cube
def cube_finder(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i]=i**3
    return cubes

a=int(input("enter any number:"))
print(cube_finder(a))
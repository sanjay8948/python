#closure or first class function
def to_power(n):
    def calc_power(x):
        return x**n
    return calc_power

cube=to_power(3)
square=to_power(2)

print(cube(5))
print(square(5))

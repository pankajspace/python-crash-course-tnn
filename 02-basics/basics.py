# # execution order matters
# print("line 1") # this will be printed first
# print("line 2") # this will be printed second
# print("line 3") # this will be printed third

# # data types

# # strings
# print("Hello, World!") # double quotes
# print('Hello, World!') # single quotes
# print("""Hello, World!""") # triple double quotes
# print('''Hello, World!''') # triple single quotes
# print("Hello, " + "World!") # string concatenation
# name = "Bob"
# age = 30
# print(f"My name is {name} and I am {age} years old.") # f-strings

# # integers
# print(42) # integer literal
# print(-7) # negative integer
# print(0) # zero

# # floats
# print(3.14) # float literal, shows 3.14
# print(-0.001) # negative float, shows -0.001
# print(2.0) # float that looks like an integer, shows 2.0
# print(1e3) # scientific notation for 1000.0, shows 1000.0
# print(2.5e-4) # scientific notation for 0.00025, shows 0.00025
# print(0.1 + 0.2) # floating point precision issue, shows 0.30000000000000004
# print(0.1 + 0.2 == 0.3) # False due to precision issue, shows False
# print(round(0.1 + 0.2, 10) == 0.3) # True when rounded, shows True
# print(round(0.1 + 0.2, 10)) # shows the rounded result, shows 0.3

# # booleans
# print(True) # boolean literal for true
# print(False) # boolean literal for false
# print(1 == 1) # equality comparison, shows True
# print(1 != 2) # inequality comparison, shows True
# print(3 > 2) # greater than comparison, shows True
# print(2 < 3) # less than comparison, shows True
# print(3 >= 3) # greater than or equal to comparison, shows True
# print(2 <= 3) # less than or equal to comparison, shows True
# print(True and False) # logical AND, shows False
# print(True or False) # logical OR, shows True
# print(not True) # logical NOT, shows False
# print(not False) # logical NOT, shows True

# # variables
# x = 10 # integer variable
# y = 3.14 # float variable
# name = "Alice" # string variable
# is_active = True # boolean variable
# print(x) # shows 10
# print(y) # shows 3.14
# print(name) # shows Alice
# print(is_active) # shows True

# # variable reassignment
# x = 20 # x is now 20
# y = y + 1.0 # y is now 4.14
# name = "Bob" # name is now Bob
# is_active = not is_active # is_active is now False
# print(x) # shows 20
# print(y) # shows 4.14
# print(name) # shows Bob
# print(is_active) # shows False

# # variable naming rules

# # valid variable names
# my_variable = 5
# variable2 = 10
# _variable = 15
# myVariable = 20 # camelCase
# MY_VARIABLE = 25 # UPPER_SNAKE_CASE
# my_variable_name = 30 # snake_case
# print(my_variable) # shows 5
# print(variable2) # shows 10
# print(_variable) # shows 15
# print(myVariable) # shows 20
# print(MY_VARIABLE) # shows 25
# print(my_variable_name) # shows 30

# # invalid variable names (uncommenting these will cause errors)
# # 2variable = 10 # cannot start with a number
# # my-variable = 15 # cannot contain hyphens
# # my variable = 20 # cannot contain spaces
# # my.variable = 25 # cannot contain periods
# # def = 30 # cannot use reserved keywords

# # basic arithmetic operations
# a = 10
# b = 3
# print(a + b) # addition, shows 13
# print(a - b) # subtraction, shows 7
# print(a * b) # multiplication, shows 30
# print(a / b) # division, shows 3.3333333333333335
# print(a // b) # floor division, shows 3
# print(a % b) # modulus, shows 1
# print(a ** b) # exponentiation, shows 1000
# print(-a) # negation, shows -10
# print(+b) # unary plus, shows 3

# # operator precedence
# print(2 + 3 * 4) # multiplication before addition, shows 14
# print((2 + 3) * 4) # parentheses change order, shows 20
# print(10 - 2 + 3) # left to right, shows 11
# print(10 - (2 + 3)) # parentheses change order, shows 5
# print(2 ** 3 ** 2) # right to left for exponentiation, shows 512
# print((2 ** 3) ** 2) # parentheses change order, shows 64
# print(10 / 2 * 3) # left to right for same precedence, shows 15.0
# print(10 / (2 * 3)) # parentheses change order, shows 1.6666666666666667

# # type conversion
# # implicit conversion
# x = 5 # integer
# y = 2.0 # float
# z = x + y # x is converted to float, z is float
# print(z) # shows 7.0
# print(type(z)) # shows <class 'float'>

# explicit conversion
a = 10 # integer
b = 3.14 # float
c = "42" # string
d = "3.14" # string
e = "Hello" # string
f = int(c) # explicit conversion from string to integer
g = float(d) # explicit conversion from string to float
print(f) # shows 42
print(g) # shows 3.14
print(type(f)) # shows <class 'int'>
print(type(g)) # shows <class 'float'>

# converting float to int (truncates decimal part)
h = int(b) # explicit conversion from float to integer
print(h) # shows 3
print(type(h)) # shows <class 'int'>

# converting int to float
i = float(a) # explicit conversion from integer to float
print(i) # shows 10.0
print(type(i)) # shows <class 'float'>

# converting int to string
j = str(a) # explicit conversion from integer to string
print(j) # shows "10"
print(type(j)) # shows <class 'str'>

# converting float to string
k = str(b) # explicit conversion from float to string
print(k) # shows "3.14"
print(type(k)) # shows <class 'str'>

# converting boolean to int
l = int(True) # True becomes 1
m = int(False) # False becomes 0
print(l) # shows 1
print(m) # shows 0
print(type(l)) # shows <class 'int'>
print(type(m)) # shows <class 'int'>

# converting boolean to float
n = float(True) # True becomes 1.0
o = float(False) # False becomes 0.0
print(n) # shows 1.0
print(o) # shows 0.0
print(type(n)) # shows <class 'float'>
print(type(o)) # shows <class 'float'>

# converting boolean to string
p = str(True) # True becomes "True"
q = str(False) # False becomes "False"
print(p) # shows "True"
print(q) # shows "False"
print(type(p)) # shows <class 'str'>
print(type(q)) # shows <class 'str'>

# converting string to boolean
r = bool("Hello") # non-empty string becomes True
s = bool("") # empty string becomes False
print(r) # shows True
print(s) # shows False
print(type(r)) # shows <class 'bool'>
print(type(s)) # shows <class 'bool'>

# converting int to boolean
t = bool(1) # non-zero integer becomes True
u = bool(0) # zero becomes False
print(t) # shows True
print(u) # shows False
print(type(t)) # shows <class 'bool'>
print(type(u)) # shows <class 'bool'>

# converting float to boolean
v = bool(0.1) # non-zero float becomes True
w = bool(0.0) # zero becomes False
print(v) # shows True
print(w) # shows False
print(type(v)) # shows <class 'bool'>
print(type(w)) # shows <class 'bool'>

# invalid conversions (uncommenting these will cause errors)
# x = int("Hello") # cannot convert non-numeric string to int
# y = float("World") # cannot convert non-numeric string to float
# z = int("3.14") # cannot convert float string directly to int
# print(x)
# print(y)
# print(z)


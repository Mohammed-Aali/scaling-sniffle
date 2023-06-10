import sys

try: 
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print('Must input a number')
    sys.exit(2)

try:
    result = x/y
except:
    print('Error: Connot divide by 0.')
    sys.exit(1)


print(f'x divided by y: {result}')
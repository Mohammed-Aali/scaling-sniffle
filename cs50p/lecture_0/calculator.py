try:
    x = float(input('x: '))
    y = float(input('y: '))
    print(round(x + y, 3))
except ValueError:
    print('Please input an integer' )

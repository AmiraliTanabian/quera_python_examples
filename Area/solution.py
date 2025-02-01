from math import pi 

def get_func(ls):
    result = []


    square = lambda side : side ** 2 
    circle = lambda raduis : raduis ** 2 * pi
    rectangle = lambda l,w : l * w
    triangle = lambda rule, h : (rule * h) / 2

    funcs = {'square':square,
             'circle':circle,
             'rectangle':rectangle,
             'triangle':triangle
            }
    
    for shape in ls : 
        if shape in funcs.keys() : 
            result.append(funcs[shape])

    return result



# Test the function 

ls = get_func(['square', 'circle', 'rectangle', 'triangle'])

print(ls[0](1))      # 1
print(ls[1](2))      # 12.566370614359172
print(ls[2](2, 4))   # 8
print(ls[3](4, 5))   # 10.0

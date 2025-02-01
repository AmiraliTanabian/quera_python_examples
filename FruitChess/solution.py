
def fruits(fruit_list):

    good_fruits = {}

    for fruit in fruit_list : 
        if fruit['shape'] == 'sphere':
            if fruit['mass'] >= 300 and fruit['mass'] <= 600 :
                if fruit['volume'] >= 100 and fruit['volume'] <= 500 :

                    if fruit['name'] in good_fruits :
                        # The good fruit exists on the good fruits list 
                        good_fruits[fruit['name']] += 1 
                    
                    else : 
                        # Good fruit is not in the list of good fruits
                        good_fruits[fruit['name']] = 1

    return good_fruits



# Test the function
output = fruits ((
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))
print(output)

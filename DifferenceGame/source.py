def game(number):
    digits = [str(number)[0], str(number)[1]]
    digits = list(map(lambda num:int(num), digits))
    print(digits)
    
    max_digit = max(digits)
    min_digit = min(digits)
    return max_digit - min_digit


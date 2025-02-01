def alpha_postion(alpha):
    alpha = alpha.lower()
    return (ord(alpha)- ord('a') + 1)

def compare(string1, string2):
    while string1 != '' and string2 != '':
        first_letter_1 = string1[0]
        first_letter_2 = string2[0]

        if alpha_postion(first_letter_1) < alpha_postion(first_letter_2):
            string1 = string1[1:]
            print(string1)
        
        elif alpha_postion(first_letter_1) > alpha_postion(first_letter_2):
            string2 = string2[1:]  
            print(string2)
        else:
            string2 = string2[1:]
            string1 =  string1[1:]
            print(string1,string2)

        # when one of them of strings is '' we don't like to reverse there
        if string1 != '' and string2 != '':
            string1 = string1[::-1]
            string2 = string2[::-1]
        
        print("--------------\n",string1,string2,'\n------------------')

    # Return the result 
    if string1 == '' and string2 == '':
        return "Both strings are empty!"

    elif string1 == '':
        return string2

    elif string2 == '': 
        return string1
        
    

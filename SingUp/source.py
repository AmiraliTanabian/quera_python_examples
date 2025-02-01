def check_registration_rules(**kwargs):
    '''Help for call this function :
    >>> check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$') '''
    
    available_username = []

    print(kwargs)
    for username in kwargs: 

        if username != 'codecup'and username != 'quera' and len(username) >= 4 :
            password = kwargs[username]
            
            if len(password) >= 6 and not password.isdigit():
                available_username.append(username)
            
    return available_username

print(check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$'))

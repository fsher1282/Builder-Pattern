import Builder

if __name__ == '__main__':

    country_list = ['USA', 'Hungary', 'French', 'Mexico']

    print('Welcome to the International Address Generator...')

    print('Available countries include...')

    for i in country_list:
        print(i)

    print('\n')
    print('Enter your information below')

    fn = input('First Name: ')
    ln = input('Last Name: ')
    hn = input('House/Apt Number: ')
    st = input('Street Name: ')
    city = input('City: ')
    post_code = input('Postal Code: ')
    country = input('Type in which country you want to ship to: ')

    b = Builder.Builder(fn, ln, hn, st, city, post_code, country)

    if country.upper() == 'USA':
        state = input('Enter which State: ')
        print('\n')
        print(b.american_address(state))

    elif country.lower() == 'hungary':
        print('\n')
        print(b.hungarian_address())

    elif country.lower() == 'mexico':
        state = input('Enter which Colony you wish to ship: ')
        print('\n')
        print(b.mexican_address(state))

    elif country.lower() == 'france':
        print('\n')
        print(b.french_address())

    else:
        print("'Country you entered isn't supported here")
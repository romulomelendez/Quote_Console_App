import requests

# BUILDING A CONSOLE MENU


def set_line(size=50):
    return '-' * size


def header(text):
    print(set_line())
    print(text.center(50))
    print(set_line())


def menu(list):
    header('Quotation Console App')
    print('Choose a Option:')
    c = 1
    for item in list:
        print(f'{c}) {item}')
        c += 1
    print('\n{}'.format(set_line()))


menu(['USD-BRL', 'EUR-BRL', 'EXIT'])

# END OF THE CONSOLE MENU

# FUNCTIONS TO GET THE QUOTATIONS

# making a request to API and getting the response in JSON format
quote = (requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")).json()


def showQuoteDolar():
    global quote
    print(quote['USDBRL']['bid'])


def showQuoteEuro():
    global quote
    print(quote['EURBRL']['bid'])


def switch(case_selected):
    match case_selected:
        case 1:
            return showQuoteDolar()
        case 2:
            return showQuoteEuro()
        case 3:
            return exit()
        case default:
            return print('Invalid option!')


if __name__ == '__main__':

    response = int(input('You option here: '))

    # building a Switch Case
    switch(response)

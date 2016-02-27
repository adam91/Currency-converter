import bs4
from bs4 import BeautifulSoup

import requests

dict = {
        'PLN' : 0,
        'USD' : 3,
        'EUR' : 6,
        'GBP' : 9,
        'INR' : 12,
        'AUD' : 15,
        'CAD' : 18,
        'SGD' : 21,
        'MYR' : 24,
        'JPY' : 27,
        }

def check_amount():
    try:
        amount = raw_input("How much money do you have? ")
        float(amount) / float(amount)
        return amount
    except ValueError:
        print "Type a number"
        return check_amount()
        
def check_my_currency():
    my_currency = raw_input("What currency do you have? ")
    if my_currency in dict:
        return my_currency
    else:
        print 'You must type three-letter symbol rate'
        return check_my_currency()
    

def check_currency():
    currency = raw_input("What currency do you want to buy? ")
    if currency in dict:
        return currency
    else:
        print 'You must type three-letter symbol rate'
        return check_currency()

def main():
    amount = check_amount()
    for key, value in dict.iteritems() :
        print key
    my_currency = check_my_currency()
    currency = check_currency()
    website = requests.get('http://www.x-rates.com/table/?from=PLN&amount=1')
    website.raise_for_status()
    soup = bs4.BeautifulSoup(website.text, 'html.parser')
    if dict[my_currency] == 0:
        my_rate = 1
    else:
        my_rate = '.ratesTable td:nth-of-type(' + str(dict[my_currency]) + ')'
        my_rate = soup.select(my_rate)
        my_rate = my_rate[0].text
    if dict[currency] == 0:
        rate = 1
    else:
        rate = '.ratesTable td:nth-of-type(' + str(dict[currency]) + ')'
        rate = soup.select(rate)
        rate = rate[0].text
    wynik = float(my_rate) / float(rate) * float(amount)
    wynik = round(wynik, 2)
    print "You'll get " + str(wynik) + " " + str(currency)

if __name__ == '__main__':
    main()

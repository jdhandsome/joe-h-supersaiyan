import requests

print('\n', 'converstion values: ','\n', '\n','CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON', 'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS', 'KRW', 'PLN', "\n")

test_list = ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON', 'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS', 'KRW', 'PLN']
conversion_currency_name = input('what currency would you like to convert? input 3 digit currency: ')
print('\n')

conversion_currency_name = conversion_currency_name.upper()#converts what's entered into uppercase
if conversion_currency_name not in test_list: #checks if value is in test_list
    print('Please input valid value', '\n')
    exit()

conversion_to_name = input('what would you like to convert it to? input 3 digit currency ')
print('\n')


conversion_to_name = conversion_to_name.upper() #converts what's entered into uppercase
if conversion_to_name not in test_list: #checks if value is in test_list
    print('Please input valid value', '\n')
    exit()

url_get = (' https://api.exchangeratesapi.io/latest?base=' + conversion_currency_name)
conversion_amount = input('How much to convert?: ')
print('\n')

try:
    conversion_amount = float(conversion_amount) #error checker to see if what's entered is number
except:
    print('Please enter a valid number', '\n')
    exit()
url = requests.get(url_get) #get currency rates
s = url.text #pull contents from website
s = s[10:-35] # remove headers and footers. format string
s = s.split(',') # split string using comma as a seperator

currency_rt = [] # create list to hold key value pairs
rates = {} #create dictionary to hold data

for i in s: # loop through the split string and append currency_rt list
    i=i.split(':')
    currency_rt.append(i)

for c in currency_rt: # remove extra "" contained in the string, add key value for each currency
    i = (c[0])
    i = i[1:-1]
    rates[i] = c[1]

rt = float(rates[conversion_to_name]) #convert value into a float and round to the 2nd place
rt = round(rt, 2)
rate_calc = conversion_amount * rt #calculate the exchange rate
print(conversion_amount, conversion_currency_name, " equals ", rate_calc, conversion_to_name, '\n')

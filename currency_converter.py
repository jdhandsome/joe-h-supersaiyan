import requests

converstion_currency_name = input('what currency would you like to convert? input 3 digit currency: ')
conversion_to_name = input('what would you like to convert it to? input 3 digit currency')
url_get = (' https://api.exchangeratesapi.io/latest?base=' + converstion_currency_name)
conversion_amount = input('How much to convert?: ')
conversion_amount = float(conversion_amount)
url = requests.get(url_get) #get currency rates
s = url.text #pull contents from website
s = s[10:-35] # remove headers and footers. format string
s = s.split(',') # split string using comma as a seperator
currency_rt = [] # create list to hold key value pairs
rates = {} #create dictionary to hold data

for i in s: # loop through the split string and append currency_rt list
    i=i.split(':')
    currency_rt.append(i)

for c in currency_rt: # remove extra "" contained in the string, add key value for each currencty
    i = (c[0])
    i = i[1:-1]
    rates[i] = c[1]

rt = float(rates[conversion_to_name]) #convert value into a float and round to the 2nd place
rt = round(rt, 2)
rate_calc = conversion_amount * rt #calculate the exchange rate
print(conversion_amount, converstion_currency_name, " equals ", rate_calc, conversion_to_name)

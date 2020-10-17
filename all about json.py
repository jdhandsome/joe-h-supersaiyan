import requests
import json

#api call to hosting website
json_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
#gets json text from website
json_string = json.loads(json_todo.text)

#json list with global counters
completed=[]
counter = 0
total = 0
ct = 0
#loops through json string
for key in json_string:
    total = total + 1 #increments counter
    #finds the key completed, you can add virtually any key.If you search multiple keys, just put a comma and same content. i.e. (key['id'], key['title'])
    if (key['completed']) == True:
        #adds entry to completed list
        completed.append(key)
        #increments counter
        counter =  counter + 1
print('there are ' + str(counter) + ' people complete out of ' + str(total))

#convert list to json string
jl = json.dumps(completed, indent=4)

#encode json string to python
js = json.loads(jl)
#test encoding
print(js)

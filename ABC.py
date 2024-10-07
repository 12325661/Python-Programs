import json 
 
# Open the JSON file 
with open('ABC.json', 'r') as file: 
    # Load the contents into a Python dictionary 
    data = json.load(file) 
 
# Print the data 
print(data)
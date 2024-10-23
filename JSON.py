import json # This library holds all the built in json functions.
import re # This is the regex library and I need it for splitting the JSON strings when I load them


catalog = []


class inventory:

    data = dict()

    def __init__(self, name = 'Abrahms tank', number = 150, location = 'The Moon'):

        self.data["item_name"] = name
        self.data["item_number"] = number
        self.data["item_location"] = location

    def save(self, file):
        print(self.data)
        json.dump(self.data, file)

    def __str__(self):
        return(f"\n++++++++++++++++++NEXT ITEM++++++++++++++++++\nitem name is {self.data['item_name']}\nitem number is {self.data['item_number']}\nitem location is {self.data['item_location']}")


with open('JSON_test.json', 'r') as file:

    temp = file.read()

    print(temp)

while temp != '':

    found = re.search("}", temp) # re.search returns a match object, it contains the span function which tells where in the string the match was found

    if found == None:
        print('There has been an egregious error!')
        temp = ''

    else:

        temp2 = temp[0:found.span()[1]] # I need to reference the second value since the first is the match itself

        temp = temp[found.span()[1]:] # Now I trim the retrieved value from the list

        temp2 = json.loads(temp2) # This converts temp2 from a json string to a dictionary object

        print(f'Temp2 is {temp2} and temp is {temp}')
        
        temp3 = inventory(temp2['item_name'], temp2['item_number'], temp2['item_location'])

        catalog.append(temp3)
        
        print(catalog[0])


# Simple function to add an object to the list
def newJSON():

    name = input("Please enter the item's name: ")
    number = int(input("Please enter the number of items: "))
    location = input("Please enter the location where these items are kept: ")

    global catalog
    catalog.append(inventory(name, number, location))

def dispAll():
    for i in range(0,3,1):
        print(catalog[i])

    print('\n++++++++++++++++++END OF ITEMS++++++++++++++++++\n\n')

'''
This is a function which will take advantage of two other functions,
it will use newJSON and dispAll in order to change the selected object
'''
def editJSON():
    pass

def deleteJSON():
    pass

def abort():
    pass

def save():
    with open('JSON_test.json', 'w') as file:
        for item in catalog:
            item.save(file)

    global cont
    cont = False

# I have to do this because Python doesn't have a switch function
def switcher(arg, default):
    sw = {
        # Unfortunately I can't just execute functions from here for some reason...
        # So I send a function pointer back then call it from the menu loop
        1: newJSON,
        2: editJSON,
        3: deleteJSON,
        4: dispAll,
        5: abort,
        0: save
    }
    return sw.get(arg, default)


cont = True

# This is where my menu/main function runs
while cont == True:
    print('1. Create a new JSON')
    print('2. Manipulate a JSON')
    print('3. Delete a JSON')
    print('4. Display all JSON objects')
    print('5. Close and without saving')
    print('0. Close and save')
    choice = int(input('Please input your choice from above: '))

    print(choice, type(choice))

    # Now I reference the function I made earlier to get a makeshift switch
    func = switcher(choice, "You have not entered a correct choice, please try again.")

    func()

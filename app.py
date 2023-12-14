
import os
import json
from enum import Enum
from icecream import ic



class Actions(Enum):
    PRINT = 1
    ADD = 2
    SEARCH = 3
    DELETE = 4
    EXIT = 5
    
animals =[]
my_data_file ='animals.json'

def menu():
    for x in Actions:
        print(f'{x.value} - {x.name}')
        
    return Actions(int(input("Enter your selection:")))

def load_data(): #load a list from a file
    global animals
    with open(my_data_file, 'r') as file:
        json_string = file.read()
        animals = json.loads(json_string)
        
def main():
    os.system('cls' if os.name == 'nt' else 'clear') #clear screen
    load_data() #load data from a file
    
    while(True):
        userSelection = menu() #display a menu and get user selection and implements menu
        if userSelection == Actions.EXIT: exit_func()
        if userSelection == Actions.PRINT: ic(animals)
        if userSelection == Actions.ADD: add_animal()
        if userSelection == Actions.SEARCH: search_animal()
        if userSelection == Actions.DELETE: delete()
        
def add_animal():
    animals.append({"Name":input("Enter a name:"), "Type":input("Enter animal's type:"), "Age":input("Enter animal's age:")})
    
    
def exit_func():
    json_string = json.dumps(animals)
    #save the list in a file
    with open(my_data_file, 'w') as file:
        file.write(json_string)
    print("c ya")
    exit()
    
def search_animal():
    search_term = input("Enter a search term: ").lower()
    matching_animals = [
        animal for animal in animals
        if any(search_term in value.lower() for value in animal.values())
    ]
    if matching_animals:
        print("Matching contacts:")
        for animal in matching_animals:
            print(animal)
    else:
        print("No matching contacts found.")
        
def delete():
    global animals
    if not animals:
        print("No contacts to delete.")
        return

    search_term = input("Enter a search term (animal name/ age/ type) to delete: ").lower()
    matching_animals = [
        animal for animal in animals
        if any(search_term in value.lower() for value in animal.values())
    ]

    if matching_animals:
        print("Matching contacts:")
        for i, contact in enumerate(matching_animals, start=1):
            print(f"{i}. {contact}")

        try:
            index_to_delete = int(input("Enter the index of the contact to delete:")) - 1
            if 0 <= index_to_delete < len(matching_animals):
                deleted_animal = matching_animals[index_to_delete]
                animals.remove(deleted_animal)
                print(f"Contact {deleted_animal} deleted successfully.")
            else:
                print("Invalid index. No contact deleted.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
    else:
        print("No matching contacts found.")
    
if __name__ == "__main__":
    main()
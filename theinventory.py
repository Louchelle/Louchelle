#A program to help a store represent their inventory statistics
from tabulate import tabulate

#Opening the 'inventory.txt' and saving it as the variable: "file"
file = open('inventory.txt', 'r+')

#List of shoe objects (at least 5):
list_of_shoes = []


#Class Shoe:
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        self.value = int(cost) * int(quantity)

    def the_quantity(self):
        return self.quantity

    def the_country(self):
        return self.country

    def the_code(self):
        return self.code

    def the_product(self):
        return self.product
    
    def the_cost(self):
        return self.cost

    def the_value(self):
        return self.value

    def change_quantity(self, value):
        self.quantity = value
    
    def data(self):
        return f'''Country: {self.country}
Code: {self.code}
Product: {self.product}
Cost: {self.cost}
Quantity: {self.quantity}\n'''
    
#Function = read_data() - reading and printing the data of each item:
    def read_data():
        #Try-except block for reading:
        try:
            for line in file:
                raw_line_numbers = file.readlines()
                line_numbers = raw_line_numbers[1:]
                for line in line_numbers:
                    line = line.split(',')
                    print(line[0])      # Printing the countries of each item
                    print(line[1])      # Printing each items' codes
                    print(line[2])      # Printing each products' names
                    print(line[3])      # Printing each items' price
                    print(line[4])      # Printing the quantity of each item
        except FileNotFoundError:
            print("The file: 'inventory.txt' could not be found.")


#List of shoe objects (at least 5):
shoe1 = Shoe('South Africa', 'SKU44386', 'Air Max 90', '2300', '20')
shoe2 = Shoe('Russia', 'SKU89999', 'Air Force 1', '2000', '43')
shoe3 = Shoe('Egypt', 'SKU19888', 'Dunk SB', '1500', '26')
shoe4 = Shoe('Morocco', 'SKU77744', 'Challenge Court', '1450', '11')
shoe5 = Shoe('Brazil', 'SKU44600', 'Air Jordan 11', '3870', '24')
#Adding the shoe objects to 'list_of_shoes':
list_of_shoes.append(shoe1)
list_of_shoes.append(shoe2)
list_of_shoes.append(shoe3)
list_of_shoes.append(shoe4)
list_of_shoes.append(shoe5)

def writing_to_file():
    for shoe_list_object in list_of_shoes:
        file.write(shoe_list_object.data())
        file.write("\n")

#Lowest quintity
def lowest_quantity(list_of_shoes):
    low_value = list_of_shoes[0]
    for low in list_of_shoes:
        if low.the_quantity() < low_value.the_quantity():
            low_value = low
    return low_value
    #Restock


#Highest quantity
def highest_quantity():
    high_value = list_of_shoes[0]
    for high in list_of_shoes:
        if high.the_quantity() > high.the_quantity():
            high_value = high
    print(high_value.data(), "\nThe item has been marked as sale\n")


#value_per_item
def value_per_item():
    for line in file:
        line = line.split(',')
        if line[0] != "Country":
            equition = int(line[3]) * int(line[4])
            return equition



#MENU
while True:
#Options:
    options = input('''Enter the number of the option you want to select & press Enter.

Options:
1: View the information of each item in the inventory.
2: Search shoes by item code.
3: View the information of the item with the lowest quantity.
4: View the information of the item with the highest quantity.
5: View the table of the objects shoe list.
e: Exit
:''')
#If options =   
    if options == "1":      # Working
        print("Each item and its' information as found in the inventory.txt file:")
        print(Shoe.read_data())

#Elif options = 2
    elif options == "2":
        print("Search shoes by item code.")
        item_code = input("Enter the code of the item you want to find:\n")
        print("The item you searched for is:\n")
        for line in file:
            line = line.split(',')
            if line[1] == item_code:
                print(f"Country: {line[0]}" +
               '\n' + f"Code: {line[1]}" +
               '\n' + f"Product: {line[2]}" +
               '\n' + f"Cost: {line[3]}" +
               '\n' + f"Quantity: {line[4]}")
       

#Elif options = 3
    elif options == "3":
        print("The item with the lowest quantity is:\n")
        lowest = lowest_quantity(list_of_shoes)
        print(lowest.data())
        #restock
        menu = input('''Do you want to order new stock?
1: Yes
2: No
:''')
        if menu == "1":
            stock = input("Enter the amount of the current item you want to order.")
            print('''\nNew stock has been ordered
Latest arrival: next friday\n''')
                
#Elif options = 4
    elif options == "4":
         print("The item with the highest quantity is:\n")
         highest_quantity()

#Elif options = 5

    elif options =="5":
        print("Table based on the objects shoe list:")

        with open('new_inventory.txt', 'r') as file2:
            read_line = file2.readlines()
            data = []
            for row in read_line:
                data.append(row.rstrip().split(','))
            header = data
            table = tabulate(data, headers = ["Country", "Code", "Product", "Cost", "Quantity", "value_per_item()"])
            print(table)
        
        
#Elif options = e
    elif options == "e":
        print("Goodbye")
        file.close()
        break


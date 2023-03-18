#import tabulate
from tabulate import tabulate
class Shoes:
   def __init__(self, country, code, product, cost, quantity):
       self.country = country
       self.code = code
       self.product = product
       self.cost = cost
       self.quantity = quantity
   #method to return the cost of the shoes
   def get_cost(self):
       return self.cost
   #method to return the quantity of the shoes
   def get_quantity(self):
       return self.quantity
   #defining a function get country
   def get_country(self):
        return self.country
   #defining the function get code
   def get_code(self):
        return self.code
   #defining the fundtion get product 
   def get_product(self):
        return self.product
   #method that reprresents the string representation of a class
   def __str__(self):
       return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

inventory_read = open("inventory.txt", "r")
inventory_write = open("inventory.txt", "a+")

shoes_list = []
shoes_obj = []
#empty list to store the shoes objects
def read_shoes_data(): #function to read the shoes from the file inventory.txt
   #reading data from the file
   file = None
   try:
       for lines in inventory_read:
            strip_lines = lines.strip("\n")
            split_lines = strip_lines.split(",")
            shoes_list.append(split_lines)

       for i in range(1, len(shoes_list)):
          items = shoes_list[i]
          shoe1 =  Shoes(items[0], items[1], items[2], items[3], int(items[4]))
          shoes_obj.append(shoe1)      
           
   except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

   finally:
      if file is not None:
          file.close()
              
def capture_shoes(): #function to capture data about a shoe
   #below required information about the shoe is stored in variables
   country = input("Enter the country of origin: ")
   code = input("Enter the SKU code: ")
   product = input("Enter the product name: ")
   cost = input("Enter the cost: ")
   quantity = input("Enter the quantity: ")
   shoe = Shoes(country, code, product, cost, quantity)
   #storing the data of the shoe on the list
   shoes_list.append(shoe)
   inventory_write.write(f'\n{country},{code},{product},{cost},{quantity}')
   print("\nThank you, your product has been loaded!\n")

   inventory_write.close()
   
def view_all(): #function to view the content of the shoes
   file = None
   try:

        print("\n---------------------------------------------STOCKLIST---------------------------------------------\n")
        #cxreating empty lists to store data that will be displayed
        country = []
        code = []
        product = []
        cost = []
        table  = []
        quantity = []

        for lines in shoes_obj:
            country.append(lines.get_country())
            code.append(lines.get_code())
            product.append(lines.get_product())
            cost.append(lines.get_cost())
            quantity.append(lines.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid'))

        print("\n---------------------------------------------END-------------------------------------------------\n")

   except FileNotFoundError as error:
      print("\nSorry, this file does not exist!\n")
      print(error)
      
      
   finally:
      if file is not None:
            file.close()      

def re_stock():
   #dedrtemining and storing the shoe with the lowest quantity in variable min_quality
   min_quantity_shoe = min(shoes_obj, key=lambda x: x.quantity)
   #asking for user input
   #if the user wants to restock then the quantity is updated 
   response = input(f"Do you want to restock {min_quantity_shoe.product}? (y/n) ")
   #if the user chooses y, then the item is updated
   if response == "y":
       quantity = input("Enter the new quantity: ")
       min_quantity_shoe.quantity = quantity
       output = ''
       for item in shoes_obj:
            output += (f'{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n')

       file2 = open("inventory.txt", "w")
       file2.write(output)
       file2.close()

       print("Item has benn added")
       
def search_shoe(code):#function that allows the user to search for a specific shoe
   for shoe in shoes_obj:
       if shoe.code == code:
           return shoe
         
def value_per_item():#function to calculate the total value of shoe
   for shoe in shoes_obj:
       value = int(shoe.cost) * int(shoe.quantity)
       print(f"{shoe.product}: {value}")
       
def highest_quantity():#function to dertemine the shoe with highest quality and storing in the variable below

    highest_qua = []

    for line in shoes_obj:
        highest_qua.append(line)

    print("\n----------------------------Highest stock item:----------------------------\n")

    print(max(shoes_obj, key=lambda item: item.quantity))
    print("\nThis item has now been marked on sale\n")
    print("\nPlease select an option from the menu below")

# ====================================================== OUTPUT =============================================== #

def main():
   read_shoes_data()
   while True:
      #Display instructions to the user
       print("1. Capture shoes")
       print("2. View all shoes")
       print("3. Restock shoes")
       print("4. Search for a shoe")
       print("5. Calculate value per item")
       print("6. Determine highest quantity shoe for sale")
       print("7. Exit")
       choice = int(input("Enter your choice: "))
       if choice == 1:
           capture_shoes()
       elif choice == 2:
           view_all()
       elif choice == 3:
           re_stock()
       elif choice == 4:
           code = input("Enter the SKU code: ")
           shoe = search_shoe(code)
           if shoe:
               print(shoe)
           else:
               print("Shoe not found.")
       elif choice == 5:
           value_per_item()
       elif choice == 6:
           highest_quantity()
       elif choice == 7:
           break
main()

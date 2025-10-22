#define the main function for the taqueria ordering system
def taqueria():
    cash = 0 #initialize the total cost to 0

    #define the menu as a dictionary; item name:price
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

    #start an infinite loop to continuously prompt the user for orders
    while True:
        try:
            #prompt the user for an input item; title() capitalizes each word to match menu keys
            item = input("Item: ").title()

            #check if the input item is in the menu
            if item in menu:
                cash += menu[item] #add the item's price to the total
                #print the updated total with 2 decimal places
                print(f"Total: ${cash:.2f}")

        except EOFError:
            #exit the loop on EOF (Ctrl+D or Ctrl+Z)
            break

#call the function to start the program
taqueria()

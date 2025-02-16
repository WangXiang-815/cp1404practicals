def main():                                     #define main
    items_num = int(input("Number of items: ")) #get number of items
    while items_num <= 0:
        print("Invalid number of items, please enter valid number") #error checking
        items_num = int(input("Number of items: ")) #If invalid num is input, then input again.

    total_price = 0

    for i in range(items_num):            #get every item's price through for loop
        price = float(input("Please input price of item: "))
        total_price += price

    if total_price > 100:                   #determine whether if there's discount
        total_price = total_price * 0.9

    print(f"Total price for {items_num} items is ${total_price:.2f}") #print the output in 2 2 decimal places.

main()                   #using main for avoiding global variable pollution

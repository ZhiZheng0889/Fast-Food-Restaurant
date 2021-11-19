#simple list search by looping through the list to find
def search(products):
    for i in range(0, len(product_names) + 1):
        if i == listlength:
            print(f"Sorry, we don't sell {productsearch}.")

        elif product_names[i] == productsearch:
            print(f"We sell {product_names[i]} at {product_costs[i]} per unit")
            print(f"We currently have {product_quantity[i]} in stock")
            return
#printing the lists in a table format with format method and zip method
def productlist():
    print("{:<15} {:<15} {:<10}".format("Product", "Price", "Quantity"))
    for (i, j, k) in zip(product_names, product_costs, product_quantity):
        print("{:<15} {:<15} {:<10}".format(i, j, k))
    return

#add new product into the database by triple looping(one for name, one for cost, and one for quantity)
def addproduct():
    newproduct = input("Enter a new product name: ")
    for i in range(0, len(product_names) + 1):
        print(i)
        if i == listlength:
            product_names.append(newproduct)
            h = 0
            while h < 4:
                try:
                    newprice = (input("Enter a product cost:"))
                    test1 = float(newprice)
                    if test1 <= 0.0:
                        print("Invalid cost try again")
                    else:
                        product_costs.append(test1)

                        while h < 4:
                            try:
                                newquantity = input("Enter a product quantity:")
                                test2 = int(newquantity)
                                if test2 <= 0:
                                    print("Invalid quantity try again")
                                else:
                                    product_quantity.append(test2)
                                    h = 5

                            except ValueError:
                                print("Oops!  That was no valid number.  Try again...")

                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            print("Product added!")
            return product_names, product_costs, product_quantity

        elif product_names[i] == newproduct:
            print(f"We already sell {product_names[i]}.")
            return

#removing object from lists through pop function
def removeproduct():
    productremove = input("Enter a product name: ")
    for i in range(0, len(product_names) + 1):
        if i == listlength:
            print(f"Product doesn't exist. Can't remove {productremove}.")

        elif product_names[i] == productremove:
            product_names.pop(i)
            product_costs.pop(i)
            product_quantity.pop(i)
            print(f"Product {productremove} removed.")
            return

#updating objects in the lists by finding the object place in the list
#Then replace object in that place with new object
def updateproduct():
    productupdate = input("Enter a product name: ")
    for i in range(0, len(product_names) + 1):
        print(i)
        if i == listlength:
            print("Product doesn't exist. Can't update.")

        elif product_names[i]==productupdate:
            updatechoice = input("What would you like to update? \b (n)ame, (c)ost or (q)uantity: ")
            if updatechoice == 'n':
                try:
                    newname = input('Enter a new name: ')
                    if product_names[i] == newname:
                        print('Duplicate name!')
                    elif product_names[i] != newname:
                        product_names[i] = newname
                        print('Product name has been updated')
                except ValueError:
                    print("Oops!  That was no valid number. Try again...")

            if updatechoice == 'c':
                try:
                    newcost = float(input('Enter a new cost: '))
                    if newcost <= 0.0:
                        print("Invalid cost!")
                    elif newcost > 0.0:
                        product_names[i] = newcost
                        print('Product cost has been updated')
                except ValueError:
                    print("Oops!  That was no valid number. Try again...")

            if updatechoice == 'q':
                try:
                    newquantity = int(input('Enter a new name: '))
                    if newquantity <= 0:
                        print("Invalid cost!")
                    elif newquantity > 0:
                        product_quantity[i] = newquantity
                        print('Product quantity has been updated')

                except ValueError:
                    print("Oops!  That was no valid number. Try again...")
            else:
                print("Invalid entry, please try again!")
        return

def productreport():
    for i in range(0, len(product_names)):
        product = (float(product_costs[i])*float(product_quantity[i]))
    return

product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_quantity = [10, 5, 20]

while True:
    listlength = (len(product_names))

    searchinput = input('(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ')

    if searchinput == 's':
        productsearch = input("Enter a product name: ")
        search(productsearch)

    elif searchinput == 'l':
        productlist()

    elif searchinput == 'a':
        addproduct()

    elif searchinput == 'r':
        removeproduct()

    elif searchinput == 'u':
        updateproduct()

    elif searchinput == 'e':
        productreport()

    elif searchinput == 'q':
        print('See you soon!')
        break

    else:
        print('Invalid option, try again.')

    print(product_names, product_costs, product_quantity)
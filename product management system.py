products = []
prices = []

while True:
    print("\n===== PRODUCT MENU =====")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Update Product Price")
    print("4. Delete Product")
    print("5. search")

    choice = int(input("Enter your choice: "))

    # Add product
    if choice == 1:
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))

        products.append(product)
        prices.append(price)

        print("Product added successfully!")

    # Display products
    elif choice == 2:
        if len(products) == 0:
            print("No products available.")
        else:
            print("\n--- Product List ---")
            for i in range(len(products)):
                print(products[i], "₹", prices[i])

    #update product price
    elif choice ==3:
        product = input("Enter product name: ")
        if product in products:
            index=products.index(product)
            updated_price = input("Enter updated price ")
            prices[index]=updated_price
            print("uodated sucessfully ")
        else:
            print("product is not available ")
    #delete product
    elif choice ==4:
            product = input("Enter product name: ")
            if product in products:
                index=products.index(product)
                products.pop(index)
                prices.pop(index)
                print("deleted sucessfully ")
            else:
                print("product is not available ")
    #search
    elif choice ==5:
        product = input("Enter product name: ")
        if product in products:
            print("product is available")
            index=products.index(product)
            print(products[index],prices[index])
        else:
            print("product is not available ")

    

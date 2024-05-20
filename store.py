"""ساخت یک فروشگاه برای محصولات خوراکی که محصولات را نمایش میدهد مدیریت بتواند  کارهای خاصی انجام دهد
و اطلاعات مشتریان و خرید ها ذخیره  شود"""
def __init__(self):
    self.inventory = {
        "milk": {"inventory": 10, "price": 100},
        "yogurt": {"inventory": 1, "price": 300},
        "fruit_juice": {"inventory": 30, "price": 100},
        "cake": {"inventory": 5, "price": 50},
        "ice_cream": {"inventory": 15, "price": 150},
    }
    self.income = 0
    self.customers = []

def add_product(self, product_name, inventory, price):
    self.inventory[product_name] = {"inventory": inventory, "price": price}

def run(self):
    while True:
        print("Hello and welcome to the supermarket, please enter your name:")
        customer_name = input()

        if customer_name == "boss":
            self.handle_boss()
        else:
            self.handle_customer(customer_name)
def handle_customer(self, customer_name):
    print(f"hi {customer_name} ,list product")
    for product_name, product_info in self.inventory.items():
        print(f"- {product_name}: {product_info['inventory']} price: {product_info['price']} ")

    chosen_product = input("Please select your desired product: ")
    if chosen_product not in self.inventory:
        print(f"  The'{chosen_product}' is not available")
        return

    product_info = self.inventory[chosen_product]
    if product_info["inventory"] == 0:
        print(f" The '{chosen_product}' product is finished")
        return

    quantity = int(input(f"{chosen_product} Enter the number you want"))
    if quantity > product_info["inventory"]:
        print(f"{chosen_product} {product_info['inventory']} This number is not available")
        return

    price = product_info["price"] * quantity
    if input(f"Do you want a discount?(yes/no): ").lower() == "yes":
        price -= 10

    self.income += price
    product_info["inventory"] -= quantity
    self.customers.append((customer_name, chosen_product, quantity))
    print(f"Thanks for your purchase{customer_name} Your payment amount{price} ")

    def handle_boss(self):
        print("Hello, dear manager, please select the type of information you want:")
        print("1-List of customer names")
        print("2- number of customers")
        print("3- Total revenue")
        print("4- List of available products")
        print("5- List of finished products")
        print("6- Sara  shopping review")
        print("7- Add new product")

        choice = input("your choice: ")

        if choice == "1":
            print("List of customer names:")
            for customer_name in self.get_customer_names():
                print(customer_name)
        elif choice == "2":
            print(f"Number of customers: {len(self.customers)}")
        elif choice == "3":
            print(f"Total revenue: {self.income} ")
        elif choice == "4":
            print("List of available products:")
            for product_name, product_info in self.inventory.items():
                print(f"- {product_name}: {product_info['inventory']} number")
        elif choice == "5":
            print("List of finished products:")
            for product_name in self.get_out_of_stock_products():
                print(product_name)
        elif choice == "6":
            self.handle_boss_question_about_sara()
        elif choice == "7":
            self.add_new_product()
        else:
            print("Invalid selection.")
            
def get_customer_names(self):
    return [customer_name for customer_name, _, _ in self.customers]

        
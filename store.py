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
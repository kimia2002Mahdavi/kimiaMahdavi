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
class Product:
    def __init__(self, name, category, price, kil):
        self.name = name
        self.category = category
        self.price = price
        self.kil = kil

    def change_price(self, new_price):
        self.price = new_price

    def change_kil(self, new_kil):
        self.kil = new_kil


class Order:
    def __init__(self):
        self.products = []
        self.total = 0

    def add_product(self, product, kil):
        if product.kil >= kil:
            self.products.append((product, kil))
            product.kil -= kil
        else:
            print("Not have the product :")

    def calculator_tovar(self):
        self.tovar = 0
        for product, kil in self.products:
            self.tovar += product.price * kil
        return self.tovar


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

def load_products(filename):
    products = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, category, price, kil = line.strip().split(",")
            product = Product(name, category, float(price), int(kil))
            products.append(product)

    return products
def load_customers(filename):
    customers = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, email = line.strip().split(",")
            customers.append(Customer(name, email))

    return customers

def load_orders(filename, products, customers):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(";")

            email = parts[0]

            # знаходимо клієнта
            customer = next((c for c in customers if c.email == email), None)
            if not customer:
                continue

            order = Order()

            for item in parts[1:]:
                product_name, k = item.split(":")
                k = int(k)

                # знаходимо товар
                product = next((p for p in products if p.name == product_name), None)

                if product:
                    order.add_product(product, k)

            customer.add_order(order)
products = load_products("products.txt")
customers = load_customers("customers.txt")

load_orders("orders.txt", products, customers)
print("------Goods--------")
for p in products:
    print(f"{p.name} | {p.category} | {p.price} | {p.kil}")

print("\n********Customers**************")

for c in customers:
    print(f"{c.name}, Email: {c.email}")

    if not c.orders:
        print("  No order")
        continue

    for i, order in enumerate(c.orders, 1):
        print(f"  Order {i}:")

        for product, k in order.products:
            print(f"    {product.name} x{k}")

        print(f"    Total: {order.calculator_tovar()}")
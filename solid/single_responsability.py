"""
This is the first principle of the SOLID method:
Single responsibility = High cohesion.
Using class that are responsible for only a single thing ensure that they are way more reusable.
In our case, the order class deals with order AND with payments, this clearly if 2 responsibilities.
Here's how we can improve cohesion of the Order class
"""


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def set_status(self):
        self.status = "Paid"


class PaymentProcessor:

    @staticmethod
    def pay_debit(security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")

    @staticmethod
    def pay_credit(security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 10)

    print(order.total_price())
    payment_processor = PaymentProcessor()
    payment_processor.pay_credit("0546466")
    order.set_status()


if __name__ == "__main__":
    main()
"""
The second principle is : Open/Closed.
This means our code should be open for extensions but closed to modifications.
We should be able to extend the current functionalities of our code without having to modify it.
Here's how we can improve that for the payment classes.
In order to add a payment method we now don't have to modify the PaymentProcessor class
"""

from abc import ABC, abstractmethod


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
    @abstractmethod
    def pay(self, security_code):
        pass


class CreditPaymentProcessor(PaymentProcessor):

    def pay(self, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")


class DebitPaymentProcessor(PaymentProcessor):

    def pay(self, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")


class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, security_code):
        print("Processing paypal payment type")
        print(f"Verifying security code: {security_code}")


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 10)

    print(order.total_price())
    payment_processor = CreditPaymentProcessor()
    payment_processor.pay("0546466")
    order.set_status()


if __name__ == "__main__":
    main()
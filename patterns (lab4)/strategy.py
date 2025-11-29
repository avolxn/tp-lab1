class PaymentStrategy:
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Оплата {amount} картой"


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Оплата {amount} PayPal"


class PaymentProcessor:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount: float):
        if self.strategy:
            return self.strategy.pay(amount)
        return "Стратегия не выбрана"


if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.set_strategy(CreditCardPayment())
    print(processor.process_payment(1000))
    processor.set_strategy(PayPalPayment())
    print(processor.process_payment(500))

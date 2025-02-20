from abc import ABC, abstractmethod


class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, card_info: dict) -> None:
        pass

    @abstractmethod
    def refund_payment(self, amount: float) -> None:
        pass

    @abstractmethod
    def get_transaction_status(self, transaction_id: str) -> str:
        pass


class PayPalAPI:
    def make_payment(self, value: float, paypla_data: dict) -> None:
        print(f"Processing payment of {value} with card info: {paypla_data}")

    def reverse_transaction(self, payment_id: str) -> None:
        print(f"Reversing transaction {payment_id}")

    def check_status(self, payment_id: str) -> str:
        return f"Transaction {payment_id} is successful"


class StripeAPI:
    def charge(self, amount: int, stripe_token: str) -> None:
        print(f"Charging {amount} with stripe token: {stripe_token}")

    def refund(self, charge_id: str) -> None: 
        print(f"Refunding charge {charge_id}")

    def get_charge_status(self, charge_id: str) -> str:
        return f"Charge {charge_id} is successful"


class StripeAdapter(IPaymentProcessor):
    def __init__(self, stripe_api: StripeAPI):
        self.stripe_api = stripe_api

    def process_payment(self, amount: float, card_info: dict) -> None:
        self.stripe_api.charge(amount, card_info["stripe_token"])

    def refund_payment(self, amount: float) -> None:
        self.stripe_api.refund(amount)

    def get_transaction_status(self, transaction_id: str) -> str:
        return self.stripe_api.get_charge_status(transaction_id)


class PayPalAdapter(IPaymentProcessor):
    def __init__(self, paypall_api: PayPalAPI):
        self.paypall_api = paypall_api

    def process_payment(self, amount: float, card_info: dict) -> None:
        self.paypall_api.make_payment(amount, card_info)

    def refund_payment(self, amount: float) -> None:
        self.paypall_api.reverse_transaction(amount)

    def get_transaction_status(self, transaction_id: str) -> str:
        return self.paypall_api.check_status(transaction_id)


class PaymentProcessor:
    def __init__(self, payment_processor: IPaymentProcessor):
        self.payment_processor = payment_processor

    def process_payment(self, amount: float, card_info: dict) -> None:
        self.payment_processor.process_payment(amount, card_info)

    def refund_payment(self, amount: float) -> None:
        self.payment_processor.refund_payment(amount)

    def get_transaction_status(self, transaction_id: str) -> str:
        return self.payment_processor.get_transaction_status(transaction_id)


paypal_api = PayPalAPI()
stripe_api = StripeAPI()

paypal_adapter = PayPalAdapter(paypal_api)
stripe_adapter = StripeAdapter(stripe_api)

payment_processor = PaymentProcessor(paypal_adapter)
payment_processor.process_payment(100, {"stripe_token": "1234567890"})

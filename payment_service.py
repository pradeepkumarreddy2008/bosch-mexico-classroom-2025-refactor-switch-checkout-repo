from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

# Checkout function
def checkout(mode: PaymentMode, amount: float):
    match mode:
        case PaymentMode.PAYPAL:
            print(f"Processing PayPal payment of ${amount:.2f}")
            process_paypal(amount)
            # Add PayPal-specific logic here

        case PaymentMode.GOOGLEPAY:
            print(f"Processing GooglePay payment of ${amount:.2f}")
            # Add GooglePay-specific logic here
            process_googlepay(amount)

        case PaymentMode.CREDITCARD:
            print(f"Processing Credit Card payment of ${amount:.2f}")
            # Add Credit Card-specific logic here
            process_creditcard(amount)

        case _:
            print("Invalid payment mode selected!")


# ====== Payment mode functions ======
def process_paypal():
    print("Paypal Handler is executing")


def process_googlepay():
    print("Google Pay Handler is executing")


def process_creditcard():
    print("Credit Card Handler is executing")
# ====================================


# Example usage
if __name__ == "__main__":
    amount = 150.75

    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)

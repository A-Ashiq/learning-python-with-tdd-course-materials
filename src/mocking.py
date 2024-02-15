import time


class User:
    def __init__(self, email_address: str):
        self.email_address = email_address


def notify_user(user: User) -> None:
    email_address: str = user.email_address
    send_email(email_address=email_address)
    # do some other stuff


def send_email(email_address: str) -> None:
    time.sleep(10)

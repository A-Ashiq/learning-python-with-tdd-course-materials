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


def do_something_first() -> None:
    ...


def do_something_following() -> None:
    ...


def do_something_next() -> None:
    ...


def do_something_last() -> None:
    ...


def some_func() -> None:
    do_something_first()
    do_something_following()
    do_something_next()
    do_something_last()
    # Do other stuff

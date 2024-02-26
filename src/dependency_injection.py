import time


class User:
    def __init__(self, user_id: int):
        self.user_id = user_id


class UserRepository:
    @classmethod
    def get_user(cls, user_id: int) -> User:
        time.sleep(5)  # Wait for 5s to emulate db query
        return User(user_id=user_id)


class UserInterface:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user(self, user_id: int) -> User:
        user = self.repository.get_user(user_id=user_id)

        # do some extra stuff
        return user

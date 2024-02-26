from src.dependency_injection import User, UserInterface


class FakeUserRepository:
    def __init__(self, users: list[User]):
        self._users = users

    def get_user(self, user_id: int) -> User:
        return next(user for user in self._users if user.user_id == user_id)


class TestUserInterface:
    def test_get_user(self):
        """
        Given a `User` object
        When `get_user()` is called from an instance of `UserInterface`
        Then the correct `User` object is returned
        """
        # Given
        user_id = 123
        user = User(user_id=user_id)
        fake_user_repository = FakeUserRepository(users=[user])
        user_interface = UserInterface(respository=fake_user_repository)

        # When
        retrieved_user: User = user_interface.get_user(user_id=user_id)

        # Then
        assert retrieved_user == user

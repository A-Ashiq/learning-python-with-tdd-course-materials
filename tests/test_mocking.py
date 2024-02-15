from unittest import mock

from src.mocking import User, notify_user


class TestMocking:
    @mock.patch(target="src.mocking.send_email")
    def test_send_email_is_called_with_correct_arg(
        self, spy_send_email: mock.MagicMock
    ):
        """
        Given a `User` object
        When `notify_user()` is called
        Then the call is delegated
            to the `send_email()` function
        """
        # Given
        email_address = "jane.doe@gmail.com"
        user = User(email_address=email_address)

        # When
        notify_user(user=user)

        # Then
        spy_send_email.assert_called_once_with(email_address=email_address)

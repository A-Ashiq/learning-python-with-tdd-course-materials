from unittest import mock

from src.mocking import User, notify_user, some_func, some_func_revised


class TestNotifyUser:
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


class TestSomeFunc:
    @mock.patch(target="src.mocking.do_something_first")
    @mock.patch(target="src.mocking.do_something_following")
    @mock.patch(target="src.mocking.do_something_next")
    @mock.patch(target="src.mocking.do_something_last")
    def test_code_smell_patch_stack(
        self,
        mocked_do_something_first: mock.MagicMock,
        mocked_do_something_following: mock.MagicMock,
        mocked_do_something_next: mock.MagicMock,
        mocked_do_something_last: mock.MagicMock,
    ):

        some_func()


class TestSomeFuncRevised:
    @mock.patch(target="src.mocking.do_first_steps")
    @mock.patch(target="src.mocking.do_last_steps")
    def test_code_smell_patch_stack(
        self,
        mocked_do_first_steps: mock.MagicMock,
        mocked_do_last_steps: mock.MagicMock,
    ):

        some_func_revised()

import pytest

from app.services.users import User, create_user


def test_create_user_success():
    user = create_user("Alice")

    assert isinstance(user, User)
    assert user.id == 1
    assert user.name == "Alice"


def test_create_user_empty_name():
    with pytest.raises(ValueError) as exc:
        create_user("")

    assert str(exc.value) == "Name is required"

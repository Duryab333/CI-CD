from app import create_message


def test_create_message_with_name() -> None:
    assert create_message("Duryab") == "Hello, Duryab!"


def test_create_message_default_value() -> None:
    assert create_message() == "Hello, DevOps!"

def create_message(name: str = "DevOps") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main() -> None:
    """Run the application."""
    print(create_message())


if __name__ == "__main__":
    main()

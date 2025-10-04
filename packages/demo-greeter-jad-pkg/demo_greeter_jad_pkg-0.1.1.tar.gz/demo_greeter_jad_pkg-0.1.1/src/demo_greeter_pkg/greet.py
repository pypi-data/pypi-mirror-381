def greet(name: str = None) -> str:
    """Return a friendly greeting."""
    if not name:
        name = "World"
    return f"Hello, {name}!"


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Say hello from the command line.")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))
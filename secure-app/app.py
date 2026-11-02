def run_command(user_input: str) -> None:
    if not isinstance(user_input, str):
        raise TypeError("Input must be text")

    print(user_input)


if __name__ == "__main__":
    message = input("Enter a message: ")
    run_command(message)

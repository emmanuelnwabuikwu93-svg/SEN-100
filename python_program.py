def greet(name):
    return f"Hello {name}! Welcome to my portfolio."

if __name__ == "__main__":
    user_name = input("Enter your name: ").strip() or "friend"
    print(greet(user_name))

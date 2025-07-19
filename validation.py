from display_menu import menu

def login():
    saved_pin = '1234'
    attempts = 3

    while attempts > 0:
        user_pin = input("Enter your 4 digit pin: ")

        if len(user_pin) != 4:
            print("Try Again! Enter a four-digit pin.")
            continue

        if user_pin == saved_pin:
            print("Login successful ")
            menu()
            break
        else:
            attempts -= 1
            print(f"Wrong pin entered! Attempts left: {attempts}")

            if attempts == 0:
                print("Account frozen for 24 hours.")
                return

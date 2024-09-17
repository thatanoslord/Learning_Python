import random
rand_pin = random.randint(1000, 9999)
pin_code = int(input("Enter you 4-Digit PIN CODE: "))
if len(str(pin_code)) != 4:
    print(f"{pin_code} is not 4-Digits. Please enter 4-Digit PIN CODE")
else:
    if rand_pin == pin_code:
        print(f"Your PIN Code is matching the machine PIN Code {rand_pin}")
    else:
        print(f"You Your PIN Code '{pin_code}' does not match the machine PIN Code {rand_pin}")
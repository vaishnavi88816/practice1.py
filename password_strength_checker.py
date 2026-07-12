def check_password(password):
    length = len(password) >= 8
    upper = False
    lower = False
    digit = False
    special = False

    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        elif char in special_chars:
            special = True

    print("\nPassword Analysis")
    print("-" * 20)

    if length:
        print("✅ Length: Good")
    else:
        print("❌ Password should be at least 8 characters.")

    if upper:
        print("✅ Uppercase letter found")
    else:
        print("❌ Add at least one uppercase letter.")

    if lower:
        print("✅ Lowercase letter found")
    else:
        print("❌ Add at least one lowercase letter.")

    if digit:
        print("✅ Number found")
    else:
        print("❌ Add at least one number.")

    if special:
        print("✅ Special character found")
    else:
        print("❌ Add at least one special character.")

    if length and upper and lower and digit and special:
        print("\n🎉 Strong Password")
    else:
        print("\n⚠️ Weak Password")


password = input("Enter your password: ")
check_password(password)
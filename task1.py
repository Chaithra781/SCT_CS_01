def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'e':
        result = caesar_encrypt(text, shift)
        print("Encrypted message:", result)
    elif choice == 'd':
        result = caesar_decrypt(text, shift)
        print("Decrypted message:", result)
    else:
        print("Invalid choice. Use 'e' or 'd'.")

if __name__ == "__main__":
    main()

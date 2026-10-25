
def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


print("=== Caesar Cipher Encryption Tool ===")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose an option (1 or 2): ")
text = input("Enter your message: ")
shift = int(input("Enter shift value (key): ")) % 26

if choice == "1":
    encrypted = caesar_cipher(text, shift, "encrypt")
    print("Encrypted text:", encrypted)

elif choice == "2":
    decrypted = caesar_cipher(text, shift, "decrypt")
    print("Decrypted text:", decrypted)

else:
    print("Invalid choice. Please select 1 or 2.")

import hashlib
import random
from os import system


# TODO: Randomly select a song from the list as the key
def select_random_song(songs):
    return random.choice(songs)

# TODO: Generate a pseudo-random key from a list of song titles
def generate_key(songs, text_length):
    key = ''.join(songs).replace(' ', '').upper()
    return (key * (text_length // len(key) + 1))[:text_length]

# TODO: Vigenère Cipher Encryption
def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)].upper()) - 65
            encrypted_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# TODO: Vigenère Cipher Decryption
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ''
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)].upper()) - 65
            decrypted_char = chr((ord(char.upper()) - shift - 65) % 26 + 65)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# TODO: Generate hash code
def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# TODO: Encrypt text and merge with hash code
def encrypt(plain_text, songs):
    song_title = select_random_song(songs)
    encrypted_text = vigenere_encrypt(plain_text, song_title)
    hash_code = generate_hash(encrypted_text)
    with open('decrypt.txt', 'a') as file:
        file.write(f"{encrypted_text}#{hash_code}: {plain_text}\n")
    return f"{encrypted_text}#{hash_code}"

# TODO: Find original text from decrypt.txt
def find_original_text(encrypted_text, hash_code):
    with open('decrypt.txt', 'r') as file:
        for line in file:
            if line.startswith(f"{encrypted_text}#{hash_code}"):
                return line.split(': ')[1].strip()
    return "No matching record found."

# TODO: Decrypt text and write to file
def decrypt(merged_text, song_title, original_text):
    encrypted_text, hash_code = merged_text.split('#')
    if generate_hash(encrypted_text) == hash_code:
        decrypted_text = vigenere_decrypt(encrypted_text, song_title)
        with open('decrypt.txt', 'a') as file:
            file.write(f"Original: {original_text}, Decrypted: {decrypted_text}, Hash: {hash_code}\n")
        return decrypted_text
    else:
        return "Invalid hash code. Decryption failed."


# MAIN PROGRAM
def main():
    songs = open('database.txt').read().splitlines()

    while True:
        print("""
══════════════════════════════════════════

█▀ █░█░█ █ █▀▀ ▀█▀
▄█ ▀▄▀▄▀ █ █▀░ ░█░

█▀▀ █ █▀█ █░█ █▀▀ █▀█
█▄▄ █ █▀▀ █▀█ ██▄ █▀▄

        
────█▀█▄▄▄▄─────██▄
────█▀▄▄▄▄█─────█▀▀█
─▄▄▄█─────█──▄▄▄█
██▀▄█─▄██▀█─███▀█
─▀▀▀──▀█▄█▀─▀█▄█▀

              
░ © 2023 | 13522140 Yasmin Farisah Salma ░
══════════════════════════════════════════
""")
        choice = input("""
                       
█▀▄▀█ █▀▀ █▄░█ █░█ ▀
█░▀░█ ██▄ █░▀█ █▄█ ▄
═════════════════════
              
░ 1. Encrypt
░ 2. Decrypt
░ 3. Exit

░ Choose: """)

        if choice == '1':
            print()
            system('pause')
            system('cls')
            print("""

█▀▀ █▄░█ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █ █▀█ █▄░█
██▄ █░▀█ █▄▄ █▀▄ ░█░ █▀▀ ░█░ █ █▄█ █░▀█
════════════════════════════════════════
                  
                  """)
            user_plain_text = input("░ Plain text\t\t: ")
            merged_encrypted_text = encrypt(user_plain_text, songs)
            print("░ Encrypted text\t:", merged_encrypted_text)

        elif choice == '2':
            print()
            system('pause')
            system('cls')
            print("""

█▀▄ █▀▀ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █ █▀█ █▄░█
█▄▀ ██▄ █▄▄ █▀▄ ░█░ █▀▀ ░█░ █ █▄█ █░▀█
═══════════════════════════════════════
                                    
                  """)
            encrypted_text = input("░ Decrypted text\t: ")
            hash_code = input("░ Hash code\t\t: ")
            original_text = find_original_text(encrypted_text, hash_code)
            if original_text != "No matching record found.":
                print("Original Text\t:", original_text)
            else:
                print("\n░ Decryption FAILED.\n░ Invalid encrypted text or hash code.")

        elif choice == '3':
            system('pause')
            system('cls')
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        print("""

              
█▀▀ █▀█ █▄░█ ▀█▀ █ █▄░█ █░█ █▀▀
█▄▄ █▄█ █░▀█ ░█░ █ █░▀█ █▄█ ██▄
════════════════════════════════
              """)
        continue_choice = input(">> Do you want to encrypt/decrypt more? (y/n): ")
        if continue_choice.lower() == 'y':
            print()
            system('pause')
            system('cls')

        elif continue_choice.lower() == 'n':
            print()
            system('pause')
            system('cls')
            break

if __name__ == "__main__":
    main()
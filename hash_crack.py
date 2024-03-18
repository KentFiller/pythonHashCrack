import hashlib
import pyfiglet
import sys

ascii_banner = pyfiglet.figlet_format("Hash Cracker")
print(ascii_banner)  # Styling in terminal

print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA256 | SHA384")

# Prompt for user input
hash_type = input("What is your chosen hash type?: ").lower()
wordlist_loc = input("Enter wordlist location: ")
hash_val = input("Enter Hash: ")

# Read wordlist
with open(wordlist_loc, 'r') as file:
    word_list = file.read().splitlines()

# Get hash function algorithm that was chosen by user
hash_func = getattr(hashlib, hash_type.lower(), None)

if not hash_func:
    print("Error: The specified hash type is not supported. Please choose one that fits the previously listed choices.")
    sys.exit(1)

# Hash crack attempt
for word in word_list:
    hash_object = hash_func(word.encode('utf-8'))
    hashed = hash_object.hexdigest()

    if hash_val == hashed:
        print("\033[1;32mHash found:\033[0m", word)
        sys.exit(0)  # Exiting with success status

print("Hash not found in the wordlist.")
sys.exit(1)  # Exiting with error status

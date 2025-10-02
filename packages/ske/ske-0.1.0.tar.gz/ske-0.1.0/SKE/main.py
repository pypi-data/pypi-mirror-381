import argparse
import os

def xor_data(data, key):
    key_bytes = key.encode()
    result = bytearray()
    for i, byte in enumerate(data):
        result.append(byte ^ key_bytes[i % len(key_bytes)])
    return result

def encrypt_file(filename, key):
    with open(filename, "rb") as f:
        data = f.read()
    encrypted = xor_data(data, key)
    new_name = filename + ".ske"
    with open(new_name, "wb") as f:
        f.write(encrypted)
    print(f"File encrypted → {new_name}")

def decrypt_file(filename, key, keep=False):
    if not filename.endswith(".ske"):
        print("The file does not have the .ske extension!")
        return
    with open(filename, "rb") as f:
        encrypted = f.read()
    decrypted = xor_data(encrypted, key)
    original_name = filename[:-4]  # remove ".ske"
    with open(original_name, "wb") as f:
        f.write(decrypted)
    print(f"File decrypted → {original_name}")

    if not keep:
        os.remove(filename)
        print(f"File {filename} has been deleted.")

def main():
    parser = argparse.ArgumentParser(description="Simple XOR file encryptor (.ske)")
    parser.add_argument("-p", "--process", choices=["encrypt", "decrypt"], required=True, help="Operation")
    parser.add_argument("-f", "--file", required=True, help="File to encrypt/decrypt")
    parser.add_argument("-k", "--key", nargs="+", required=True, help="Password (encryption: 2 times, decryption: 1 time)")
    parser.add_argument("--keep", action="store_true", help="Keep the .ske file after decryption")

    args = parser.parse_args()

    if args.process == "encrypt":
        if len(args.key) != 2:
            print("Error: Provide the password twice for encryption!")
            return
        if args.key[0] != args.key[1]:
            print("Error: Passwords do not match!")
            return
        encrypt_file(args.file, args.key[0])

    elif args.process == "decrypt":
        if len(args.key) != 1:
            print("Error: Provide only one password for decryption!")
            return
        decrypt_file(args.file, args.key[0], keep=args.keep)

if __name__ == "__main__":
    main()

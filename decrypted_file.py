from Crypto.PublicKey import RSA
import sys


if len(sys.argv) != 2:
    print("Usage: python scrypt.py private_key.pk8")
    sys.exit(1)

private_key_file = sys.argv[1]

try:

    with open(private_key_file, "rb") as key_file:
        pkcs8_key = key_file.read()


    try:
        private_key = RSA.import_key(pkcs8_key)
        pem_key = private_key.export_key()
    except ValueError:
  
        private_key = RSA.import_key(pkcs8_key, passphrase=None)
        pem_key = private_key.export_key(passphrase=None)

    with open("private_key.pem", "wb") as pem_file:
        pem_file.write(pem_key)

    print("Private key successfully converted and saved as private_key.pem.")

except Exception as e:
    print(f"An error occurred: {e}")

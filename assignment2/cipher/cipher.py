import pyAesCrypt

from os import stat, remove, startfile
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

# encrypt


def encrypt(encryption_password):
    with open("moby10b.txt", "rb") as fIn:
        with open("moby10b_encrypt.txt", "wb") as fOut:
            pyAesCrypt.encryptStream(
                fIn, fOut, encryption_password, bufferSize)


# get encrypted file size
encFileSize = stat("moby10b_encrypt.txt").st_size

# decrypt


def decrypt(decryption_password):
    with open("moby10b_encrypt.txt", "rb") as fIn:
        with open("moby10b_decrypt.txt", "wb") as fOut:
            # decrypt file stream
            pyAesCrypt.decryptStream(
                fIn, fOut, decryption_password, bufferSize, encFileSize)


encryption_password = input("Please Enter Password to Encrypt: ")
encrypt(encryption_password)
startfile("moby10b_encrypt.txt")


decryption_password = input("Please Enter Password to Decrypt: ")
decrypt(decryption_password)
startfile("moby10b_decrypt.txt")

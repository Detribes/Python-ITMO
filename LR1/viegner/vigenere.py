def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    k = 0
    for i in range(len(plaintext)):
        char = plaintext[i]
        shift = ord(keyword[k % len(keyword)].lower()) - 97
        k += 1
        if (((char.isdigit()) == True) | ((char.isalpha()) == False)):
            ciphertext += char
        else:
            if (char.isupper()):
                ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    k = 0
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        shift = ord(keyword[k % len(keyword)].lower()) - 97
        k += 1
        if (((char.isdigit()) == True) | ((char.isalpha()) == False)):
            plaintext += char
        else:
            if (char.isupper()):
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
    return plaintext
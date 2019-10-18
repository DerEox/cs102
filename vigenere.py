def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ''
    while len(keyword) < len(plaintext):
        for i in keyword:
            if len(keyword) < len(plaintext):
                keyword += i       
    if keyword.isupper():
        code_A, code_Z = 65, 90
    else: code_A, code_Z = 97, 122
    for ch, k in zip(list(plaintext), list(keyword)):
        if ord(ch) + ord(k) - code_A > code_Z:
            ch = chr((ord(ch)) - 26)
        ciphertext += chr(ord(ch) + (ord(k) - code_A))
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ''
    while len(keyword) < len(ciphertext):
        for i in keyword:
            if len(keyword) < len(ciphertext):
                keyword += i   
    if keyword.isupper():
        code_A = 65
    else: code_A = 97
    for ch, k in zip(list(ciphertext), list(keyword)):
        if (ord(ch) < ord(k)):
            ch = chr(ord(ch) + 26)
        plaintext += chr(ord(ch) - (ord(k) - code_A))
    return plaintext
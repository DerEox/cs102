def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    key = list(keyword)
    ciphertext = []
    while len(key)<len(plaintext):
        for i in keyword:
            if len(key)<len(plaintext):
                key.append(i)        
    if keyword.isupper():
        for l, k in zip(plaintext, key):
            if (ord(l)+ord(k))-65 >90:
               l = chr((ord(l))-26)
            c = (chr(ord(l) + (ord(k)-65)))
            ciphertext.append(c)
    elif keyword.islower():
        for l, k in zip(plaintext, key):
            if (ord(l)+ord(k))-97 >122:
                l = chr((ord(l))-26)
            c = (chr(ord(l) + (ord(k)-97)))
            ciphertext.append(c)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    return plaintext
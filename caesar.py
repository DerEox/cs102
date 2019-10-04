def encrypt_caesar(shift: int, plaintext: str) -> str:
	ciphertext = []
	for l in plaintext:
		if l.isupper(): #for uppercase
			if ord(l)<=90-shift:
				l = chr(ord(l)+shift)
				ciphertext.append(l)
			else:
				l = chr(ord(l)-26+shift)
				ciphertext.append(l)
		elif l.islower(): #for lowercase
			if ord(l)<=122-shift:
				l = chr(ord(l)+shift)
				ciphertext.append(l)
			else:
				l = chr(ord(l)-26+shift)
				ciphertext.append(l)
		else:
			ciphertext.append(l)
	return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    return plaintext
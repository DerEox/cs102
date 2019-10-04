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


def decrypt_caesar(shift: int, ciphertext: str) -> str:
	plaintext = []
	for l in ciphertext:
		if l.isupper(): #for uppercase
			if ord(l)>65+shift:
				l = chr(ord(l)-shift)
				plaintext.append(l)
			else:
				l = chr(ord(l)+26-shift)
				plaintext.append(l)
		elif l.islower(): #for lowercase
			if ord(l)>97+shift:
				l = chr(ord(l)-shift)
				plaintext.append(l)
			else:
				l = chr(ord(l)+26-shift)
				plaintext.append(l)
		else:
			plaintext.append(l)
	return plaintext
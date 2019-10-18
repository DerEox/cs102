def encrypt_caesar(shift: int, plaintext: str) -> str:
	ciphertext = ''
	for ch in plaintext:
		if ch.isalpha(): 
			if ch.isupper():
				code_Z = 90
			else:
				code_Z = 122
			if ord(ch) <= code_Z - shift:
				ch = chr(ord(ch) + shift)
				ciphertext += ch
			else:
				ch = chr(ord(ch)-26 + shift)
				ciphertext += ch
		else:
			ciphertext += ch
	return ciphertext


def decrypt_caesar(shift: int, ciphertext: str) -> str:
	plaintext = ''
	for ch in ciphertext:
		if ch.isalpha(): 
			if ch.isupper():
				code_A = 65
			else:
				code_A = 97
			if ord(ch) > code_A + shift:
				ch = chr(ord(ch) - shift)
				plaintext += ch
			else:
				ch = chr(ord(ch) + 26 - shift)
				plaintext += ch
		else:
			plaintext += ch
	return plaintext
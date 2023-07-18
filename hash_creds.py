
import hashlib


def hash(email, passwd):
	creds = email+passwd
	h = hashlib.new('sha256')
	h.update(creds.encode())
	hash_data = h.hexdigest()

	return hash_data



import random
import string
import hashlib


def generate_api_key():
    letters_and_digits = string.ascii_letters + string.digits
    api_key = "".join((random.choice(letters_and_digits) for i in range(32)))
    api_key_hash = hashlib.sha512(str.encode(api_key)).hexdigest()

    return (api_key, api_key_hash)

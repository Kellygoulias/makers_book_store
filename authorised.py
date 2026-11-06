import hashlib

def hash(password):
    m = hashlib.sha256(password.encode("utf-8"))
    return m.hexdigest()

print(hash("1234"))

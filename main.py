import hashlib

def generate_sha1(input):
    sha1 = hashlib.sha1()
    sha1.update(input.encode())
    return sha1.hexdigest()

input = "dawodu"
sha1_show = generate_sha1(input)
print(f"sha1 Hash: {sha1_show}")
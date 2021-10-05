from pprint import pprint
import hashlib

def gen_md5(path):
    file = open(path)
    for line in file:
        hash = hashlib.md5(line.encode())
        yield hash.hexdigest()
    file.close()

for hash in gen_md5('countries_link.txt'):
    pprint(hash)

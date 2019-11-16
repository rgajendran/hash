import hashlib
import sys

filename = sys.argv[1]

md5 = hashlib.md5()
with open(filename, 'rb') as open_file:
    content = open_file.read()
    md5.update(content)

sha1 = hashlib.sha1()
with open(filename, 'rb') as open_file:
    content = open_file.read()
    sha1.update(content)

sha256 = hashlib.sha256()
with open(filename, 'rb') as open_file:
    content = open_file.read()
    sha256.update(content)

print("\n===============================================================")
print("                      GAJU HASHER                              ")
print("===============================================================")
print ("MD5    :   " + md5.hexdigest())
print ("SHA1   :   " + sha1.hexdigest())
print ("SHA256 :   " + sha256.hexdigest() + '\n\n')

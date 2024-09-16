import random
import string

A = list(string.ascii_letters)+list(string.digits)+list(string.punctuation)

password = ''

for i in range(12):
    password += random.choice(A)
    
print(password)

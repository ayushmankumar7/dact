import os 


print(os.listdir())

for i, line in enumerate(open('testing.py')):
    print(line)
    print(i)

import os 


print(os.listdir())

# for i, line in enumerate(open('testing.py', 'a')):
#     print(line)
#     print(i)

#     if i == 1:


with open('testing.py', 'r') as b:
    lines = b.readlines()

print(lines)
with open('testing.py', 'w') as b:
    for i, line in enumerate(lines):
        print(i)
        if i == 2:
            b.write("\tSomething \n")
        b.write(line)
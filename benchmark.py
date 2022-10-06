duration = 30

import random, string, time

c = 0
a = []
s = "000000"

t = time.time()
while True:
    x = ''.join(random.choices(string.digits, k=6))
    a.append(x)
    for e in a:
        if e == s:
            pass
    c = c + 1
    if time.time() - t > float(duration):
        u = time.time()
        break
del a

d = u-t

print("Your score:")
print(round(c/d))
print("\n\n")
print("Press enter to continue!")
input()
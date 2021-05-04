s = ''
f = open('login.users','r')
for linia in f:
    s = linia.strip()
    print(s)
print(s.split(' - '))
f.close()
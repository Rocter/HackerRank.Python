s = 'HackerRank.com presents "Pythonist 2".'
l = list(s)
o = []
for i in range(0,len(l)):
    if ord(l[i]) >= 65 and ord(l[i]) <= 90:
       o.append(chr(ord(s[i]) + 32))
    elif ord(l[i]) >= 95 and ord(l[i]) <= 122:
       o.append(chr(ord(s[i]) - 32))
    else:
       o.append(l[i])
p = ''.join(o)
print(p)

#or 

s = 'HackerRank.com presents "Pythonist 2".'
string = ""
for i in s:
   if i.isupper() == True:
      string= string + i.lower()
   else:
      string= string + i.upper()
print( string)

#or

print(s.swapcase())
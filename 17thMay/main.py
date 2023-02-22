list = [5, 6, 8, 9]

list.insert(2, 21)

for i in list:
    print(i)

print("chr(122) == "+ chr(122) + "\nord('z') == " + str(ord('z')))

l1 = [1, 2, 3]
l2 = l1
l2[0] = '7'
print(l1)

str = 'test'
byte = b'test'
print(type(byte))
print(type(str))

i = 1
while i < 6:
  print(i)
  if i == 3:
      i += 1
      continue
  i += 1
else:
  print("i is no longer less than 6")
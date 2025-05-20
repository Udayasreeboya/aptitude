string = "doubtful"
mid = len(string) // 2
half1 = string[:mid:]
rev1=half1[::-1]
half2 = string[mid::]
rev2=half2[::-1]
res1=""
for i in rev1:
    res1 += chr(ord(i) + 1)
res2 =""
for j in rev2:
    res2+= chr(ord(j) - 1)
result = res1 + res2
print(result)

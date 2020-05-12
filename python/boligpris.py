import re, pyperclip, sys

a = pyperclip.paste()

b = re.split("\n", a)
c = list()
for i, s in enumerate(b):
    if ("Omkostninger" in s):
        omkostninger = b[i+1]

    if ("Felleskost" in s):
        felleskost = b[i+1]

    # temp = re.sub("\D", "", s)
    # if (s != ""):
    #     c.append(temp)

pris = b[0]
pris         = float(re.sub("\D", "", pris))
omkostninger = float(re.sub("\D", "", omkostninger))
felleskost   = float(re.sub("\D", "", felleskost))


# d = list()
# for s in c:
#     if (s != "") :
#         d.append(s)

# print(b)
# pris         = float(d[0])
# omkostninger = float(d[2])
# felleskost   = float(d[4])

pers = float(sys.argv[1])
pr_mnd = pris*0.03/12.0 + felleskost

print(f"\nPris pr. pers: {pr_mnd/pers}")
print(f"")
print(f"Pers: {pers}")
print(f"Pris pr. mnd: {pr_mnd}\n")

abc = open("email")
for line in abc:
    line =line.rstrip()
    if not line.startswith("we"): continue
    words =line.split()
    print(words[2])

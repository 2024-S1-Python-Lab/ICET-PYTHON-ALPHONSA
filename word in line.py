s=input("enter a sentance:");
print(s)
wordslist=s.split()
print(wordslist)
for i in wordslist:
    print(f"{i}occurs {wordslist.count(i)}times")

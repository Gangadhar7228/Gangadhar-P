text=input("enter a string=")

print("first character:",text[0]if text else"empty string")
print("last character:",text[-1] if text else"empty string")
print("first five characters:",text[5])
print("reversed string:",text[-1])

print("uppercase:",text.upper())
print("lowercase:",text.lower())

sub=input("enter a character/substring to count:")
print("occurence count:",text.count(sub))

old=input("enter a world to replace:")
new=input("enter a new word:")
print("after replacment:",text.replace(old,new))

words=text.split()
print("split words:",words)
print("joined with'-':","-".join(words))

start_sub=input("enter a starting substring to check:")
end_sub=input("enter a ending substring to check:")
print("starts with given substring:",text.startswith(start_sub))
print("ends with given substing:",text.endswith(end_sub))
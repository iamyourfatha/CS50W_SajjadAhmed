#create an empty set
s = set()

# add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # no element can ever appear twice in a set
print(s)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements.")
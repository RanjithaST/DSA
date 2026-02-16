# SET IN PYTHON (ALL TOGETHER)

# Creating a set
s = {1, 2, 3}
print("Initial set:", s)

# Add elements
s.add(4)
print("After add(4):", s)

# Add multiple elements
s.update([5, 6])
print("After update([5,6]):", s)

# Remove elements
s.remove(3)     # error if not present
print("After remove(3):", s)

s.discard(10)   # no error if not present
print("After discard(10):", s)

# Pop random element
s.pop()
print("After pop():", s)

# Length
print("Length:", len(s))

# Max, Min, Sum
print("Max:", max(s))
print("Min:", min(s))
print("Sum:", sum(s))

# Another set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Set operations
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)
print("Symmetric Difference:", a ^ b)

# Using methods
print("Union method:", a.union(b))
print("Intersection method:", a.intersection(b))
print("Difference method:", a.difference(b))
print("Symmetric Difference method:", a.symmetric_difference(b))

# Relationship checks
print("Is subset:", a.issubset(b))
print("Is superset:", a.issuperset(b))
print("Is disjoint:", a.isdisjoint(b))

# Clear set
s.clear()
print("After clear():", s)




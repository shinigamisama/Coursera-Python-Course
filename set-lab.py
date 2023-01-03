# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print("convert ",album_list,"/n to the following set /n",album_set)


# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])

# Add element to set

A.add("NSYNC")
print("Added NSYNC to the sample set",A)

# Remove the element from set

A.remove("NSYNC")
print("Removed NSYNC to the sample set",A)


# Verify if the element is in the set

check = "AC/DC" in A
print("AC/DC exist in the set",check)

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets

print(album_set1, album_set2)

# Find the intersections

intersection = album_set1 & album_set2
print(intersection)

# Find the difference in set1 but not set2

difference = album_set1.difference(album_set2)  
print(difference)

# Find the union of two sets

union = album_set1.union(album_set2)
print("This is the union", union)

# Check if subset

subset = set(album_set2).issubset(album_set1)     
print(subset)

# Check if superset

superset = set(album_set1).issuperset(album_set2)   
print(superset)
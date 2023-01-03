

# Create your first tuple

tuple1 = ("disco",10,1.2 )
print (tuple1)

# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
print("Concatenate two tuples:",tuple2)

# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple

RatingsSorted = sorted(Ratings)

# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# Print the first element in the second nested tuples

NestedT[2][1][0]
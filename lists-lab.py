from colorama import Fore, Back, Style

# Create a list

L = ["Michael Jackson", 10.1, 1982]

# Print the elements on each index

print(Fore.BLUE + "Print the elements on each index:" + Style.RESET_ALL)

print('the same element using negative and positive indexing:\n Postive:',L[0],'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],'\n Negative:' , L[-1]  )

# Update Sample list

print(Fore.BLUE + "Update Sample list:" + Style.RESET_ALL)

L = ["Michael Jackson", 10.1,1982,"MJ",1]


# List slicing

print(Fore.BLUE + "List slicing:" + Style.RESET_ALL)
L[3:5]

# Use extend to add elements to list

print(Fore.BLUE + "Use extend to add elements to list:" + Style.RESET_ALL)
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print("This is the list after extend:\n",L)

# Use append to add elements to list

print(Fore.BLUE + "Use append to add elements to list:" + Style.RESET_ALL)
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print("This is the list after append:\n",L)

# Change the element based on the index

print(Fore.BLUE + "Change the element based on the index:" + Style.RESET_ALL)
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)


# Delete the element based on the index

print(Fore.BLUE + "Delete the element based on the index:" + Style.RESET_ALL)
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space

print(Fore.BLUE + "Split the string, default is by space:" + Style.RESET_ALL)
'hard rock'.split()


# Split the string by comma

print(Fore.BLUE + "Split the string by comma:" + Style.RESET_ALL)
'A,B,C,D'.split(',')

# Copy (copy by reference) the list A

print(Fore.BLUE + "Copy (copy by reference) the list A:" + Style.RESET_ALL)
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)


# Examine the copy by reference

print(Fore.BLUE + "Examine the copy by reference:" + Style.RESET_ALL)
print('B[0]:', B[0])
A[0] = "banana"
print('B[0] after value in A[0] change:', B[0])




# Clone (clone by value) the list A

print(Fore.BLUE + "Clone (clone by value) the list A:" + Style.RESET_ALL)
B = A[:]
B

# Now if you change A, B will not change:

print(Fore.BLUE + "Now if you change A, B will not change::" + Style.RESET_ALL)
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0] after value in A[0] change:', B[0])
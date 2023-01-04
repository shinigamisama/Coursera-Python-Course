# Uncomment these if working locally, else let the following code cell run.
# download of the example file 
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

# Read the Example1.txt
example1 = "Example1.txt"
file1 = open(example1, "r")

# Print the path of file

print("This is the name of the sample file:\n",file1.name)

# Print the mode of file, either 'r' or 'w'

file1.mode
print("This is how the sample file is open:\n",file1.mode)

# Read the file

FileContent = file1.read()
print("This is the content of the sample file:\n\n",FileContent)

# Close file after finish

print("Closing the file...")
file1.close()

#######################################################################

# Open file using with

with open(example1, "r") as file1:
    FileContent = file1.read()
    print("This is the content of the file opened using with statement:\n\n",FileContent)

# Verify if the file is closed

print("The file is automatically closed?",file1.closed)

# See the content of file

print("\n\n",FileContent)




#######################################################################

# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Read file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Write multiple lines to file

with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Write a new line to text file
# mode "a" is the append mode

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

# Verify if the new line is in the text file

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


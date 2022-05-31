# Do you need to look for a specific string in a text file?
# Use-cases: if you're looking for a malware hash signature, bad IP, scanner activity, transaction, specific file, path, etc.,
# Create a text file name test with some lines, we're looking for "security" string in the text file.
string1 = 'security'
file="test.txt"
# opening the test file
file1 = open(file, "r")

# setting flag and index to 0
flag = 0
index = 0

# search line by line using loop
for line in file1:
    index += 1

    # if string1 is in the text
    if string1 in line:
        flag = 1
        break

# checking condition for string found or not
if flag == 0:
    print(f"{string1} in not found in {file}")
else:
    print(f"{string1} in found in line {index}")

# closing text file
file1.close()


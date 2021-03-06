# Write a program to eliminate repeated lines from a file.
lines_seen = set()  # holds lines already seen
outfile = open('employee.txt', "w")
infile = open('demo.txt', "r")
print ("The content of file demo.txt is as follows")
for line in infile:
    print(line)
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print("----------------------------------------------")
print("The content of file employee.txt is as follows")
for line in open('employee.txt', "r"):
    print(line)
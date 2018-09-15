import sys, os

# print(os.path.join(sys.path[0], "backup.sh"))

input = sys.stdin.readlines()
line = input[0]
words = line.split()
command = " ".join(words[1:])
file = open(os.path.join(sys.path[0], "backup.sh"), "a")
file.write(" && \\\n" + command)
file.close()
print(command + " written to backup script.")


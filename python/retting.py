import os, sys

files_in_cwd = [f for f in os.listdir('.') if os.path.isfile(f)]
if ("retting.py" in str(files_in_cwd)):
    sys.exit("Ikke kjoer script i retting folder. Da kjoerer scriptet seg selv")

for root, dirs, files in os.walk(os.getcwd()):
    print("dir:     " + os.path.basename(root)) # Folder
    navn = os.path.basename(os.path.dirname(root))
    for f in files:
        if ("old_duplicates" in os.path.basename(root)):
            continue
        if (".py" in str(f)):
            path_to_file = root + os.sep + str(f)
            infile = open(path_to_file, "r")
            print()
            print("fil: " + f)
            print("navn: " + navn)
            print("==========================")
            print("           FIL            ")
            print("==========================")
            print(infile.read())
            infile.close()
            print("==========================")
            print("          OUTPUT          ")
            print("==========================")
            os.system("python3 " + path_to_file) # run file
            print("==========================")
            print("fil: " + f)
            print("navn: " + navn)
        else:
            print("\n" + navn + ": Ikke pythonfil: " + str(f) + "\n")
        input("\nTrykk for neste\n")



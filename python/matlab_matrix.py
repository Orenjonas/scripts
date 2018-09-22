import sys
import pyperclip

"""
This script takes in a matrix separated by whitespace and newlines (the format of matlab output)
and copies a LaTex format matrix to clipboard.

Usage:
>>python3 matlab_matrix.py "
    1.0000    0.7000         0         0         0
         0         0    0.5000         0         0
         0    0.3000         0    0.6000         0
         0         0    0.5000         0         0
         0         0         0    0.4000    1.0000
"
\begin{bmatrix*}
     1   0.7     0     0     0 \\
     0     0   0.5     0     0 \\
     0   0.3     0   0.6     0 \\
     0     0   0.5     0     0 \\
     0     0     0   0.4     1
\end{bmatrix*}
 
Copied to clipboard.

"""

lines = sys.argv[1].split("\n")

longestnr = lines
while type(longestnr) != str:
    longestnr = max(longestnr)

longestnr = max(longestnr.split())

columnwidth = len(longestnr)

texmatrix = r"\begin{bmatrix*}" + "\n"
for i, line in enumerate(lines):
    elems = line.split()
    for j, elem in enumerate(elems):
        elem = float(elem)
        exec( "number = '{:>%dg}'.format(elem)" % columnwidth )
        if (j > 0):
            texmatrix += " && "
        texmatrix += number

    if i < len(lines)-2:
        texmatrix += r" \\"
    if i < len(lines) - 1:
        texmatrix += "\n"

texmatrix += "\end{bmatrix*}\n"

pyperclip.copy(texmatrix)
print(texmatrix, "\nCopied to clipboard." )



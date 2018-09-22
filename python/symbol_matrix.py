import sys
import pyperclip

"""
This script takes in a matrix of symbols separated by whitespace and newlines (the format of matlab output)
and copies a LaTex format matrix to clipboard.

Usage:
>>> python3 symbol_matrix.py "a b c
> d e f
> g e h
> "
\begin{bmatrix*}
a && b && c \\
d && e && f \\
g && e && h
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
        # elem = float(elem)
        exec( "number = '{:>%d}'.format(elem)" % columnwidth )
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



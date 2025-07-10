#Short script to alter txt from space to tab delimited for easier spreadsheet input.
#I can't promise it will work perfectly, always backup the file before running in case of damage.
#Created 18/02/2025 in python 3.12.8
#Matthew Leonard

import re #RegEx module

def load_file(filename):
    file = open(filename, "r")
    content = file.read().splitlines(keepends=True) #Split into lines to preserve \n
    file.close()
    return content

print("This will replace ALL spaces in a txt with tabs and save it to a new txt.\nIf you only want some spaces replaced, move them to a separate txt first.\nNothing should happen to the original, but backup first to be safe.")
print("\nI have only tested and designed this to work with txt.\nIt might work with other file formats, depending on how python reads them.")
print("Include .txt in the input.")

badFile = True
while badFile:
    try:
        filename = str(input("\nFile to edit >>> "))
        content =  load_file(filename)
        badFile = False
        break #redundant but it feels wrong to not have it
    except(FileNotFoundError):
        print("Invalid file. Make sure to include file extensions eg. ('.txt') in the input.\nCheck the file is in the same directory as this script.")

#print("\nFile Contents:\n", content) preserved for testing if you want it

newContent = ""

for line in content:
    newLine = re.sub(r"[^\S\n\t]+", "\t", line) #regex to match the inverse of: non whitespace, \n, and \t, for all instances, which is then replaced with a tab (\t)
    #print("newLine:", newLine) preserved for testing if you want it
    newContent = newContent + newLine

#print("New Format:\n", newContent) preserved for testing if you want it

newFilename = "tab-delimited " + filename
with open(newFilename, "w") as tabFile:
    tabFile.write(newContent)
tabFile.close()

print("File created.")

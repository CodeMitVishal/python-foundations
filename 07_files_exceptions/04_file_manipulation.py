"""Module 7 · File manipulation

List, copy, rename, move and delete files from code with the os and shutil
modules, then do the same kind of thing with pathlib.

Everything happens inside a throwaway "playground" folder next to this
script, so none of your real files are touched.

Run it:  python 07_files_exceptions/04_file_manipulation.py
"""
import os      # talks to the operating system: folders, renames, deletes
import shutil  # higher-level file tools: copy, move, remove whole folders
from pathlib import Path   # modern, object-style way to work with paths

# ---------------------------------------------------------------
# STEP 1: Set up a safe "playground" folder to experiment in
# ---------------------------------------------------------------

# Path(__file__)  -> the full path of THIS script file
# .parent         -> the folder the script is in (07_files_exceptions)
# / "playground"  -> join a sub-folder name onto it (/ joins path parts)
# Result: .../07_files_exceptions/playground
playground = Path(__file__).parent / "playground"

# Delete the playground folder AND everything inside it, if it exists.
# ignore_errors=True -> don't crash if the folder isn't there yet (first run).
# This gives us a clean, empty start every time we run the script.
shutil.rmtree(playground, ignore_errors=True)

# Create the (now empty) playground folder.
os.makedirs(playground)

# Change the "current working directory" to the playground.
# From now on, plain file names like "data.csv" mean "inside playground".
os.chdir(playground)

# ---------------------------------------------------------------
# STEP 2: Create some sample files to play with
# ---------------------------------------------------------------

# Loop over three file names and create each one.
for name in ["data.csv", "old.txt", "temp.txt"]:
    # "w" = write mode: creates the file (or empties it if it already exists).
    # "with" closes the file automatically when the block ends.
    with open(name, "w") as f:
        f.write("sample\n")      # put one line of text in each file

# ---------------------------------------------------------------
# STEP 3: Look around: list files and check they exist
# ---------------------------------------------------------------

# os.listdir(".") -> a list of every file/folder name in the current folder.
# "." means "the folder I'm in right now" (the playground).
print(os.listdir("."))               # ['data.csv', 'old.txt', 'temp.txt']

# os.path.exists(...) -> True if that file or folder is there, else False.
print(os.path.exists("data.csv"))    # True

# ---------------------------------------------------------------
# STEP 4: Make two sub-folders to copy and move files into
# ---------------------------------------------------------------

# exist_ok=True means "don't complain if the folder is already there"
os.makedirs("backup", exist_ok=True)     # playground/backup/
os.makedirs("archive", exist_ok=True)    # playground/archive/

# ---------------------------------------------------------------
# STEP 5: Copy, rename, move and delete
# ---------------------------------------------------------------

# COPY: makes a second copy of data.csv inside backup/.
# The original data.csv stays where it is -> now there are 2 copies.
shutil.copy("data.csv", "backup/")

# RENAME: old.txt becomes new.txt (same folder, new name).
os.rename("old.txt", "new.txt")

# MOVE: takes new.txt OUT of the playground and puts it in archive/.
# (Like cut + paste: only one copy exists afterwards.)
shutil.move("new.txt", "archive/")

# DELETE: removes temp.txt permanently.
# Careful: it does NOT go to the Recycle Bin, so there's no undo!
os.remove("temp.txt")

# ---------------------------------------------------------------
# STEP 6: Check the result
# ---------------------------------------------------------------

# What's left in the playground now? data.csv (original) plus the two
# folders. old.txt was renamed and moved; temp.txt was deleted.
print(os.listdir("."))               # ['archive', 'backup', 'data.csv']

# What's inside archive/? The renamed-and-moved file.
print(os.listdir("archive"))         # ['new.txt']

# Final layout:
#   playground/
#   ├── archive/
#   │   └── new.txt    <- renamed + moved
#   ├── backup/
#   │   └── data.csv   <- copy
#   └── data.csv       <- original

# ---------------------------------------------------------------
# STEP 7: The same ideas with pathlib (the modern way)
# ---------------------------------------------------------------

# A Path object represents a file path and knows its own parts.
p = Path("data.csv")

# p.name     -> full file name         : data.csv
# p.stem     -> name WITHOUT extension : data
# p.suffix   -> the extension          : .csv
# p.exists() -> is the file there?     : True
print(p.name, p.stem, p.suffix, p.exists())   # data.csv data .csv True

# file_sorter
Python script that sorts a messy folder into categories (images, documents, videos and more)
File Sorter
A small Python script that sorts a messy folder into categories:
Images, Documents, Videos, Audio, Archives and Code.
## Files
- sorter_v1.py: the simple 20-line version
- sorter_v2.py: a safer version (dry run, renames duplicates, Other folder)
- make_test_files.py: creates 30 dummy files to test on
## How to run Broxie Video Guide: File Sorter in 20 Lines of Python Page 9
1. python make_test_files.py
2. python sorter_v1.py
For the safer version:
- python sorter_v2.py --dry-run (shows what would happen)
- python sorter_v2.py (does it for real)
## Warning
This script MOVES files. Test on a dummy folder or a copy first.
## What I learned
- How to use pathlib and shutil to work with files
- Why testing matters: [write the real problem you found]
## Video
[paste your YouTube link]
To upload without Git: on github.com click +, New repository, name it file-sorter, make it Public, tic

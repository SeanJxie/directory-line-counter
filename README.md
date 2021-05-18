# Usage
```
usage: count_lines.py [-h] --path [--extension [--extension ...]]

Count the lines of code in a directory.

positional arguments:
  --path       The path of the directory.
  --extension  A file extension that should be targeted for counting.

optional arguments:
  -h, --help   show this help message and exit
  ```

For example, in the command-line:
```
C:\> python count_lines.py C:\MyDir .py .cpp .c .h .hpp
```
Output:
```
Scanning...

Done!

Found a total of 67357 files while searching for: ['.py', '.cpp', '.c', '.h', '.hpp'], totaling 17342688 lines of code.

The code composition is shown below:
---------------------------------------------
.py  65937 files containing 16682634 lines
.cpp 22 files containing 3997 lines
.c   176 files containing 353291 lines
.h   1222 files containing 302766 lines
.hpp 0 files containing 0 lines
```

"""

A command line tool for counting lines of code

"""

import os
import argparse


VALID_EXTENTIONS = sorted(
    (
        ".py", 
        ".java", 
        ".c", 
        ".cpp",
        ".h",
        ".hpp",
        ".go"
    )
)


def get_file_ext(file_name):
    return os.path.splitext(file_name)[1].lower()

def assert_extensions_valid(extensions):
    for ext in extensions:
        if ext not in VALID_EXTENTIONS:
            return False
    return True

def count_lines(file_path):
    # Credit to https://stackoverflow.com/a/30521948/11768102 for an error-handling solution
    nLines = 0
    with open(file_path, mode='r') as f:
        iterobject = iter(f)
        while iterobject:
            try:
                if next(iterobject) != '\n':
                    nLines += 1
            except StopIteration:
                break
            except UnicodeDecodeError:
                pass
    return nLines

parser = argparse.ArgumentParser(description="Count the lines of code in a directory.")

parser.add_argument(
    "dir_path",
    metavar="--path",
    type=str,
    help="The path of the directory."
)

parser.add_argument(
    "extensions",
    metavar="--extension",
    type=str,
    nargs="*",
    help="A file extension that should be targeted for counting."
)


args = parser.parse_args()
DIRPATH = args.dir_path
EXTENTIONS = args.extensions

if os.path.isdir(DIRPATH):
    if assert_extensions_valid(EXTENTIONS):
        # Counting done here
        name_file_line_map = {name: [0, 0] for name in EXTENTIONS}

        for dpath, dnames, fnames in os.walk(DIRPATH):

            for fname in fnames:
                file_ext = get_file_ext(fname)

                if file_ext in EXTENTIONS:
                    fullPath = os.path.join(dpath, fname)
                    nFileLines = count_lines(fullPath)

                    print(f"\nScanning valid file {fullPath}")
                    print(f"Found {nFileLines} lines.")

                    name_file_line_map[file_ext][0] += 1
                    name_file_line_map[file_ext][1] += nFileLines

        only_files = map(lambda x: x[0], name_file_line_map.values())
        only_lines = map(lambda x: x[1], name_file_line_map.values())
        nTotalLines = sum(only_lines)
        nTotalFiles = sum(only_files)

        print(f"\nDone!\n\nFound a total of {nTotalFiles} files while searching for: {EXTENTIONS}, totaling {nTotalLines} lines of code.")
        
        print("\nThe code composition is shown below:\n" + '-' * 45)
        for k, v in name_file_line_map.items():
            print(f"{k}:" + ' ' * (5 - len(k)) + f"{v[0]} files containing {v[1]} lines")
        
    else:
        print("Invalid extension detected!\nValid extensions are:")
        for ext in VALID_EXTENTIONS:
            print(f"  {ext}")

else:
    print("Directory path does not exist!")

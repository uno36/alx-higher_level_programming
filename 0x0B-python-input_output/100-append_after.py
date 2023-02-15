#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
    a specific string
    Args:
        filename: name of the file
        search_string: the specific string that need to search
        new_string: the new string that need to add
    """
    data = ""
    with open(filename, "r+") as f:
        for line in f:
            data += line
            if search_string in line:
                data += new_string
        f.seek(0)
        f.write(data)

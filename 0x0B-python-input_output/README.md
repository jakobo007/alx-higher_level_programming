This is a 0x0B-python-input_output directory

Reading nad writing files:
    open() returns a file object and is commonly used with two positional arguments and one key word argument
    open(filename, mode, encoding=None)

    1st argument is the filename
    2nd a string describing the way the file will be opened: (r = read only
                w = write only (if an exisiting file with the same name is present it will be erased)
                a = opens the file for appending: any written data will be added to the end of the file
                r+ = read and write
                )
    
    
    It is good practice to use the with keyword when dealing with file objects.

    >>> with open('workfile', encoding="utf-8") as f:
    ...    read_data = f.read()

        # We can check that the file has been automatically closed.
    >>> f.closed

Methods of File Objects:
    f.read(size) ==> Read a file's contents. 
                        returns a string(in text mode)

                        >>> f.read()
                        'The files contents.\n'
                        >>> f.read()
                        ''

    f.readline() ==> Reads a single line from the line.
                        a newline character(\n) is left at the end of the string and is only ommited on the last line of the file if the file doesn't end in a newline

                        >>> f.readline()
                        'This is the first line of the file.\n'
                        >>> f.readline()
                        'Second line of the file\n'
                        >>> f.readline()
                        ''

                        For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

                        >>> for line in f:
                                print(line, end='')

                        This is the first line of the file.
                        Second line of the file

    If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

    f.write(string) ==> write the contents of the string to the file, returning the number of characters written.
                >>> f.write('This is a test\n')
                15

                Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:

                >>> value = ('the answer', 42) # this is a tuple
                >>> s =  str(value) # convert the tuple into a string
                >>> f.write(s)
                18
    f.tell() ==> returns an integer giving the file objects current position in the file represented as number if bytes from the beginning if the file when in binary mode and an opaque number in when text mode.

    f.seek(offset, whence) ==> To change a file object's position
            >>> f = open('workfile', 'rb+')
            >>> f.write(b'0123456789abcdef')
            16



Saving structured data with json:

        JSON (JavaScript Object Notation) is a lightweight data interchange format commonly used for transmitting data between a server and a web application, or between different parts of an application. It's based on a subset of the JavaScript programming language and is easy for humans to read and write, while also being easy for machines to parse and generate.

    ******************
        The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

        ***********

    Here's a list of commonly used JSON functions in Python's built-in `json` module:

        1. `json.loads()`: Converts a JSON string into a Python object.
        2. `json.dumps()`: Converts a Python object into a JSON string.
        3. `json.load()`: Reads JSON data from a file-like object and parses it into a Python object.
        4. `json.dump()`: Writes a Python object to a file-like object in JSON format.
        5. `json.JSONDecoder()`: Decodes JSON data incrementally.
        6. `json.JSONEncoder()`: Encodes Python objects into JSON format.
        7. `json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`: Serialize obj as a JSON formatted stream to fp.
        8. `json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`: Serialize obj to a JSON formatted str.

    These functions provide a convenient way to work with JSON data in Python, allowing you to serialize and deserialize JSON strings, read and write JSON data to files, and customize the JSON encoding and decoding process.

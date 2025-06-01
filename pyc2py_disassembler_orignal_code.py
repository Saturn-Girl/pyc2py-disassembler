import marshal
import types
import dis
import sys
import os

Running = True
print("Hello and again welcome to the pyc2py disassembler a special text based python-ish disassembler")

while Running:
    File = input("Enter your pyc or command file ").strip().lower()
    if os.path.exists(File):
        with open(File, 'rb') as f:
            f.read(16)  # skip header (magic number, timestamp, etc.)
            code = marshal.load(f)
            dis.dis(code)
            print(code)
    elif File == "help":
        print("YourFile.pyc - decompiles the file")
        print("Exit -- exit to program")
    elif File == "exit":
        Running = False
        sys.exit()
    else:
        print(f"Cannot find {File} or maybe missing or corrupted")

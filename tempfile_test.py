import tempfile

# tempfile opens a temporary file in w+b mode

# creates a file with invisible name
temp = tempfile.TemporaryFile()
print(temp)
print(temp.name)

# creates a file but with visible name
temp = tempfile.NamedTemporaryFile()
print(temp)
print(temp.name)

temp = tempfile.NamedTemporaryFile(prefix="pre_", suffix="_suf")
# after writing pointer points the end of file
temp.write(b"welcome to my darkness")
# seek(0) shifts pointer to the beginning
temp.seek(0)

print(temp.name)
print(temp.read())

temp.close()

# creating temporary directory
temp_dir = tempfile.TemporaryDirectory()
print(temp_dir)

secure_temp = tempfile.mkstemp(prefix="c_", suffix=".json")
print(secure_temp)

secure_temp = tempfile.mkdtemp(prefix="c_", suffix="_dir")
print(secure_temp)

# we can set a location where the files are stored by default it's /tmp
tempfile.tempdir = "/tmp"
print(tempfile.gettempdir())

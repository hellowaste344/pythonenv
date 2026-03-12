import shutil
from pathlib import Path

dir = Path(".")

source = dir / "shutil_test.py"

destination = dir / "copyfile.txt"

# shutil.copyfile() -> metadata is not preserved unlike .copy()
# shutil.copytree() -> copy directories
# shutil.which() -> return path
cp = shutil.copy(source, destination)

print(f"file {cp} created")

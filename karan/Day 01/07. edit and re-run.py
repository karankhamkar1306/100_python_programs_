import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output

print("Setup complete")
print("hello, world!")
check_output("hello, python!")

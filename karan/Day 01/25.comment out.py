print("red")
#print("orange")
print("blue")
#print("purple")
print("green")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("red\nblue\ngreen")

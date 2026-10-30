first = "second"
last = "first"
first, last = last, first
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(first, "first")
check(last, "second")

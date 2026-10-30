final_x = 4
final_y = 3
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(final_x, 4, hint="Trace one line at a time: after x = x + y, x is 7.")
check(final_y, 3)

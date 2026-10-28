sweets = 17
children = 5
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
each = 17//5
left_over = 17%5
check(each, 3)
check(left_over, 2)

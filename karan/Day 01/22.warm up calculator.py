print(24*60*60)
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("86400", hint="Print the expression 24 * 60 * 60 (no quotes!).")

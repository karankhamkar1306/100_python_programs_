raw_name = "  aDA lovelace  "

clean_name = raw_name.strip().title()
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(clean_name, "Ada Lovelace")

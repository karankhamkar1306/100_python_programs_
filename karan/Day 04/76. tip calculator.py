bill = 84.50
tip_percent = 18
people = 4

tip = (18/100)*84.50
total = round(84.50 + tip,2)
per_person = round(total/4,2)
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(tip, 15.21)
check(total, 99.71)
check(per_person, 24.93, hint="Divide the (already rounded) total by people, then round to 2 places.")

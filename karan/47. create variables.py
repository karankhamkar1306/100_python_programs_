planet = "mars"
moons = 2
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(planet, "mars")
check(moons, 2)

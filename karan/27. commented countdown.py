print("ready","set","go!",sep="...")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("Ready... Set... Go!", hint="Three values, and a separator of '... '.")

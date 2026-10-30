print(2026,10,18,sep="-")
print("Loading", end="...")
print("done!")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("2026-10-18\nloading... done!",hint="try print(2026,10,18, sep=...) and print('loading',end=...).")

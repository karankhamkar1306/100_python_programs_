print("area of a 12 by 7 room",end=":")
print((10*8)+4)
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("area of 12 by 7 room:84 sqaure meters",hint="print('area of a 12 by 7 room:',12*7,'square meters')")

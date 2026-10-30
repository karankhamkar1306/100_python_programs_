name = "Ada"
age = 36

sentence = (f"{name} is {age} years old and will be {age+1} next year.")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check(sentence, "Ada is 36 years old and will be 37 next year.")

# your code here
price = float(input("Enter the price: "))
tax_rate = float(input("Enter the tax rate in precent: "))
total = price + (price * tax_rate / 100)
print(f"Total: {total:.2f}")
import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
check_output("Total: 86.00", inputs=["80", "7.5"])
check_output("Total: 23.99", inputs=["19.99", "20"])

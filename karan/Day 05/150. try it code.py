# 1. input
text = input("Temperature in fahrenheit: ")

# 2. convert
fahrenheit = float(text)

# 3. compute
celsius = (fahrenheit -32) * (5 / 9)

# 4. output
print(f"{fahrenheit}°f is {celsius:.1f}°C")

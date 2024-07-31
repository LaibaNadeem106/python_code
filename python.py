# 1. Age Assignments Based on the Riddle
anton=21
beth=anton+6
chen=beth+20
drew=chen+anton
ethan=chen

print(f"anton is {anton}")
print(f"beth is {beth}")
print(f"chcen is {chen}")
print(f"drew is {drew}")
print(f"ethan is {ethan}")

# 2. Formatted String Interpolation
name="Alice"
age=30
city="New York"
sentence=f"{name} is {age} years old and lives in {city}"
print(sentence)

# 3. String Manipulation
s:str = "hElLo WoRlD"
capitalized =s.capitalize()
uppercased= s.upper()
lowercased= s.lower()

print(capitalized)
print(uppercased)
print(lowercased)

# 4. Substring Search
s:str ="the quick brown fox jumps over the lazy dog"
index_fox=s.find("fox")
count_the=s.count("the")

print(f"index of 'fox' is {index_fox}")
print(f" 'the' appears {count_the} times")

# 5. String Replacement
s= "i love programming in python"
replace_s=s.replace("python","JAVA")
print(replace_s)

# 6. String Splitting and Joining
s="apple,banana,cherry,dates"
split_list=s.split(',')
joined_string= ' '.join(split_list)

print(split_list)
print(joined_string)

# 7. String Stripping and Justifying
s="   pyhton is fun!  "
stripped_s =s.strip()
left_justified= stripped_s.ljust(20,'*')
right_justified= stripped_s.rjust(20,'*')

print(stripped_s)
print(left_justified)
print(right_justified)

# 8. Convert an integer to its binary representation
num=45
binary_representation=bin(num)
print(f"Binary represntation: {binary_representation}")

# 9. Calculate Powers of Numbers
base=3
exponent=4
power_result=base**exponent
print(f"power result: {power_result}")

# 10. Round floating-point numbers
value=12.34567
rounded_integer = round(value)
rounded_two_decimals= round(value, 2)

print(f"Rounded to nearest integer:{rounded_integer}")
print(f"Rounded to two decimal places:{rounded_two_decimals}")
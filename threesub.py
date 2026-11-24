print("STUDENT MARKS CALCULATION")

name = input("Enter Student Name: ")
usn = input("Enter USN: ")

m1 = float(input("Enter Subject 1 Marks: "))
m2 = float(input("Enter Subject 2 Marks: "))
m3 = float(input("Enter Subject 3 Marks: "))

total = m1 + m2 + m3
average = total / 3
percentage = (total / 300) * 100

print("\n----- STUDENT RESULT -----")
print("Student Name:", name)
print("USN:", usn)
print("Subject 1:", m1)
print("Subject 2:", m2)
print("Subject 3:", m3)
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
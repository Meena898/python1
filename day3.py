marks1 = float(input())
marks2 = float(input())
marks3 = float(input())

average = (marks1 + marks2 + marks3) / 3

if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")

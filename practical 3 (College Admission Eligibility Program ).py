print("========= College Admission Eligibility =========")

age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

if age >= 18 and age <= 25:
    print("You are eligible for college admission")

    if marks >= 60:
        print("You are eligible for college admission based on marks")

        if marks >= 85:
            print("You are eligible for admission in AIML")
        elif marks >= 75:
            print("You are eligible for admission in CSE")
        else:
            print("You are eligible for other courses")

    else:
        print("You are not eligible for college admission due to marks")

else:
    print("You are not eligible for admission due to your age")

feedback = input("Enter Your Feedback: ")

print("\n" + "CUSTOMER FEEDBACK REPORT".upper().center(50))
print("----------------------------------------".center(50))

print("Original Feedback:".title())
print(feedback.center(50))

print("----------------------------------------".center(50))
print("FEEDBACK SUMMARY:".upper().center(50))

print("Total Characters        :", len(feedback))
print("Total Words             :", len(feedback.split()))
print("Total Spaces            :", feedback.count(" "))
print("Total Exclamation Marks :", feedback.count("!"))

print("----------------------------------------".center(50))
print("Formatted Feedback:".title().center(50))

print("Lowercase               :", feedback.lower())
print("Uppercase               :", feedback.upper())
print("Title Case              :", feedback.title())
print("Capitalize              :", feedback.capitalize())
print("Swap Case               :", feedback.swapcase())
print("Stripped                :", feedback.strip())

print("----------------------------------------".center(50))
print("WORDS ANALYSIS:".upper().center(50))

print("Split Words List        :", feedback.split())

print("----------------------------------------".center(50))
print("THANK YOU FOR YOUR VALUABLE FEEDBACK".upper().center(50))

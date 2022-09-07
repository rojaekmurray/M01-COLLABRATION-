while True:
    M_name = input("Student's Last Name: (ZZZ to quit)")
    if M_name == "ZZZ":
        break
    R_name = input("Student's First Name: ")
    gpa = float(input("Student's GPA: "))
    if gpa >= 3.5:
        print(R_name, M_name, "has made it to the Deans list!")
    if gpa >= 3.25:
        print(R_name, M_name, "has made the Honor Roll!")
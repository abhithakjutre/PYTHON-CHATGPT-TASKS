

def percentage():
    total = (marks[0] + marks[1] + marks[2] + marks[3] + marks[4])
    result = total/ 5
    return result, total

def grade(per):
    print("\n")
    if percent >= 90:
        print("Grade: A+")
    elif percent >= 80:
        print("Grade: A")
    elif percent >= 70:
        print("Grade: B")
    elif percent >= 60:
        print("Grade: C")
    elif percent >= 50:
        print("Grade: D")
    else:
        print("Fail")




if __name__ == "__main__":
    name = input("Enter Student Name:  ")
    roll = int(input("Enter Student Rollno: "))

    marks = []

    subject = ["Hindi", "English", "Maths", "Science", "Drawing"]

    for i in subject:
        while True:
            sub = int(input(f"Enter {i} marks: "))
            if sub > 100 or sub < 1:
                print("Invalid Subject Number: ")
            else:
                marks.append(sub)
                break

    percent,total_marks = percentage()
    print("\n\nStudent Card: ")
    print(f"\nName : {name}")
    print(f"Roll no: {roll}")
    for i in range(0,5):
        print(f"{subject[i]} : {marks[i]}")

    print(f"Total Marks: {total_marks}")
    print(f"Percentage : {percent}%")
    grade(percent)


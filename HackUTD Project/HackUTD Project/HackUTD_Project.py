import csv
#cs = 21
#count = 0
instructor = ""
subject = ""
catalog = ""
newProf = ""
semester = input("Enter Semester (ex: Fall): ")
year = input("Enter Year: ")
subjectCode = input("Enter Subject Code (ex: ACCT): ")
catalogNum = input("Enter Catalog Number (ex: 2301): ")
instructors = []
def printLine():
    print("-----------------------------------------------------------------------------------------------------------------------")
def findProfessor(sub, catnum):
    with open(r'C:\Users\abbas\OneDrive\Documents\GitHub\utd-grades\raw_data\\' + semester + " " + year + '.csv', "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            instructor = f'{row["Instructor 1"]}'
            subject = f'{row["Subject"]}'
            catalog = f'{row["Catalog Number"]}'
            if sub == subject and catnum == catalog:
                instructors.append(instructor)
            line_count += 1
def findGrades(prof, sub, catnum):
    with open(r'C:\Users\abbas\OneDrive\Documents\GitHub\utd-grades\raw_data\\' + semester + " " + year + '.csv', "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            instructor = f'{row["Instructor 1"]}'
            if instructor == prof and sub == f'{row["Subject"]}' and catnum == f'{row["Catalog Number"]}':
                if (f'{row["A+"]}' != ""):
                    print("Number of Students with A+: " + f'{row["A+"]}')
                if (f'{row["A"]}' != ""):
                    print("Number of Students with A: " + f'{row["A"]}')
                if (f'{row["A-"]}' != ""):
                    print("Number of Students with A-: " + f'{row["A-"]}')
                if (f'{row["B+"]}' != ""):
                    print("Number of Students with B+: " + f'{row["B+"]}')
                if (f'{row["B"]}' != ""):
                    print("Number of Students with B: " + f'{row["B"]}')
                if (f'{row["B-"]}' != ""):
                    print("Number of Students with B-: " + f'{row["B-"]}')
                if (f'{row["C+"]}' != ""):
                    print("Number of Students with C+: " + f'{row["C+"]}')
                if (f'{row["C"]}' != ""):
                    print("Number of Students with C: " + f'{row["C"]}')
                if (f'{row["C-"]}' != ""):
                    print("Number of Students with C-: " + f'{row["C-"]}')
                if (f'{row["D+"]}' != ""):
                    print("Number of Students with D+: " + f'{row["D+"]}')
                if (f'{row["D"]}' != ""):
                    print("Number of Students with D: " + f'{row["D"]}')
                if (f'{row["D-"]}' != ""):
                    print("Number of Students with D-: " + f'{row["D-"]}')
                if (f'{row["F"]}' != ""):
                    print("Number of Students with F: " + f'{row["F"]}')
                if (f'{row["P"]}' != ""):
                    print("Number of Students with P: " + f'{row["P"]}')
                if (f'{row["CR"]}' != ""):
                    print("Number of Students with CR: " + f'{row["CR"]}')
                if (f'{row["NC"]}' != ""):
                    print("Number of Students with NC: " + f'{row["NC"]}')
                if (f'{row["I"]}' != ""):
                    print("Number of Students with I: " + f'{row["I"]}')
                if (f'{row["W"]}' != ""):
                    print("Number of Students with W: " + f'{row["W"]}')
                break
            line_count += 1
def pullRMP(prof, sub, catnum):
    with open(r'C:\Users\abbas\OneDrive\Documents\HackUTD_RMP_Data.csv', "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            if prof == f'{row["name"]}' and (sub + catnum) == f'{row["class_name"]}':
                print("Rating: " + f'{row["star_rating"]}' + "/5")
                print("Review: " + f'{row["comments"]}')
                print("Percentage Willing to Take Again: " + f'{row["take_again"]}')
                print("Difficulty: " + f'{row["diff_index"]}' + "/5")
                print("Attendance: " + f'{row["attendence"]}')
            line_count += 1
findProfessor(subjectCode, catalogNum)
instructors = [*set(instructors)]
print("\n")
printLine()
i = 1
for n in instructors:
    print(str(i) + ". " + n)
    i += 1;
professorNum = int(input("Enter Number Corresponding to Professor: "))
professor = ""
for n in instructors:
    if professorNum - 1 == instructors.index(n):
        professor = n;
        break
print("\n")
printLine()
findGrades(professor, subjectCode, catalogNum)
print("\n")
printLine()
pullRMP(professor, subjectCode, catalogNum)
print ("Program: Target GPA")
print ("Programmer: Michael Mordec")
print ("-------------------------")
# ---------------------------------------------------
# variables declared and initialized
msg1 = ""
msg2 = ""
totalHours = 0
creditsEarned = 0
creditsCurrent = 0
creditHoursEnrolled = 0
currentGPA = 0
targetGPA = 0 
targetGradePoints = 0
requiredGPA = 0
# ... declare and assign any additional variables here ...
# ---------------------------------------------------
print ("----- INPUTING Data -----")
msg1 = "GPA credit hours already completed ( Credits Earned ) "
creditsEarned = int(input("enter " + msg1))

msg2 = "Credit hours currently enrolled ( Remaining / Planned Credits )"
creditsCurrent = int(input("enter " + msg2))

msg3 = "Current GPA ( Cumulative ) "
currentGPA = float(input("enter " + msg3))
# ... complete the input section of this program ...
msg4 = "Target GPA "
targetGPA = float(input("enter" + msg4))

# ---------------------------------------------------
print ("----- PROCESSING Data -----")
totalHours = creditsEarned + creditsCurrent
targetGradePoints = targetGPA * totalHours
targetGradePoints -= creditsEarned * currentGPA
bestGPA=(creditsEarned*currentGPA+creditsCurrent*4)/(creditsEarned+creditsCurrent)
# ... complete the processing section of this program ...

# ---------------------------------------------------
print ("----- OUTPUTTING Data -----")
print ("The Desired Computed GPA:", targetGPA)
print ("The Best Possible Current GPA ( assuming Straight A's ):",bestGPA)
print ("An Echo of the Current Term Number of Credit Hours:",creditsCurrent)

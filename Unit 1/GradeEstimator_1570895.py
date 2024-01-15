#Requesting first name in the variable firstname, added space after question so input has space between question and answer.`strip()` function is used to remove any leading or trailing spaces from the user input. The `lower()` function converts the input to lowercase, and `capitalize()` is then applied to make the first letter uppercase. 
firstname=input("What is your first name? ").strip().lower().capitalize()
#Requesting last name in the variable lastname, added space after question so that there is room after question for user input.`strip()` function is used to remove any leading or trailing spaces from the user input. The `lower()` function converts the input to lowercase, and `capitalize()` is then applied to make the first letter uppercase.
lastname=input("What is your last name? ").strip().lower().capitalize()
#Saying Hello and printing the last name that was given in line 4 & first name that was given in line 2. 
print("Hello "+lastname + ", " + firstname)
#Assigning points for the homeworks for unit 1 of what I think I got. 
Unit1_discussion_points= 50
Unit1_course_project_points= 50
Unit1_core_assessment_points= 50
#This is the maximum amount of points for each task
task_maximum_points= 50
#This is to calculate the total points for the unit
total_points = Unit1_discussion_points + Unit1_course_project_points + Unit1_core_assessment_points
#This is uesd to display the total points
print("Total Points:", total_points)
#This is to check if maximum points were received for each of the tasks
discussion_max_points = (Unit1_discussion_points == task_maximum_points)
course_project_max_points = (Unit1_course_project_points == task_maximum_points)
core_assessment_max_points = (Unit1_core_assessment_points == task_maximum_points)
#This is to display the results for whether or not max points were received for each area of study
print("Got maximum points for Unit 1 discussion?", discussion_max_points)
print("Got maximum points for Unit 1 course project?", course_project_max_points)
print("Got maximum points for Unit 1 core assessment?", core_assessment_max_points)

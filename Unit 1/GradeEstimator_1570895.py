#Requesting first name in the variable firstname, added space after question so input has space between question and answer.`strip()` function is used to remove any leading or trailing spaces from the user input. The `lower()` function converts the input to lowercase, and `capitalize()` is then applied to make the first letter uppercase. 
firstname=input("What is your first name? ").strip().lower().capitalize()
#Requesting last name in the variable lastname, added space after question so that there is room after question for user input.`strip()` function is used to remove any leading or trailing spaces from the user input. The `lower()` function converts the input to lowercase, and `capitalize()` is then applied to make the first letter uppercase.
lastname=input("What is your last name? ").strip().lower().capitalize()
#Saying Hello and printing the last name that was given in line 4 & first name that was given in line 2 and added a space. 
print("Hello "+lastname + " " + firstname)
#Assigning points for the homeworks for unit 1 of what I received.
Unit1_discussion_points= 50
Unit1_course_project_points= 50
Unit1_core_assessment_points= 10
#This is the maximum amount of points for each task
#Professor did no state to remove the task_maximum_points but I made it a comment due to the different tasks have different numbers because Core Assessment only has 400 and the
#Course Project and Discussions have 800 points. d
#task_maximum_points= 400
#This is to calculate the total points for the unit by adding the units that have been completed Unit 3 direction A & B request for these variables.
#Unit2 variables were not requested to be made so input raw numbers.
total_discussion_points= [Unit1_discussion_points, 50]
total_course_project_points= [Unit1_course_project_points, 50]
total_core_assessment_points= [Unit1_core_assessment_points]
#This is uesd to display the total points for each of the different areas that decide the grade for the overall class while using a string as requested from Unit 3 direction C. 
disresult = "Currently you have " + str(sum(total_discussion_points)) + " points for discussions out of "+ str(400) 
print(disresult)
couresult= "Currently you have " + str(sum(total_course_project_points)) + " points for the Course Project out of " + str(400)
print(couresult)
corresult= "Currently you have " + str(sum(total_core_assessment_points))+ " points for the Core Assessment out of "+ str(200)
print(corresult)
#This is to check if maximum points were received for each of the tasks
#Professor did not request for the below to be modified in Unit 3, not sure if Unit 3 direction C was supposed to replace this.
#Updated to raw numbers because task minimums were removed due to new requirements in Unit 3 but causes an error. I do not believe this is necessary but do not want to get marked down points because Professor did not say remove.
discussion_max_points= (total_discussion_points == 400 )
course_project_max_points= (total_course_project_points == 400)
core_assessment_max_points= (total_core_assessment_points == 200)
#This is to display the results for whether or not max points were received for each area of study
#Professor did not request for the below to be modified in Unit 3, not sure if Unit 3 direction C was supposed to replace this.
#All responses will be False due to Unit 3 C asking us to update the maximum to the amount for the entire class such as 400 or 800 for Course Projects, Discussions, or Course Assessment
print("Got maximum points for Unit 1 discussion?", discussion_max_points)
print("Got maximum points for Unit 1 course project?", course_project_max_points)
print("Got maximum points for Unit 1 core assessment?", core_assessment_max_points)

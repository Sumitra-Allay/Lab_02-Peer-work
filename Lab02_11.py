# Lab02_11
# Smart Classroom Quiz and Performance Analyzer

# Step 1: Take IDs of students to generate unique value
id1 = input("Enter Student 1 ID: ")  #student id 1
id2 = input("Enter Student 2 ID: ")  #student id 2

# take last two digits
last1 = int(id1[-2:]) #2 last digits of std 1
last2 = int(id2[-2:]) #2 last digits of std 2

# Generate unique value
unique_value = (last1 + last2) % 10  #calculate unique value
print("Unique Value:", unique_value)  # Print unique value

# Step 2: Store student names
students = {} #sava name

while True: #use "While True until it reach to break"
    name = input("Enter student name (or type 'exit' to stop): ") #add names of the students and type "exit" if you want to stop
    
    # Stop condition (simple version)
    if name == "exit" or name == "EXIT" or name == "Exit": # Exit by typing "exit" if (any case)
        break
    
    # Check empty name
    if name == "": #If the name is empty
        print("Warning: Name cannot be empty. Skipping...")  #show "Warning: Name cannot be empty. Skipping..." 
        continue #continue to next
    
    # Store student with initial score 0
    students[name] = 0 #Store student 

# Display student names
print("List of Students:") #Print "List of Students:"
for s in students: #students in s
    print("-", s) #Then print it

# Step 3: Conduct quiz
for student in students: #Access each student
    print("Quiz for", student) #print quiz message for each students
    
    score = 0 #Initial score is 0
    
    # Question 1
    ans1 = int(input("Q1: " + str(unique_value) + " + 2 = ")) #ask question 1
    if ans1 == unique_value + 2: #check
        score = score + 1 #Add score 1 if correct answer
    
    # Question 2
    ans2 = int(input("Q2: " + str(unique_value) + " * 3 = ")) #Ask question 2 
    if ans2 == unique_value * 3: #check answer
        score = score + 1 #Add 1 point if correct answer
    
    # Question 3
    ans3 = int(input("Q3: " + str(unique_value) + " + 5 = ")) #Ask question 3
    if ans3 == unique_value + 5: #check
        score = score + 1 #Add 1 point if correct answer
    
    # Store score
    students[student] = score #Store score
    
    # Step 4: Performance level
    if score == 3: #If the student score 3
        performance = "Excellent" #excellent level
    elif score == 2: #If the student score 2
        performance = "Good" #good level
    elif score == 1: #If the student score 1
        performance = "Average" #Average level
    else: #If the student score 0 or less
        performance = "Poor" #poor level
    
    # Step 5: Certificate eligibility
    if score >= 2: #if the student score more than 2 
        certificate = "Eligible" #it is  "Eligible"
    else: #Or else
        certificate = "Not Eligible" #it is "Not Eligible"
    
    # Warning if score is 0
    if score == 0: #if they score 0
        print("Warning: Score is 0") #it will warn as "Warning: Score is 0"
    
    # Step 6: Display result
    print("Score:", score) #print score 
    print("Performance:", performance) # print performance 
    print("Certificate:", certificate) #print certificate
    
    # Step 7: Star pattern
    print("Stars Pattern:") #print "Stars Pattern:"
    print("*" * score) #print star score  of the students
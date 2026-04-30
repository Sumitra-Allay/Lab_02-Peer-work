# Lab02_11
# Smart Classroom Quiz & Performance Analyzer

# Step 1: Take student IDs and generate unique value
id1 = input("Enter Student 1 ID: ") 
id2 = input("Enter Student 2 ID: ")

# Extract last two digits
last1 = int(id1[-2:])
last2 = int(id2[-2:])

# Generate unique value
unique_value = (last1 + last2) % 10
print("Unique Value:", unique_value)

# Step 2: Store student names
students = {}

while True:
    name = input("Enter student name (or type 'exit' to stop): ")
    
    # Stop condition (simple version)
    if name == "exit" or name == "EXIT" or name == "Exit":
        break
    
    # Check empty name
    if name == "":
        print("Warning: Name cannot be empty. Skipping...")
        continue
    
    # Store student with initial score 0
    students[name] = 0

# Display student names
print("List of Students:")
for s in students:
    print("-", s)

# Step 3: Conduct quiz
for student in students:
    print("Quiz for", student)
    
    score = 0
    
    # Question 1
    ans1 = int(input("Q1: " + str(unique_value) + " + 2 = "))
    if ans1 == unique_value + 2:
        score = score + 1
    
    # Question 2
    ans2 = int(input("Q2: " + str(unique_value) + " * 3 = "))
    if ans2 == unique_value * 3:
        score = score + 1
    
    # Question 3
    ans3 = int(input("Q3: " + str(unique_value) + " + 5 = "))
    if ans3 == unique_value + 5:
        score = score + 1
    
    # Store score
    students[student] = score
    
    # Step 4: Performance level
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Average"
    else:
        performance = "Poor"
    
    # Step 5: Certificate eligibility
    if score >= 2:
        certificate = "Eligible"
    else:
        certificate = "Not Eligible"
    
    # Warning if score is 0
    if score == 0:
        print("Warning: Score is 0")
    
    # Step 6: Display result
    print("Score:", score)
    print("Performance:", performance)
    print("Certificate:", certificate)
    
    # Step 7: Star pattern
    print("Stars Pattern:")
    print("*" * score) 
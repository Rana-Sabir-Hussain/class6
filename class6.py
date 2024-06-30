"""
Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76


1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].

2. Write a for loop to calculate the average score of the students. Print the average score.

3. Write a for loop to assign grades based on the following criteria:
Score >= 90: Grade A
Score >= 80 and < 90: Grade B
Score >= 70 and < 80: Grade C
Score < 70: Grade D
Store these grades in a new dictionary called student_grades.

4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
Print the updated student_scores dictionary.
"""
student_scores={"Alice": 85,
                "Bob": 78,
               "Charlie": 92,
                "Diana": 88,
                "Evan": 76}
for name,score in student_scores.items():
    print(f"Student: {name}, Score: {score}")
total_scores=0
for score in student_scores.values():
    total_scores+=(score)
    
    average_score=(total_scores)/ len (student_scores)
    
print(f"the average_score is:{average_score}")

# 3. Assign grades based on score and store in student_grades dictionary
student_grades={}
for name,score in student_scores.items():
    if score>=90:
        student_grades[name]= "A"
    elif score>=80 and score<90:
        student_grades[name]= "B"
    elif score>=70 and score<80:
        student_grades[name]= "C"
    elif score<70:
        student_grades[name]= "D"
print(student_grades)

"""4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
Print the updated student_scores dictionary."""
for name,score in student_scores.items():
    student_scores[name]=int(score ) + 5
print(f"student_grades is : {student_scores}")

"""
Create a dictionary named employee_data with the following key-value pairs:
"John": 55000
"Emma": 60000
"Harry": 70000
"Sophia": 65000
"Mike": 48000

1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names.
2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly.

"""
employee_data={"John": 55000,
               "Emma": 60000,
               "Harry": 70000,
               "Sophia": 65000,
                "Mike": 48000  }
for name in employee_data:
    if employee_data[name]>60000:
        print(name)
salary={}
for salaryes in employee_data:
    salary[salaryes]=employee_data[salaryes]*1.1
print(salary)
    
"""
consider the list of dicts
book_list = [{"name": "The Great Gatsby", "quantity": 4}, {"name": "1984", "quantity": 6}, {"name": "To Kill a Mockingbird", "quantity": 3}, {"name": "Moby Dick", "quantity": 2}]
Write a for loop to assign one more detail "stock" based on the number of copies available:
Copies >= 5: "Popular"
Copies >= 3 and < 5: "Available"
Copies < 3: "Limited"
Store these stock categories in a same dict i.e book_list.
"""
book_list = [
    {"name": "The Great Gatsby", "quantity": 4},
    {"name": "1984", "quantity": 6},
    {"name": "To Kill a Mockingbird", "quantity": 3},
    {"name": "Moby Dick", "quantity": 2},
]

for book in book_list:
  quantity = book["quantity"]
  if quantity >= 5:
    book["stock"] = "Popular"
  elif quantity >= 3:
    book["stock"] = "Available"
  else:
    book["stock"] = "Limited"

print(book_list)

    
    
    
    
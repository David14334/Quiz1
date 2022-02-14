''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode

students = open("students.csv", 'r')

# create a csv object from the file object

students_file = csv.reader(students, delimiter = ",")

#skip the header row

next(students_file)

#create an outfile object for the pocessed record

outfile = open("processedStudents.csv", 'w')

#create a new dictionary named 'student_dict'

student_dict = {"student": [
{"stud_id": 124596780, 
"gpa" : 2.70},
{"stud_id": 345678901,
"gpa": 2.80},
{"stud_id": 789012345,
"gpa": 2.50},
{"stud_id": 890123456,
"gpa": 2.20}]}



#use a loop to iterate through each row of the file

for record in students_file:
    outfile.write(record[0] + ',' + record[1] + ',' + record[2] + ',' + record[3] + ',' + record[4] + ',' + record[5] + ',' + record[6] + ',' + record[7] + ',' + record[8] + "\n")

    #check if the GPA is below 3.0. If so, write the record to the outfile

gpa = float(record[8])
if gpa < 3.0 in students_file:
    outfile.write(record[8] + ',')
        



    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    





#print the entire dictionary

print(student_dict)

#Print the student id 

print(record[0])

#print out the corresponding GPA from the dictionary

print(record[8])

#close the outfile

outfile.close()








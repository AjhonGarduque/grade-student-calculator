import math

#ask for the student's namegit push origin main
name = input("What is your last name?: " )

#loops the code until a valid grade is entered
while True:

#collects the grades of the student
    first = int(input("What is your grade in Science?: "))
    second = int(input("What is your grade in English?: "))
    third = int(input("What is your grade in Math?: "))
    fourth = int(input("What is your grade in Physics?: "))
    fifth = int(input("What is your grade in P.E?: "))

#stores the grades of the student
    grades = [first, second, third, fourth, fifth]

#calculates the grades
    total = sum(grades)
    subs = len(grades)
    average = total / subs
    final = round(average)

    #validates input: makes sure that the grade inserted is below or equal to 100 and not less than 0
    if any(grade > 100 or grade < 0 for grade in grades):
        print("Grades must be below 100")
        #loops back if the grade inputted is invalid
        continue 
    else:
        #if all grades are valid, it shows each subject grade
        print("------------------")
        print('Science: ' +str(first))
        print('English: ' +str(second))
        print('Math" ' +str(third))
        print('Physics: ' +str(fourth))
        print('P.E: ' +str(fifth))

        #checks if the students passed or not
        print("------------------")
        print("Your grade total is: " +str(total))
        print("------------------")
        print("Your average is: " + str(average))
        
        #honor recognition
        if average >= 75:
            print("You passed!", end=" ")
            if average >= 98:
                print("Final Grade: " +str(final) + " Conrgrats! with highest honors")
            elif average >= 94.5:
                print("Final Grade: " +str(final) + " Congrats!! With high honors")
            elif average >= 89.5:
                print("Final Grade: " +str(final)+ " Congrats! With honors")
        #if average is below 75, displays the message
        else:
            print("Final Grade:" +str(final) + " You failed, do better next time")
        #exits the loop once complete    
        break
    
      
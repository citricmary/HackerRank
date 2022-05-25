def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] < 38:
            pass
        else:
            if grades[i] % 5 == 4:
                grades[i] += 1
            elif grades[i] % 5 == 3:
                grades[i] += 2
            else:
                pass
    print(grades)

gradingStudents([38, 42, 43, 44, 50])

        


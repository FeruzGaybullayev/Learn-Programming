universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]



import statistics
currency = '$' # global currency 

def enrollment_stats(universities):
    # Statistical calculation 
    total_number_of_enrolled_students = [i[1] for i in universities]
    annual_tuition_fees = [i[2] for i in universities]

    total_students = f"{sum(total_number_of_enrolled_students):,}"
    total_tuition = f"{currency}{sum(annual_tuition_fees):,}"

    student_mean = f"{statistics.mean(total_number_of_enrolled_students):,.2f}"
    student_median = f"{statistics.median(total_number_of_enrolled_students):,}"

    tuition_mean = f"{currency}{statistics.mean(annual_tuition_fees):,.2f}"
    tuition_median = f"{currency}{statistics.median(annual_tuition_fees):,}"
    
    # results 
    return f'''
*****************************
Total students: {total_students}
Total tuition: {total_tuition}

Student mean: {student_mean}
Student median: {student_median}

Tuition mean: {tuition_mean}
Tuition median: {tuition_median}
******************************
'''

print(enrollment_stats(universities))

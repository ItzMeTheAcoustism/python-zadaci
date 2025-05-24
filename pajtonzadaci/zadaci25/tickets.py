class ticketPrice:
    def __init__(mysillyobject, age, uni_student, weekend):
        mysillyobject.age = age
        mysillyobject.uni_student = uni_student
        mysillyobject.weekend = weekend

    price = 0

    def calculate_ticket_price_based_on_age(mysillyobject):
        age_of_user = mysillyobject.age

        if age_of_user >= 0 and age_of_user <= 4:
            return "Your ticket is free."
        if age_of_user >= 5 and age_of_user <= 12:
            price = 10
        if age_of_user >= 13 and age_of_user <= 17:
            price = 15
        if age_of_user >= 18 and age_of_user <= 64:
            price = 20
        if age_of_user >= 65:
            price = 12
        if age_of_user > 0 and age_of_user > 120:
            return "Incorrect input, try again."
        
        return price
    

    
    def uni_student_discount(mysillyobject):
        are_you_a_student = mysillyobject.uni_student
        uni_student_price = 0

        if are_you_a_student == "yes":
            uni_student_price = price * 0.90
            return uni_student_price
        if are_you_a_student == "no":
            uni_student_price = price + 0

        return price

    def weekend_discount(mysillyobject):
        is_it_the_weekend = mysillyobject.weekend
        weekend_price = 0

        if is_it_the_weekend == "yes":
            weekend_price = price * 0.90
            return weekend_price
        if is_it_the_weekend == "no":
            weekend_price = price + 0




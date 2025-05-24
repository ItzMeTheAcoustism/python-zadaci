from tickets import ticketPrice

traveller = ticketPrice((int(input("Input age: "))), (input("Are you a student? ")),  (input("Is it a weekend? ")) )
print("Your price for ticket is:", traveller.calculate_ticket_price_based_on_age(), traveller.uni_student_discount(), traveller.weekend_discount(), "euros.")



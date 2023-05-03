#Declare Variable we need 

total_seats = 150
normal_seats = 130
recliner_seats = 20
normal_price = 250
recliner_price = 400
combo_price = 300

# Ask the user how many tickets they want to book
num_tickets = int(input("How many tickets do you want to book? _____"))

# Check if the number of tickets are available in system or not
if num_tickets > total_seats:
    print("Sorry, We'r Fully Booked")
else:

# Ask the user for ticket type 
    seat_type = input("Do you want to book normal or recliner Seats?_____ ")

    if seat_type == "normal":
        total_seats -= num_tickets
        normal_seats -= num_tickets
        total_price = (250 * num_tickets)
        
    elif seat_type == "recliner":
        total_seats -= num_tickets
        recliner_seats -= num_tickets
        total_price = (400 * num_tickets)

    else:
        print("Please Choose Right Ticket Type")
        
# Ask the user if they want to add a combo      
    combo = input("Do you want to add a combo for Rs. 300/- ?______ ")

    if combo == "yes":
        total_price += combo_price
        
    print("-"*100)

#print final bill
    print("Total Seats Available : ", total_seats)
    print("Total Normal Seats Available : ", normal_seats)
    print("Total Recliner Seats Available : ", recliner_seats)
    
    print("-"*100)
    
    print("Total price for your show : ", total_price)


total_seats = 150
normal_seats = 130
recliner_seats = 20
normal_price = 250
recliner_price = 400
combo_price = 300

while True:
    name = input("Enter Your name here : ")
    # Ask the user how many tickets they want to book
    num_tickets = int(input("How many tickets do you want to book? _____"))

    # Check if the number of tickets are available in system or not
    if num_tickets > total_seats:
        print("Sorry, We're Fully Booked")
        break
    else:
        # Ask the user for ticket type 
        seat_type = input("Do you want to book normal or recliner Seats?_____ ")
        if seat_type == "normal":
            if num_tickets <= normal_seats:
                total_seats -= num_tickets
                normal_seats -= num_tickets
                total_price = normal_price * num_tickets
            else:
                print("Sorry, we have only available normal seats: ",normal_seats)
                continue
        elif seat_type == "recliner":
            if num_tickets <= recliner_seats:
                total_seats -= num_tickets
                recliner_seats -= num_tickets
                total_price = recliner_price * num_tickets
            else:
                print("Sorry, we have only available recliner seats: ",recliner_seats)
                continue
        else:
            print("Please Choose Right Ticket Type")
            continue

        # Ask the user if they want to add a combo      
        combo = input("Do you want to add a combo for Rs. 300/- ?______ ")
        if combo == "yes":
            total_price += combo_price

        print("-"*100)

        #print final bill
        print("Customer Name: ",name)
        print("Total Seats Available : ", total_seats)
        print("Total Normal Seats Available : ", normal_seats)
        print("Total Recliner Seats Available : ", recliner_seats)
        print("-"*100)
        print("Total price for your show : ", total_price)

    if num_tickets > total_seats:
        print("we have only seats available now: " ,total_seats)
        print("_"*60)
        break

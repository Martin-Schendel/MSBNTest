while True:
    # initialize list of days, sales list, and total sales
    daysOfTheWeek = ["Sunday", "Monday", "Tuesday",
                     "Wednesday", "Thursday", "Friday", "Saturday"]
    salesList = []
    totalSales = 0.0
# for loop to get user to input sales
    for day in daysOfTheWeek:
        print("Enter the sales for", day, end="")
        daySales = float(input(": $"))
# validate for greater or equal to zero
        while daySales < 0.0:
            print("You must enter a number greater than or equal to 0.")
            print("Enter the sales for ", day, end="")
            daySales = float(input(": $"))
# append validated input to saleslist
        salesList.append(daySales)
# calculate total sales
    totalSales = sum(salesList)
# output total sales properly formatted
    print("Total sales for the week: $", format(totalSales, '.2f'), sep="")
# ask user if they want to run again
    print("Would you like to enter another week?")
    runAgain = input("Enter Y to continue or N to quit: ")
    if runAgain != "y" and runAgain != "Y":
        break

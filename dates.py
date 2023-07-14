
import sys

def main():
    while True:
        try:
            date = input()
            p(date)
        except  EOFError as e:
            break
flag = True
stderr_message = True
def p(date):
    
    final_output = ""
    checked = ""
    valid_days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    valid_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    # Splits the test date by ethier /, - or space 
    date_split = date.split("/")
    if len(date_split) != 3:
        date_split = date.split(" ")
    if len(date_split) != 3:
        date_split = date.split("-")
    if len(date_split) != 3:
        checked = " - INVALID"
        print(date+checked, file=sys.stdout)
        print("Invalid date input format", file=sys.stderr)
        global flag
        flag = False
        global stderr_message
        stderr_message = False

        
        #sys.exit(1)
    
        # Method day_check that looks at the day section of the split and calculates if the day is valid within the possible days
        # array and returns the newly formatted day else stores an error message.
    if flag == True and stderr_message == True:
        def day_check(day):
            output = day
            global error_message_day
            global checked
            if output.isdigit() != True or len(output) > 2:
                checked = " - INVALID"
                print(date+checked, file=sys.stdout)
                print("Invailid day input", file=sys.stderr)
                global flag
                flag = False
                global stderr_message
                stderr_message = False
            if stderr_message == True:
                if len(output) ==1:
                    output="0"+ day
                if valid_days.count(output) > 0:
                        return output
                else:
                    checked = " - INVALID"
                    print(date+checked, file=sys.stdout)
                    print("Invailid day input", file=sys.stderr)
                    flag = False
                    stderr_message = False
                return output        


        # Method year_check that uses the year stored split and formated the year into the format requried and then clacultes if the year
        # is valid and in range of the years allowed and returns or stores error message.
    if flag == True and stderr_message ==True:
        def year_check(year):
            output = year
            global error_message_year
            global checked
            if output.isdigit() == True:
                if len(output) == 2:
                    if int(output) >= 50:
                        output = "19"+output
                    if int(output) <= 49:
                        output = "20"+output
                if int(output) > 3000 or int(output) < 1753:
                    checked = " - INVALID"
                    print(date+checked, file=sys.stdout)
                    print("Year out of range", file=sys.stderr)
                    global flag
                    flag = False
                    global stderr_message
                    stderr_message = False
                    
                
            else:
                checked = " - INVALID"
                print(date+checked, file=sys.stdout)
                print("Year does not contant charaters", file=sys.stderr)
                flag = False
                stderr_message = False
            if stderr_message == True:
                if len(output) > 4:
                    checked = " - INVALID"
                    print(date+checked, file=sys.stdout)
                    print("Year does not contant charaters", file=sys.stderr)
                    flag = False
                    stderr_message = False
            return output


        # Method month_check that formates the month output in the split array by checking to see if it is a string input or number imput.
        # returns the formated month or stores an error message.
    if flag == True and stderr_message == True:
        def month_check(month):
            output = month
            global error_message_month
            global checked
            
            if len(output) > 3:
                checked = " - INVALID"
                print(date+checked, file=sys.stdout)
                print("Invailid month character input", file=sys.stderr)
                global flag
                flag = False
                global stderr_message
                stderr_message = False
            if stderr_message == True:
                if len(output) == 3:
                    if output.isupper() == True or output.islower() == True or output.istitle() == True:
                        output = month.capitalize()
                        if valid_months.count(output) > 0:
                            return output
                    else: 
                        checked = " - INVALID"
                        print(date+checked, file=sys.stdout)
                        print("Invailid month character input", file=sys.stderr)
                        flag = False
                        stderr_message = False
                        
            if stderr_message == True:        
                if output.isnumeric():
                    if len(output) < 3:
                            if int(output) == 1:
                                    output = "Jan"
                                    return output
                            elif int(output) == 2:
                                    output = "Feb"
                                    return output
                            elif int(output) == 3:
                                    output = "Mar"
                                    return output
                            elif int(output) == 4:
                                    output = "Apr"
                                    return output
                            elif int(output) == 5:
                                    output = "May"
                                    return output
                            elif int(output) == 6:
                                    output = "Jun"
                                    return output
                            elif int(output) == 7:
                                    output = "Jul"
                                    return output
                            elif int(output) == 8:
                                    output = "Aug"
                                    return output
                            elif int(output) == 9:
                                    output = "Sep"
                                    return output
                            elif int(output) == 10:
                                    output = "Oct"
                                    return output
                            elif int(output) == 11:
                                    output = "Nov"
                                    return output
                            elif int(output) == 12:
                                    output = "Dec"
                                    return output
                            else: 
                                checked =  " - INVALID"
                                print(date+checked, file=sys.stdout)
                                print("Month input greater then 12", file=sys.stderr)
                                flag = False
                                stderr_message = False
                else:
                    checked =  " - INVALID"
                    print(date+checked, file=sys.stdout)
                    print("Month input greater then 12", file=sys.stderr)
                    flag = False 
                    stderr_message = False

                        

            return output

        # Method leap_year that calculates if the year that has been imported in a leap year or not.
    def leap_year(year):
        output  = False
        if (year % 400 == 0) and (year % 100 == 0):
            output = True
        elif (year % 4 ==0) and (year % 100 != 0):
            output = True
        return output
    
    if flag == True and stderr_message == True:       
        current_day = day_check(date_split[0])
    if flag == True and stderr_message == True: 
        current_month = month_check(date_split[1])
    if flag == True and stderr_message == True: 
        current_year = year_check(date_split[2])

            # checks to see if the month input is a month that is only 30 days not 31.
    if flag == True and stderr_message == True:
        if current_month == "Apr" and int(current_day) == 31 or current_month == "Jun" and int(current_day) == 31 or current_month == "Sep" and int(current_day) == 31 or current_month == "Nov" and int(current_day) == 31:   
            checked = " - INVALID"
            print(date+checked, file=sys.stdout)
            print("Invalid day input for month", file=sys.stderr)
            flag = False  
            stderr_message = False
            # If feb then can only be 28 days. 
    if flag == True and stderr_message == True:
        if current_month == "Feb" and int(current_day) > 28 and leap_year(int(current_year))==False:
            checked = " - INVALID"
            print(date+checked, file=sys.stdout)
            print("Invalid day input for month", file=sys.stderr)
            flag = False
            stderr_message = False
            # If its a current leap year then feb can be up to 29 days.
    if flag == True and stderr_message == True:
        if current_month == "Feb" and int(current_day) == 29 and leap_year(int(current_year)) == True:
            checked = ""
        #print(type(current_day))
        #print(type(current_month))
        #print(type(current_year))  
    if flag == True and stderr_message == True:
        final_output = current_day + " " + current_month + " " + current_year 
        print(final_output)
    flag = True
    stderr_message = True


if __name__ == "__main__":
    main()

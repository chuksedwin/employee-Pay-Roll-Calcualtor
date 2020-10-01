# program for payroll calculations

#function for number of hours worked, checking data entry validation and  friendly  error message output.

def numberOfHours(prompt, minimum, maximum) :
    goodValue = False
    while not goodValue :
        try :
            lineOfInput = input(prompt)
            value = float(lineOfInput)
            if (value < minimum) or (value > maximum) :
                print("** Hours Worked must be greater than zero ... Try again. You entered", value)
            else :
                goodValue = True;
        except ValueError:
            print("Non numeric characters entered. Must enter only numeric characters. You entered", lineOfInput)

    return value

#function for rate of pay, checking data entry validation and  friendly  error message output.

def rateOfPay(prompt, minimum, maximum) :
    goodValue = False
    while not goodValue :
        try :
            lineOfInput = input(prompt)
            value = float(lineOfInput)
            if (value < minimum) or (value > maximum) :
                print("** Rate of pay must be greater than zero ... Try again. You entered", value)
            else :
                goodValue = True;
        except ValueError:
            print("Non numeric characters entered. Must enter only numeric characters. You entered", lineOfInput)

    return value

#function for percentage deduction,checking data entry validation and  friendly  error message output.

def deductionPercentage(prompt, minimum, maximum) :
    goodValue = False
    while not goodValue :
        try :
            lineOfInput = input(prompt)
            value = float(lineOfInput)
            if (value < minimum) or (value > maximum) :
                print("** Percentage must be greater than zero (minimum = 1 and maximum = 100)... Try again. You entered", value)
            else :
                goodValue = True;
        except ValueError:
            print("Non numeric characters entered. Must enter only numeric characters. You entered", lineOfInput)

    return value

#getting names as input  from employees, number of work hours and hourly rate
    
employeeNames = input("Enter the employee's name : ",)


numberOfHours = numberOfHours("Enter hours worked : ", 1, 1000)


rateOfPay = rateOfPay("Enter hourly rate of pay : ", 1, 1000)


# creating grosspay, amountOfDeduction and netPay as variables

grossPay = 0 ;

amountOfDeduction = 0 ;

netPay = 0 ;

# Employee tax exempt code section

taxExempt = input("Is the employee  tax exempt? [Y/N] : ", )
if  (taxExempt == "N" ):
    deductionPercentage = deductionPercentage("Enter deduction percentage : ", 1, 100) # tax rate (%)
else:
    deductionPercentage =  0 ;
    
#calculate and output gross pay, deductions and net pay 

grossPay = numberOfHours * rateOfPay

amountOfDeductions = grossPay * deductionPercentage / 100

netPay = grossPay - amountOfDeductions

print("\n","______________________________________________________")
print("Employee Name: ","\t", employeeNames )
print("Hourly Rate: "," ","\t","$","","","{:.2f}".format(rateOfPay) )
print("Hour Worked: ","\t","\t"," ","","","{:.2f}".format(numberOfHours) )
print(" ","\t"," ", " ", "  "," ","      ----------")
print("Gross Pay: ","\t","\t","$","","{:.2f}".format(grossPay) )
print("Deductions: ","\t"," "," "," ","-","$"," ","{:.2f}".format(amountOfDeductions) )
print(" ","\t"," ", " ", "  "," ","      ----------")
print("Net Pay: ","\t","\t","$","","{:.2f}".format(netPay) )


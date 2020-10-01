# program use to calculate payroll of employees in an organization

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



while True:
    employeeNames = int(input("Enter the employee's name :  "))
    if type(employeeNames) is int:
        continue
    else:
        print ("You entered a STR data type. Congratulations")
        break

#get the number of  hours worked from the employee 

numberOfHours = numberOfHours("Enter hours worked : ", 1, 1000)

#get the  hourly rate from the employee ($)

rateOfPay = rateOfPay("Enter hourly rate of pay : ", 1, 1000)

# grossPay, amountOfDeduction and netPay variables

grossPay = 0

amountOfDeduction = 0

netPay = 0

# Is the employee tax exempt

taxExempt = input("Is the employee  tax exempt? [Y/N] : ", )
if  (taxExempt == "N" ):
    deductionPercentage = deductionPercentage("Enter deduction percentage : ", 1, 100) # tax rate (%)
else:
    deductionPercentage =  0
    
grossPay = numberOfHours * rateOfPay

amountOfDeductions = grossPay * deductionPercentage / 100

netPay = grossPay - amountOfDeductions

print("\n","______________________________________________________")
print("Employee Name: " ," "," ",       employeeNames )
print("Hourly Rate: " ," "," ", " ","$","",    "{:.2f}".format(rateOfPay) )
print("Hour Worked: " ," "," "," ", " ","",     "{:.2f}".format(numberOfHours) )
print(" ", " ", " ", "  "," ","         ----------")
print("Gross Pay: " ," "," "," "," ",   "$","{:.2f}".format(grossPay) )
print("Deductions:"," "," "," " ,"-","$","","{:.2f}".format(amountOfDeductions) )
print(" ", " ", " ", "  "," ","         ----------")
print("Net Pay: "," "," "," "," ", " ", "$","{:.2f}".format(netPay) )


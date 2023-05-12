


#--------------------
#---- Nested If------
#---------------------


uName = "Salar"
isStudent = "yes"
uCountry = "Deutschland"
cName = "Python"
cPrice = 100

if uCountry == "Deutschalnd" or uCountry == "USA" :
    # print(f"Hi {uName} because U R from {uCountry}") # Hi Salar because U R from Deutschalnd
    if isStudent == "yes":
        print(f"Hi {uName} because U R from {uCountry} And Student ") # Hi Salar because U R from Deutschland And Student
        print(f"The Course {cName} price is  {cPrice - 90}") #  The Course Python Price is 10
    else :
        print(f"Hi {uName} because U R from {uCountry}") # Hi Salar because U R from Deutschalnd
        print(f"The Course {cName} price is  {cPrice - 80}") #  The Course Python price is  20

elif uCountry == "USA" :
    print(f"Hi {uName} because U R from {uCountry}") # Hi Salar because U R from USA
    print(f"The Course {cName} price is  {cPrise - 80}") # The Course Python price is 20

elif uCountry == "Croatia" or uCountry == "Polen": 
    print(f"Hi{uName.strip()} because U R from {uCountry} ") # Hi Salar because U R from Croatia 
    print(f"The Course{cName.strip()} Price is  {cPrice - 60} ") # The Course Python Price is  40


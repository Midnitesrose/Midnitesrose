 
def Dcalc():
    a = int(input ("Please enter the number of miles to convert to Kilometers: "))
    Kcalc = float( a * 1.60344)
    print (a, " miles is equal to ", Kcalc, "kilometers.")
    return
 
def Tcalc():
    b = int(input ("Please enter the temperature in Fahrenheit to convert to Celius: " ))
    Ccalc = float((b - 32) *5/9)
    print (b, " degrees Fahrenheit is equal to ", Ccalc, "degrees Celsius.")
    return
 
def Wcalc():
    c = int(input ("Please enter the amount of pounds to convert to Kilogram: "))
    kilocalc = float( c * 0.4535237)
    print (c, " pounds is equal to ", kilocalc, "Kilograms")
    return
 
def main():
    print ("\n" "DISTANCE", "\n" )
    Dcalc()
    print ("\n" "TEMPERATURE",   "\n")
    Tcalc()
    print ("\n" "WEIGHT", "\n")
    Wcalc()
    return
 
main()

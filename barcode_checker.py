# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Loan
# Section: 574
# Assignment: 9.2
# Date: 9 10 22
#
count = 0
filename = input("Enter the name of the file:") #ask user for the name of the file
barcodeReader = open(filename,'r+') # we create a used variable that opens the file the user wants
for nextline in barcodeReader:#we read through every line of the file
    
    lst1 = [] 
    lst2 = []
    check = False
    sum1 = 0
    sum2 = 0 
    for i in range(12):# take the first 12 digits of every line
        if i % 2 == 0:
            lst1.append(int(nextline[i]))#sort it to every other one starting with the 1st value
        else:
            lst2.append(int(nextline[i]))#sort it to every other one starting with the 2nd value
    for i in range(len(lst1)):# add this list to create a total sum
        sum1 += lst1[i]
        sum2 += lst2[i]
    sum2 *= 3
    sum2 += sum1
    sum2 = str(sum2)
    sum2 = sum2[len(sum2)-1]
    sum2 = 10 - int(sum2)
    if (sum2 == int(nextline[12])):  # checks to see if the last digit of the sum calculations is equal to the last digit of the barcode
        check = True
    with open("valid_barcodes.txt", 'w') as outputBarcode:#if it is true we add that barcode onto our new text file
        if check == True:
            outputBarcode.write(nextline)
    with open('valid_barcodes.txt','r') as outputBarcode:#we read the new text file to see the amount of valid barcodes
        for countline in outputBarcode:
            count += 1 
            
print(f" There are {count} valid barcodes")
barcodeReader.close()

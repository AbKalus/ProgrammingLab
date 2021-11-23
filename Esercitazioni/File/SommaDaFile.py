#Funzione che somma le vendite da un file
def sumSalesFromFile(openedFile):
    sumSales = 0
    for line in openedFile:
        elements = line.split(',')
        if elements[0] != 'Date':
            sumSales += float(elements[1])
    return sumSales

def sumSalesTest(openedFile):
    sumSales = 0
    for i,line in enumerate(openedFile):
        if i == 3:
            break
        elements = line.split(',')
        if elements[0] != 'Date':
            sumSales += float(elements[1])
    return sumSales

#Apro e leggo il file
my_file = open('shampoo_sales.csv', 'r')

#Stampo sumSales ovvero la somma delle vendite
print("Sum Sales = {}" .format(sumSalesTest(my_file)))
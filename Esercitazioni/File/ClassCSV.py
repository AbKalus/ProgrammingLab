class CSVFile():
    
    def __init__(self, file_name):
        
        #Set File name and file
        self.name = file_name

    def get_data(self):
        file_list = []
        openedFile = open(self.name, 'r')
        for line in openedFile:
            lineElements = line.split(',')
            if lineElements[0] != 'Date':
                lineElements[1] = lineElements[1].strip()
                file_list.append({lineElements[0] : lineElements[1]})
        return file_list

shampooFile = CSVFile('shampoo_sales.csv')
shampooList = shampooFile.get_data()

for line in shampooList:
    print(line)
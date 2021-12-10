class CSVFile():
    
    def __init__(self, file_name):
        
        #Set File name and file
        self.name = file_name            
        

    def get_data(self):
        file_list = []
        try:
            openedFile = open(self.name, 'r')
            for line in openedFile:
                lineElements = line.split(',')
                if lineElements[0] != 'Date':
                    for element in lineElements:
                         lineElements[1] = lineElements[1].strip()
                    file_list.append({lineElements[0] : lineElements[1]})
        except Exception as e:
            print('E\' stato riscontrato il seguente problema: "{}"'.format(e))
        return file_list

class NumericalCSVFile(CSVFile):
    def get_data(self):
        file_list = []
        try:
            if isinstance(self.name, str):
                raise ErroreAIDA('Il nome del file non è una stringa, nome -> {}'.format(self.name))
            else:
                openedFile = open(self.name, 'r')
                for line in openedFile:
                    lineElements = line.split(',')
                    if lineElements[0] != 'Date':
                        try:
                            lineElements[1] = float(lineElements[1].strip())
                            file_list.append({lineElements[0] : lineElements[1]})
                        except Exception as e:
                            print('E\' stato riscontrato il seguente errore di conversione: "{}"'.format(e));
        except ErroreAIDA as a:
            print("{}".format(a))
        except Exception as e:
            
            print('E\' stato riscontrato il seguente problema: "{}"'.format(e))
        return file_list

shampooFile = NumericalCSVFile(1235)
shampooList = shampooFile.get_data()

for line in shampooList:
    print(line)
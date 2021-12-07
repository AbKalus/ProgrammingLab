#CSVFile exercise
#classe CSVFile
class CSVFile:

    #costruttore __init__ classe
    def __init__ (self, name):
        """Costruttore, setta il parametro nome ovvero il nome file
            name -- nome del file
        """
        
        #Set filename
        self.name = name
        
        #test lettura file
        #flag per sapere se il file è leggibile
        self.readable = True
        if isinstance(self.name, str):
            try:
                #Apro il file, leggo la prima riga e lo chiudo
                test_fr = open(self.name, 'r')
                test_fr.readline()
                test_fr.close()
            except Exception as e:
                #se il file non è leggibile setto il flag a false e stampo l'errore generato
                self.readable = False
                print('--------------ERRORE--------------\n...è stato riscontrato il segunete problema{}'.format(e))
        else:
            raise Exception('Ho avuto un errore, ecco il parametro che lo ha generato: "{}"'.format(self.name))
    
    def len_file(self):
        file = open(self.name, 'r')
        count = 0.
        for line in file:
            count += 1.
        return count
    
    #metodo per restituire il file sottoforma di lista
    def get_data (self, start=None, end=None):
        """ This method return the list of the CSV file
            Keyword arguments:
            start -- this parameter determines which line you want to start from
            end -- this parameter determines which line you want to go up to
        """
        
        #Controllo se i valori inseriti non sono stringhe
        if not isinstance(start, str) or not isinstance(end, str):
            #se non sono stringhe ma sono float allora li converto per difetto in interi
            if type(start) == float:
                print('Il valore start è stato arrotondato per difetto')
                start = int(start)
        
            if type(end) == float:
                print('Il valore end è stato arrotondato per difetto')
                end = int(end)
        else:
            #se sono stringhe non faccio nulla
            self.readable = False
        
        #Il valore start deve essere minore del valore end, se è maggiore non stampo nulla
        if start > end:
            print('Lettura file IMPOSSIBILE la riga di inzio e maggiore di quella di fine')
            self.readable = False
        
        #dichiarazione lista vuota (valore di ritorno)
        file_list = []
        
        #controlo il valore del flag per vedere se posso leggere il file
        if self.readable:
            #lettura file
            file_read = open(self.name, 'r')
            n_row = self.len_file()-1
            if start is None and end is None:
                print('I valori "start" ed "end" non sono stati impostati.\nVerra restituito la lista contente tutte le righe.')
                start = 0;
                end = n_row;
            if start < 0:
                print('Il valori "start" è inferiore a 0 quindi la riga iniziale sarà impostata a 0')
                start = 0;
            if end > n_row:
                print('Il valori "end" è maggiore del numero di righe del file quindi la lettura verrà effettuata fino all\'ultimo elemento')
                end = n_row;
            
            #scorrimento file e inserimento dati nella lista
            #dichiarazione variaibile contatore
            count = 0
            for line in file_read:
                #divido la riga in colonne delimitandola con il carattere ','
                line_elements = line.split(',')
                #controllo per saltare la lettura dell'intestazione
                if line_elements[0] != 'Date':
                    if count >= start and count <= end:
                        #elimino il carattere '\n' dall'ultima colonna
                        line_elements[-1] = line_elements[-1].strip()
                        file_list.append(line_elements)
                count+=1
            #chiusura del file
            file_read.close()
        else:
            file_list = None
        return file_list

#estensione classe CSVFile in NumericalCSVFile
class NumericalCSVFile(CSVFile):
    
    #override metodo
    def get_data (self, start=None, end=None):
        """ This method return the list of the CSV file
            Keyword arguments:
            start -- this parameter determines which line you want to start from (default None)
            end -- this parameter determines which line you want to go up to (default None)
        """
        
        file_list = super().get_data(start, end)
        numerical_file_list = []
        
        for line in file_list:
            #gestisco un eventuale errore generato da una conversione in float
            try:
                for i in range(1,len(line)):
                    line[i] = float(line[i])
                    i+=1
                    numerical_file_list.append(line)
            except Exception as e:
                print('-----------ERRORE--------------\n...è stato generato il seguente errore: {}'.format(e))
        
        return numerical_file_list

nFile_ss = NumericalCSVFile('shampoo_sales.csv')
nList_ss = nFile_ss.get_data(0,100)
if nList_ss is None:
    print('file_list: {}'.format(nList_ss))
else:
    for line in nList_ss:
        print('{}'.format(line))
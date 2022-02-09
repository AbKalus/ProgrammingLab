from operator import itemgetter
from numpy import empty

class ExamException(Exception):
    pass

class CSVFile:
    '''
    Classe usata per leggere un file
    
    ...
    
    Attributi
    ---------
    name : str
        nome del file
    '''
    
    def __init__ (self, name):
        '''
        Costruttore classe CSVFile
        
        ...
        
        Parametri
        ---------
        name : str
            nome del file
        readable : bool
            flag lettura file
        '''
        self.name = name
        self.readable = True
    
    def get_data (self):
        ''' 
        Metodo per restituire una lista del file csv in lettura
        
        ...
        
        Raises
        ------
        ExamException
            - nel caso il file non sia stato passato come stringa
            - nel caso il file non sia leggibile
            
            
        
        Return
        ------
        list of lists
            lista di liste del file CSV

        '''
        #Dichiarazione lista vuota (valore di ritorno)
        file_lst = []
        
        #Test lettura file
        #Flag per sapere se il file è leggibile
        if isinstance(self.name, str):
            try:
                #Apro il file, leggo la prima riga e lo chiudo
                test_fr = open(self.name, 'r')
                test_fr.readline()
                test_fr.close()
            except:
                #Se il file non è leggibile setto il flag a false e stampo l'errore generato
                self.readable = False
        else:
            raise ExamException('Ho avuto un errore, ecco il parametro che lo ha generato: "{}"'.format(self.name))
        
        #Uso il flag per vedere se posso leggere il file
        if self.readable:
            #Lettura file
            file_rd = open(self.name, 'r')
            
            #Scorrimento file e inserimento dati nella lista
            for line in file_rd:
                #Divido la riga in colonne delimitandola con il carattere ','
                line_elements = line.split(',')
                
                #Controllo per saltare la lettura dell'intestazione
                if line_elements[0] != 'date':
                    #elimino il carattere '\n' dall'ultima colonna
                    line_elements[-1] = line_elements[-1].strip()
                    file_lst.append(line_elements)
            #chiusura del file
            file_rd.close()
        else:
            raise ExamException('Il file non è leggibile o non esiste')
        return file_lst
    
class CSVTimeSeriesFile(CSVFile):
    '''
    Classe usata per file conteneti time series
    Estensione della classe CSVFile
    
    ...
    
    Attributi
    ---------
    name : str
        nome del file
    '''
    
    def __init__(self, name):
        '''
        Costruttore classe CSVTimeSeriesFile
        
        ...
        
        Parametri
        ---------
        name : str
            nome del file
        '''
        super().__init__(name)
    
    def get_data(self):
        '''
        Override metodo get_data di CSVFile
        
        ...
        
        Raises
        ------
        ExamException
            - La lista contiene valori dupplicati, tipo errore Timestamp
            - Timestamp error, CSV file non ordinato
        
        Return
        ------
        list of lists
            lista di liste contente i dati del file CSV
        '''
        csv_lst = super().get_data()
        if csv_lst is not empty:
            lst_of_lsts = []
            dct = {}
            #Filtro la lista aggiungedo mantendendo solo i valori con l'anno convertibile in intero
            for line in csv_lst:
                if isinstance(line[1], int) and  line[1] > 0:
                    try:
                        int(line[0].split('-')[0])
                        lst_of_lsts.append(line)
                    except:
                        pass
            
            dct = {line[0]: line[1] for line in lst_of_lsts}
            
            #Se la lunghezza del dizionario non coincide con quella del lista filtrata allora sono presenti valori dupplicati
            if len(dct) != len(lst_of_lsts):
                raise ExamException('La lista contiene valori dupplicati, tipo errore Timestamp')
            
            #lst_of_lsts oridnata ListOfLists per data (ordine crescente)
            sorted_ll = sorted(lst_of_lsts, key=itemgetter(0))
            #Controllo se la posizione degli elementi delle liste sono cambiate, se sono cambiate significa che le date sono disordinate
            for el1,el2 in zip(lst_of_lsts, sorted_ll):
                if not(el1[0].__eq__(el2[0])):
                    raise ExamException('Timestamp error, CSV file non ordinato')
        
        return lst_of_lsts

def is_list_of_list(lst_of_lsts):
    '''
    Funzione per controllare se è stata passata una lista di liste
    
    ...
    
    Parametri
    ---------
    lst_of_lsts : list of lists
        lst_of_lsts è la lista da controllare
    '''
    res = True
    for lst in lst_of_lsts:
        if isinstance(lst, list):
            res *= True
        else:
            res *= False
    return res


def compute_avg_monthly_difference(time_series, first_year=None, last_year=None):
    '''
    Funzione per calcolare la differenza media del numero di passeggeri mensile tra anni consecutivi
    
    ...
    
    Parametetri
    -----------
    time_series : list of lists
        time series è la lista di liste contenete i dati per il calcolo della differrenza media mensile
    first_year : str
        first_year è l'anno di inizio dell'intervallo su cui si vuole calcolare la differenza media mensile
    last_year : str
        last_year è l'anno finale dell'intervallo su cui si vuole calcolare la differenza media mensile
        
    Raises
    ------
    ExamException
        - se time_series non p una lista
        - se time-series è vuota
        - se time_series non è una lista di liste
        - se la lista di liste è completamente vuota
        - se gli anni non sono stringhe
        - se l'anno di partenza dell'intervallo è maggiore di quello finale
        - se la lunghezza del dizionario creato non coincide con quella della time_series
        - se ordinando la time_series non coincide con la time_series non ordinata
        - se first_year o last_year oppure entrambi non sono anni presenti nella time_series
    
    Return
    ------
    list
        la funzione restituisce la lista delle differenze medie mesnili
    '''
    #Controllo se time_series è una lista
    if not(isinstance(time_series, list)):
        raise ExamException('Errore time series non è una lista')

    #Controllo se la time_series ha elementi
    if time_series is empty:
        raise ExamException('Errore time series è una lista vuota')
    
    #Controllo se la lista è una lista di liste
    if not(is_list_of_list(time_series)):
        raise ExamException('La lista non è una lista di liste')
    
    #Controllo se la lista di liste è completamente vuota
    if not(any(time_series)):
        raise ExamException('Lista di liste vuote')
    
    #Controllo se gli anni sono di tipo corretto
    if (not(isinstance(first_year, str))) or (not(isinstance(last_year, str))):
        raise ExamException('Valori first_year = {} e last_year = {} non ammissibili'.format(first_year, last_year))
    
    #Converto gli anni in valori numerici e se first year e maggiore alzo un eccezione
    fy_magg = False
    try:
        if int(first_year) > int(last_year):
           fy_magg = True
    except:
        raise ExamException('Valori first_year = {} e last_year = {} non convertibili in numeri'.format(first_year, last_year))
    
    #Controllo del flag fy_magg
    if fy_magg:
        raise ExamException('L\'anno di partenza dell\'intervallo è maggiore di quello finale')

    #Creo un dizionario della lista
    dct = {line[0]: line[1] for line in time_series}

    #Controllo se la lunghezza del dizionario coincide con quella della lista
    if len(dct) != len(time_series):
        raise ExamException('La lista contiene dupplicati - !Timestamp!')
    
    #Ordino la time_series per confrontare l'ordine
    ordered_time_series = sorted(time_series, key=itemgetter(0))
    for el1,el2 in zip(time_series, ordered_time_series):
        if el1[0] != el2[0]:
            raise ExamException('Time_series non è ordinata')
    
    #Creo una lista degli anni presenti nella time_series
    years_lst = []
    [years_lst.append(line[0].split('-')[0]) for line in time_series if line[0].split('-')[0] not in years_lst]
    
    #Controllo se gli anni sono presenti
    if first_year not in years_lst or last_year not in years_lst:
        raise ExamException('Valore first_year = {} o last_year = {} non esistente'.format(first_year, last_year))
    
    #Converto gli anni da stringhe in valori numerici
    num_fy = int(first_year)
    num_ly = int(last_year)
    
    #Lista che contiene la differenza tra i mesi 
    diff_lst = []
        
    for i in range(1,12):
        str_ym_1 = None
        str_ym_2 = None
        sum_diff = 0
        cont = 0
        for year in range(num_fy, num_ly):
            if i in range(10):
                str_ym_1 = str(year)+'-0'+str(i)
                str_ym_2 = str((year+1))+'-0'+str(i)
            else:
                str_ym_1 = str(year)+'-'+str(i)
                str_ym_2 = str((year+1))+'-'+str(i)
            if str_ym_1 in dct and str_ym_2 in dct:
                sum_diff += (dct.get(str_ym_2) - dct.get(str_ym_1))
                cont+=1
        if cont != 0:
            diff_lst.append([sum_diff, cont])
        else:
            diff_lst.append([None, None])

    months_avg = []
    for line in diff_lst:
        if line is None:
            months_avg.append(line[0])
        else:
            months_avg.append(line[0]/line[1])
    return months_avg
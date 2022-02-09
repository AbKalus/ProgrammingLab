#Dichiarazione classe ExamException per alzare le eccezioni
class ExamException(Exception):
    pass

class Diff:

    def __init__(self, ratio=1):
        self.ratio = ratio
        if not(isinstance(self.ratio, (int, float))):
            raise ExamException('Errore, ratio non è un numero')
        if self.ratio == 0:
            raise ExamException('Errore, ratio è 0')

    #controllo se la lista è interamente numerica
    def check_list(self, l):
        for item in l:
            if not(isinstance(item, (float,int))):
                raise ExamException('Errore, il valore non è numerico')
        
    def compute(self, l):
        if not(isinstance(l, list)):
            raise ExamException('Errore, non è stata passata una lista')
        l_len = len(l)
        if l_len <= 1:
            raise ExamException('Errore, lista valori vuota o non sufficiente')
        self.check_list(l)
        l_res = []
        for i in range(l_len-1):
            if self.ratio == 1:
                l_res.append(l[i+1]-l[i])
            else:
                l_res.append((l[i+1]-l[i])/self.ratio)
        return l_res
class Model():
    def fit(self, data):
        #fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    
    def predict(self, data):
        #predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
        prediction = None
        if data is None and :
            raise Exception('Lista vuota')
        if len(data)<=1:
            raise Exception('Impossibile fare la predizione con un elemento')
        len_data = len(data)
        prediction = data[len_data-1]
        increment = 0
        for i in range(1, len_data):
            increment+=abs(data[i-1]-data[i])       
        prediction = prediction + increment/(len_data-1)
        return prediction

list_x
x = IncrementModel()
print('Predizione: {}'. format(x.predict(list_x)))
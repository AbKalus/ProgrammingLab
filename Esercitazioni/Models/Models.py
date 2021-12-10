class Model():
    def fit(self, data):
        #fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    
    def predict(self, data):
        #predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def calc_increment(self, data):
        if data is None:
            raise Exception('Lista vuota')
        if len(data)<=1:
            raise Exception('Impossibile fare la predizione con un elemento')
        len_data = len(data)
        increment = 0
        for i in range(1, len_data):
            increment+=data[i]-data[i-1]
        increment = increment/(len_data-1)
        return increment

class IncrementModel(Model):

    def predict(self, data):
        prediction = None
        increment = super().calc_increment(data)
        prediction = data[-1] + increment
        return prediction

class FitIncrementModel(IncrementModel):
    
    def __init__(self):
        self.global_avg_increment = 0

    def fit(self, dataset):
        self.global_avg_increment = super().calc_increment(dataset)  

    def predict(self, data):
        data_increment = super().calc_increment(data)
        prediction = data[-1] + (self.global_avg_increment + data_increment)/2
        return prediction

list_y = [8, 19, 31, 41]
list_x = [50, 52, 60]
x = FitIncrementModel()
x.fit(list_y)
print('Predizione: {}'. format(x.predict(list_x)))

data = [8,19,31,41,50,52,60]
prediction = 68
from matplotlib import pyplot
pyplot.plot(data + [prediction], color='tab:red')
pyplot.plot(data, color='tab:blue')
pyplot.show()

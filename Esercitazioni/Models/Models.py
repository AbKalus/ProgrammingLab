from matplotlib import pyplot
from Class_CSVFile import CSVFile
from Class_CSVFile import NumericalCSVFile

class Model():
    def fit(self, data):
        #fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    
    def predict(self, data):
        #predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    #Metodo che calcola il l'incremento medio di un dataset
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

    #Implmentazione metodo per una predizione
    def predict(self, data):
        prediction = None
        increment = super().calc_increment(data)
        prediction = data[-1] + increment
        return prediction

class FitIncrementModel(IncrementModel):

    def __init__(self, dataset):
        self.global_avg_increment = 0
        self.dataset = dataset
        self.dset_len = len(dataset)

    #Metodo per restituire il dataset per il fitting
    def dataset_to_fit(self):
        return self.dataset[0: self.dset_len-3]

    #Metodo per restituire il dataset per la predizione
    def dataset_to_predict(self):
        return self.dataset[self.dset_len-3: self.dset_len]

    #Metodo per aggiungere elemento al dataset
    def update_dataset(self, new_el):
        self.dataset.append(new_el)
        self.dset_len = len(self.dataset)
    
    #Metodo per il fitting del dataset originale
    def fit(self):
        self.global_avg_increment = super().calc_increment(self.dataset_to_fit())

    #Metodo per una predizione più accurata
    def predict(self):
        data = self.dataset_to_predict()
        data_increment = super().calc_increment(data)
        prediction = data[-1] + (self.global_avg_increment + data_increment)/2
        return prediction


shampoo_file = NumericalCSVFile('shampoo_sales.csv')
shampoo_dataset = shampoo_file.get_data()
official_dataset = shampoo_file.get_only_column_n(1)
tmp_dataset = official_dataset.copy()
shampoo_model = FitIncrementModel(tmp_dataset)
tmp = []
for i in range(20):
    shampoo_model.fit()
    prediction = shampoo_model.predict()
    shampoo_model.update_dataset(prediction)
    tmp.append(prediction)
    
pyplot.plot(official_dataset + tmp, color='tab:red')
pyplot.plot(official_dataset, color='tab:blue')
pyplot.show()

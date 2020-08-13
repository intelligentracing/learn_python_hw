import os

class Finance:

    

    def __init__(self,filename):
        self.filename = filename
        self.price_history = {}
        path = os.path.dirname(os.path.abspath(__file__))
        sourse_file = open(path + '/' + self.filename, 'r')
        for line in sourse_file.readlines()[1:]:
            line_list = line.split(',')
            self.price_history[line_list[0]] = line_list[1:]


    def price_average(self):
        average_dictionary = dict()
        for data in self.price_history:
            average_value = (float(self.price_history[data][1]) + float(self.price_history[data][2]) )/ 2
            average_dictionary[data] = average_value

        return average_dictionary

    def price_search(self, low, high):
        result_list = []
        for data in self.price_history:
            real_high = float(self.price_history[data][2])
            real_low = float(self.price_history[data][3])
            if real_high < high and real_low > low:
                result_list.append(data)

        return result_list
#######################Finance class test #######################################
aapl = Finance('AAPL.csv')
print(aapl)
#print(aapl.price_average())
print(aapl.price_search(103, 199))
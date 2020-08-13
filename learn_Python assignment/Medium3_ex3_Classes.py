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
        for date in self.price_history:
            average_value = (float(self.price_history[date][1]) + float(self.price_history[date][2]) )/ 2
            average_dictionary[date] = average_value

        return average_dictionary

    def price_search(self, low, high):
        result_list = []
        for date in self.price_history:
            real_high = float(self.price_history[date][2])
            real_low = float(self.price_history[date][3])
            if real_high < high and real_low > low:
                result_list.append(date)

        return result_list
#######################Finance class test #######################################
aapl = Finance('AAPL.csv')
print(aapl.price_history)
#print(aapl.price_average())
print(aapl.price_search(103, 199))
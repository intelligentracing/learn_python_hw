import os

class Finance:

    def __init__(self,filename):
        self.filename = filename
        self.price_history = {}
        path = os.path.dirname(os.path.abspath(__file__))
        sourse_file = open(path + '/' + self.filename, 'r')
        for line in sourse_file.readlines()[1:]:
            line_list = line.split(',')
            # line_list = [2019-08-07,195.410004,199.559998,193.820007,199.039993,196.692566,33364400]
            line_list[-1] = line_list[-1].replace("\n", '')
            self.price_history[line_list[0]] = tuple(line_list[1:])
            #self.price_history[key] = tuple(value)


    def price_average(self):
        average_dictionary = dict()  # {}
        for date in self.price_history:
            #                   Date          Open         High       Low        Close     Adj       Close   Volume
            # prcie_history = {'2019-08-07': 195.410004,199.559998,193.820007,199.039993,196.692566,33364400}
            average_value = (float(self.price_history[date][1]) + float(self.price_history[date][2]) )/ 2
            average_dictionary[date] = average_value
            #average_dictionary['2019-08-07'] = （199.559998 = 193.820007）/2
        return average_dictionary

    def price_search(self, low = 100, high = 300):

        result_list = []
        for date in self.price_history:
            #real_high -> High = 199.559998
            real_high = float(self.price_history[date][1])
            # real_low = 193.820007
            real_low = float(self.price_history[date][2])
            #199.559998 < 300 and 193.820007 > 100 --> the result is true
            if real_high < high and real_low > low:
                #date = '2019-08-07'
                result_list.append(date)

        return result_list
#######################Finance class test #######################################
aapl = Finance('AAPL.csv')
#print(aapl.price_history)
#print(aapl.price_average())
print(aapl.price_search(50, 299))
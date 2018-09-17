#Simple Script to calculate the gas savings of a Tesla using average gas prices
#in big cities around the country

from energyData import energyData
from vehicleData import vehicleData

out_file = open('user_report.txt', 'w')


print("Make: ", self.make[index], "\nModel: ", self.model[index], "\nYear: ",
      self.year[index], "\nCity MPG: ", self.city_mpg[index], "\nHighway MPG: ",
      self.hiway_mpg[index])


#bo = energyData()
me = vehicleData()
man = me.get_brand()
mod = me.get_model(man)
year = me.get_year(mod)
me.print_vehicle_data()

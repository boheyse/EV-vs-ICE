#Simple Script to calculate the gas savings of a Tesla using average gas prices
#in big cities around the country

from energyData import energyData
from vehicleData import vehicleData

out_file = open('user_report.txt', 'w')


bo = energyData()
bo.get_data()

me = vehicleData()
man = me.get_brand()
mod = me.get_model(man)
year = me.get_year(mod)
#me.print_vehicle_data()

output = ("************************* Your Vehicle vs Electric Vehicles ****************************\n\n" +
          "Vehicle Data                                                Energy Data \n\n" +
          "Manufacturer: " + man + "                                     State: " + bo.user_state + " \n" +
          "Model: " + mod + "                                             Average Electric Rate: " + bo.state_elec_rate + "\n" +
          "Year: " + year + "                                           Miles Driven Per Month: " + bo.miles_Driven + "\n")

#out_file.write("************************* Your Vehicle vs Electric Vehicles ****************************\n\n")


out_file.write(output)

# print("Avg", bo.gas_avg)
# print("Low", bo.gas_low)
# print(bo.user_state)
#print(bo.state_elec_rate)

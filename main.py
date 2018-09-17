#Simple Script to calculate the gas savings of a Tesla using average gas prices
#in big cities around the country

from energyData import energyData
from vehicleData import vehicleData

# def white_space(input):
#     length = len(input)
#     space = ""
#     while(length != 55):
#         space = space + " "
#         length +=1
#     return space

def white_space(input):
    length = len(input)
    space = ""
    while(length != 55):
        space = space + " "
        length +=1
    return space

out_file = open('user_report.txt', 'w')


bo = energyData()
bo.get_data()

me = vehicleData()
man = me.get_brand()
mod = me.get_model(man)
y = me.get_year(mod)

elec_rate = float(bo.state_elec_rate)/100
avg_mpg = (me.city_mpg[y] * 0.4) + (me.hiway_mpg[y] * 0.6)
gallons = round(int(bo.miles_Driven)/avg_mpg, 1)
avg_gas_cost = round(gallons * float(bo.gas_avg), 2)
low_gas_cost = round(gallons * float(bo.gas_low), 2)

manufacturer = ("Manufacturer: " + man)
model = ("Model: " + mod)
year = ("Year: " + str(me.year[y]))
city_mpg = ("City MPG: " + str(me.city_mpg[y]))
h_mpg = ("Highway MPG: " + str(me.hiway_mpg[y]))
average_mpg = ("Average MPG: " + str(avg_mpg))

output = ("************************* Your Vehicle vs Electric Vehicles ****************************\n\n" +
          "     Vehicle Data                                                  Energy Data \n\n" +
          manufacturer + white_space(manufacturer) + "State: " + bo.user_state + "\n" +
          model + white_space(model) + "Average Electric Rate: $ " + str(elec_rate) + "/kWh\n" +
          year + white_space(year) + "Average Gas Cost Per Gallon: " + bo.gas_avg + "\n" +
          city_mpg + white_space(city_mpg) + "Lowest Gas Cost Per Gallon: " + bo.gas_low + "\n" +
          h_mpg + white_space(h_mpg) + "Miles Driven Per Month: " + bo.miles_Driven + "\n" +
          average_mpg + white_space(average_mpg) +"Gallons Per Month: " + str(gallons) + "\n" +
          "                                                       Average Gas Cost Per Month: $ " + str(avg_gas_cost) + "\n" +
          "                                                       Lowest Gas Cost Per Month: $ " + str(low_gas_cost) + "\n")


out_file.write(output)



out_file.close()
# print("Avg", bo.gas_avg)
# print("Low", bo.gas_low)
# print(bo.user_state)
#print(bo.state_elec_rate)

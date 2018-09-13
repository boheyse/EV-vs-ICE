#Simple Script to calculate the gas savings of a Tesla using average gas prices
#in big cities around the country
#energyData
import bs4 as bs
import requests
import pandas as pd
import numpy as np
import timeit

class energyData(object):

    data = pd.read_csv('electric_rates.csv')
    states = data.iloc[3:53, 0:2].values
    elec_data = dict((x[0], (x[1])) for x in states[1:])


    def __init__(self):
        return

    #get the users zip_code to search for on gasbuddy.com and on average miles driven per month
    def get_User_data(self):
        zip_code = input("Enter Zip Code: ")
        miles_Driven = input("Miles driven per month: ")
        gas_fill_ups = input("Number of times you fill up your vehicle: ")


#allows access to the url
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

gas_url= "https://www.gasbuddy.com/home?search=" + zip_code + "&fuel=1"
#grabs all html code from url
html_code = requests.get(gas_url, headers=headers)

#stores the code in a beautifulSoup object to allow for parsing
price_soup = bs.BeautifulSoup(html_code.text, 'html.parser')

#looks for specific html code to find average prices, varies depending on code you want to parse
gas_results = price_soup.find_all('', attrs={'class':'style__header3___3T2tm style__header___onURp style__snug___2HJ4K styles__priceHeader___38ONR'})
state_results = price_soup.find_all('', attrs={'class':'styles__resultsHeader___1TEzC'})

state = str(state_results[0].contents)
#state = str(state.contents)
state = state[2:]
STATE = []

if ', ' in state:
    start_index = state.index(",")
    end_index = state.index("'")
    for x in range(start_index+2, end_index):
        STATE.append(state[x])

if 'n ' in state:
    start_index = state.index("n")
    end_index = state.index("'")
    for x in range(start_index+2, end_index):
        STATE.append(state[x])

usable_state = "".join(STATE)
print(usable_state)


#store the html code we want into a string variable so we can grab the average price
lowest_price = gas_results[0]
average_price = gas_results[1]
usable_avg = str(average_price.contents)
usable_avg = usable_avg[3:7]
usable_low = str(lowest_price.contents)
usable_low = usable_low[3:7]

print("Avg", usable_avg)
print("Low", usable_low)

#takes the state we are in as output, compares with dictionary of electric rates to find states rate
def get_electric_rates(state, elec_data):
    for x in range(len(elec_data)):
        if state in elec_data:
            print(elec_data[state])
            break

get_electric_rates(usable_state, elec_data)

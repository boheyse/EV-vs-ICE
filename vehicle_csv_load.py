import pandas as pd
import numpy as np
import timeit
import types

start = timeit.default_timer()

data = pd.read_csv('vehicles.csv')
city_mpg = data.iloc[0:40056, 0].values
hiway_mpg = data.iloc[0:40056, 4].values
make = data.iloc[0:40056, 5].values
model = data.iloc[0:40056, 6].values
year = data.iloc[0:40056, 7].values

class vehicle_data(self):

    def get_brand():
        manufacturer = []
        #creates a list of all auto manufacturers from 1985-2019
        for brand in make:
            if brand not in manufacturer:
                manufacturer.append(brand)

        manufacturer = sorted(manufacturer)

        for y in manufacturer:
            print(y)
        print("\nChoose One Of The Above Manufacturers: ")
        man = input()
        return man

    def get_model(man):
        models = []
        brand_indices = []

        #makes a list of indices that indicates where the users choice is located
        #this can be used to create a list of the models
        b_count = 0
        for brand in make:
            if brand == man:
                brand_indices.append(b_count)
            b_count += 1

        #makes a list of all the different models for the users selection
        for x in brand_indices:
            if model[x] not in models:
                 models.append(model[x])

        models = sorted(models)
        for y in models:
            print(y)
        print("\nChoose One Of The Above Models: ")
        mod = input()
        return mod

    def get_year(mod):
        year_produced = []
        model_indices = []

        #makes a list of the indices for a specific model
        m_count = 0
        for i in model:
            if i == mod:
                model_indices.append(m_count)
            m_count += 1

        #makes a list of all years that specific model is available
        for y in model_indices:
            if year[y] not in year_produced:
                year_produced.append(year[y])

        year_produced = sorted(year_produced)

        for y in year_produced:
            print(y)

        print("What year is your car: ")

        user_year = str(input())

        for y in model_indices:
            if str(year[y]) == user_year:
                return y
                break

stop = timeit.default_timer()

bo = vehicle_data()

man = bo.get_brand()
mod = bo.get_model(man)
index = bo.get_year(mod)

print("Make: ", make[index], "\nModel: ", model[index], "\nYear: ", year[index],
      "\nCity MPG: ", city_mpg[index], "\nHighway MPG: ", hiway_mpg[index])

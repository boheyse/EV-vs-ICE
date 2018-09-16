import pandas as pd
import numpy as np
import types


class vehicleData(object):

    data = pd.read_csv('vehicles.csv')
    city_mpg = data.iloc[0:40056, 0].values
    hiway_mpg = data.iloc[0:40056, 4].values
    make = data.iloc[0:40056, 5].values
    model = data.iloc[0:40056, 6].values
    year = data.iloc[0:40056, 7].values

    def __init__(self):
        return

    def get_brand(self):
        manufacturer = []
        #creates a list of all auto manufacturers from 1985-2019
        for brand in self.make:
            if brand not in manufacturer:
                manufacturer.append(brand)

        #capitalize all choices
        for i in range(len(manufacturer)):
            manufacturer[i] = manufacturer[i].lower()
            manufacturer[i] = manufacturer[i].capitalize()

        manufacturer = sorted(manufacturer)

        for y in manufacturer:
            print(y)

        print("\nChoose One Of The Above Manufacturers: ")
        man = input()
        return man

    def get_model(self, man):
        models = []
        brand_indices = []

        #makes a list of indices that indicates where the users choice is located
        #this can be used to create a list of the models
        b_count = 0
        for brand in self.make:
            if brand == man:
                brand_indices.append(b_count)
            b_count += 1

        #makes a list of all the different models for the users selection
        for x in brand_indices:
            if self.model[x] not in models:
                 models.append(self.model[x])

        for i in range(len(models)):
            models[i] = models[i].lower()
            models[i] = models[i].capitalize()

        models = sorted(models)
        for y in models:
            print(y)
        print("\nChoose One Of The Above Models: ")
        mod = input()
        return mod

    def get_year(self, mod):
        year_produced = []
        model_indices = []

        #makes a list of the indices for a specific model
        m_count = 0
        for i in self.model:
            if i == mod:
                model_indices.append(m_count)
            m_count += 1

        #makes a list of all years that specific model is available
        for y in model_indices:
            if self.year[y] not in year_produced:
                year_produced.append(self.year[y])

        year_produced = sorted(year_produced)

        for y in year_produced:
            print(y)

        print("What year is your car: ")

        user_year = str(input())

        for y in model_indices:
            if str(self.year[y]) == user_year:
                return y
                break

    def print_vehicle_data(self):
        print("Make: ", self.make[index], "\nModel: ", self.model[index], "\nYear: ",
              self.year[index], "\nCity MPG: ", self.city_mpg[index], "\nHighway MPG: ",
              self.hiway_mpg[index])

bo = vehicle_data()

man = bo.get_brand()
mod = bo.get_model(man)
index = bo.get_year(mod)
bo.print_vehicle_data()

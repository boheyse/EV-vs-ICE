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
    model_indices = []
    user_mod = ""
    user_year = ""

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
        man = 'Acura'#input()
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
        self.user_mod = 'TSX'#input()
        return self.user_mod

    def get_year(self, user_mod):
        year_produced = []

        #makes a list of the indices for a specific model
        m_count = 0

        for i in self.model:
            if i.upper() == user_mod.upper():
                self.model_indices.append(m_count)
            m_count += 1

        #makes a list of all years that specific model is available
        for y in self.model_indices:
            if self.year[y] not in year_produced:
                year_produced.append(self.year[y])

        year_produced = sorted(year_produced)

        for y in year_produced:
            print(y)

        print("What year is your car: ")

        self.user_year = '2004'#str(input())

        for y in self.model_indices:
            if str(self.year[y]) == self.user_year:
                return y
                break

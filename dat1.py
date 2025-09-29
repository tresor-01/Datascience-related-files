# import pandas as pd
# url = './car_specs_combined.csv'
# data = pd.read_csv(url, header=None)
# data.head(5)

# path = './data.csv'

# from dmodule import connect 

from sqlalchemy import create_engine


conne = create_engine('sqllite://cars.db')
connnection = conne.connect()

# connection = connect('cars', 'root','ibyishakamysql@2025')
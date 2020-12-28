import pandas as pd
import matplotlib.pyplot as plt
from utils import weekday_date

inventory_avaibility = pd.read_csv('tvaberta_inventory_availability.csv', sep=';')
program_audience = pd.read_csv('tvaberta_program_audience.csv')


df = pd.DataFrame({
    'signal': pd.Series(inventory_avaibility['signal']),
    'program_code': pd.Series(inventory_avaibility['program_code']),
    'weekday': pd.Series(inventory_avaibility['date']),
    'available_time': pd.Series(inventory_avaibility['available_time']),
    'predicted_audience': '',
})

for index, row in inventory_avaibility.iterrows():
    program_code = program_audience[program_audience.program_code == row['program_code']]
    program_signal = program_code[program_code.signal == row['signal']]
    order_date = program_signal.sort_values('exhibition_date')
    media = []
    for index_x, row_x in order_date.iterrows():
        if weekday_date(False, row['date'].replace('/', '')) == weekday_date(True, row_x['exhibition_date'].replace('-','')):
            media.append(row_x['average_audience'])
    df.loc[index, 'predicted_audience'] = sum(media[-4:])/4


# def exact_program()

# mask = (df['weekday'] >= '25/08/2020') & (df['weekday'] <= '30/08/2020')
print(df[(df['weekday'] >= '25/08/2020') & (df['weekday'] <= '30/08/2020')])

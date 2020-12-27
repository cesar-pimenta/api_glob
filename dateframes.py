import pandas as pd
import matplotlib.pyplot as plt
from utils import weekday_date

inventory_avaibility = pd.read_csv('tvaberta_inventory_availability.csv', sep=';')
program_audience = pd.read_csv('tvaberta_program_audience.csv')

# print(inventory_avaibility['signal'])
# print(inventory_avaibility['program_code'])


# for x in program_audience:
#     print(x)
#     # if x['program_code'] == 'SHOV':
#     #     print(x['program_code'])
#

# print(inventory_avaibility.head(5))

# program_code = str(input('> programa code : '))
# data_program = str(input('> data do programa : '))

# program_code = program_audience[program_audience.program_code == 'VALE']
# program_signal = program_code[program_code.signal == 'SP1']
# order_date = program_signal.sort_values('exhibition_date')
# last_programs = order_date[-4::]
# clear_data = last_programs['exhibition_date'].values[0].replace('-', '')
# # print(datetime.datetime(last_programs['exhibition_date'].values[0]))
# print(weekday_date(clear_data))

# print((last_programs['average_audience'].sum() / 4))

# x = inventory_avaibility[inventory_avaibility.program_code == 'VALE']
# print(x)
new_df = pd.DataFrame({'signal': [inventory_avaibility['signal']], 'media': [], 'over': []}, ignore_index=True)
for index, row in inventory_avaibility.iterrows():
    program_code = program_audience[program_audience.program_code == row['program_code']]
    program_signal = program_code[program_code.signal == row['signal']]
    order_date = program_signal.sort_values('exhibition_date')
    media = []
    for index_x, row_x in order_date.iterrows():
        if weekday_date(False, row['date'].replace('/', '')) == weekday_date(True, row_x['exhibition_date'].replace('-','')):
            media.append(row_x['average_audience'])
    new_df.append({'media': sum(media[-4:])/4}, ignore_index=True)
print(new_df)


# print(program_audience[::1000])
#
# for x in program_audience.iterrows():
#     print(program_audience[(1+x[0])])

# print(y[y.exhibition_date == data_programa])
# # print(y[(y.signal == 'SP1') & (y.exhibition_date == '2020-06-06')])

# print(program_audience.head(5))

# Função 'loc' do pandas, localização - [(periodo que nem slice), [(colunas de escolha do data frame)]]
# print(inventory_avaibility.loc[:, ['signal', 'program_code']])

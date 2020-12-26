import pandas as pd
import matplotlib.pyplot as plt

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

program_code = str(input('> programa code : '))
data_programa = str(input('> data do programa : '))
# print(program_audience[::1000])
#
# for x in program_audience.iterrows():
#     print(program_audience[(1+x[0])])

y = program_audience[program_audience.program_code == program_code]

print(y[y.exhibition_date == data_programa])

# print(y[(y.signal == 'SP1') & (y.exhibition_date == '2020-06-06')])

x = inventory_avaibility[inventory_avaibility.program_code == program_code]
print(x)


# print(program_audience.head(5))


# Função 'loc' do pandas, localização - [(periodo que nem slice), [(colunas de escolha do data frame)]]

# print(inventory_avaibility.loc[:, ['signal', 'program_code']])

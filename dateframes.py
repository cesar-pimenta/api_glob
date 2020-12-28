import pandas as pd
from utils import weekday_date

inventory_avaibility = pd.read_csv('dataframes/tvaberta_inventory_availability.csv', sep=';')
program_audience = pd.read_csv('dataframes/tvaberta_program_audience.csv')

df = pd.DataFrame({
    'signal': pd.Series(inventory_avaibility['signal']),
    'program_code': pd.Series(inventory_avaibility['program_code']),
    'weekday': pd.Series(inventory_avaibility['date']),
    'available_time': pd.Series(inventory_avaibility['available_time']),
    'predicted_audience': '',
})


def upload_dataframes():
    for index, row in inventory_avaibility.iterrows():
        program_code = program_audience[program_audience.program_code == row['program_code']]
        program_signal = program_code[program_code.signal == row['signal']]
        order_date = program_signal.sort_values('exhibition_date')
        media = []
        for index_x, row_x in order_date.iterrows():
            if weekday_date(False, row['date'].replace('/', '')) == weekday_date(True,
                                                                                 row_x['exhibition_date'].replace('-',
                                                                                                                  '')):
                media.append(row_x['average_audience'])
        df.loc[index, 'predicted_audience'] = sum(media[-4:]) / 4
    return 'DataFrames OK!'


def forecast_audience_by_code_program(code_program, date):
    """
        Function that searches audience prediction by exact date and program code
    """
    result = df[(df['program_code'] == code_program) & (df['weekday'] == date)]
    return result


def forecast_audience_by_date(start_date, end_date):
    """
        Function that searches for audience forecast by date range
    """
    result = df[(df['weekday'] >= start_date) & (df['weekday'] <= end_date)]
    return result


def forecast_all():
    """

    """
    result = df
    return result

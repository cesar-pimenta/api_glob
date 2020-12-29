from flask import Flask
from flask_jsonpify import jsonpify
from dateframes import upload_dataframes, forecast_audience_by_date, forecast_audience_by_code_program, forecast_all

forecast = Flask('forecast')

upload_dataframes()

@forecast.route('/')
def home():
    return 'Hello - Api_glob - user <br>' \
           '<strong> Return all datas </strong> - /forecast/ <br>' \
           '<strong> code program and data exact </strong> - /forecast/code=<string:code>&date=<string:date> -' \
           '<strong> ex - </strong>/forecast/code=huck&date=08-08-2020 <br> ' \
           '<strong> date range </strong> - /forecast/start_date=<string:start_date>&end_date=<string:end_date>' \
           '<strong> ex - </strong>/forecast/start_date=25-04-2020&end_date=25-08-2020 <br> '

@forecast.route('/forecast/')
def forecasts():
    dataframe_temp = forecast_all()
    dataframe_list = dataframe_temp.values.tolist()
    result = jsonpify(dataframe_list)
    return result


@forecast.route('/forecast/code=<string:code>&date=<string:date>')
def forecast_code_program(code, date):
    code_program = code.upper()
    date_program = date.replace('-', '/')
    dataframe_temp = forecast_audience_by_code_program(code_program, date_program)
    dataframe_list = dataframe_temp.values.tolist()
    result = jsonpify(dataframe_list)
    return result


@forecast.route('/forecast/start_date=<string:start_date>&end_date=<string:end_date>')
def forecast_date_rage(start_date, end_date):
    start_date = start_date.replace('-', '/')
    end_date = end_date.replace('-', '/')
    dataframe_temp = forecast_audience_by_date(start_date, end_date)
    dataframe_list = dataframe_temp.values.tolist()
    result = jsonpify(dataframe_list)
    return result


if __name__ == '__main__':
    forecast.run()


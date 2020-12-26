import datetime


def weekday_date(date):
    data = datetime.datetime(year=int(date[4:8]), month=int(date[2:4]), day=int(date[0:2]))
    return data.isoweekday()
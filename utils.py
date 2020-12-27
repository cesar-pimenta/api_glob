import datetime


def weekday_date(reverse, date):
    if reverse:
        data = datetime.datetime(year=int(date[0:4]), month=int(date[4:6]), day=int(date[6:8]))
    else:
        data = datetime.datetime(year=int(date[4:8]), month=int(date[2:4]), day=int(date[0:2]))
    return data.isoweekday()
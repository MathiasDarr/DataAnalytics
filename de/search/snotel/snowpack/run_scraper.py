from datetime import  timedelta
from pipelines.snotel.snowpack.populate_tables import generate_url, insert_snowpack_data, extract_snowpack_data


def date_list(startdate, enddate):
    '''
    Returns a list of urls that will be scraped
    :param startdate:
    :param enddate:
    :return:
    '''
    delta = enddate - startdate  # as timedelta
    days = []
    for i in range(delta.days + 1):
        day = startdate + timedelta(days=i)
        days.append((day.year, day.month, day.day))
    return days


def scrape_snowpack_data(startdate, enddate ):
    dates = date_list(startdate, enddate)
    for date in dates:
        url = generate_url(date[0], date[1],date[2])
        insert_snowpack_data(extract_snowpack_data(url))
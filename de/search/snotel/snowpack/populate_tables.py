from pipelines.snotel.snowpack.sql_queries import snowpack_table_insert
from snotel.postgresConnection import get_postgres_connection
import os
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta
import requests

rds_password = os.environ.get('KALADIN_RDS_PASSWORD')


def backfill_data_urls(startdate, enddate):
    '''
    Returns a list of urls that will be scraped
    :param startdate:
    :param enddate:
    :return:
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    delta = enddate - startdate  # as timedelta
    urls = []
    for i in range(delta.days + 1):
        day = startdate + timedelta(days=i)
        urls.append(generate_url(months[day.month - 1], day.day, day.year))
    return urls


def generate_url(year, month, day):
    '''
    Generate a URL that points to the snowpack data to be scraped on the input month, day and year
    :param month:
    :param day:
    :param year:
    :return: url string
    '''
    return 'https://wcc.sc.egov.usda.gov/reports/UpdateReport.html?textReport=Washington&textRptKey=12&textFormat=SNOTEL+Snow%2FPrecipitation+Update+Report&StateList=12&RegionList=Select+a+Region+or+Basin&SpecialList=Select+a+Special+Report&MonthList={}&DayList={}&YearList={}&FormatList=N0&OutputFormatList=HTML&textMonth=March&textDay=11&CompYearList=select+a+year'.format(
        month, day, year)


def insert_snowpack_data(basins_dict, extract_date=datetime.datetime.today().date()):
    conn = get_postgres_connection()
    cur = conn.cursor()

    year = basins_dict.pop('year')
    day = basins_dict.pop('day')
    month = basins_dict.pop('month')
    print("day " + str(day))
    # date_ = date(year, month, day)

    date_ = extract_date
    locationID = 1
    for region in basins_dict.keys():
        basins_dict[region].pop('Basin Index')
        locations = basins_dict[region].keys()

        for location in locations:
            location_dict = basins_dict[region][location]
            snow_current = validate_data(location_dict['Snow Current (in)'])
            snow_median = validate_data(location_dict['Snow Median (in)'])
            snow_pct_median = validate_data(location_dict['Snow Pct of Median'])
            water_current = validate_data(location_dict['Water Current '])
            water_current_average = validate_data(location_dict['Water Average (in)'])
            water_pct_average = validate_data(location_dict['Water Pct of Average'])
            try:
                cur.execute(snowpack_table_insert, (
                    locationID, date_, snow_current, snow_median, snow_pct_median, water_current, water_current_average,
                    water_pct_average,))
            except Exception as e:
                print(e)
            locationID += 1
        conn.commit()
    conn.close()


def extract_snowpack_data(url='https://wcc.sc.egov.usda.gov/reports/UpdateReport.html?report=Washington',
                          extract_date=datetime.datetime.today().date()):
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    snowpackTable = soup.find('table', {'id': 'update_report_data'})
    metrics = ['Elev (ft) ', 'Snow Current (in)', 'Snow Median (in)', 'Snow Pct of Median', 'Water Current ',
               'Water Average (in)', 'Water Pct of Average']

    region_dictionary = {}

    currentdate = datetime.datetime.now()
    todayyear = currentdate.year
    todaymonth = currentdate.month
    todayday = currentdate.day

    region_dictionary['year'] = todayyear
    region_dictionary['month'] = todaymonth
    region_dictionary['day'] = todayday

    for i, row in enumerate(snowpackTable.select('tr')):
        columns = row.find_all('td')
        if len(columns) == 1:
            # Okay this is or region...  i.e SPOKANE, LOWERCOLUMBIA etc... As this row will always precede the associated data rows and basin index rows, here we set the current_region variable which will be used by the subsequent conditional statements..
            col_text = columns[0].getText()
            region_name = ''.join(filter(str.isalpha, col_text))
            current_region = region_name
            region_dictionary[region_name] = {}

        if len(columns) == 3:
            # Here we have our basin index.. which has aggregate values such as percentage of median etc for the basin
            for j, column in enumerate(columns):
                column_text = column.getText()
                if j == 1:
                    try:
                        pct_med = int(''.join(filter(str.isdigit, column_text)))
                    except:
                        pct_med = 0
                    region_dictionary[current_region]['Basin Index'] = {}
                    region_dictionary[current_region]['Basin Index']['pctmedian'] = pct_med
                elif j == 2:
                    pct_avg = int(''.join(filter(str.isdigit, column_text)))
                    region_dictionary[current_region]['Basin Index']['pctavg'] = pct_avg

        if len(columns) == 8:
            ## This is the actual data...  We have 8 data columns as defined in the metrics variable.  For each region there are multiple locations at which

            for j, column in enumerate(columns):
                column_text = column.getText()
                if j == 0:
                    current_loc = column_text.split('\xa0\xa0')[1]
                    if "." in current_loc:
                        current_loc = current_loc.replace(".", "")
                    # This is to handle a corner case
                    region_dictionary[current_region][current_loc] = {}
                else:
                    try:
                        region_dictionary[current_region][current_loc][metrics[j - 1]] = int(
                            ''.join(filter(str.isdigit, column_text)))
                    except:
                        region_dictionary[current_region][current_loc][metrics[j - 1]] = ''
    return region_dictionary


def validate_data(data):
    if data == '':
        data = 0
    return data

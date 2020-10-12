from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
from pipelines.snotel.wta.sql_queries import trip_report_table_insert
from pipelines.search.snotel.postgresConnection import get_postgres_connection


def get_page_soup(page_url):
    client = uReq(page_url)
    page_html = client.read()
    client.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup


def parse_trip_report(trip_report_url):
    client = uReq(trip_report_url)
    trip_report_html = client.read()
    client.close()
    tripsoup = soup(trip_report_html, "html.parser")
    content = tripsoup.find("article", {"id": "content"})
    trip_text = content.find('p').text
    region = content.find_all('span')[1].text
    trip_title = content.find('h1').text
    date = content.find('span', {"class": "elapsed-time"})
    date_string = str(date).split('datetime=')[1].split('"')[1]

    docuemntHead = content.find("h1", {"class": "documentFirstHeading"})
    location = docuemntHead.text
    location_link = str(docuemntHead.find('a')).split('"')[1]
    trip_report = {'title': trip_title, 'region': region, 'trip_report': trip_text, 'date': date_string,
                   'location': location, 'location_link': location_link}
    return trip_report


def insert_trip_report(conn, trip_report):
    cur = conn.cursor()
    cur.execute(trip_report_table_insert, (
    trip_report['title'], trip_report['trip_report'], 2300, 45.3, ['location1', 'location2'], datetime.datetime.now()))
    conn.commit()


def scrape_range(start,end):
    conn = get_postgres_connection('snowpackDB', 'snowpack')

    for page_number in range(start,end):
        report_list_url = 'https://www.wta.org/@@search_tripreport_listing?b_size=100&amp;b_start:int=%d&amp;_=1584045459199"' % int(
            100 * page_number)
        try:
            report_list_soup = get_page_soup(report_list_url)
            reports = report_list_soup.find_all("a", {"class": "listitem-title"})
            for report in reports:
                report_url = str(report).split('href=')[1].split('"')[1]
                trip_report = parse_trip_report(report_url)
                insert_trip_report(conn, trip_report)
                print("Inserted ")
                conn.commit()
        except Exception as e:
            print("We have a problem with the url at")
            print(e)
    conn.close()

scrape_range(0,5)
from airflow import DAG
from datetime import datetime, timedelta
from psycopg2.extras import execute_values
from plugins.operators.scrape_usda_operator import ScrapeUSDAOperator

default_args = {
    'owner': 'mddarr',
    'start_date': datetime(2020, 3, 1),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': False
}

snowpack_dag = DAG('snowpack_dag',
          default_args=default_args,
          description='Load snowpack data in Redshift with Airflow',
          schedule_interval='* * * * *',
          catchup = False
         )

stage_events_to_redshift = ScrapeUSDAOperator(
    task_id='scrape_snowpack',
    dag=snowpack_dag,
)





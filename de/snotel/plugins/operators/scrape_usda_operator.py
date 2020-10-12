import logging
from airflow.models import BaseOperator
from snowpack.populate_tables import extract_snowpack_data, insert_snowpack_data

class ScrapeUSDAOperator(BaseOperator):
    def execute(self, context):
        insert_snowpack_data(extract_snowpack_data())
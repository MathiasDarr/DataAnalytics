from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from plugins.operators import MyFirstOperator, MyFirstSensor
from airflow.operators.bash_operator import BashOperator
dag = DAG('pip', description='Another tutorial DAG',
          schedule_interval='* * * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)
sensor_task = MyFirstSensor(task_id='my_sensor_task', poke_interval=30, dag=dag)
operator_task = MyFirstOperator(my_operator_param='This is a test.',
                                task_id='my_first_operator_task', dag=dag)

t1 >> sensor_task >> operator_task
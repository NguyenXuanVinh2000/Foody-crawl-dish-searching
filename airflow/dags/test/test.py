from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import sys
import os
from datetime import datetime, timedelta

os.system("cd /opt/airflow/dags/test")
sys.path.append('dags/test')


default_args = {
        'owner': 'FOODY_V1',
        'start_date': datetime(2022, 6, 1)
        }
dag = DAG('FOODY_V1', default_args=default_args, schedule_interval='@hour', catchup=False)
t1 = BashOperator(
    task_id='crawl_data',
    bash_command='cd /opt/airflow/dags/test && scrapy crawl foody',
    dag=dag)
    
t1

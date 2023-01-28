import os

from airflow import DAG

from datetime import datetime

from airflow.operators.python import PythonOperator

from scrape import capture_data

from main import batch_records

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")


scraper_workflow = DAG(
    "ScraperDag",
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 23)
)

with scraper_workflow:
    scraping_task = PythonOperator(
        task_id='Scrape',
        python_callable=capture_data,   
    ) 

    batch_task = PythonOperator(
        task_id='Batch',
        python_callable=batch_records,
        op_kwargs=dict(
            data='data.csv',
            sheet_name='test_sheet',
            worksheet='data4'
        )
    )


    scraper_workflow >> batch_task


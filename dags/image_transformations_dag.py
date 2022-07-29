from image_transformations.resizing import resize, normalize
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
        dag_id= 'image_transformations',
        default_args={
            'depends_on_past': False,
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        description='This dag contains all the transformation that we need in the preprocessing step',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2021, 1, 1),
        catchup=False
) as dag:
    t1 = PythonOperator(
        task_id='resizing',
        python_callable=resize,
    )
    t2 = PythonOperator(
        task_id='normalization',
        python_callable=normalize,
    )

    t1 >> t2

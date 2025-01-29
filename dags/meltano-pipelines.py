from airflow import DAG
from datetime import datetime, date
from airflow.operators.bash import BashOperator

today = date.today()

with DAG('meltano-pipelines', default_args={"owner": "Bruno Justen Santos"}, tags=["meltano"], start_date=datetime(2025, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    pipeline1 = BashOperator(
        task_id='pipeline1',
        env={'INIT_DAY': str(today)},
        bash_command='cd /opt/airflow/meltano; source /opt/airflow/.venvs/meltano/bin/activate && meltano run pipeline1'
    )
    pipeline2 = BashOperator(
        task_id='pipeline2',
        env={'INIT_DAY': str(today)},
        bash_command='cd /opt/airflow/meltano; source /opt/airflow/.venvs/meltano/bin/activate && meltano run pipeline2'
    )

    pipeline1 >> pipeline2
        
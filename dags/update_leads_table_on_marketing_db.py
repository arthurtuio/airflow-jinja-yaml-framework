"""
DAG gerada automaticamente
"""

from airflow import DAG
from datetime import timedelta, datetime


from lib.operators.postgres_operator import PostgresOperator
default_args = {
    "owner": 'MARKETING',
    "depends_on_past": False,
    "start_date": '2021-01-05',
    "email": 'marketing@dundermifflin.com',
    "email_on_failure": True,
    "email_on_retry": 3,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    dag_id='update_leads_table_on_marketing_db',
    catchup=False,
    default_args=default_args,
    max_active_runs=1,
    schedule_interval='@daily',
)

dag.doc_md = __doc__





update_leads_table_on_marketing_db_task = PostgresOperator(
    task_id="update_leads_table_on_marketing_db_task",
    postgres_conn_id="substitua_esse_valor_por_sua_conn",
    sql=" UPDATE mkt_schema.leads_table l SET l.id = c.lead_id FROM mkt_schema.company c WHERE l.updated_at >= current_date - '5 days'::INTERVAL AND c.email = l.lead_email AND l.lead_email IS NOT NULL; ",
    autocommit=True,
    depends_on_past=False,
    dag=dag,
)


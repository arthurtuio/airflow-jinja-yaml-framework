# YAMLs creation

## Campos obrigatorios
Para entender como preencher cada campo, confira a documentação do Airflow

### Campos presentes em todas as DAGs, com exemplos
- **dag_name**: 
- **owner**: MARKETING
- **email**: marketing@dundermiffling.com
- **start_date**: 2019-01-05
- **schedule**: "@daily"

### Campos presentes na task
Na hora de criação da Task, é preciso que sejam preenchidos os seguintes campos
obrigatórios:
- tasks:
    - **task_name**: "send_data_from_bq_to_hubspot"
    - **operator**: PostgresOperator 
    
Além destes, há campos que precisam ser preenchidos, a depender
do valor usado em **operator**

Para ver a lista completa de possibilidades, acesse a documentação: <<criar a doc>>

Como exemplo, temos:
- tasks:
    - **task_name**: "update_table"
    - **operator**: "PostgresOperator"
    - **sql**: 
        ```` 
        """
        UPDATE mkt_schema.leads_table l
        SET l.id = c.lead_id
        FROM mkt_schema.company c
        WHERE l.updated_at >= current_date - '5 days'::INTERVAL
          AND c.email = l.lead_email
          AND l.lead_email IS NOT NULL;
        """ 
        ````

### Campos opcionais
- **retries**: Default `3`, se quiser preencher fazer conforme o exemplo: `0`
- **retry_delay**: Default `timedelta(minutes=5)`, 
  se quiser preencher fazer conforme o exemplo: `timedelta(minutes=10)`
- **depends_on_past**: Default `False`, se quiser preencher fazer conforme o exemplo: True
- **email_on_failure**: Default `True`, se quiser preencher fazer conforme o exemplo: False
- **email_on_retry**: Default `False`, se quiser preencher fazer conforme o exemplo: True
- **catchup**: Default `False`, se quiser preencher fazer conforme o exemplo: True
- **max_active_runs**: Default `1`, se quiser preencher fazer conforme o exemplo: 2


## Como criar um arquivo .yaml
- Apenas salve o seu arquivo com a extensão `.yaml`

## Automatizando a criação de DAGs no Airflow usando Jinja e YAML

### Arquitetura do Repo:
- Pastas por contexto de negócio (ex: Marketing, Analytics, HR, etc), dentro da pasta `contexts/`;
  - Dentro de cada pasta, temos os YAMLs com as regras da criação da DAG, sendo 1 YAML = 1 DAG;
- Pasta de templates, uma vez que possuímos diversos operators, gerando a necessidade de diversos templates
- Pasta com os scripts para criação de DAGs

### Como o código funciona
- A pessoa adiciona/atualiza o arquivo YAML com todas as informações necessárias para criar a DAG (
  para isso veja o `CONTEXTS_README` presente na pasta `contexts/`
  )
- O arquivo Python é criado e enviado para a branch master, ou para o local de produção delas, por ex a pasta `dags/`
  - No caso deste repo, foi decidido que será enviado para a pasta `dags/`

### Sobre as pastas:
- `contexts/`: Pasta onde ficam armazenados os YAMLs por contexto da empresa.  
Dentro dessa pasta há um README explicando os padrões de criação dos YAMLs

- `templates/`: Pasta onde ficam os arquivos `.template`, que são as bases para o Jinja criar as DAGs.
  - temos o arquivo `dag.template`
  - temos os operators já adicionados via template
  - temos um README com os operators já adicionados

- `scripts/` : Scripts tanto para transformar YAML em DAG, quanto para validar se o YAML está correto
    - `yml_converter.py`: Responsável por criar DAGs a partir do YAML
    
- `dags/`: Pasta padrão do airflow, pode ficar nesse repositório ou em outro, ou até em outra branch. 

### Referencias:
  - https://medium.com/tech-grupozap/airflow-com-dags-em-yaml-dags-e-kubernetes-operator-d049865bb453
  - https://towardsdatascience.com/data-engineers-shouldnt-write-airflow-dags-part-2-8dee642493fb
  - https://stackoverflow.com/questions/66323798/reading-a-yaml-configuration-file-and-creating-a-dag-generator-in-airflow-2-0

### TBD
- Implementar testes na estrutura dos YAMLs. Uma sugestão é usar a lib `cerberus`
- Implementar CI para os testes. Uma sugestão é usar o proprio `github_actions`
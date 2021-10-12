import os
import yaml

from jinja2 import Environment, FileSystemLoader, environment

from helpers.enrich_dag import EnrichDag
from helpers.paths_configuration import PathsConfiguration


class ConvertYamlInDag:
    DAGS_DIR = PathsConfiguration.DAGS_DIR.value
    TEMPLATES_DIR = PathsConfiguration.TEMPLATES_DIR.value
    CONTEXTS_DIR = PathsConfiguration.CONTEXTS_DIR.value

    def __init__(self, yaml_file_name):
        self.yaml_file_name = yaml_file_name

    def execute(self):
        enriched_dag = EnrichDag(
            self._load_yaml()
        ).execute()

        self.renderize_template_into_dag(
            yml_dag=enriched_dag,
            filename=self._set_filename(self._load_yaml()),
            template=self._get_template()
        )

    def _load_yaml(self) -> dict:
        yaml_file = open(self.CONTEXTS_DIR + "/marketing/" + self.yaml_file_name + ".yaml")

        return yaml.load(yaml_file, Loader=yaml.FullLoader)

    def _set_filename(self, yml_dag: dict) -> str:
        dag_name = yml_dag["dag_name"]

        return os.path.join(
            self.DAGS_DIR,
            '{}.py'.format(dag_name)
        )

    def _get_template(self) -> environment.Template:
        env = Environment(loader=FileSystemLoader(self.TEMPLATES_DIR))

        template = env.get_template('dag.template')
        return template

    @staticmethod
    def renderize_template_into_dag(
        yml_dag: dict,
        filename: str,
        template: environment.Template
    ):
        with open(filename, 'w') as fh:
            fh.write(template.render(
                **yml_dag
            ))


if __name__ == '__main__':
    ConvertYamlInDag("update_leads_table_on_marketing_db").execute()

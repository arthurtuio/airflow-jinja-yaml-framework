from helpers.operator_mapping import operator_mapping


class EnrichDag:
    def __init__(self, yml_dag_as_dict: dict):
        self.yml_dag_as_dict = yml_dag_as_dict

    def execute(self) -> dict:
        return self._enrich_with_default_values(
            self._enrich_with_operator_values()
        )

    @staticmethod
    def _enrich_with_default_values(yml_dag_as_dict: dict) -> dict:
        """
        Neste método é que são adicionados os valores defaults
        para as chaves opcionais. Caso você queira
        adicionar mais chaves opcionais, lembre-se
        depois de adicioná-las também aqui :)

        Por exemplo, você pode adicionar chaves
        opcionais na criação dos Operators,
        e fazer a adicção do valor default das mesmas
        aqui, ou em outro método!
        """
        yml_dag_as_dict["retries"] = yml_dag_as_dict.get("retries", 3)
        yml_dag_as_dict["retry_delay"] = yml_dag_as_dict.get("retry_delay", "minutes=5")
        yml_dag_as_dict["depends_on_past"] = yml_dag_as_dict.get("depends_on_past", False)
        yml_dag_as_dict["email_on_failure"] = yml_dag_as_dict.get("email_on_failure", True)
        yml_dag_as_dict["email_on_retry"] = yml_dag_as_dict.get("retries", False)
        yml_dag_as_dict["catchup"] = yml_dag_as_dict.get("catchup", False)
        yml_dag_as_dict["max_active_runs"] = yml_dag_as_dict.get("max_active_runs", 1)

        return yml_dag_as_dict

    def _enrich_with_operator_values(self) -> dict:
        """
        Todo: Melhorar o tratamento de erro
        """
        if not self.yml_dag_as_dict["tasks"]["operator"]:
            raise Exception("Campo operator obrigatório no arquivo YAML!")

        if self.yml_dag_as_dict["tasks"]["operator"] in operator_mapping():
            self.yml_dag_as_dict["tasks"]["operator_class"] = operator_mapping()[self.yml_dag_as_dict["tasks"]["operator"]]

        else:
            raise Exception("Operator ainda não foi criado por DE")

        return self.yml_dag_as_dict

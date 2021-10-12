import os
from enum import Enum


_HOME_DIR = os.path.expanduser('~')
_REPO_DIR = _HOME_DIR + "/clone_airflowjinjayamlframework/airflow-jinja-yaml-framework"


class PathsConfiguration(Enum):
    DAGS_DIR = _REPO_DIR + "/dags"
    TEMPLATES_DIR = _REPO_DIR + "/templates"
    SCRIPTS_DIR = _REPO_DIR + "/scripts"
    CONTEXTS_DIR = _REPO_DIR + "/contexts"

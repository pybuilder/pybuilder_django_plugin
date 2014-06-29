from pybuilder.core import task


@task
def initialize_django_project(project, logger):
    logger.info("Initializing Django project")

#   pybuilder_django_plugin
#   Copyright 2014 PyBuilder team
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from pybuilder.core import description, task
from subprocess import call
from os.path import join


@task
def initialize_django_project(project, logger):
    logger.info("Initializing Django project")


@task
@description('Starts Django development server')
def django_run_server(project, logger):
    """ This task is here for backwards compatibility. """
    logger.info('Starting Django development server ...')
    django_module_name = project.get_property('pybuilder_django_plugin_project_name')
    path_to_manager = join(django_module_name, 'manage.py')
    call(['python', path_to_manager, 'runserver'])

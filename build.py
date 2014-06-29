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

import sys

sys.path.insert(0, 'src/main/python')

from pybuilder.core import Author, init, use_plugin
from pybuilder_django_plugin import initialize_django_project, django_run_server

use_plugin('python.core')
use_plugin('python.distutils')
use_plugin('python.flake8')
use_plugin('python.install_dependencies')
use_plugin('pypi:pybuilder_release_plugin')

description = 'This plugin makes it possible to use PyBuilder with your Django project'

name = 'pybuilder_django_plugin'
authors = [Author('Michael Gruber', 'aelgru@gmail.com')]
license = 'Apache License, Version 2.0'
summary = 'PyBuilder Django PlugIn'
version = '0.0.1'

default_task = ['initialize_django_project', 'analyze', 'publish']


@init
def set_properties(project):
    project.depends_on('Django')

    project.set_property('pybuilder_django_plugin_project_name', 'example_application')

    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_break_build', True)

    project.get_property('distutils_commands').append('bdist_wheel')
    project.set_property('distutils_classifiers', [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'])

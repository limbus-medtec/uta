############################################################################
# Theme setup

html_theme = 'invitae'

html_theme_path = ['themes']
if html_theme == 'sphinx_rtd_theme':
    import sphinx_rtd_theme
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
elif html_theme == 'bootstrap':
    import sphinx_bootstrap_theme
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()


############################################################################
# Project config

import uta
version = uta.__version__
release = str(uta.__version__)

project = u'UTA'
authors = project + ' Contributors'
copyright = u'2015, ' + authors

extlinks = {
    'issue': ('https://bitbucket.org/biocommons/uta/issue/%s', 'UTA issue '),
}

man_pages = [
    ('index', 'uta', u'UTA Documentation', [u'UTA Contributors'], 1)
]

############################################################################
# Boilerplate

# , 'inherited-members']
autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']
exclude_patterns = ['build', 'static', 'templates', 'themes']
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',
    'sphinx.ext.pngmath',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinxcontrib.fulltoc',
]
html_favicon = 'static/favicon.ico'
html_logo = 'static/logo.png'
html_static_path = ['static']
html_title = '{project} {release}'.format(project=project, release=release)
intersphinx_mapping = {
    'http://docs.python.org/': None,
}
master_doc = 'index'
pygments_style = 'sphinx'
source_suffix = '.rst'
templates_path = ['templates']

# <LICENSE>
# Copyright 2014 UTA Contributors (https://bitbucket.org/biocommons/uta)
##
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
##
# http://www.apache.org/licenses/LICENSE-2.0
##
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# </LICENSE>

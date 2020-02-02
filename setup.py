import os
from setuptools import setup

current_directory = os.path.dirname(__file__)
with open(os.path.join(current_directory, 'readme.rst')) as readme:  # É necessário criar um readme.rst
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

REQUIREMENTS = []

with open(os.path.join(current_directory, "django_template/requirements/production.txt"), 'r') as requirements:
    # Caminho do arquivo com as dependências da aplicação em production mode
    REQUIREMENTS = requirements.read().splitlines()

setup(
    name='django template',  # nome do pacote/aplicação
    version='0.0.1.dev7',  # Versão do pacote -> Deve ser atualizada a cada deploy
    packages=['django_template'],  # O nome da pasta com o conteúdo da aplicação.
    include_package_data=True,
    entry_points={'console_scripts': [
        'manage_application = django_template:manage',
        # Criação do comando de administração da app (função manage dentro de django_template/__init__.py).
    ]},
    license='License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    maintainer="Alisson Claudino",                 # Squad responsável pelo projeto
    maintainer_email='acjesus@inf.ufrgs.br',  # Email da squad responsável pelo projeto
    description='A template for production-ready applications',
    long_description=README,
    url='https://github.com/claudinoac/django-template.git',
    author='Alisson Claudino',
    author_email='acjesus@inf.ufrgs.br',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.7',  # Aqui é possível limitar a aplicação para uma ou mais versões do python.
    install_requires=REQUIREMENTS  # Um array com as dependências do projeto
)

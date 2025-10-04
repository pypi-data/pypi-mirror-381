from setuptools import setup, find_packages

setup(
    name='calculadora-simples-seu-nome', # Use um nome único para o seu teste!
    version='0.1.0',
    description='Um pacote simples para operações matemáticas básicas.',
    long_description=open('README.md').read(),
    author='Seu Nome Aqui',
    author_email='seu.email@exemplo.com',
    url='https://github.com/SeuUsuario/calculadora_simples_project',
    packages=find_packages(), # Encontra automaticamente a pasta 'calculadora_simples'
    python_requires='>=3.8',
)
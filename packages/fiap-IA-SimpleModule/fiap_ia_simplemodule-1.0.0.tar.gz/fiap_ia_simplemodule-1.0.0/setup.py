from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fiap-IA-SimpleModule',
    version='1.0.0',
    packages=find_packages(),
    description='Lib pdo Curso FIAP de IA para DEV\'s',
    author='Ricardo Franco Hernandez',
    author_email='ricardo.hern@icloud.com',
    url='https://github.com/ricardoHer/FIAP-IA-SimpleModule',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)

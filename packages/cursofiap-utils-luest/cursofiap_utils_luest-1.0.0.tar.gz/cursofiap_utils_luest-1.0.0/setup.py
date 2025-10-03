from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='cursofiap-utils-luest',
    version='1.0.0',
    packages=find_packages(),
    description='Descricao da sua lib cursofiap',
    author='Luciana Estevam',
    author_email='luestevam@hotmail.com',
    url='https://github.com/tadrianonet/luestevam',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)

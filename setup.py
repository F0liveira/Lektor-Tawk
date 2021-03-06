import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_tawk.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='Fabio Oliveira',
    author_email='lopesoliveirafabio@hotmail.com',
    description=description,
    keywords='Lektor plugin static-site Tawk',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-tawk',
    packages=find_packages(),
    py_modules=['lektor_tawk'],
    url='https://github.com/F0liveira/Lektor-Tawk',
    version='0.1',
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ],
    entry_points={
        'lektor.plugins': [
            'tawk = lektor_tawk:TawkPlugin',
        ]
    }
)

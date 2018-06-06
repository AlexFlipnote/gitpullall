import re
import codecs

from setuptools import setup


version = ''
with open('gitpullall/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


if not version:
    raise RuntimeError('version is not set')


try:
    f = codecs.open('README.md', encoding='utf-8')
    long_description = f.read()
    f.close()
except Exception as e:
    long_description = ''


setup(
    name='gitpullall',
    author='AlexFlipnote',
    url='https://github.com/AlexFlipnote/gitpullall',
    version=version,
    packages=['gitpullall'],
    license='GNU v3',
    description='A Python module that calls "git pull" on all subfolders',
    long_description=long_description,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'gitpullall=gitpullall.gitpullall:main',
            'gpa=gitpullall.gitpullall:main'
        ]
    }
)

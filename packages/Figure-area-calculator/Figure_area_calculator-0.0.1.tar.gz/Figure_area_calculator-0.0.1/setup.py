from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r', encoding="utf8") as f:
    return f.read()


setup(
  name='Figure_area_calculator',
  version='0.0.1',
  author='Vladimir_Zhurbenko',
  author_email='zhurben89@mail.ru',
  description='This project is a simple module designed to calculate the area of geometric figure.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/VladimirZhur/Resume_projects.git',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='',
  project_urls={
    'GitHub': 'https://github.com/VladimirZhur/Resume_projects.git'
  },
  python_requires='>=3.6'
)
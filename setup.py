from setuptools import setup

setup(name='scaffold_project',
      version='0.2',
      description='A package that lets you automate a new service setup.',
      author='Pavithra',
      license='MIT',
      packages=['scaffold_project'],
      install_requires=['jinja2', 'pyyaml'],
      entry_points={
        'console_scripts': ['scaffold_project=scaffold_project.command_line:main']
      },
      zip_safe=False)

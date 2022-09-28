from setuptools import setup, find_packages
setup(
    name = 'GemBased',
    version = '1.0',
    packages = find_packages(include = ('gembased*', )) + ["prophecy_config_instances"],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.3.5'],
    entry_points = {
'console_scripts' : [
'main = gembased.pipeline:main', ], },
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)

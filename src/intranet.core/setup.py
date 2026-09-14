Set-Content -Path "src\intranet.core\setup.py" -Value @"
from setuptools import find_packages, setup

setup(
    name='intranet.core',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api',
        'plone.app.dexterity',
    ],
)
"@
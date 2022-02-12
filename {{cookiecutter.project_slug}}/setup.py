import os
from pathlib import Path

from setuptools import find_packages, setup

root_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))

# We lock these in the requirements.txt file
install_requires = [
]

# Because we do not have a dev dependencies lock file, lock them here
dev_requires = [
    "pip-tools==6.2.0",
    "coverage==5.5",
    "pytest==6.2.4",
    "pytest-mock==3.6.1",
]

setup(
    name="{{ cookiecutter.project_slug }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=Path(f"{root_dir}/README.md").read_text().strip(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=dev_requires,
    extras_require={"dev": dev_requires},
    python_requires=">={{ cookiecutter.python_version.split('.', 1)[0] }}.0",
    platforms="any",
    version="0.0.0",
    author="{{ cookiecutter.project_author }}",
    license="Proprietary",
    classifiers=[
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: {{ cookiecutter.python_version.rsplit('.', 1)[0] }}",
        "Programming Language :: Python :: {{ cookiecutter.python_version.split('.', 1)[0] }} :: Only",
    ],
)


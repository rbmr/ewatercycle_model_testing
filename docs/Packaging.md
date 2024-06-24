Install the package and its dependencies in edit mode.
> pip install -e .

Install development dependencies:
> pip install .[dev]

Build and distribute the package.
> pip install setuptools wheel twine

> python setup.py sdist bdist_wheel

Upload to test pypi

> twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Download from test pypi

> pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple ewatercycle-model-testing

Upload to PyPi

> twine upload dist/*

Download from PyPi

> pip install ewatercycle-model-testing





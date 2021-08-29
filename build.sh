python setup.py bdist_wheel
python -m twine upload dist/*

rm -rf build
rm -rf dist


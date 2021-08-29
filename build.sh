python setup.py bdist_wheel
python -m twine upload dist/*

rm -rf build
rm -rf dist
rm -rf tracardi_plugin_sdk.egg-info


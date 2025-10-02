pip install build twine


rm -rf dist
python -m build

python -m twine upload dist/*

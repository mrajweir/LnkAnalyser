import os
import sys
import json
import shutil

# Autobump the micro version
with open("version", "r") as version_file:
    version = json.load(version_file)
    version["micro"] = int(version["micro"]) + 1

with open("version", "w") as version_file:
    json.dump(version, version_file)

if sys.argv[1] == 'test':
    shutil.rmtree('dist')
    os.mkdir('dist')
    os.system('python setup.py sdist bdist_wheel')
    #os.system('python -m twine upload --repository testpypi dist/*')
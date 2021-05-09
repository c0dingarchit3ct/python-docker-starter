#!/bin/sh

echo " doing pip install"
pip install -r requirements.txt
echo "running tests"
cd /sourcecode/tests
ls -al
python tests.py
cd /sourcecode
echo "run the app"
python app.py
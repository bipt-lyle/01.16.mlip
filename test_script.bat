@echo off
git pull origin staging
pip install -r requirements.txt
python -m unittest discover
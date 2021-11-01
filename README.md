OS: Ubuntu 21.04
Python: 3.9.7


pip install virtualenv
python -m virtualenv BI_Pain
source BI_Pain/bin/activate

pip install google-api-python-client
pip install kivy
pip install bs4
pip install biopython
pip install aiohttp
pip install pandas
pip install scipy
pip install scanpy
pip install opencv-python
pip3 install lxml

pip freeze > requirements.txt  
python pain.py

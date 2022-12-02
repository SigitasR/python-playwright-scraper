### Playwright / Python web scraper:
Simple web scraper in Python and Playwright. Subject is local online grocery store barbora.lt.

Scrapes given category and saves product data to CSV file.

Writen for training purposes to familiarize myself with Python version of Playwright, and it's use as a standalone library (without `pytest`).

Project requires:



#### Setup:
Create Python and activate virtual environment. Inside project root run:

```commandline
python -m venv .env

source .env/bin/activate
```

Install required dependencies:

```commandline
pip install -r requirements.txt
```

Before running `main.py` set Node.js memory option to avoid out of memory errors when crawling trough categories with very large amount of items:
```commandline
export NODE_OPTIONS="--max-old-space-size=16384"
```

Install Playwright browsers:
```commandline
playwright install
```

Run main.py inside virtual env
```commandline
python main.py
```

or (to see available command line parameters):

```commandline
python main.py -h
```


Results are saved into CSV file `output-{unix time stamp}.csv`
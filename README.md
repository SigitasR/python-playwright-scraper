### After cloning repo run:

```commandline
poetry install

poetry shell
```

Before running `main.py` set Node.js memory option to avoid out of memory errors when crawling trough categories with very large amount of items:
```commandline
export NODE_OPTIONS="--max-old-space-size=16384"
```

Run main.py inside Poetry virtual env
```commandline
python main.py
```

Results are saved into CSV file `output-{unix time stamp}.csv`
# json2csv

`json2csv` is a simple Python script that converts simple, non-hierarchical JSON files to CSV ready for importing into a relational database or loading into Excel or other spreadsheets.

It needs [unicodecsv](https://github.com/jdunck/python-unicodecsv). This can be installed using your favourite Python package manager e.g.

    pip install unicodecsv

Or

    easy_install unicodecsv

Then you run `json2csv` as follows:

    ./json2csv myjsonfile.json mycsvfile.csv

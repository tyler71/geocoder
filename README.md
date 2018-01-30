usage: __main__.py [-h] [-f {python,json,csv}] [-c COLUMN] [--config CONFIG]
                   files [files ...]

For each address in file, print Address, Latitude and Longitude of Address

positional arguments:
  files

optional arguments:
  -h, --help            show this help message and exit
  -f {python,json,csv}, --format {python,json,csv}
                        Output format
  -c COLUMN, --column COLUMN
                        Which header to parse, default "addresses"
  --config CONFIG

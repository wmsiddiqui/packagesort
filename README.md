This project sorts packages based on the width, height, length, and mass.

## Dependencies 
To run this project, you must have Python3 installed. Python3 should come with the only dependency needed for this project, which is `unittest`, to run the tests.

## Run with default parameters
to run the project, you may run, from the root of this project `python3 package_sorter.py` to run the package sorter with the default parameters already hard coded.

## Unit tests
To run the unit tests, from your root, run `python package_sorter_tests.py`. This will run all of the unit tests in that file.

## Run from commandline with custom parameters
From the root directory, run
`python3 package_sorter.py 100 100 100 120`

Note that if you do not provide the exact number of parameters, it will throw an exception. Also if the number is not parsable to a float, it will throw an exception:
`could not convert string to float: '149.9999999a9'`

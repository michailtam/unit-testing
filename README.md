# Unit Testing (TDD) in Python using Argparse

This code snippet shows how command line arguments can be passed via the terminal using Python,
the argparse library and executing unit testing. The code executes three simple tests:

1. Checks if the command line image name is the right one
2. Checks if the training-set len is the right one
3. Checks if the test-set len is the right one

**NOTE:** For simplicity, the Dataset class holds only the len of the training and test
set and is set fixed. These values are getting calculated in real applications
based on the dataset data. The code sipped only shows the methodology.

To execute the test (without any error) issue the following command in the terminal:

`python test_unit.py --image images/img_0004.png --train-len 10000 --test-len 1000`

Changing the above values leads to the respective error.

**Output:**
```...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```
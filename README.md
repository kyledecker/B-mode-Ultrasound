# Assignment 5: B-mode Ultrasound v1.0.0

## SUMMARY
This package is used to generate B-mode images from raw beamformed RF data. RF data is read in from a binary file and shaped according to parameters in a JSON file. The data is then envelope detected, log compressed, and post-processed to generate a B-mode ultrasound image. 

## MODULES
* *main.py* - wrapper script used to perform generate and display/save B-mode image
* *read_binary.py* - reads binary RF data into 1-D array
* *parse_metadata.py* - reads in acquisition parameters from JSON file 
* *parse_cli.py* - parses command line inputs 
* *envelope_detection.py* - performs envelope detection by taking the magnitude of the analytic signal
* *log_compression.py* - performs normalization and log compression 
* *manipulate.py* - reshapes the 1-D RF data array based on acquisition parameters
* *output_generation.py* - calculates the scan geometry and displays/saves the final image

## UNIT TESTING
Unit testing of core functions can performed by running *py.test* from the base directory

## RUN CODE
The B-mode ultrasound script can be run from the base directory using the following command:
```
python main.py
```

**Be sure to set inputs for binary file path, JSON file path, etc.** 
For help and description of input arguments:
```
python main.py --help
```
# MHWsim 

<p align="center"><img src="/media/mhw_tanks.png" alt="5 gallon tanks in lab containing strabwerry anemones on coral frag tiles" width="50%"/></p>

## What's in this repository?
This repository contains the scripts and files related to the development of a Marine Heatwave Simulator (MHWsim) using a Raspberry Pi.

This repository is maintained by Amelia Ritger (GitHub: [@ameliaritger](https://github.com/ameliaritger)) at the University of California, Santa Barbara in the Department of Ecology, Evolution, & Marine Biology. Please direct any questions or comments about this repository to [Amelia Ritger](mailto:aritger@ucsb.edu). The repository DOI is: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5520736.svg)](https://doi.org/10.5281/zenodo.5520736)

## How is this repository structured?
```
.
|
├── media/                                # Directory containing media files for project repo
|
├── code/                                 # Directory with scripts for the MHWsim
|   └── Alert.py                          # Script for sending SMS alerts
|   └── CleanUp.py                        # Script for saving data, clearing lists/variables, and going to sleep
|   └── IO_ctrl.py                        # Script for initializing relay board
|   └── MHWRamp.py                        # Script for ramping up and down temperatures at start/end of MHW event
|   └── MHWsim.py                         # Script for initializing MHWsim objects, parameters and then running the MHWsim 
|   └── Memory.py                         # Script for constructing and saving to .csv file
|   └── PID.py                            # Script for Proportional–integral–derivative controller algorithm
|   └── SensorAverage.py                  # Script for averaging multiple consecutive temperature probe readings and calculating the average temperature across replicates
|   └── SensorInfo.py                     # Script to enter temperature probe ROM numbers and location identification, and calibration values for each probe
|   └── Temperature.py                    # Script for reading temperature probes
|   └── main.py                           # Main script to run all code associated with MHWsim
|   └── mhw_profile.csv                   # MHWsim experiment data (from SBC LTER), required for initial code test
|
├── documentation/                        # Directory containing MHWsim system build documentation
|   └── rpiMHWsimConstruction.docx        # Document for building the RPi MHWsim system
|
├── .gitignore
|
├── LICENSE
|
├── README.md
|
└── MHWsim.Rproj
```

# MHWsim 

<p align="center"><img src="/media/mhw_tanks.png" alt="5 gallon tanks in lab containing strabwerry anemones on coral frag tiles" width="50%"/></p>

## What's in this repository?
This repository contains the scripts and files related to the development of a Marine Heatwave Simulator (MHWsim) using a Raspberry Pi.

This repository is maintained by Amelia Ritger (GitHub: [@ameliaritger](https://github.com/ameliaritger)) at the University of California, Santa Barbara in the Hofmann Lab, Department of Ecology, Evolution, & Marine Biology. Please direct any questions or comments about this repository to [Amelia Ritger](mailto:aritger@ucsb.edu).

## How is this repository structured?
```
.
|
├── media/                                      # directory containing media files for project repo
|
├── simulator/                                  # directory containing resources for building and running the RPi MHWsim system
|   └── code/                                   # directory with scripts for the MHWsim
|      └── Alert.py                             # script for sending SMS alerts
|      └── CleanUp.py                           # script for saving data, clearing lists/variables, and going to sleep
|      └── IO_ctrl.py                           # script for initializing relay board
|      └── MHWRamp.py                           # script for ramping up and down temperatures at start/end of MHW event
|      └── MHWsim.py                            # script for initializing MHWsim objects, parameters and then running the MHWsim 
|      └── Memory.py                            # script for constructing and saving to .csv file
|      └── PID.py                               # script for Proportional–integral–derivative controller algorithm
|      └── SensorAverage.py                     # script for averaging multiple consecutive temperature probe readings and calculating the average temperature across replicates
|      └── SensorInfo.py                        # script to enter temperature probe ROM numbers and location identification, and calibration values for each probe
|      └── Temperature.py                       # script for reading temperature probes
|      └── main.py                              # main script to run all code associated with MHWsim
|      └── mhw_profile.csv                      # MHWsim experiment data, required for initial code test
|
|   └── documentation/                          # directory containing MHWsim system build documentation
|      └── rpiMHWsimConstruction.docx           # document for building the RPi MHWsim system
|
├── .gitignore
|
├── LICENSE
|
├── README.md
|
└── MHWsim.Rproj
```

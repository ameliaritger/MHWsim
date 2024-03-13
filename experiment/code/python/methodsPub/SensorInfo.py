#Establish temperature sensor locations
hot_tank = ["28-00000eb3cf7d", "28-00000eb42add"]
cold_tank = ["28-00000eb5045f", "28-00000eb3fd89"]
mix_tank = ["28-00000eb4cb62", "28-00000eb3e681", "28-00000eb51050"]
no_tank = ["28-00000eb52c32", "28-00000eb50e10", "28-00000eb501b0", "28-00000eb496d2", "28-00000eb3f54e", "28-00000eb4619b"]
#"28-00000ec24f93", "28-00000ec23ab6", "28-00000ec25534", "28-00000eb4b7e0", "28-00000eb4a798", 

#Establish temperature sensor calibration parameters
ref_high = 49 #Oakley lab water bath temperature
ref_low = 0 #ice bath temperature
ref_range = ref_high - ref_low
device_cal = {"28-00000eb42add": [48.687, 0.25], #0
              "28-00000ec23ab6": [48.812, 0.125],
              "28-00000eb50e10": [48.75, 0.187],
              "28-00000eb5045f": [48.687, 0.187], #3
              "28-00000eb4a798": [48.562, 0.125],
              "28-00000eb4cb62": [48.687, 0.25],
              "28-00000eb51050": [48.75, 0.25], #6
              "28-00000ec25534": [48.937, 0.25],
              "28-00000eb501b0": [48.75, 0.25],
              "28-00000eb496d2": [48.75, 0.187], #9
              "28-00000eb4b7e0": [48.812, 0.25],
              "28-00000eb3fd89": [48.937, 0.187],
              "28-00000ec24f93": [48.812, 0.062], #12
              "28-00000eb3cf7d": [48.875, 0.25],
              "28-00000eb3f54e": [48.75, 0.25], 
              "28-00000eb4619b": [48.812, 0.187], #15
              "28-00000eb52c32": [49.0, 0.25],
              "28-00000eb3e681": [48.937, 0.312]}
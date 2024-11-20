import time
import pandas as pd
import numpy as np
import Temperature as tm
import SensorInfo as sinfo

#Iniitialize lists and variables
avg_temps, all_temps_avg = ([] for i in range(2)) #initialize blank list for each treatment plus sensor temp correction

#Initialize sleep times
sleep_process = 0.1 #number of seconds to sleep between ever sensor reading (to allow processor to catch up)

repeat_measurements = 3

def get_avg_temp(temp_ctrl, sleep_repeat):
    all_temps_df = pd.DataFrame(0, index = np.arange(3), columns = (sinfo.chill_devices + sinfo.severe_devices + sinfo.extreme_devices + sinfo.sump_devices))
    for number_of_rows in range(repeat_measurements):
        for index in range(len(temp_ctrl)):
            temp_ctrl[index].load_temp() #Read temperatures on chill tank sensors
            device_cal_val = sinfo.device_cal[temp_ctrl[index].Name] #Get calibration values for sensor
            raw_high =  device_cal_val[0] #Read in high calibration value for sensor
            raw_low = device_cal_val[1] #Read in low calibration value for sensor
            raw_range = raw_high - raw_low #Calculate the calibration value range
            calibrated_val = (((temp_ctrl[index].Temp  - raw_low) * sinfo.ref_range) / raw_range) + sinfo.ref_low #Calibrate sensor readings
            matching_cell = all_temps_df.columns.get_loc(temp_ctrl[index].Name)
            all_temps_df.iloc[(number_of_rows, matching_cell)] = calibrated_val
            time.sleep(sleep_process)
        time.sleep(sleep_repeat)
    avg_chill = all_temps_df[all_temps_df.columns.intersection(sinfo.chill_devices)].mean().mean()
    avg_severe = all_temps_df[all_temps_df.columns.intersection(sinfo.severe_devices)].mean().mean()
    avg_extreme = all_temps_df[all_temps_df.columns.intersection(sinfo.extreme_devices)].mean().mean()
    print(f"The chill tank temp average is {avg_chill}")
    print(f"The severe tank temp average is {avg_severe}")
    print(f"The extreme tank temp average is {avg_extreme}")
    avg_temps = [avg_chill, avg_severe, avg_extreme] #create list of average temperatures for each treatment
    all_temps = all_temps_df.mean(axis=0).apply(lambda x: round(x,3)).tolist() #create a list of the mean average temps for each sensor, rounded to 3 digits
    sump_temps = all_temps[-3:] #extract sump tank temperatures
    sump_temps[0], sump_temps[1] , sump_temps[2] = sump_temps[2], sump_temps[0], sump_temps[1] #reorder sump tank temperatures from chill > extreme
            
    return all_temps, avg_temps, sump_temps

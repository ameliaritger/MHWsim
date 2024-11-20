import glob
import datetime
import SensorInfo as sinfo

class MEM(object):
    def __init__(self, device_folder, external_path):
        self.Probe = device_folder + '/w1_slave'
        self.Name = device_folder.split('/')[-1]
        
        base_dir = '/sys/bus/w1/devices/'            #directory where thermistor files are populated
        device_folders = glob.glob(base_dir + '28*') #get list of all thermistor folders
        num_therm = len(device_folders)              #calculate the number of thermistor pairs
        
        self.external_path = external_path

        self.dt = datetime.datetime #use this module for getting the date/time

        self.file_name = str(self.dt.now()) + ".csv" #construct csv file name using datetime so it is always unique
        self.external_file_name = self.external_path + self.file_name #append to external path

        self.external_file = open(self.external_file_name, 'a');
        #write header to file
        header = ["Timestamp", "Chill set", "Severe set", "Extreme set", "Chill heater", "Severe heater", "Extreme heater"]
        for device_list in [sinfo.chill_devices, sinfo.severe_devices, sinfo.extreme_devices, sinfo.sump_devices]:
            for device in device_list:
                header.append(device)
        self.external_file.write(',' .join(header) + ',' + '\n')
        self.external_file.close()

    def save(self, data_list):#target_temp, measured_temp):
        time = self.dt.now() #get date/time data
        #data = str(time) + ',' + str(target_temp) + ',' + str(measured_temp) + ',' #contruct data point
        data = str(time) + ',' + ','.join(str(value) for value in data_list) + ','
        
        self.external_file = open(self.external_file_name, 'a');
        self.external_file.write(data + '\n') #write data to external file
        self.external_file.close()

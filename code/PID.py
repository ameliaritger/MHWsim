import time

pid_error, pid_output = ([0,0,0] for i in range(2)) #initialize blank lists

sleep_process = 0.1 #number of seconds to sleep between readings (to allow processor to catch up)

def control_temps(temp_sets, measured_temps, previous_temp, error_integral, error_derivative, Kp, Ki, Kd):
    for index_num in range(len(temp_sets)):
        pid_error[index_num] = (temp_sets[index_num] - measured_temps[index_num]) # Calculate the error
        pid_output[index_num] = Kp[index_num] * pid_error[index_num] + Ki[index_num] * error_integral[index_num] + Kd[index_num] * error_derivative[index_num] # Calculate the PID output
        error_integral[index_num] += pid_error[index_num] # Update the error integral
        error_derivative[index_num] = pid_error[index_num] - previous_temp[index_num] # Update the error derivative
        previous_temp[index_num] = measured_temps[index_num] #previous temp is now the most recent temp (for next time)

        time.sleep(sleep_process)
        
    return pid_output, previous_temp, error_integral, error_derivative

        
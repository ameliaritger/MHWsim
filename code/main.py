import MHWsim as sim
import CleanUp as clean
import time

if __name__ == "__main__":
    while True: #restart program if it breaks
        try:
            sim.mhw_sim()
            break #stop the program once everything has run
        except:
            clean.send_email() #email amelia
            print("there's an issue!")
            time.sleep(2*60) #wait 2 minutes before starting the program over

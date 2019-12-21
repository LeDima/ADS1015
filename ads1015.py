import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)# Start ranging
#tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

# time.sleep(1)
count=0
sumdistance=chan.voltage

while True:
    count=count+1
    
    for i in range(10):
        sumdistance=sumdistance+(chan.voltage-sumdistance)/10
        time.sleep(0.05)
       
    
#     if (distance >1200):
#         distance=1200
#     if (distance > 0):
#         print("%d mV, %d" % (distance,  count))
    print("%5.3f, %d" % (sumdistance,  count))
    f= open("distance.txt","w")
    f.write( "%5.3f\r\n"% sumdistance)
    f.close() 
    
#     time.sleep(0.5)
    

#tof.stop_ranging()
#tof.close()
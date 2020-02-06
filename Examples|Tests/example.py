from marvelmind import MarvelmindHedge
from time import sleep
import sys

def main():
    hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=12, debug=False) # create MarvelmindHedge thread
    hedge.start() # start thread
    pos = hedge.position()
    while True:
        try:
            sleep(1)
            print (pos) # get last position and print
            hedge.print_position()
            if (hedge.distancesUpdated):
				hedge.print_distances()
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()
main()

#DAY-8
#PAINT AREA CALC
import math
heightofwall=int(input("Height of the wall: "))
widthofwall=int(input("wWidth of the wall: "))
coverage=5
def paintarea(height,width,cover):
    no_of_cans=math.ceil((heightofwall*widthofwall)/coverage)
    
    print(f"You'll need to buy {no_of_cans} of paints")
paintarea(height=heightofwall, width=widthofwall, cover=coverage)

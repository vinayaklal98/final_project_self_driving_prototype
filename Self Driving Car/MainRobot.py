
from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule

##################################################
motor = Motor(2,3,4,17,22,27)
##################################################

def main():

    img = WebcamModule.getImg() # Get the image fom webcam
    curveVal = getLaneCurve(img,1) # Sending to Lane Module to get the curve

    sen = 1.3  # SENSITIVITY
    maxVAl= 0.3 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)

    #Dead Zone - Where car goes straight
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    motor.move(0.20,curveVal*sen,0.05) # Sending value to the Motors
    #cv2.waitKey(1)

if __name__ == '__main__':
    while True:
        main()
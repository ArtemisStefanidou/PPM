
import myComLib as lib
 
#main program
AM = 21996

queue_code = lib.AM_toBinary(AM)


listOfThree = []
listOfThree = lib.pairsOfThree(queue_code)
 
ppm = "10000000"
decimal_list = []
ppm_list = []
ppm_done = 0
ppm_tmp = 0

gray_list=[]
    
#converse the binary to decimal
for i in range(0,len(listOfThree)):
               gray_list.append(lib.binaryToGray(listOfThree[i]))  

for i in range(0,len(gray_list)):
    
    ppm_list.append(lib.shiftRight(gray_list[i],ppm))

one_by_one_list = []
one_by_one_list = lib.oneByOne(ppm_list) 

#plot all of the signal
Ts = 3*1e-6 # --> transmission rate equal to 1Mb/s
xAxons , yAxons = lib.ppm_waveform(one_by_one_list,Ts)

lib.plot_signal(xAxons,yAxons,True,True,True)
import numpy as np
import matplotlib.pyplot as plt

#plot the signal
def plot_signal(t, x, close_all = False,show_samples = False,show_grid = False,
                plot_type = 'o',xlabel = 't', ylabel = 'x(t)'):
    
    
    if close_all:
        plt.close('all')
        
    plt.plot(t,x)
    plt.xlabel('t [μsec]')
    plt.ylabel('x(t)')
    
     
    if show_samples:
        samples = np.asarray(x)
        samplesAxon = np.ma.masked_where(samples < 1,samples)
        plt.plot(t,samplesAxon,plot_type)
        
    if show_grid:
        plt.grid()
        
        
#separate one by one the bits that i can plot them
def oneByOne(ppm_list):
    
    one_by_one_list = []
    #put all the ppm in a string
    temp = ''
    for i in range(0,len(ppm_list)):
        temp = temp + ppm_list[i]
   
    for i in range(1,len(temp)+1):
        one_by_one_list.append(int(temp[i-1:i]))
    return one_by_one_list
    

#separate in pairs of three the binary AM to encoded for PPM
def pairsOfThree(queue_code):
    
    listOfThree = []
    pairs= ""
    while len(queue_code) != 0:
    
        for i in range(0, 3):
            
            pairs = pairs + str(queue_code[0])
            queue_code.pop(0)
            
        listOfThree.append(pairs)  
        pairs = ""
    return listOfThree

# create a waveform for the PPM 
def ppm_waveform(ak #ta platoi
                  , Ts #period of each palm
                  , samples = 10 #the 10 samples that asked in the exercise
                  ):
    
    M = 8  # 8-PPM
        
    ak=list(np.repeat(ak,samples))
        
    #Πολλαπλασιάζω με 10**6 για να το μετρήσω τον χρόνο σε μs για να είναι 
    #πιο ευανάγνωστο το διάγραμμα
    xAxons = list(np.arange(0, len(ak)*(Ts*10**6/(M*10)), Ts*10**6/(M*10)))
    return xAxons,ak
    
#converse decimal to gray
def binaryToGray(n):
    #converse binary to 
    #decimal to do the or and shift
    n = int(n,2)
    inv = 0;
    
    # Taking or end shift right until
    # n becomes zero
    while(n):
        inv = inv ^ n;
        n = n >> 1;
    return inv;

#shift the 1 to right so many times as the gray
#the correspondence between gray and 8-ppm
def shiftRight(timesOfShift,shift_number):
    
    for i in range(0,timesOfShift):
        shift_number = "0" + shift_number 
        
    if shift_number == "10000000":
        return shift_number
    else:
        #how many 0 will cut from the end of the string to be 8bits again
        #to plot for the 8-ppm
        shift_number = shift_number[:-timesOfShift]
        return shift_number
    
    
        
# AM from decimal to binary  
def AM_toBinary(AM):
    
    queue_code = []
    
    x = AM
    
    while x> 0 :
    
        if x % 2 == 0:
            queue_code.append(0)
        else :
            queue_code.append(1)
        x = x / 2.0
        x = int(x)
    
    #add 0 to be the len multiple of 3
    while len(queue_code) % 3 != 0:
        queue_code.append(0)
        
    queue_code.reverse()
    return queue_code
import sys
import pyaudio
import wave
import array
import numpy as np
import math

x = str(sys.argv[1])
#ca_two = str(sys.argv[2])
#print "My command line args are " + x

count = 0
chunk = 2048
import numpy


# open up a wave
wf = wave.open(x, 'rb')
#print "opened"
#wf = wave.open('test.wav', 'rb')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
# use a Blackman window
window = numpy.blackman(chunk)
#print "opened 1"
# open stream
p = pyaudio.PyAudio()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = RATE,
                output = True)
#print "opened audio"
# read some data
data = wf.readframes(chunk)
# play stream and find the frequency of each chunk
file= open ("audio.txt", 'w')
while len(data) == chunk*swidth:
    # write data out to the audio stream
    stream.write(data)
    # unpack the data and times by the hamming window
    indata = numpy.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
                                         data))*window
    # Take the fft and square each value
    fftData=abs(numpy.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = numpy.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        print "The freq is %f Hz." % (thefreq)
	#array.count(thefreq)
	#np.count(thefreq)
	#print "The freq is %f Hz." % (thefreq)
	#print numpy.count_nonzero(thefreq)
	#print "The lenghth of file is" % (len(find(thefreq)))
	file.write('%s \n' %thefreq)
	file.flush()
    else:
        thefreq = which*RATE/chunk
        print "The freq is %f Hz." % (thefreq)
	len(thefreq)
	#print "The lenghth of file is" % (len)
	file.close()
	#text_file.close()
    # read some more data
    data = wf.readframes(chunk)
if data:
    stream.write(data)

vals = []
with open('audio.txt') as f:
    for line in f:
        vals.append(float(line.strip()))

#print(vals)

# Print output
#print("Min: %s" % min(vals))   
#print("Max: %s" % max(vals)) 
ratio = round (max(vals)/min(vals))
#print ("ratio : %.2f" %ratio)
print("Feature_1: %.2f" % round (max(vals)/min(vals)))


x = len(vals)
print ("length x is: %f" % x)
y = sum(vals)
#print ("Sum of vals: y is %f" % y)
z = y/x
print ("Avg : %f" % z)

res =[]
for i in range(x):
    d= (vals[i] - z)
    sq = (d**2)
    res.append(sq)
    #a=sum(res)
a = sum(res)/x
P = math.sqrt(a)
feature2=P/z
print ("Feature_2 : %s" %feature2)

diff =max(vals) - min(vals)
if diff > 1000 and z >2000:
   print "Intrusion: Glass break"

if z<290 and z>100:
    print "Intrusion: Like Explosion"

#print ("Count is : %s" %x)
#if x < 5:
 #  print "Intrusion: Door handle sound"

#for i in range(x-1):
#    if abs(vals[i] - vals[i+1]) > 900:
 #       print "Intrusion: Dog barking"

for i in range(x-1):
    if abs(vals[i] - vals[i+1]) > 900 and z <1000 and z>290:
        print "Intrusion: Dog barking"
    elif abs(vals[i] - vals[i+1]) < 900 and ratio < 5 and x < 4:
        print "Intrusion: Door handle sound"


#with open ('audio.txt') as f:
	#count = sum(1 for line in f)
#print "Count is" % (count)
#print numpy.count_nonzero(thefreq)
stream.stop_stream()
stream.close()
p.terminate()

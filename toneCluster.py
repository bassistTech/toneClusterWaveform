'''The MIT License (MIT)
Copyright (c) 2016 Francis Deck

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.'''

# Tone cluster audio waveform. This is the Python code extracted from
# The Jupyter notebook of the same name.

import math, numpy, numpy.random, numpy.fft, matplotlib.pyplot, wave

block_length = 4096 # block length in units of samples for waveform, should be a power of 2
sample_rate = 44100 # sampling rate in samples/sec

tfile = 300 # Length of file in seconds
fmin = 10 # Minimum frequency we're interested in
fmax = 20000 # Maximum frequency we're interested in
ratio = 1.1 # Approximate ratio from one frequency to the next
fThresh = 100
ratio2 = 1.1

j = math.ceil(fmin*block_length/sample_rate) # Starting frequency in cycles per block
fpos = [] # List of frequencies in cycles per block
f = [] # List of frequencies in Hz

while True:
    fpos.append(j)
    f.append(j*sample_rate/block_length) # Get this frequency
    fnext = f[-1]*ratio # Estimate the next frequency
    j = math.ceil(fnext*block_length/sample_rate); # Convert to next higher integer
    if fnext > fmax:
        break

print('index', 'cycles/block', 'freq (Hz)', sep = '\t')
for i in range(len(fpos)):
    print(i, fpos[i], f[i], sep = '\t')

numpy.random.seed()
tblock = block_length/sample_rate
nblocks = math.ceil(tfile/tblock)

ts = 1/sample_rate # Time period of each sample
t = numpy.arange(0, tblock, ts, dtype = numpy.float) # Array of time values
a = numpy.zeros_like(t, dtype = numpy.float); # Start with a zeroed-out array

for i in range(len(f)):
    omega = 2*numpy.pi*f[i]
    phase = numpy.random.rand()*2*numpy.pi
    s = numpy.sin(omega*t + phase)
    a = a + s

# Normalize to +/- 1, with an amplitude just shy of 32768

a = a*32000/max(abs(a))

aint = numpy.array(a, dtype = numpy.int16)

wf = wave.open('tonez44100.wav', 'wb')
wf.setnchannels(1) # number of channels, this will be monaural
wf.setsampwidth(2) # width of each sample, in bytes
wf.setframerate(int(sample_rate)) # intended sampling rate
for i in range(nblocks):
    wf.writeframes(aint)
wf.close()

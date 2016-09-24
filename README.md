# toneClusterWaveform
# Under Construction, files not uploaded yet

## Overview

This is a **jupyter** notebook that generates a tone cluster waveform file for use as a signal generator in PC based audio analysis.

Common DIY approaches to PC based audio spectrum analysis are based on generation of random noise, processing through a device-under-test, and Fourier transform (FT) analysis of the resulting signal. 

A drawback to a random input is that the output of the analysis is also random, i.e., successive measurements will produce slightly different results: Measurements will seem erratic when displayed in real time. This variation can be reduced by averaging, but doing so works against real time analysis, by requiring many successive measurements in order to produce a stable display.

I've experimented with yet another approach, which is to generate an artificial signal that is broadband in its content, but definitely not random. In this notebook, the signal is a "tone cluster," or a summation of sinusoids at discrete frequencies. 

I've also chosen frequencies so that each individual tone comes out to an integer number of cycles within a "block" of data read by the analyzer, whose length is typically a power of two. Thus from the standpoint of Fourier analysis, each sinusoid behaves like a continuous tone. Analyzing this tone cluster requires no apodization or "window" function.

My method assumes that there's nothing of interest lurking between the generated frequencies, which is not always a good assumption, but works well enough for measuring things like the low frequency behavior of speakers, or the functioning of mainstream audio circuits.

### Intended audience

I'm assuming that you fall into one of the following three categories:

* You're familiar with Python and Jupyter, and using this code won't be hard for you, even if you have to install some of the libraries.

* You're interested in the underlying theory, in which case the code does a decent job of documenting it, even if you're not planning on running it yourself.

* You just want the files already.

### TL;DR, just give me the file already

The file **tonez44110.mp3** is what you need for mainstream PC use. I've found that compressing it to MP3 format has no adverse effect on audio analysis. You will need to set up your analyzer for a 44.1 kHz sampling rate, 16k block length, and no windowing function. Just play it using the MP3 player app on your computer.

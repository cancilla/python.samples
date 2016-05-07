# python.samples

## Introduction

These samples demonstrate how to use the following python libraries when building an IBM Streams application with the Python Application API:

 * numpy
 * scipy
 * scikit-learn
 * pandas

**NOTE**: The samples are not intended to demonstrate the best practices with regards to building machine-learning or predictive models with the ababove-mentioned libraries. Rather, the purpose here is to show how these libraries can be used when writing applications with the Python Application API.


## Installation

    pip3 install numpy
    pip3 install scipy
    pip3 install scikit-learn
    pip3 install pandas

Additional installation instructions can be found at the following links: 

 * http://www.numpy.org/
 * http://www.scipy.org/
 * http://scikit-learn.org/stable/
 * http://pandas.pydata.org/


## Samples

### Timeseries

 * [convolve.py](convolve.py) - Demonstrates how to convolve data from a stream with a Hann window
 * [fftconvolve.py](fftconvolve.py) - Demonstrates how to perform FFT convolution on data data from a stream with a Hann window
 * [correlate.py](correlate.py) - Demonstrates how to correlate data from a stream with a Hann window 
 * [fft.py](fft.py) - Demonstrates how to perform FFT analysis on data from a stream
 * [ifft.py](ifft.py) - Demonstrates how to perform Inverse FFT analysis on data from a stream
 * [lowpassfilter.py](lowpassfilter.py) - Demonstrates how to filter incoming data with a low-pass Butterworth filter

### Supervised learning models
 * [knclassifier_sample.py](knclassifier_sample.py) - Demonstrates how to train a KNeighborsClassifier and score data in real-time


### Unsupervised learning models

**COMING SOON**


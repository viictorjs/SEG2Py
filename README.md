# SEG2Py
SEG2Py is a under development Python 3 module tested on Windows and Linux that works around the ObsPy framework. It offers a flexible and easy way to visualize SEG2 seismic sections.

Dependencies: ObsPy (which depends on Matplotlib, Numpy, Scipy and others).

How to install: use `pip install SEG2Py`

- Current functions:

  - Plot SEG2 seismic section:
   
     `plotSEG2(obspy_stream, *args, **kwargs)`
    
    - Parameters:
    
      - `obspy_stream`(**required**): ObsPy stream object returned after an ObsPy read( );
      - `normalized`(**optional - True/False**): if True the traces are normalized against each trace maximum (*default = True*);
      - `gain`(**optional - int/float**): energy gain factor to be applied on each trace amplitudes (*default = 1*);
      - `shading`(**optional - True/False**): if True all the negative amplitudes of each trace will be shaded (*default = False*);
      - `clip`(**optional - True/False**): if True all amplitudes superposition will be cutted off (*default = False*);
      - `invertY`(**optional - True/False**): if True will invert the time axis (*default = False*).
      - `record_start`(**optional - int/float**): sets where (in miliseconds) the time axis will start (*default = 0*);
      - `record_end`(**optional - int/float**): sets where (in miliseconds) the time axis will end in miliseconds (*default = the ObsPy stream original record length*).
    
  - Usage sample: 
      ```
      from obspy import read
      from SEG2Py import *
            
      st = read('seg2_waveform_data')
      plotSEG2(st, gain = 3, shading = True, clip = True, record_end = 100)
      ```
    

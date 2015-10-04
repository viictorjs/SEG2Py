# SEG2Py
SEG2Py is a in development Python 3 module tested on Windows and Linux that works around the ObsPy framework offering a flexible and easy way to visualize SEG2 waveform data.

Dependencies: ObsPy (which depends on Matplotlib, Numpy, Scipy and others)

How to install: use `pip install SEG2Py`

- Current functions:

  - Normalized section plotting: `plotSEG2(obspy_stream, gain, shading, clip, invertY)`
    
    - `obspy_stream` (**required**): ObsPy stream object returned after an ObsPy read( );
    - `gain` (**optional - int/float**): energy gain factor to be applied on each traces aplitudes;
    - `shading` (**optional - True/False**): if True all the negative amplitudes of each trace will be shaded;
    - `clip` (**optional - True/False**): if True will deny amplitudes superposition;
    - `invertY` (**optional - True/False**): if True will invert the Y axis.
    
    - Usage sample: 
        ```
        from obspy import read
        import SEG2Py
            
        st = read('seg2_waveform_data')
        SEG2Py.plotSEG2(st, gain = 3, shading = True, clip = True, invertY = True)
        ```
    

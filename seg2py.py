
'''

    Seg2Py is a Python 3 module which offers a flexible and easy way to visualize
    SEG2 waveform data using the ObsPy framework.
    
    Author: Victor Guedes (Geophysics undergraduate stundent at University of Brasilia - Brazil)
    E-mail: vjs279@hotmail.com

                               '''

import matplotlib.pyplot as plt

def plotSEG2(obspy_stream, *args, **kwargs):

    # default:
    amplitude_gain = 1
    amplitude_shading = False
    invertY = False
    clip = False
    
    for i in kwargs:

        if i == 'gain':

            if type(kwargs[i]) == int or type(kwargs[i]) == float:
            
                amplitude_gain = kwargs['gain']

            else:

                print('\nSeg2Py error: the gain parameter should be an intenger or a float.')
                amplitude_gain = 'error'                

        elif i == 'shading':

            if kwargs[i] == True:

                amplitude_shading = True

            elif kwargs[i] == False:

                amplitude_shading = False

            else:

                print('\nSeg2Py error: the shading parameter should be True or False.')
                amplitude_shading = 'error'

        elif i == 'clip':

            if kwargs[i] == True:

                clip = True

            elif kwargs[i] == False:

                clip = False

            else:

                print('\nSeg2Py error: the clip parameter should be True or False.')
                clip = 'error'

        elif i == 'invertY':

            if kwargs[i] == True:

                invertY = True

            elif kwargs[i] == False:

                invertY = False

            else:

                print('\nSeg2Py error: the invertY parameter should be True or False.')
                invertY = 'error'
        
    if amplitude_gain != 'error' and amplitude_shading != 'error' and invertY != 'error' and clip != 'error':

        if obspy_stream[0].stats._format == 'SEG2':
            
            pos_geophone1 = float(obspy_stream[0].stats.seg2['RECEIVER_LOCATION'])
            geophones_dx = float(obspy_stream[1].stats.seg2['RECEIVER_LOCATION'])-float(obspy_stream[0].stats.seg2['RECEIVER_LOCATION'])
            fig = plt.figure()
            ax = fig.add_subplot(111)

            for i in range(len(obspy_stream)):
                
                trace, = ax.plot((obspy_stream[i].data/obspy_stream[i].data.max())*(-1)*amplitude_gain+pos_geophone1+geophones_dx*i,
                            [obspy_stream[i].stats.delta*k*1000 for k in range(len(obspy_stream[i]))], color='black')

                if clip == True:

                    trace.get_xdata()[trace.get_xdata() < pos_geophone1+i*geophones_dx-((geophones_dx/2)*0.9)] = pos_geophone1+i*geophones_dx-((geophones_dx/2)*0.9)
                    trace.get_xdata()[trace.get_xdata() > pos_geophone1+i*geophones_dx+((geophones_dx/2)*0.9)] = pos_geophone1+i*geophones_dx+((geophones_dx/2)*0.9)
                    trace.set_xdata(trace.get_xdata())

                if amplitude_shading == True:

                    somb = ax.fill_betweenx(trace.get_ydata(),pos_geophone1+geophones_dx*i,trace.get_xdata(),
                                        where = trace.get_xdata() >= pos_geophone1+i*geophones_dx,color='black')

            plt.title('Source: %s m | %d channels'%(obspy_stream[0].stats.seg2['SOURCE_LOCATION'],len(obspy_stream)))
            plt.xlabel('Distance (m)')
            plt.ylabel('Time (ms)')
            plt.xlim(pos_geophone1-geophones_dx,pos_geophone1+geophones_dx*len(obspy_stream))

            if invertY == True:

                plt.gca().invert_yaxis()
            
            plt.show()

        else:

            print("\nSeg2Py error: the obspy_stream you are using is not in seg2 format.")
                


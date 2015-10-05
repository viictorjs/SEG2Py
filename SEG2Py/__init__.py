
'''

    SEG2Py is a Python 3 module that works around the ObsPy framework offering a flexible and
    easy way to visualize SEG2 seismic sections.
    
    Author: Victor Guedes (Geophysics undergraduate stundent at University of Brasilia - Brazil)
    E-mail: vjs279@hotmail.com

                               '''

import matplotlib.pyplot as plt

def plotSEG2(obspy_stream, *args, **kwargs):

    # default:
    normalized = True
    gain = 1
    shading = False
    invertY = False
    clip = False
    record_start = 0
    record_end = obspy_stream[0].stats.delta*len(obspy_stream[0])*1000
    parameter_error = None
    
    for i in kwargs:

        if i == 'normalized':

            if kwargs[i] == True:

                pass

            elif kwargs[i] == False:

                normalized = False

            else:

                print('\SEG2Py ERROR: THE normalized PARAMETER SHOULD BE TRUE OR FALSE.')
                parameter_error = True 

        elif i == 'gain':

            if type(kwargs[i]) == int or type(kwargs[i]) == float:

                if kwargs[i] > 0:
            
                    gain = kwargs['gain']

                else:

                    print('\nSEG2Py ERROR: THE gain PARAMETER SHOULD BE GREATER THAN 0.')
                    parameter_error = True     
            else:

                print('\nSEG2Py ERROR: THE gain PARAMETER SHOULD BE AN INTEGER OR A FLOAT.')
                parameter_error = True              

        elif i == 'shading':

            if kwargs[i] == True:

                shading = True

            elif kwargs[i] == False:

                pass

            else:

                print('\SEG2Py ERROR: THE shading PARAMETER SHOULD BE TRUE OR FALSE.')
                parameter_error = True 

        elif i == 'clip':

            if kwargs[i] == True:

                clip = True

            elif kwargs[i] == False:

                pass

            else:

                print('\nSEG2Py ERROR: THE clip PARAMETER SHOULD BE TRUE OR FALSE.')
                parameter_error = True 

        elif i == 'invertY':

            if kwargs[i] == True:

                invertY = True

            elif kwargs[i] == False:

                pass

            else:

                print('\nSEG2Py ERROR: THE invertY PARAMETER SHOULD BE TRUE OR FALSE.')
                parameter_error = True

        elif i == 'record_start':

            if type(kwargs[i]) == int or type(kwargs[i]) == float:

                if kwargs[i] < record_end:
            
                    record_start = kwargs[i]

                else:
                    
                    print('\nSEG2Py ERROR: THE record_start PARAMETER SHOULD BE LESS THAN %.1f ms.'%record_end)
                    parameter_error = True 

            else:

                print('\nSEG2Py ERROR: THE record_start PARAMETER SHOULD BE AN INTEGER OR A FLOAT.')
                parameter_error = True

        elif i == 'record_end':

            if type(kwargs[i]) == int or type(kwargs[i]) == float:

                if kwargs[i] > 0 and kwargs[i] > record_start:
            
                    record_end = kwargs[i]

                else:
                    
                    print('\nSEG2Py ERROR: THE record_end PARAMETER SHOULD BE GREATER THAN %.1f ms.'%record_start)
                    parameter_error = True 

            else:

                print('\nSEG2Py ERROR: THE record_end PARAMETER SHOULD BE AN INTEGER OR A FLOAT.')
                parameter_error = True

        else:

            print('\nSEG2Py ERROR: %s IS NOT A SEG2Py RECOGNIZED PARAMETER.'%str(i))
            parameter_error = True 
        
    if parameter_error == None:

        if obspy_stream[0].stats._format == 'SEG2':
            
            pos_geophone1 = float(obspy_stream[0].stats.seg2['RECEIVER_LOCATION'])
            geophones_dx = float(obspy_stream[1].stats.seg2['RECEIVER_LOCATION'])-float(obspy_stream[0].stats.seg2['RECEIVER_LOCATION'])
            fig = plt.figure()
            ax = fig.add_subplot(111)
            st_max = max([max(obspy_stream[i]) for i in range(len(obspy_stream))])

            for i in range(len(obspy_stream)):

                if normalized == True:
                
                    trace, = ax.plot((obspy_stream[i].data/max(obspy_stream[i].data))*(-1)*gain+pos_geophone1+geophones_dx*i,
                                [obspy_stream[i].stats.delta*k*1000 for k in range(len(obspy_stream[i]))], color='black')

                else:
                
                    trace, = ax.plot((obspy_stream[i].data/st_max)*(-1)*gain+pos_geophone1+geophones_dx*i,
                                [obspy_stream[i].stats.delta*k*1000 for k in range(len(obspy_stream[i]))], color='black')    

                if clip == True:

                    trace.get_xdata()[trace.get_xdata() < pos_geophone1+i*geophones_dx-((geophones_dx/2)*0.9)] = pos_geophone1+i*geophones_dx-((geophones_dx/2)*0.9)
                    trace.get_xdata()[trace.get_xdata() > pos_geophone1+i*geophones_dx+((geophones_dx/2)*0.9)] = pos_geophone1+i*geophones_dx+((geophones_dx/2)*0.9)
                    trace.set_xdata(trace.get_xdata())

                if shading == True:

                    somb = ax.fill_betweenx(trace.get_ydata(),pos_geophone1+geophones_dx*i,trace.get_xdata(),
                                        where = trace.get_xdata() >= pos_geophone1+i*geophones_dx,color='black')

            plt.title('Source: %s m | %d channels'%(obspy_stream[0].stats.seg2['SOURCE_LOCATION'],len(obspy_stream)))
            fig.canvas.set_window_title('SEG2Py - Seismic section')
            plt.xlabel('Distance (m)')
            plt.ylabel('Time (ms)')
            plt.ylim(record_start,record_end)
            plt.xlim(pos_geophone1-geophones_dx,pos_geophone1+geophones_dx*len(obspy_stream))

            if invertY == True:

                plt.gca().invert_yaxis()
            
            plt.show()

        else:

            print("\nSEG2Py ERROR: THE OBSPY STREAM YOU'RE USING IS NOT IN SEG2 FORMAT.")
                

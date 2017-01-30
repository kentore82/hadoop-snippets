#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
# import glob
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from __future__ import print_function
import numpy as np
import sys

#import ais
import ais_old as ais
import re
import geohash
import time

def print_usage():
	print('''''')
	sys.exit()

def unroll_msg20(aisdata):
    for res_num in range(0,len(aisdata[u'reservations'])):
        for res_cont in aisdata['reservations'][res_num]:
            aisdata[u'res_' + res_cont + '_' + str(res_num)]=aisdata[u'reservations'][res_num][res_cont]        
    del aisdata[u'reservations']
    return aisdata
		
 
def decode_nmea(nmea):
    commasplit=nmea.split(',')    
    transmitter_info=commasplit[0].split('\\')    
    
    station=transmitter_info[-1].split('s:')[-1].split('//')[0]
    port_no=transmitter_info[-1].split('s:')[-1].split('//')[1][5:]
    MMSI=transmitter_info[-1].split('MMSI=')[-1]
    unixtime=commasplit[1].split('c:')[-1].split('*')[0] #transmitter_info[0].split('*')[0][2:]
    nmea_talkerid=commasplit[1].split('\\')[-1]
    fragment_no=commasplit[3]
    seq_message_id=commasplit[4]  
    radio_channel=commasplit[5]    
    payload=commasplit[-2]    
    fill_bits=int(commasplit[-1][0])
    
    #Decode ais payload
    msg_type=[]
    try:
        aisdata=ais.decode(payload,fill_bits)
        msg_type=int(aisdata['id'])
    except:
        try:
            fill_bits=2            
            aisdata=ais.decode(payload,fill_bits)
            msg_type=int(aisdata['id'])
        except:
            msg_type=30
            aisdata={'id':msg_type}          
    if msg_type==20:
	aisdata=unroll_msg20(aisdata) 
    
    if 'x' in aisdata and 'y' in aisdata: # and 'x'!=181 and 'y'!=91: # x- longitude , y- latitude
        try:
            aisdata[u'geohash'] = geohash.encode(aisdata['y'],aisdata['x'],13)
        except:
            aisdata[u'geohash'] = '0'

              
    #Append NMEA Tag Blocks         
    aisdata[u'n_station'] = station
    aisdata[u'n_port'] = port_no
    aisdata[u'n_MMSI'] = MMSI
    aisdata[u'unixtime'] = unixtime
    aisdata[u'n_talkerid'] = nmea_talkerid
    aisdata[u'n_fragmentno'] = fragment_no
    aisdata[u'n_seqmsg'] = seq_message_id
    aisdata[u'n_radiochannel'] = radio_channel
    aisdata[u'n_aispayload'] = payload
    aisdata[u'n_fillbits'] = fill_bits
    
    #append AIS: to the rest
    #data={'G':geodata,'O':aisdata}    
    
    return aisdata

def main(argv):
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_usage()
    
    infile = open(str(sys.argv[1]))
    
     
    #Counting variables 
    s=0
    mtype=[]
    start_time=time.time()

    #jump to line
    #n = 16351296#16349457#16345350
    #for i in range(0,n):
    #	infile.next()
    
    print("Decoding NMEA messages...")
    for nmea in infile:

	s+=1
        if nmea[:3]=='\s:':        
        	aisdata=decode_nmea(nmea)
        	mtype.append(aisdata["id"])
        
        
        print(str(s),end="\r")
    
    end_time=time.time()
        
    count=np.bincount(mtype)
    ii=np.nonzero(count)[0]
    count=np.vstack((ii,count[ii])).T

    print("Total time: " + str(round(end_time - start_time,2))+ ' seconds')
 
    
    print("Message type distribution")
    print("0 - error") 
    print(count)
    print("Sum dist. "+str(sum(count[:,1]))+'\n')
    
    print("No. lines in file: " + str(s))
    infile.close
 
 
if __name__ == '__main__':
    main(sys.argv[1:])
  
 

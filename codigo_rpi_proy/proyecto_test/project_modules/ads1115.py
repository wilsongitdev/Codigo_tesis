import smbus

bus = smbus.SMBus(1)# Get I2C bus

def ads1115config(canal,fs): #RANGO +-4.096V 
    
    if (canal=='A0') & (fs=='250'):
        data=[0xC2,0xA0] #CANAL A0 -->[0xC2,0xA0]
    elif (canal=='A1') & (fs=='250'):
        data=[0xD2,0xA0] #CANAL A1 -->[0xD2,0xA0]
    elif (canal=='A2') & (fs=='250'):
        data=[0xE2,0xA0] #CANAL A2 -->[0xE2,0xA0]
    elif (canal=='A3') & (fs=='250'):
        data=[0xF2,0xA0] #CANAL A3 -->[0xF2,0xA0]
    elif (canal=='A0-A1') & (fs=='250'):
        data=[0x82,0xA0]

    
    elif (canal=='A0') & (fs=='128'):
        data=[0xC2,0x80] #CANAL A0 -->[0xC2,0x80]
    elif (canal=='A1') & (fs=='128'):
        data=[0xD2,0x80] #CANAL A1 -->[0xD2,0x80]
    elif (canal=='A2') & (fs=='128'):
        data=[0xE2,0x80] #CANAL A2 -->[0xE2,0x80]
    elif (canal=='A3') & (fs=='128'):
        data=[0xF2,0x80] #CANAL A3 -->[0xF2,0x80]
    elif (canal=='A0-A1') & (fs=='128'):
        data=[0x82,0x80]
    
    elif (canal=='A0') & (fs=='64'):
        data=[0xC2,0x60] #CANAL A0 -->[0xC2,0x60]
    elif (canal=='A1') & (fs=='64'):
        data=[0xD2,0x60] #CANAL A1 -->[0xD2,0x60]
    elif (canal=='A2') & (fs=='64'):
        data=[0xE2,0x60] #CANAL A2 -->[0xE2,0x60]
    elif (canal=='A3') & (fs=='64'):
        data=[0xF2,0x60] #CANAL A3 -->[0xF2,0x60]
    elif (canal=='A0-A1') & (fs=='64'):
        data=[0x82,0x60]
        
    elif (canal=='A0') & (fs=='32'):
        data=[0xC2,0x40] #CANAL A0 -->[0xC2,0x40]
    elif (canal=='A1') & (fs=='32'):
        data=[0xD2,0x40] #CANAL A1 -->[0xD2,0x40]
    elif (canal=='A2') & (fs=='32'):
        data=[0xE2,0x40] #CANAL A2 -->[0xE2,0x40]
    elif (canal=='A3') & (fs=='32'):
        data=[0xF2,0x40] #CANAL A3 -->[0xF2,0x40]
    elif (canal=='A0-A1') & (fs=='32'):
        data=[0x82,0x40]
    
    elif (canal=='A0') & (fs=='16'):
        data=[0xC2,0x20] #CANAL A0 -->[0xC2,0x20]
    elif (canal=='A1') & (fs=='16'):
        data=[0xD2,0x20] #CANAL A1 -->[0xD2,0x20]
    elif (canal=='A2') & (fs=='16'):
        data=[0xE2,0x20] #CANAL A2 -->[0xE2,0x20]
    elif (canal=='A3') & (fs=='16'):
        data=[0xF2,0x20] #CANAL A3 -->[0xF2,0x20]
    elif (canal=='A0-A1') & (fs=='16'):
        data=[0x82,0x20]
    #adc
	#configurar config reg
    bus.write_i2c_block_data(0x48,0x01,data)
	
	#configurar lO_thresh register
    data1=[0x00,0x00] 
    bus.write_i2c_block_data(0x48,0x02,data1)
	
    #configurar HI_thresh register
    data2=[0x80,0x00] 
    bus.write_i2c_block_data(0x48,0x03,data2)
    bus.write_byte(0x48,0x00)
 
def ads1115conv():
    data = bus.read_i2c_block_data(0x48, 0x00, 2)
    raw_adc = (data[0] * 256 + data[1])
    if raw_adc > 32767:
       raw_adc -= 65535
    return raw_adc  

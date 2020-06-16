import numpy as np 
import serial
import socketio
import sqlalchemy as db
import yaml
<<<<<<< HEAD

from astropy.time import Time
from itertools import chain
=======
import astropy.units as u
from astropy.time import Time
from itertools import chain
import logging
>>>>>>> 7fdc453eb9f65a463f1c7f25dad89c269fb4ea8a

class FakeGuider():
    def __init__(self):
        return
    def send_query(self, qr):
        return

<<<<<<< HEAD
    def get_status(self):
            status = {'echo_command':'A', 
                      'mode': 1,
                      'volume': 1,
                      'finder_sound': 1,
                      'x_exposure': 1.0,
                      'y_exposure': 1.0,
                      'x_ra_pos': 1,
                      'y_ra_pos': 1,
                      'x_opt_offset': 1,
                      'y_opt_offset': 1,
                      'x_mech_offset': 1,
                      'y_mech_offset': 1,
                      'x_correction': 1,
                      'y_correction': 1,
                      'agressivness': 1,
                      'corr_estimate': 1,
                      'xscale': 1,
                      'yscale': 1,
                      'theta_X': 1,
                      'y_direction': 1,
                      'fw_version': 1.0,
                      'relay_state': 1,
                      'sun_vis': 1,
                      'cal_state': 1,
                      'message': "FakeGuider",
                      'checksum': "324sdf"}        
            status['sun_intensity'] = -100
            return status

class Guider():
    def __init__(self): 
        config = yaml.safe_load(open('solar_config.yml', 'r'))
        sp = serial.Serial()
        sp.port = config['guider_port']
=======

class Guider():
    def __init__(self): 
        self.config = yaml.safe_load(open('solar_config.yml', 'r'))
        sp = serial.Serial()
        sp.port = self.config['guider_port']
>>>>>>> 7fdc453eb9f65a463f1c7f25dad89c269fb4ea8a
        sp.baudrate = 38400
        sp.parity = serial.PARITY_NONE
        sp.bytesize = serial.EIGHTBITS
        sp.stopbits = serial.STOPBITS_ONE
        sp.timeout = 1 #1.5 to give the hardware handshake time to happen
        sp.xonxoff = True
        sp.rtscts = False
        sp.dtrdsr = False
        sp.open()
        sp.setDTR(0)
        self.sp = sp
<<<<<<< HEAD
        self.engine = db.create_engine(config['mysql_engine'])
        self.sio = socketio.Client()
        self.sio.connect(config['socketServer'])
=======
        self.engine = db.create_engine(self.config['mysql_engine'])
        self.sio = socketio.Client()
        self.sio.connect(self.config['socketServer'])
>>>>>>> 7fdc453eb9f65a463f1c7f25dad89c269fb4ea8a

    def send_query(self, qr):
        self.sp.write(str.encode(qr))
        out = self.sp.readline()

    def get_status(self, save_status=False):
        try:
            self.sp.write(str.encode('S'))
            out = str(self.sp.readline()).split(',')
<<<<<<< HEAD
            status = {'echo_command':out[0], 
                      'mode': np.long(out[1]),
                      'volume': np.long(out[2]),
                      'finder_sound': np.long(out[3]),
                      'x_exposure': np.float(out[4]),
                      'y_exposure': np.float(out[5]),
                      'x_ra_pos': np.long(out[6]),
                      'y_ra_pos': np.long(out[7]),
                      'x_opt_offset': np.long(out[8]),
                      'y_opt_offset': np.long(out[9]),
                      'x_mech_offset': np.long(out[10]),
                      'y_mech_offset': np.long(out[11]),
                      'x_correction': np.long(out[12]),
                      'y_correction': np.long(out[13]),
                      'agressivness': np.long(out[14]),
                      'corr_estimate': np.long(out[15]),
                      'xscale': np.long(out[16]),
                      'yscale': np.long(out[17]),
                      'theta_X': np.long(out[18]),
                      'y_direction': np.long(out[19]),
                      'fw_version': np.float(out[20]),
                      'relay_state': np.long(out[21]),
                      'sun_vis': np.long(out[22]),
                      'cal_state': np.long(out[23]),
                      'message': out[24],
                      'checksum': out[25]}        
            status['sun_intensity'] = np.log2(23.4 / status['x_exposure'])
=======
            status = {'guider_echo_command':out[0], 
                      'guider_mode': np.long(out[1]),
                      'guider_volume': np.long(out[2]),
                      'guider_finder_sound': np.long(out[3]),
                      'guider_x_exposure': np.float(out[4]),
                      'guider_y_exposure': np.float(out[5]),
                      'guider_x_ra_pos': np.long(out[6]),
                      'guider_y_ra_pos': np.long(out[7]),
                      'guider_x_opt_offset': np.long(out[8]),
                      'guider_y_opt_offset': np.long(out[9]),
                      'guider_x_mech_offset': np.long(out[10]),
                      'guider_y_mech_offset': np.long(out[11]),
                      'guider_x_correction': np.long(out[12]),
                      'guider_y_correction': np.long(out[13]),
                      'guider_agressivness': np.long(out[14]),
                      'guider_corr_estimate': np.long(out[15]),
                      'guider_xscale': np.long(out[16]),
                      'guider_yscale': np.long(out[17]),
                      'guider_theta_X': np.long(out[18]),
                      'guider_y_direction': np.long(out[19]),
                      'guider_fw_version': np.float(out[20]),
                      'guider_relay_state': np.long(out[21]),
                      'guider_sun_vis': np.long(out[22]),
                      'guider_cal_state': np.long(out[23]),
                      'guider_message': out[24],
                      'guider_checksum': out[25]}        
            status['guider_sun_intensity'] = "{0:4.3f}".format(np.log2(23.4 / status['guider_x_exposure']))
            status['guider_sun_location'] = "({0:02d}, {1:02d}), ({2:02d}, {3:02d})".format(status['guider_x_ra_pos'],
                                                 status['guider_y_ra_pos'],
                                            self.config['guider_x_center'],
                                            self.config['guider_y_center'])
            status['guider_update_time'] = (Time.now() - 7*u.h).iso[0:19]
>>>>>>> 7fdc453eb9f65a463f1c7f25dad89c269fb4ea8a
            if save_status:
              self.save_status(status)
            return status
        except:
<<<<<<< HEAD
            return {}
            pass
=======
            x = self.get_status(save_status=save_status)
            return x
>>>>>>> 7fdc453eb9f65a463f1c7f25dad89c269fb4ea8a

    def save_status(self, status):
        connection = self.engine.connect()
        metadata = db.MetaData(bind=self.engine)
        guider_table = db.Table('guider', metadata, autoload=True)
        connection.execute(guider_table.insert().values(
<<<<<<< HEAD
                                                MODE = status['mode'],
                                                X_EXP = status['x_exposure'],
                                                Y_EXP = status['y_exposure'],
                                                X_RA_POS = status['x_ra_pos'],
                                                X_RA_OPT_OFF = status['y_ra_pos'],
                                                Y_RA_OPT_OFF = status['x_opt_offset'],
                                                X_RA_MECH_OFF = status['y_opt_offset'],
                                                XCORR = status['x_correction'],
                                                YCORR = status['y_correction'],
                                                RELAY_STATE = status['relay_state'],
                                                SUN_VIS = status['sun_vis'],
                                                MESSAGE = status['message']))
=======
                                                MODE = status['guider_mode'],
                                                X_EXP = status['guider_x_exposure'],
                                                Y_EXP = status['guider_y_exposure'],
                                                X_RA_POS = status['guider_x_ra_pos'],
                                                X_RA_OPT_OFF = status['guider_y_ra_pos'],
                                                Y_RA_OPT_OFF = status['guider_x_opt_offset'],
                                                X_RA_MECH_OFF = status['guider_y_opt_offset'],
                                                XCORR = status['guider_x_correction'],
                                                YCORR = status['guider_y_correction'],
                                                RELAY_STATE = status['guider_relay_state'],
                                                SUN_VIS = status['guider_sun_vis'],
                                                MESSAGE = status['guider_message']))
>>>>>>> 7fdc453eb9f65a463f1c7f25dad89c269fb4ea8a
        connection.close()







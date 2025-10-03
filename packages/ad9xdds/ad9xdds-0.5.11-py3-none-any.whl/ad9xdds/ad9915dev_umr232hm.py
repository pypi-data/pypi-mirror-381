# -*- coding: utf-8 -*-

"""package ad9xdds
author    Benoit Dubois
copyright FEMTO ENGINEERING, 2020-2025
license   GPL v3.0+
brief     API to control AD9915 DDS development board through USB to SPI
          adapter.
details   AD9915 development board is configurable by USB through
          FTDI 232H device, an USB to SPI transceiver. Class allows
          configuration of principle DDS parameters (frequency, phase,
          amplitude, PLL handling, output handling...).


Warning: correct installation of pyftdi also need to create a udev
configuration file:
- get it at https://eblot.github.io/pyftdi/installation.html
or
- use script install.sh available in archive firm_manager.tar.gz in the 'data'
directory of this package.


To connect to FTDI device use URL scheme defined as:
    ftdi://[vendor][:[product][:serial|:bus:address|:index]]/interface
With FTDI 232H device:
    ftdi://ftdi:232h:[:serial|:bus:address|:index]]/1
!! Warning !! bus and address must be in hexadecimal


FTDI UMR232H cable connection:
    UMR232H                              AD9915 Dev Board (P101)
    Black (GND)    <------------------>  GND
    Brown (CS0)    <------------------>  MPI00 (CSB)
    Orange (SCLK)  <------------------>  MPI01 (SCLK)
    Yellow (MOSI)  <------------------>  MPI02 (SDIO)
    Green (MISO)   <------------------>  MPI03 (SDO)
    Grey (GPIO4)   <------------------>  IO_UPDATE (GPLIO0)
    Purple (GPIO5) <------------------>  RESET_BUFF (GPLIO1)

    Profile selection (currently not implemented (P102))
    PS0-BUF <---> GND
    PS1-BUF <---> GND
    PS2-BUF <---> GND

Configuration of AD9915 Dev Board jumpers:
    Disable USB communication
    P203 <---> Vcc (Disable)
    P204 <---> Vcc (Disable)
    P205 <---> Vcc (Disable)

    Set serial programming mode (P101) (Datasheet AD9915 p.28):
    IOCFG3       <---> GND
    IOCFG2       <---> GND
    IOCFG1       <---> GND
    IOCFG0       <---> Vdd

    Others jumpers configuration (P101)
    SYNC_IO_BUFF <---> GND  (Disable I/O reset)

    Others jumpers configuration (P102)
    EXTPDCTL-BUF <---> GND
    RESET-BUF    <---> OPEN
    DROVR-BUF    <---> GND
    DRHOLD-BUF   <---> GND
    DRCTL-BUF    <---> GND

WARNING: To avoid problems when disconnecting the ftdi cable from USB port,
you need to add 100 kOhms pull down resistor to IOUPDATE-BUFF and RESET-BUF
lines. For the IOUPDATE-BUFF line you can add the resitor on R136B pads or
directly behind the P101 connector. For the RESET-BUF line add the resistor
directly behind the P101 connector or use a "resistor jumper" on the P102/P100
connector.
"""

import logging
import time
import fractions
from decimal import Decimal
import pyftdi.ftdi as ftdi
import pyftdi.spi as spi
from ad9xdds import InvalidState, ConnectionError, bound_value

DEBUG = False

SPI_CLOCK_FREQUENCY = 100000
SPI_MODE = 0

IFMAX = 2500000000    # Input maximum frequency (Hz)
FTW_SIZE = 32         # Frequency Tuning Word register size (bit)
PHASE_SIZE = 16       # Phase register size (bit)
DAC_OUT_SIZE = 12     # Output DAC resolution (bit)
AMAX = (1 << DAC_OUT_SIZE) - 1  # Output maximum amplitude (a.u.)

REGNAME2ADDR = {'CFR1': 0x0, 'CFR2': 0x1, 'CFR3': 0x2, 'CFR4': 0x3,
                'DigRampLowerLimit': 0x4, 'DigRampUpperLimit': 0x5,
                'RisingDigRampStepSize': 0x6, 'FallingDigRampStepSize': 0x7,
                'DigRampRate': 0x8,
                'LowerFreqJump': 0x9, 'UpperFreqJump': 0xA,
                'P0Ftw': 0xB, 'P0PhaseAmp': 0xC,
                'P1Ftw': 0xD, 'P1PhaseAmp': 0xE,
                'P2Ftw': 0xF, 'P2PhaseAmp': 0x10,
                'P3Ftw': 0x11, 'P3PhaseAmp': 0x12,
                'P4Ftw': 0x13, 'P4PhaseAmp': 0x14,
                'P5Ftw': 0x15, 'P5PhaseAmp': 0x16,
                'P6Ftw': 0x17, 'P6PhaseAmp': 0x18,
                'P7Ftw': 0x19, 'P7PhaseAmp': 0x1A,
                'USR0': 0x1B}

OPMODE = {'profile': 0,  # single tone or modulation
          'drg' : 1 ,
          'parallel': 2,
          'modulus': 3}

CFR1 = {'OSK_EN': 8}

CFR2 = {'PROFILE_EN': 23,
        'PARALLEL_EN': 22,
        'DRG_EN': 19,
        'MODULUS_EN': 16}

MAX_REQUEST = 10


# =============================================================================
def get_interfaces(pid=0x0403, vid=0x6014):
    """Get available interface of UMR232 FTDI devices.
    Return a list of UsbDeviceDescriptor, a named tuple with the following
    fields: vid, pid, bus, address, sn, index, description'.
    :returns: list of UsbDeviceDescriptor (list of NamedTuple)
    """
    interfaces = ftdi.Ftdi().find_all([(pid, vid),])
    return [interface[0] for interface in interfaces]


# =============================================================================
class Ad9915Dev():
    """Class representing AD9915 development board through USB to SPI adapter.
    Currently class use profile mode P0 only
    """

    def __init__(self, ifreq=IFMAX):
        """The constructor.
        :param ifreq: Current input frequency in Hz (float)
        :returns: None
        """
        self._url = None
        # Init properties related to FTDI device
        self._ctrl = None  # SPI controller
        self._spi = None  # SPI bus
        self._gpio = None  # Others signals needed to handle DDS
        # Init class properties
        self._ifreq = ifreq
        self._profile = 0
        self._ofreq = None
        self._phy = None
        self._amp = None
        self._pll_factor = None
        self._opmode = None

    def __del__(self):
        if self._ctrl is None:
            return
        if self.is_connected() is True:
            self.disconnect()
        if self._ctrl is not None:
            self._ctrl.terminate()

    def connect(self, url):
        """Connection process.
        :param url: FTDI url like 'ftdi://ftdi:232h:FT0GPCDF/0' (str)
        :returns: None
        """
        if self._url is None and url is None:
            logging.error("No device defined before connection")
            return
        self._url = url
        self._ctrl = spi.SpiController()
        self._ctrl.configure(self._url, debug=DEBUG)
        self._spi = self._ctrl.get_port(cs=0)
        self._spi.set_frequency(SPI_CLOCK_FREQUENCY)
        self._spi.set_mode(SPI_MODE)
        self._gpio = self._ctrl.get_gpio()
        ## GPIOL0 (b4) and GPIOL1 (b5) are outputs (='1')
        ## GPIOL0 is IO_UPDATE and GPIOL1 is MASTER_RESET
        self._gpio.set_direction(0x30, 0x30)
        ## Init IO_update and reset lines to 0
        self._gpio.write(0x00)
        # Configure/Init DDS device
        ## Reset: needed at power-up (see datasheet p.40)
        self._master_reset()
        ## Default + SDIO input only + POWERDOWN DIGITAL, DAC and REFCLK part
        self.set_reg_w8(REGNAME2ADDR['CFR1'], [0x00, 0x01, 0x00, 0xEA])
        ## Default + SDIO input only + POWERUP DIGITAL, DAC and REFCLK part
        self.set_reg_w8(REGNAME2ADDR['CFR1'], [0x00, 0x01, 0x00, 0x0A])
        ## Default + Enable profile mode
        self.set_reg_w8(REGNAME2ADDR['CFR2'], [0x00, 0x80, 0x09, 0x00])
        ## DAC cal: needed at power-up (see datasheet p.40)
        self.dac_calibration()
        self._get_dds_parameters()
        return True

    def disconnect(self):
        """Disconnect from FTDI device.
        :returns: None
        """
        if self._ctrl is not None:
            if not self._ctrl.ftdi.is_connected:
                return
            self._ctrl.ftdi.close()

    def is_connected(self):
        """Return True if interface to DDS board is ready else return False.
        """
        if self._ctrl is not None:
            if self._ctrl.ftdi.is_connected:
                return True
        return False

    def _get_dds_parameters(self):
        """Get parameters from DDS.
        """
        # !warning! parameter order initialisation is important
        '''
        if self._pll_state is None:
            self._pll_state = self.get_pll_state()
        else:
            self.set_pll_state(self._pll_state)
        if self._pll_doubler_state is None:
            self._pll_doubler_state = self.get_pll_doubler_state()
        else:
            self.set_pll_doubler_state(self._pll_doubler_state)
        if self._pll_factor is None:
            self._pll_factor = self.get_pll_multiplier_factor()
        else:
            self.set_pll_multiplier_factor(self._pll_factor)
        '''
        if self._ofreq is None:
            self._ofreq = self.get_ofreq()
        else:
            self.set_ofreq(self._ofreq)
        if self._phy is None:
            self._phy = self.get_phy()
        else:
            self.set_phy(self._phy)
        if self._amp is None:
            self._amp = self.get_amp()
        else:
            self.set_amp(self._amp)
        if self._opmode is None:
            try:
                self._opmode = self.get_operation_mode()
            except InvalidState as ex:
                self.set_operation_mode(OPMODE['modulus'])
                logging.error("No default operation mode defined, set modulus mode")
        else:
            self.set_operation_mode(self._opmode)

    def get_reg_w8(self, address, length=4):
        """Get value of a register in 8 bits word size.
        :param address: register address (int)
        :param length: size of register in byte (int)
        :returns: register value in 8 bits word size (list of int)
        """
        msg = [0x80 + address]
        self._spi.write(msg, stop=False)
        self._io_update()
        retval = self._spi.read(length, start=False)
        return list(retval)

    def set_reg_w8(self, address, values, length=4):
        """Set value of a register in 8 bits word size.
        :param address: register address (int)
        :param value: register value list to set (list of int)
        :param length: size of register in byte (int)
        :returns: None
        """
        msg = [address]
        for value in values:
            msg.append(value)
        request = 0
        while request <= MAX_REQUEST:
            self._spi.write(out=msg, stop=False)
            self._io_update()
            self._spi.write(out=[], stop=True)
            reg_value = list(self.get_reg_w8(address, length))
            if reg_value == values:
                return
            else:
                logging.error("set_reg_w8 address %r to %r error (get %r), attempt %r",
                              address, values, reg_value, request)
                request += 1
        raise ConnectionError("Could not set register {}".format(address))

    def get_reg(self, address, length=4):
        """Get register value.
        :param address: register address (int)
        :param length: size of register in byte (int)
        :returns: register value (int)
        """
        reg_value = self.get_reg_w8(address, length)
        retval = 0
        for i, val in enumerate(reg_value):
            retval += val << (8*(len(reg_value)-i-1))
        return retval

    def set_reg(self, address, value, length=4):
        """Set register value.
        :param address: register address (int)
        :param value: register value to set (int)
        :param length: size of register in byte (int)
        :returns: None
        """
        values = []
        for i in range(length-1, -1, -1):
            values.append((value >> (i * 8)) & 0xff)
        self.set_reg_w8(address, values)

    def get_reg_bit(self, address, idx):
        """Get value of a specific bit of a register.
        :param address: register address (int)
        :param idx: index position of bit to read (int)
        :returns: bit value, i.e. 0 or 1 (int)
        """
        reg_value = self.get_reg(address)
        return self.get_bit_value(reg_value, idx)

    def set_reg_bit(self, address, idx, value):
        """Set value of a specific bit of a register.
        :param address: register address (int)
        :param idx: index position of bit to read (int)
        :param value: bit value, i.e. 0 or 1 (int)
        :returns: None
        """
        reg_value = self.get_reg(address)
        # If bit value already set, stop update
        if self.get_bit_value(reg_value, idx) == value:
            return
        mask = 1 << idx
        self.set_reg(address, self.set_bit_value(reg_value, idx, value))

    @staticmethod
    def get_bit_value(n, idx):
        """Get value of a specific bit 'idx' in integer 'n'.
        :param n: integer under test  (int)
        :param idx: index position of bit to read (int)
        :returns: bit value, i.e. 0 or 1 (int)
        """
        return (n >> idx) & 1

    @staticmethod
    def set_bit_value(n, idx, value):
        """Set value 'value' of a specific bit 'idx' in integer 'n'.
        :param n: integer under test  (int)
        :param idx: index position of bit to read (int)
        :param value: bit value, i.e. 0 or 1 (int)
        :returns: integer 'n' updated (int)
        """
        mask = 1 << idx
        if value == 0:
            return n & ~mask
        else:
            return n | mask

    def dac_calibration(self):
        """DAC calibration, needed after each power-up and every time REF CLK or
        the internal system clock is changed.
        :returns: None
        """
        # Calibration 1/2: enable
        self.set_reg_w8(REGNAME2ADDR['CFR4'], [0x01, 0x05, 0x21, 0x20])
        # Wait for calibration (max calibration time is 188 us)
        time.sleep(0.001)
        # Calibration 2/2: disable
        self.set_reg_w8(REGNAME2ADDR['CFR4'], [0x00, 0x05, 0x21, 0x20])

    def set_profile(self, profile):
        """Set profile currently in use. Curently not implemented.
        :param profile: Select profile in use between 0 to 7 (int)
        :returns: None
        """
        if profile not in range(0, 8):
            raise ValueError("Profile must be in range 0 to 7, here: ",
                             profile)
        ## self._profile = profile

    def get_profile(self):
        """Get profile currently in use. Curently not implemented.
        :returns: profile currently in use (int)
        """
        return self._profile

    def set_operation_mode(self, mode: int) -> None:
        """Configure operation mode from:
        - Single tone (0)
        - Profile modulation (1)
        - Digital ramp modulation (linear sweep) (2) (not implemented)
        - Parallel data port modulation (3) (not implemented)
        - Programmable modulus mode (4)
        :param mode: index of operation mode (int)
        :returns: None
        """
        if mode == OPMODE['profile']:
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['MODULUS_EN'], 0)
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['PROFILE_EN'], 1)
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['DRG_EN'], 0)
            self.set_reg_bit(REGNAME2ADDR['CFR1'], CFR1['OSK_EN'], 1)
        elif mode == OPMODE['drg']:
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['MODULUS_EN'], 0)
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['DRG_EN'], 1)
            self.set_reg_bit(REGNAME2ADDR['CFR1'], CFR1['OSK_EN'], 1)
        elif mode == OPMODE['parallel']:
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['PARALLEL_EN'], 1)
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['MODULUS_EN'], 0)
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['PROFILE_EN'], 0)
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['DRG_EN'], 0)
            self.set_reg_bit(REGNAME2ADDR['CFR1'], CFR1['OSK_EN'], 0)
        elif mode == OPMODE['modulus']:
            # Enable modulus mode bit
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['MODULUS_EN'], 1)
            # Enable digital ramp modulation mode bit
            self.set_reg_bit(REGNAME2ADDR['CFR2'], CFR2['DRG_EN'], 1)
            # Enable OSK
            self.set_reg_bit(REGNAME2ADDR['CFR1'], CFR1['OSK_EN'], 1)
        else:
            pass
        self._opmode = mode

    def get_operation_mode(self) -> int:
        """Get operation mode status.
        :returns: operation mode (int)
        """
        paren = self.get_reg_bit(REGNAME2ADDR['CFR2'], CFR2['PARALLEL_EN'])
        moden = self.get_reg_bit(REGNAME2ADDR['CFR2'], CFR2['MODULUS_EN'])
        profen = self.get_reg_bit(REGNAME2ADDR['CFR2'], CFR2['PROFILE_EN'])
        drgen = self.get_reg_bit(REGNAME2ADDR['CFR2'], CFR2['DRG_EN'])
        osken = self.get_reg_bit(REGNAME2ADDR['CFR1'], CFR1['OSK_EN'])
        opmode_reg = f"{paren}{moden}{profen}{drgen}{osken}"
        match opmode_reg:
            case "00101" | "10101":
                opmode = OPMODE['profile']
            case "00011" | "00111" | "10011" | "10111":
                opmode = OPMODE['drg']
            case "10000":
                opmode = OPMODE['parallel']
            case "01011" | "01111" | "11011" | "11111":
                opmode = OPMODE['modulus']
            case _:
                raise InvalidState("Operation mode undefined")
        self._opmode = opmode
        return opmode

    #############################################################################
    # BEGIN SysFreq handling
    #############################################################################
    def set_ifreq(self, value):
        """Set input frequency.
        :param value: Input frequency value (float)
        :returns: None
        """
        value = float(value)
        self._ifreq = value
        self.dac_calibration()  # Needed!
        logging.debug("Set input frequency: %r", value)
        # Update DDS output frequency because ofreq = f(ifreq)
        self.set_ofreq(self._ofreq)
        return value

    def get_ifreq(self):
        """Get input frequency.
        :returns: Current input frequency value (float)
        """
        return self._ifreq

    def get_sysfreq(self):
        """Get system frequency.
        Currently, does not support PLL.
        :returns: Current system frequency value (float)
        """
        if self.get_pll_state() is True:
            # Input stage
            doubler_state = self.get_input_doubler_state()
            if doubler_state is None:
                raise InvalidState("Input doubler state undefined")
            if doubler_state is True:
                pll_input_frequency = self._ifreq * 2
            else:
                idf = self.get_input_divider_factor()
                if idf is None:
                    raise InvalidState("Input divider factor undefined")
                pll_input_frequency= self._ifreq / idf
            # PLL stage
            pmf = self.get_pll_multiplier_factor()
            if pmf is None:
                raise InvalidState("PLL multiplier factor undefined")
            sysfreq = pll_input_frequency * 2 * pmf
        else:  # PLL bypassed
            sysfreq = self._ifreq
        logging.debug("Get system frequency: %r", sysfreq)
        return sysfreq

    def set_input_divider_factor(self, value):
        """Set input divider value.
        :param factor: factor value of input divider (1, 2, 4 or 8) (int)
        :returns: None
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if value not in (1, 2, 4, 8):
            logging.error("Input divider value out of range: %r", value)
            return None
        match (value):
            case 1:
                self.set_reg_bit(REGNAME2ADDR['CFR3'], 21, 0)
                self.set_reg_bit(REGNAME2ADDR['CFR3'], 20, 0)
            case 2:
                self.set_reg_bit(REGNAME2ADDR['CFR3'], 21, 0)
                self.set_reg_bit(REGNAME2ADDR['CFR3'], 20, 1)
            case 4:
                self.set_reg_bit(REGNAME2ADDR['CFR3'], 21, 1)
                self.set_reg_bit(REGNAME2ADDR['CFR3'], 20, 0)
            case 8:
                self.set_reg_bit(REGNAME2ADDR['CFR3'], 21, 1)
                self.set_reg_bit(REGNAME2ADDR['CFR3'], 20, 1)
        logging.debug("Set input divider factor: %r", value)
        return value

    def get_input_divider_factor(self):
        """Get input divider factor.
        :returns: factor value of input divider (1, 2, 4 or 8) (int)
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        idf_msb = self.get_reg_bit(REGNAME2ADDR['CFR3'], 21)
        idf_lsb = self.get_reg_bit(REGNAME2ADDR['CFR3'], 20)
        match (idf_msb, idf_lsb):
            case (0, 0):
                current_value = 1
            case (0, 1):
                current_value = 2
            case (1, 0):
                current_value = 4
            case (1, 1):
                current_value = 8
            case _:
                raise InvalidState("Input divider factor undefined")
        return current_value

    def set_input_doubler_state(self, value: bool):
        """Set input doubler state.
        :param value: input doubler state (boolean)
        :returns: None
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if value is True:
            self.set_reg_bit(REGNAME2ADDR['CFR3'], 16, 1)
            self.set_reg_bit(REGNAME2ADDR['CFR3'], 19, 1)
        else:
            self.set_reg_bit(REGNAME2ADDR['CFR3'], 16, 0)
            self.set_reg_bit(REGNAME2ADDR['CFR3'], 19, 0)
        logging.debug("Set input doubler state: %r", value)
        return value

    def get_input_doubler_state(self):
        """Get input doubler state.
        :returns: input doubler state (boolean)
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        doubler_clock_edge = self.get_reg_bit(REGNAME2ADDR['CFR3'], 16)
        doubler_enable = self.get_reg_bit(REGNAME2ADDR['CFR3'], 19)
        return True if doubler_clock_edge == 1 and doubler_enable == 1 else False

    def set_pll_state(self, state=False):
        """Set PLL state.
        Note: A modification of the PLL state modify the output frequency.
        After changing the PLL state, you must calibrate the VCO
        :param state: - False  Disable PLL. (bool)
                      - True   Enable PLL.
        :returns: None
        """
        # reg_value = self.get_reg(REGNAME2ADDR['CFR3'])
        pll_state_bit = 18  #2
        # if state is True:
        #     reg_value |= 1 << pll_state_bit
        # else:
        #     reg_value &= ~(1 << pll_state_bit)
        # self.set_reg(REGNAME2ADDR['CFR3'], reg_value)
        self.set_reg_bit(REGNAME2ADDR['CFR3'], pll_state_bit, state)

    def get_pll_state(self):
        """Get PLL state.
        :returns: PLL state (bool)
        """
        reg_value = self.get_reg(REGNAME2ADDR['CFR3'])
        pll_state_bit = 18  #2
        return self._check_bit_set(reg_value, pll_state_bit)

    def is_pll_locked(self):
        """Return the internal PLL lock (to the REF CLK input signal) state.
        :returns: True if the internal PLL is locked else return False (bool)
        """
        reg_value = self.get_reg(REGNAME2ADDR['USR0'])
        pll_lock_bit = 24
        return self._check_bit_set(reg_value, pll_lock_bit)

    def set_pll_multiplier_factor(self, value):
        """Set PLL feedback multipler value.
        Note that here we set only the multipler factor. The overall multiplier
        value in the SysClk PLL multipler block is the double due to the by 2
        prescaler block
        :param value: PLL multipler value (between 10 to 255) (int)
        :returns: None
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if not 10 <= value <= 255:
            logging.error("PLL multipler factor value out of range: %r", value)
            value = bound_value(value, 10, 255)
        cfr3 = self.get_reg_w8(address=REGNAME2ADDR['CFR3'])
        cfr3[2] = value
        self.set_reg_w8(REGNAME2ADDR['CFR3'], cfr3)
        if self.get_reg_w8(address=REGNAME2ADDR['CFR3'])[2] != value:
            raise InvalidState("PLL multiplier factor setting failed.")
        # self._pll_factor = value
        logging.debug("Set PLL multiplier factor: %r", value)
        return value

    def get_pll_multiplier_factor(self):
        """Get SysClk PLL multipler factor.
        Note that here we get only the multipler factor. The overall multiplier
        value in the SysClk PLL multipler block is the double due to the by 2
        prescaler block
        :returns: PLL multipler value (between 10 to 255) (int)
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        pll_multipler_value = self.get_reg_w8(address=REGNAME2ADDR['CFR3'])[2]
        return pll_multipler_value

    def set_cp_current(self, value=0):
        """Set charge pump current value.
        :param value: charge pump current: - 0: 250 uA
                                           - 1: 375 uA
                                           - 2: off
                                           - 3: 125 uA
        :returns: None
        """
        raise NotImplementedError

    def get_cp_current(self):
        """Get charge pump current configuration value.
        Charge pump current: - 0: 250 uA
                             - 1: 375 uA
                             - 2: off
                             - 3: 125 uA
        :returns: charge pump current (int)
        """
        raise NotImplementedError

    def vco_calibration(self):
        """VCO calibration process.
        Include auto selection of charge pump current value.
        :returns: State of PLL (i.e. PLL is locked?) (bool)
        """
        # Reset bit before another VCO calibration
        self.set_reg_bit(REGNAME2ADDR['CFR1'], 24, 0)
        # Initialize VCO calibration
        self.set_reg_bit(REGNAME2ADDR['CFR1'], 24, 1)
        # Check PLL state
        return True if self.get_reg_bit(REGNAME2ADDR['USR0'], 24) == 1 else False



    #############################################################################
    # END SysFreq handling
    #############################################################################

    @staticmethod
    def compute_modulus_parameters(ifreq, ofreq):
        """Compute modulus parameters values given ifreq and ofreq values.
        Even if input parameters can be of float type, input parameters
        are preferably of string type to avoid casting rounding error.
        Return FTW, A and B parameters.
        :param ifreq: Input frequency value (str).
        :param ofreq: Output frequency value (str).
        :returns: FTW, A and B parameters (int, int, int)
        """
        ifreq = fractions.Fraction(ifreq)
        ofreq = fractions.Fraction(ofreq)
        (m, n) = fractions.Fraction(ofreq, ifreq).as_integer_ratio()
        ftw = int(m * 2**32 / n)
        y = 2**32 * m - ftw * n
        (a, b) = fractions.Fraction(y, n).as_integer_ratio()
        return ftw, a, b

    def set_ofreq_fine(self, value):
        """Set output frequency using modulus operation mode of DDS.
        Note: Do not forget to set operation mode to 'modulus'.
        Even if input parameters can be of float type, input parameters
        are preferably of string type to avoid casting rounding error.
        Returns output frequency.
        :param value: Output frequency value (str).
        :returns: Actual output frequency (float)
        # """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        ifreq = Decimal(self.get_sysfreq())
        ofreq = Decimal(value)
        ftw, a, b = self.compute_modulus_parameters(ifreq, ofreq)
        self.set_reg(0x04, ftw)
        self.set_reg(0x06, a)
        self.set_reg(0x05, b)
        self._ofreq = self._actual_ofreq_fine(ifreq, ftw, a, b)
        logging.debug("Set fine output frequency: %r", self._ofreq)
        return self._ofreq

    def get_ofreq_fine(self):
        ifreq = self.get_sysfreq()
        ftw = self.get_reg(0x04)
        a = self.get_reg(0x06)
        b = self.get_reg(0x05)
        self._ofreq = self._actual_ofreq_fine(ifreq, ftw, a, b)
        return self._ofreq

    def set_ofreq(self, value, profile=None):
        """Set output frequency to current DDS profile if profile parameter is
        None or set output frequency of requested DDS profile.
        Return the actual output frequency (see _actual_ofreq() method).
        :param value: Output frequency value (float).
        :param profile: Profile to update between 0 to 7 (int)
        :returns: Actual output frequency (float)
        """
        if self._opmode == OPMODE['modulus']:
            return self.set_ofreq_fine(value)

        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if profile not in range(0, 8) and profile is not None:
            raise ValueError("Profile not in range 0 to 7, here:", profile)
        if profile is None:
            profile = 0
        ofreq = float(value)
        regname = 'P{:d}Ftw'.format(profile)
        ftw = int((ofreq * (1 << FTW_SIZE)) / self.get_sysfreq())
        self.set_reg(REGNAME2ADDR[regname], ftw)
        self._ofreq = self._actual_ofreq(self.get_sysfreq(), ftw, FTW_SIZE)
        logging.debug("Set output frequency: %r", self._ofreq)
        return self._ofreq

    def get_ofreq(self, profile=None):
        """Get output frequency of current DDS profile if profile parameter is
        None or return output frequency of requested DDS profile.
        :param profile: Profile output frequency requested (int)
        :returns: Output frequency of DDS profile (float).
        """
        if self._opmode == OPMODE['modulus']:
            return self.get_ofreq_fine()

        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if profile not in range(0, 8) and profile is not None:
            raise ValueError("Profile not in range 0 to 7, here:", profile)
        if profile is None:
            profile = 0
        regname = 'P{:d}Ftw'.format(profile)
        ftw = self.get_reg(REGNAME2ADDR[regname])
        self._ofreq = self._actual_ofreq(self.get_sysfreq(), ftw, FTW_SIZE)
        return self._ofreq

    def set_phy(self, value, profile=None):
        """Set phase of output signal on DDS.
        Take the queried output phase (in degree) as argument and set
        the adequat register in the DDS.
        :param value: Output phase value (float).
        :param profile: Profile to update between 0 to 7 (int)
        :returns: Actual output phase (float)
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if profile not in range(0, 8) and profile is not None:
            raise ValueError("Profile not in range 0 to 7, here:", profile)
        if profile is None:
            profile = 0
        value = float(value)
        regname = 'P{:d}PhaseAmp'.format(profile)
        # Phase and amplitude output is handled by a common register.
        # Before writing new phase, we need to get current amplitude
        # and take care to not reset its value.
        reg_value = self.get_reg_w8(REGNAME2ADDR[regname])
        asf_list = reg_value[2:]
        phy = int((value * (1 << PHASE_SIZE)) / 360)
        phy_list = self._int_2_byte_list(phy, 2)
        msg = asf_list + phy_list
        self.set_reg_w8(REGNAME2ADDR[regname], msg)
        phy = self._actual_phy(phy, PHASE_SIZE)  # Return the actual phase
        logging.debug("Set phase: %r", phy)
        return phy

    def get_phy(self, profile=None):
        """Get output phase of profile..
        :param profile: Profile phase requested (int)
        :returns: Output phase of DDS (float).
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if profile not in range(0, 8) and profile is not None:
            raise ValueError("Profile not in range 0 to 7, here:", profile)
        if profile is None:
            profile = 0
        regname = 'P{:d}PhaseAmp'.format(profile)
        reg_value = self.get_reg_w8(REGNAME2ADDR[regname])
        # Extract phase value from register value.
        phy = (reg_value[2] << 8) + reg_value[3]
        return self._actual_phy(phy, PHASE_SIZE)  # return the actual phase.

    def set_amp(self, value, profile=None):
        """Set amplitude tuning word of output signal on DDS.
        Take the input and output frequency as argument and set the adequat
        register in the DDS.
        :param value: Output amplitude value (int)
        :param profile: Profile to update between 0 to 7 (int)
        :returns: fsc register value if transfert is ok (int)
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if profile not in range(0, 8) and profile is not None:
            raise ValueError("Profile not in range 0 to 7, here:", profile)
        if profile is None:
            profile = 0
        value = int(float(value))
        # If value is out of range, bound value and raise Warning.
        if not 0 <= value <= AMAX:
            logging.warning("Amplitude value out of range: %r", value)
            value = bound_value(value, 0, AMAX)
        regname = 'P{:d}PhaseAmp'.format(profile)
        # Phase and amplitude output is handled by a common register.
        # Before writing new amplitude, we need to get current phase
        # and take care to not reset its value.
        reg_value = list(self.get_reg_w8(REGNAME2ADDR[regname]))
        phy_list = reg_value[:2]
        asf_list = self._int_2_byte_list(value, 2)
        msg = asf_list + phy_list
        self.set_reg_w8(REGNAME2ADDR[regname], msg)
        logging.debug("Set output amplitude: %r", value)
        return value

    def get_amp(self, profile=None):
        """Get output amplitude tuning word of DDS.
        :param profile: Profile phase requested (int)
        :returns:  Output amplitude tuning of DDS (float).
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        if profile not in range(0, 8) and profile is not None:
            raise ValueError("Profile not in range 0 to 7, here:", profile)
        if profile is None:
            profile = 0
        regname = 'P{:d}PhaseAmp'.format(profile)
        reg_value = self.get_reg_w8(REGNAME2ADDR[regname])
        # Extract amplitude value from register value.
        asf = (reg_value[0] << 8) + reg_value[1]
        return asf

    def set_output_state(self, state=False):
        """Set output state.
        :param state: - False  Disable output. (bool)
                      - True   Enable CMOS output.
        :returns: None
        """
        raise NotImplementedError

    def get_output_state(self):
        """Get output state.
        :returns: Output state (bool)
        """
        reg_value = self.get_reg(REGNAME2ADDR['CFR1'])
        output_state_bit = 16
        return self._check_bit_set(reg_value, output_state_bit)

    @staticmethod
    def _actual_ofreq(ifreq, ftw, rsize):
        """Return the actual output frequency.
        Due to the resolution of the DDS, the actual output frequency
        may be (a bit) different than the queried.
        :param ifreq: Intput frequency value (float).
        :param ftw: Frequency Tuning Word register value (int).
        :param rsize: Size of register (int).
        :returns: Actual output frequency (float).
        """
        return (ftw * ifreq) / (1 << rsize)

    @staticmethod
    def _actual_ofreq_fine(ifreq, ftw, a, b):
        """Return the actual output frequency.
        Due to the resolution of the DDS, the actual output frequency
        may be (a bit) different than the queried.
        :param ifreq: Intput frequency value (float).
        :param ftw: Frequency Tuning Word register value (int).
        :param a: Modulus parameter (int).
        :param b: Modulus parameter (int).
        :returns: Actual output frequency (float).
        """
        return Decimal(ifreq) * (Decimal(ftw) + Decimal(a)/Decimal(b))/2**32

    @staticmethod
    def _actual_phy(dphy, bit):
        """Return the actual output phase.
        Due to the resolution of the DDS, the actual output phase
        may be (a bit) different than the queried.
        :param dphy: Phase register value (int).
        :param bit: Number of bits used for the phase resolution (int)
        :returns: Actual output phase offset in degree (float).
        """
        return float(360 * dphy) / (1 << bit)

    @staticmethod
    def _int_2_byte_list(value, size):
        """Take an integer and split it in a list of the corresponding
        'size' 8 bits word (byte).
        For example:
            17179869 in hexadecimal = 0x10624dd
            0x10624dd splitted in byte = [0x01, 0x06, 0x24, 0xdd]
            [0x01, 0x06, 0x24, 0xdd] in base 10 = [1, 6, 36, 221]
            => _int_2_byte_list(17179869, 4) = [1, 6, 36, 221]
        :param value: an integer to split (int)
        ;param size: sier of output list (int)
        :returns: list of byte (list of int)
        """
        value_format = '0{:d}x'.format(size * 2)
        value = format(value, value_format)
        return [int(value[i:i+2], 16) for i in range(0, size*2, 2)]


    @staticmethod
    def _check_bit_set(word, n):
        """Check if n-th bit of word is set or not.
        :param word: word to check (int)
        :param n: n-th bit of work to check (int)
        :returns: True is n-th bit is set else False (bool)
        """
        if word & (1 << n):
            return True
        return False

    def _io_update(self):
        """Generate IO update event: transfer written data from I/O buffer to
        the coresponding internal registers.
        :returns: None
        """
        self._gpio.write(0x10)
        time.sleep(0.001)
        self._gpio.write(0x0)

    def _master_reset(self):
        """Master reset: clears all memory elements and sets registers to
        default values. Required after power up.
        :returns: None
        """
        self._gpio.write(0x20)
        time.sleep(int(1 / (1000 * SPI_CLOCK_FREQUENCY)))
        self._gpio.write(0x0)


# =============================================================================
if __name__ == '__main__':
    """Basic hardware test.
    """
    LOG_FORMAT = '%(asctime)s %(levelname)s %(filename)s (%(lineno)d): ' \
        + '%(message)s'
    logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

    pylogger = logging.getLogger('pyftdi')
    pylogger.setLevel(logging.INFO)

    # List FTDI URL but exit imediately after:
    #print(spi.SpiController().configure('ftdi:///?'))

    devices = get_interfaces(0x0403, 0x6010)
    for dev in devices:
        print("{}, SN: {}, bus: {}, address:{}". \
              format(dev.description, dev.sn, dev.bus, hex(dev.address)))

    IFREQ = 0.5e9
    OFREQ = IFREQ * 0.1
    PHY = 0
    AMP = 4095

    DDS = Ad9915Dev()

    DDS.connect(url='ftdi://ftdi:232h/1')

    DDS.set_ifreq(IFREQ)

    DDS.set_phy(PHY)
    print("Get phase", DDS.get_phy())

    DDS.set_amp(AMP)
    print("Get amplitude", DDS.get_amp())

    DDS.set_ofreq(OFREQ)
    print("Get output frequency", DDS.get_ofreq())

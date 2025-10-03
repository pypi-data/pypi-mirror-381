# -*- coding: utf-8 -*-

"""package ad9xdds
author    Benoit Dubois
copyright FEMTO ENGINEERING, 2021-2025
license   GPL v3.0+
brief     Emulation of basic DDS board AD9912Dev
"""

import logging
import inspect
import signalslot as ss
from ad9xdds import InvalidState
from ad9xdds.dds_core import AbstractDds

AD_VENDOR_ID = 0x0456
AD9912DEV_PRODUCT_ID = 0xee09
AD9549DEV_PRODUCT_ID = 0xee08
DDS_DEVICE_LIST = {'AD9912': 'Ad9912Dev', 'AD9915': 'Ad9915DevUmr232Hm'}


# =============================================================================
class Ad9912Emul(AbstractDds):
    """Class 'emulating' the AD9912 DDS development board.
    Used for test when no real device is available.
    """

    FTW_SIZE = 48               # Frequency Tuning Word register size (bit)
    PHASE_SIZE = 14             # Phase register size (bit)
    DAC_OUT_SIZE = 10           # Output DAC resolution (bit)
    IFMAX = 1000000000.0        # Input maximum frequency (Hz)
    OFMAX = 400000000.0         # Output maximum frequency (Hz)
    AMAX = (1 << DAC_OUT_SIZE) - 1

    def __init__(self, ifreq=IFMAX):
        super().__init__()
        self._ifreq = None
        self._ofreq = None
        self._phy = None
        self._amp = None
        self._is_connected = False
        logging.info("Init DDS test device: %r", self)

    def connect(self, vendor_id=None, product_id=None,
                bus=None, address=None):
        logging.info("Connect to DDS test device")
        self._is_connected = True
        return True

    def disconnect(self):
        logging.debug("Disconnection")

    def is_connected(self):
        return self._is_connected

    def set_ifreq(self, ifreq):
        logging.debug("DdsTestDev.set_ifreq(" + str(ifreq) + ")")
        self._ifreq = float(ifreq)
        return ifreq

    def get_ifreq(self):
        logging.debug("DdsTestDev.get_ifreq() = " + str(self._ifreq))
        return self._ifreq

    def set_ofreq(self, ofreq):
        logging.info("DdsTestDev.set_ofreq(" + str(ofreq) + ")")
        self._ofreq = float(ofreq)
        return ofreq

    def get_ofreq(self):
        logging.debug("DdsTestDev.get_ofreq() = %r", self._ofreq)
        return self._ofreq

    def set_phy(self, phy):
        logging.debug("DdsTestDev.set_phy(" + str(phy) + ")")
        self._phy = phy
        return phy

    def get_phy(self):
        logging.debug("DdsTestDev.get_phy() = " + str(self._phy))
        return self._phy

    def set_amp(self, fsc):
        logging.debug("DdsTestDev.set_amp(" + str(fsc) + ")")
        self._amp = fsc
        return fsc

    def get_amp(self):
        logging.debug("DdsTestDev.get_amp() = " + str(self._amp))
        return self._amp

    def set_hstl_output_state(self, state=False):
        logging.debug("Set HSTL output state to: " + str(state))

    def get_hstl_output_state(self):
        pass

    def set_cmos_output_state(self, state=False):
        logging.debug("Set CMOS output state to: " + str(state))

    def get_cmos_output_state(self):
        pass

    def set_pll_state(self, state=False):
        logging.debug("Set PLL state to: %s", str(state))

    def get_pll_state(self):
        pass

    def set_cp_current(self, value=0):
        logging.debug("Set charge pump current to: " + str(value))

    def get_cp_current(self):
        pass

    def set_vco_range(self, value=None):
        logging.debug("Set VCO range to: " + str(value))

    def get_vco_range(self):
        pass

    def set_hstl_doubler_state(self, flag=False):
        logging.debug("Set HSTL doubler state to: " + str(flag))

    def get_hstl_doubler_state(self):
        pass

    def set_pll_doubler_state(self, flag=False):
        logging.debug("Set PLL doubler state to: " + str(flag))

    def get_pll_doubler_state(self):
        pass

    def set_pll_multiplier_factor(self, factor):
        logging.debug("Set PLL multiplier factor to: " + str(factor))

    def get_pll_multiplier_factor(self):
        pass

    def set_led(self, flag=False):
        logging.debug("Set LED blink: " + str(flag))

    def set_reg(self, address, value):
        logging.debug("Set " + str(value) + " @adress " + str(address))

    def get_reg(self, address):
        logging.debug("Request value @adress " + str(address))


# =============================================================================
class SAd9912Emul(Ad9912Emul):
    """Class derived from Ad9912Emul class to add signal/slot facilities.
    """

    def __init__(self, **kwargs):
        self.ifreq_updated = ss.Signal(['value'])
        self.ofreq_updated = ss.Signal(['value'])
        self.phase_updated = ss.Signal(['value'])
        self.amp_updated = ss.Signal(['value'])
        self.pll_state_updated = ss.Signal(['flag'])
        self.pll_doubler_updated = ss.Signal(['flag'])
        self.pll_factor_updated = ss.Signal(['value'])
        super().__init__(**kwargs)

    def connect(self, **kwargs):
        return super().connect(**kwargs)

    def set_ifreq(self, value, **kwargs):
        super().set_ifreq(value)
        self.ifreq_updated.emit(value=value)

    def set_ofreq(self, value, **kwargs):
        aofreq = super().set_ofreq(value)
        self.ofreq_updated.emit(value=aofreq)
        return aofreq

    def set_phy(self, value, **kwargs):
        aphy = super().set_phy(value)
        self.phase_updated.emit(value=aphy)
        return aphy

    def set_amp(self, value, **kwargs):
        aamp = super().set_amp(value)
        self.amp_updated.emit(value=aamp)
        return aamp

    def set_pll_state(self, flag, **kwargs):
        super().set_pll_state(flag)
        self.pll_state_updated.emit(flag=flag)

    def set_pll_doubler_state(self, flag, **kwargs):
        super().set_pll_doubler_state(flag)
        self.pll_doubler_updated.emit(flag=flag)

    def set_pll_multiplier_factor(self, value, **kwargs):
        super().set_pll_multiplier_factor(value)
        self.pll_factor_updated.emit(value=value)


# =============================================================================
class Ad9915DevUmr232HmEmul():

    def __init__(self, ifreq=2500000000):
        """The constructor.
        :param ifreq: Current input frequency in Hz (float)
        :returns: None
        """
        self._ifreq = ifreq
        self._input_doubler_state = False
        self._input_divider_factor = 1
        self._pll_state = False
        self._pll_multiplier_factor = 20
        self._ofreq = 8e6
        self._phy = 0
        self._amp = 511
        self._profile = 0
        self._is_connected = False
        logging.debug("DdsTestDev.%r(%r) done", inspect.stack()[0][3], ifreq)

    def connect(self, url):
        """Connection process.
        :param url: FTDI url like 'ftdi://ftdi:232h:FT0GPCDF/0' (str)
        :returns: None
        """
        self._is_connected = True
        logging.debug("DdsTestDev.%r(%r)", inspect.stack()[0][3], url)

    def disconnect(self):
        self._is_connected = False
        logging.debug("DdsTestDev.%r()", inspect.stack()[0][3])

    def is_connected(self):
        """Return True if interface to DDS board is ready else return False.
        """
        logging.debug("DdsTestDev.%r()", inspect.stack()[0][3])
        if self.is_connected:
            return True
        return False

    def dac_calibration(self):
        """DAC calibration, needed after each power-up and every time REF CLK or
        the internal system clock is changed.
        :returns: None
        """
        logging.debug("DdsTestDev.%r()", inspect.stack()[0][3])

    def set_profile(self, profile):
        """Set profile currently in use. Curently not implemented.
        :param profile: Select profile in use between 0 to 7 (int)
        :returns: None
        """
        if profile not in range(0, 8):
            raise ValueError("Profile must be in range 0 to 7, here: %r",
                             profile)
        self._profile = profile

    def get_profile(self):
        """Get profile currently in use. Curently not implemented.
        :returns: profile currently in use (int)
        """
        return self._profile

    def set_operation_mode(self, mode):
        pass

    def set_ofreq_fine(self, value):
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        self._ofreq = value
        logging.debug("DdsTestDev.%r(%r, %r)", inspect.stack()[0][3], value, profile)
        return self._ofreq

    def set_ofreq(self, value, profile=None):
        """Set output frequency to current DDS profile if profile parameter is
        None or set output frequency of requested DDS profile.
        Return the actual output frequency (see _actual_ofreq() method).
        :param value: Output frequency value (float).
        :param profile: Profile to update between 0 to 7 (int)
        :returns: Actual output frequency (float)
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        self._ofreq = value
        logging.debug("DdsTestDev.%r(%r, %r)", inspect.stack()[0][3], value, profile)
        return self._ofreq

    def get_ofreq(self, profile=None):
        """Get output frequency of current DDS profile if profile parameter is
        None or return output frequency of requested DDS profile.
        :param profile: Profile output frequency requested (int)
        :returns: Output frequency of DDS profile (float).
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        logging.debug("DdsTestDev.%r(%r)", inspect.stack()[0][3], profile)
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
        self._phy = value
        logging.debug("DdsTestDev.%r(%r, %r)", inspect.stack()[0][3], value, profile)
        return 0

    def get_phy(self, profile=None):
        """Get output phase of profile..
        :param profile: Profile phase requested (int)
        :returns: Output phase of DDS (float).
        """
        logging.debug("DdsTestDev.%r(%r)", inspect.stack()[0][3], profile)
        return self._phy

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
        self._amp = value
        logging.debug("DdsTestDev.%r(%r, %r)",
                      inspect.stack()[0][3], value, profile)
        return value

    def get_amp(self, profile=None):
        """Get output amplitude tuning word of DDS.
        :param profile: Profile phase requested (int)
        :returns: Output amplitude tuning of DDS (float).
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        logging.debug("DdsTestDev.%r(%r)", inspect.stack()[0][3], profile)
        return self._amp

    def set_output_state(self, state=False):
        """Set output state.
        :param state: - False  Disable output. (bool)
                      - True   Enable CMOS output.
        :returns: None
        """
        raise NotImplemented

    def get_output_state(self):
        """Get output state.
        :returns: Output state (bool)
        """
        logging.debug("DdsTestDev.%r()", inspect.stack()[0][3])
        return True

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
        if self.get_pll_state() is True:
            pmf = self.get_pll_multiplier_factor()
            if pmf is None:
                raise InvalidState("PLL multiplier factor undefined")
            sysfreq = pll_input_frequency * 2 * pmf
        else:  # PLL bypassed
            sysfreq = pll_input_frequency
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
        self._input_divider_factor = value
        logging.debug("Set PLL divider factor: %r", value)
        return value

    def get_input_divider_factor(self):
        """Get input divider factor.
        :returns: factor value of input divider (1, 2, 4 or 8) (int)
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        return self._input_divider_factor

    def set_input_doubler_state(self, value: bool):
        """Set input doubler state.
        :param value: input doubler state (boolean)
        :returns: None
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        self._input_doubler_state = value
        logging.debug("Set PLL divider factor: %r", value)

    def get_input_doubler_state(self):
        """Get input doubler state.
        :returns: input doubler state (boolean)
        """
        if self.is_connected() is False:
            logging.error("Device is not connected.")
            return None
        return self._input_doubler_state

    def set_pll_state(self, state=False):
        """Set PLL state.
        Note: A modification of the PLL state modify the output frequency.
        :param state: - False  Disable PLL. (bool)
                      - True   Enable PLL.
        :returns: None
        """
        self._pll_state = state
        logging.debug("DdsTestDev.%r(%r)", inspect.stack()[0][3], state)

    def get_pll_state(self):
        """Get PLL state.
        :returns: PLL state (bool)
        """
        logging.debug("DdsTestDev.%r()", inspect.stack()[0][3])
        return self._pll_state

    def is_pll_locked(self):
        """Return the internal PLL lock (to the REF CLK input signal) state.
        :returns: True if the internal PLL is locked else return False (bool)
        """
        logging.debug("DdsTestDev.%r()", inspect.stack()[0][3])
        return True

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
            value = self._bound_value(value, 10, 255)
        self._pll_multiplier_factor = value
        logging.debug("DdsTestDev.%r(%r)", inspect.stack()[0][3], value)

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
        return self._pll_multiplier_factor

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
        logging.debug("DdsTestDev.%r(%r)", inspect.stack()[0][3])

    #############################################################################
    # END SysFreq handling
    #############################################################################

    @staticmethod
    def _bound_value(value, vmin, vmax):
        """Check that a value is included in the range [min, max], if not the value
        is bounded to the range, ie:
        - if value < min  ->  min = value
        - if value > max  ->  max = value
        :param value: Value that is checked
        :param vmin: Minimum valid value.
        :param vmax: Maximum valid value.
        :returns: Bounded value.
        """
        if value < vmin:
            logging.warning("Parameter out of range (%f). Set to: %f",
                            value, vmin)
            return vmin
        if value > vmax:
            logging.warning("Parameter out of range (%f). Set to: %f",
                            value, vmax)
            return vmax
        return value
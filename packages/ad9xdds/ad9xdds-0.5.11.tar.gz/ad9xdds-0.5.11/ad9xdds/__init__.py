import logging

# =============================================================================
class InvalidState(Exception):
    """Defined exception when DDS seems in an unknown state"""
    pass


class ConnectionError(Exception):
    pass


# =============================================================================
def bound_value(value, vmin, vmax, val_name=""):
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
        logging.warning("Parameter %s out of range (%f). Set to: %f",
                        val_name, value, vmin)
        return vmin
    if value > vmax:
        logging.warning("Parameter %s out of range (%f). Set to: %f",
                        val_name, value, vmax)
        return vmax
    return value
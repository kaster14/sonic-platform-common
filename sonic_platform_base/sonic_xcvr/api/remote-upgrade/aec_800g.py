"""
    aec_800g.py

    Implementation of set_firmware_download_target_end for remote upgrade. 
    Supported by TE Connectivity and Credo as of April 5th 2024
"""

from ...fields import consts
from ..public.cmis import CmisApi

class CmisAec800gApi(CmisApi):
    def set_firmware_download_target_end(self, target):
        return self.xcvr_eeprom.write(consts.TARGET_MODE, target)

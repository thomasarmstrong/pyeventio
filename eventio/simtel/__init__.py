from ..base import KNOWN_OBJECTS, EventIOObject
from .objects import (
    SimTelRunHeader,
    SimTelMCRunHeader,
    SimTelCamSettings,
    SimTelCamOrgan,
    SimTelPixelset,
    SimTelPixelDisable,
    SimTelCamsoftset,
    SimTelPointingCor,
    SimTelTrackSet,
    SimTelCentEvent,
    SimTelTrackEvent,
    SimTelTelEvent,
    SimTelEvent,
    SimTelTelEvtHead,
    SimTelTelADCSum,
    SimTelTelADCSamp,
    SimTelTelImage,
    SimTelShower,
    SimTelPixelTiming,
    SimTelPixelCalib,
    SimTelMCShower,
    SimTelMCEvent,
    SimTelTelMoni,
    SimTelLasCal,
    SimTelRunStat,
    SimTelMCRunStat,
    SimTelMCPeSum,
    SimTelPixelList,
    SimTelCalibEvent,
)

__all__ = [
    'SimTelRunHeader',
    'SimTelMCRunHeader',
    'SimTelCamSettings',
    'SimTelCamOrgan',
    'SimTelPixelset',
    'SimTelPixelDisable',
    'SimTelCamsoftset',
    'SimTelPointingCor',
    'SimTelTrackSet',
    'SimTelCentEvent',
    'SimTelTrackEvent',
    'SimTelTelEvent',
    'SimTelEvent',
    'SimTelTelEvtHead',
    'SimTelTelADCSum',
    'SimTelTelADCSamp',
    'SimTelTelImage',
    'SimTelShower',
    'SimTelPixelTiming',
    'SimTelPixelCalib',
    'SimTelMCShower',
    'SimTelMCEvent',
    'SimTelTelMoni',
    'SimTelLasCal',
    'SimTelRunStat',
    'SimTelMCRunStat',
    'SimTelMCPeSum',
    'SimTelPixelList',
    'SimTelCalibEvent',
]

for cls in EventIOObject.__subclasses__():
    KNOWN_OBJECTS[cls.eventio_type] = cls
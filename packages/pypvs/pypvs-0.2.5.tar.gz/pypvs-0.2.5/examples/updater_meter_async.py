# This is an example of how to use a PVS updater to get data
#

import asyncio
import aiohttp

from pypvs.pvs import PVS
from pypvs.updaters.meter import PVSProductionMetersUpdater
from pypvs.models.pvs import PVSData
from pypvs.models.common import CommonProperties
from pypvs.const import SupportedFeatures
from pypvs.exceptions import ENDPOINT_PROBE_EXCEPTIONS

import logging
logging.basicConfig(level=logging.DEBUG)

# Example
async def main():
    host = "localhost:18443"

    async with aiohttp.ClientSession() as session:
        pvs = PVS(session=session, host=host, user="ssm_owner")
        try:
            await pvs.discover()
            pvs_serial = pvs.serial_number
            # The password is the last 5 characters of the PVS serial number
            pvs_password = pvs_serial[-5:]
            await pvs.setup(auth_password=pvs_password)
            logging.info(f"Connected to PVS with serial: {pvs_serial}")
        except ENDPOINT_PROBE_EXCEPTIONS as e:
            logging.error(f"Cannot communicate with the PVS: {e}")
            return

        common_properties = CommonProperties()
        meter_updater = PVSProductionMetersUpdater(pvs.getVarserverVar, pvs.getVarserverVars, common_properties)

        discovered_features = SupportedFeatures(0)
        meter_is_there = await meter_updater.probe(discovered_features)
        if not meter_is_there:
            print("No meters found for that PVS on varserver")
            return

        # setup a periodic task to fetch data every 5 seconds
        pvs_data = PVSData()
        while True:
            await meter_updater.update(pvs_data)

            print(">>>>>> Meters:")
            for meter in pvs_data.meters.values():
                print(f"{meter.serial_number}: {meter}")

            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")

"""RyseBLEDevice: async wrapper around Bleak for RYSE devices.

This module intentionally keeps responsibilities small: connect/disconnect,
read/write GATT characteristics, and deliver notifications via a callback.
"""

import asyncio
from bleak import BleakClient, BleakScanner
import logging

_LOGGER = logging.getLogger(__name__)

class RyseBLEDevice:
    """Represent a RYSE device and provide async methods to interact with it."""
    def __init__(self, address=None, rx_uuid=None, tx_uuid=None):
        self.address = address
        self.rx_uuid = rx_uuid
        self.tx_uuid = tx_uuid
        self.client = None

    async def pair(self):
        """Connect to the device and subscribe to notifications."""
        if not self.address:
            _LOGGER.error("No device address provided for pairing.")
            return False
        _LOGGER.debug("Pairing with device %s",
                      self.address)
        self.client = BleakClient(self.address)
        try:
            await self.client.connect(timeout=30.0)
            if self.client.is_connected:
                _LOGGER.debug("Successfully paired with %s",
                              self.address)
                # Subscribe to notifications
                await self.client.start_notify(self.rx_uuid, self._notification_handler)
                return True
        except Exception as e:
            _LOGGER.error("Error pairing with device %s: %s",
                          self.address, e)
        return False

    async def _notification_handler(self, sender, data):
        """Callback function for handling received BLE notifications."""
        if len(data) >= 5 and data[0] == 0xF5 and data[2] == 0x01 and data[3] == 0x18:
            # ignore REPORT USER TARGET data
            return
        _LOGGER.debug("Received notification")
        if len(data) >= 5 and data[0] == 0xF5 and data[2] == 0x01 and data[3] == 0x07:
            new_position = data[4]  # Extract the position byte
            _LOGGER.debug("Received valid notification, updating position: %d",
                          new_position)

            # Notify cover.py about the position update
            if hasattr(self, "update_callback"):
                await self.update_callback(new_position)

    async def get_device_info(self):
        if self.client:
            try:
                manufacturer_data = self.client.services
                _LOGGER.debug("Getting Manufacturer Data")
                return manufacturer_data
            except Exception as e:
                _LOGGER.error("Failed to get device info: %s", e)
        return None

    async def unpair(self):
        if self.client:
            await self.client.disconnect()
            _LOGGER.debug("Device disconnected")
            self.client = None

    async def read_data(self):
        if self.client:
            data = await self.client.read_gatt_char(self.rx_uuid)
            if len(data) < 5 or data[0] != 0xF5 or data[2] != 0x01 or data[3] != 0x18:
                # ignore REPORT USER TARGET data
                _LOGGER.debug("Received Position Report Data")
                return data
            return None

    async def write_data(self, data):
        if self.client:
            await self.client.write_gatt_char(self.tx_uuid, data)
            _LOGGER.debug("Sending data to tx uuid")

    async def scan_and_pair(self):
        _LOGGER.debug("Scanning for BLE devices...")
        devices = await BleakScanner.discover()
        for device in devices:
            _LOGGER.debug("Found device: %s (%s)",
                          device.name, device.address)
            if device.name and "target-device-name" in device.name.lower():
                _LOGGER.debug("Attempting to pair with %s (%s)",
                              device.name, device.address)
                self.address = device.address
                return await self.pair()
        _LOGGER.warning("No suitable devices found to pair")
        return False

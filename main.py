import hid

# Enumerate all connected HID devices
devices = hid.enumerate()

for device in devices:
    print(f"Vendor ID: {device['vendor_id']}, Product ID: {device['product_id']}, Manufacturer: {device.get('manufacturer_string')}, Product: {device.get('product_string')}")


# vid = 0x046d	# Change it for your device
# pid = 0xc534	# Change it for your device
#
# with hid.Device(vid, pid) as h:
# 	print(f'Device manufacturer: {h.manufacturer}')
# 	print(f'Product: {h.product}')
# 	print(f'Serial Number: {h.serial}')



# Define your device's Vendor ID and Product ID
VENDOR_ID = 0x16C0  # 5824 in decimal
PRODUCT_ID = 0x05DF  # 1503 in decimal

def main():
    try:
        # Open the USB relay device
        relay = hid.device()
        relay.open(VENDOR_ID, PRODUCT_ID)
        print("Connected to USB Relay.")

        # Example: Sending a command to turn the relay ON
        # This command may vary depending on your relay's protocol.
        # Consult the relay documentation for the correct commands.
        turn_on_command = [0x00, 0x01]  # Replace with your device's ON command
        relay.write(turn_on_command)
        print("Sent command to turn relay ON.")

        # Example: Reading a response (if supported)
        response = relay.read(64)  # Adjust the length based on your device
        print("Response from relay:", response)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Always close the connection
        relay.close()
        print("Disconnected from USB Relay.")

if __name__ == "__main__":
    main()


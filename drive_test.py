import win32file, time, ctypes
import winioctlcon

IOCTL_CDROM_LOAD_MEDIA = winioctlcon.CTL_CODE(winioctlcon.FILE_DEVICE_CD_ROM, 0x0203, winioctlcon.METHOD_BUFFERED, winioctlcon.FILE_READ_ACCESS)
#CTL_CODE(IOCTL_CDROM_BASE, 0x0203, METHOD_BUFFERED, FILE_READ_ACCESS)

# Open the CD-ROM drive
cdrom_path = r'\\.\D:'  # Replace with your CD-ROM drive letter
handle = win32file.CreateFile(
    cdrom_path,
    win32file.GENERIC_READ | win32file.GENERIC_WRITE,
    win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
    None,
    win32file.OPEN_EXISTING,
    0,
    None
)

# Send IOCTL_CDROM_LOAD_MEDIA command

buffer_size = 8  # Example size; adjust based on expected output
output_buffer = ctypes.create_string_buffer(buffer_size)

win32file.DeviceIoControl(handle, winioctlcon.IOCTL_STORAGE_EJECT_MEDIA, None, None)

time.sleep(10)

win32file.DeviceIoControl(handle, winioctlcon.IOCTL_STORAGE_CHECK_VERIFY, None, output_buffer)
returned_data = output_buffer.raw
print(f"Returned Data: {returned_data}")

handle.Close()
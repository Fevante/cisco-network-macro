# Hálpy v2.0

A Python-based network automation tool for configuring Cisco networking devices. The application provides a graphical interface to automate common network configuration tasks using GUI inputs and automated CLI command execution.

## Features

- **DHCP Configuration**: Automated DHCP server setup with interface configuration, IP addressing, and pool creation
- **RIP v2 Routing**: Configure RIPv2 routing protocol with multiple network advertisements
- **Telnet Setup**: Configure telnet access on switches and routers with password protection
- **Static NAT**: Set up static Network Address Translation with inside/outside interface configuration
- **Dynamic NAT**: Configure dynamic NAT with IP pools, access lists, and interface assignments
- **Voice Assistant**: Optional audio feedback with custom voice options (Bill and Aszi)
- **Easter Eggs**: Hidden features for fun interactions

## Requirements

- Python 3.9+ (tested with Python 3.12)
- Windows OS (uses Windows-specific command automation)
- Active Cisco device CLI session (via terminal/Packet Tracer/GNS3)

### Python Dependencies

```bash
pip install pygame pyautogui
```

Required packages:
- `pygame` - For audio playback
- `pyautogui` - For keyboard automation
- `tkinter` - GUI framework (usually included with Python)
- `configparser` - Configuration management (included in Python standard library)
- `pathlib` - Path handling (included in Python standard library)

## Installation

1. Clone or download the repository to your local machine

2. Install the required Python dependencies:
   ```bash
   pip install pygame pyautogui
   ```

3. Ensure a `config.ini` file exists in the same directory with the following structure:
   ```ini
   [voice]
   byll = 0
   baszi = 0
   ```

4. Create a `Sounds` folder in the same directory and add the following audio files:
   - `Bill_voice.mp3`
   - `Aszi_voice.wav`
   - `uwu.wav`
   - `nyan.wav`

5. Ensure you have an icon file to build it into an exe file (optional):
   - `pictures/icon.ico`
   - `pictures/icon.png`

## Usage

### Running the Application

Run the application using Python:

```bash
python main.py
```

Or if you've built the executable:

```bash
main.exe
```

### How It Works

1. **Launch** the application
2. **Select** a configuration option from the main menu if you want a (Hungarian) voice guide
3. **Fill in** the required network parameters (interface names, IP addresses, masks, etc.)
4. **Click "Done"** to confirm your inputs
5. **Wait** for the 5-second countdown
6. **Ensure** your Cisco device CLI window is active (the program will adjust the device's mode as needed)
7. The application will **automatically type** and execute the required commands
8. Configuration is **saved** to startup-config automatically

### Main Menu Options

#### 1. DHCP Configuration
Configure a DHCP server on a router:
- Interface (e.g., `gig0/0`)
- IP address (e.g., `192.168.1.1`)
- Subnet mask (e.g., `255.255.255.0`)
- Pool name (e.g., `terem1`)

**What it does:**
- Configures the interface with the specified IP
- Creates a DHCP pool
- Sets the default gateway and network range
- Saves configuration

#### 2. RIP v2 Routing
Configure RIPv2 routing protocol:
- Specify number of networks to advertise
- Enter each network address

**What it does:**
- Enables RIP routing
- Sets version 2
- Advertises all specified networks
- Saves configuration

#### 3. Telnet Configuration
Set up telnet access for remote management:
- Choose device type (Switch or Router)
- Interface (e.g., `vlan 1` for switch, `gig0/0` for router)
- IP address and mask
- Telnet password

**What it does:**
- Configures management interface
- Sets up VTY lines (0-15)
- Applies password protection
- Enables login
- Saves configuration

#### 4. Static NAT
Configure one-to-one static NAT translation:
- Inside IP address (private)
- Outside IP address (public)
- Inside interface
- Outside interface

**What it does:**
- Creates static NAT mapping
- Configures inside/outside interfaces
- Saves configuration

#### 5. Dynamic NAT
Configure dynamic NAT with IP pool:
- Start IP (pool beginning)
- End IP (pool end)
- Netmask for pool
- Permit IP (internal network)
- Permit mask (wildcard mask)
- Inside interface
- Outside interface

**What it does:**
- Creates NAT pool named "DNAT"
- Configures access list
- Links pool to access list
- Configures inside/outside interfaces
- Saves configuration

### Keyboard Shortcuts

- `1` - Open DHCP configuration
- `2` - Open RIP v2 configuration
- `3` - Open Telnet configuration
- `4` - Open Static NAT configuration
- `5` - Open Dynamic NAT configuration
- `9` - Exit application
- `0` - Enable easter egg (uwu mode)
- `n` - Play nyan sound (if voice enabled)

## Configuration

Settings are stored in `config.ini`:

```ini
[voice]
byll = 0      # Bill voice assistant (0=off, 1=on)
baszi = 0     # Aszi voice assistant (0=off, 1=on)
```

### Voice Assistants

Access voice settings via **Help → Voice Assistant** menu:

- **Byll**: Plays `Bill_voice.mp3` on startup (if enabled)
- **Aszi**: Plays `Aszi_voice.wav` on startup (if enabled)
- Only one voice assistant can be active at a time

When voice is enabled, sound effects play on button interactions.

## Important Notes

### Before Running Commands

- **Ensure your Cisco device CLI window is active** when the countdown reaches zero
- The device should be at the **user EXEC mode** (or any mode - the script will exit to user EXEC)
- **Do not interact** with your computer during command execution
- The script uses `pyautogui` to simulate keyboard input

### Command Execution

- All configurations start by exiting to user EXEC mode (4x `exit`)
- Enters privileged EXEC mode (`enable`)
- Enters global configuration mode (`configure terminal`)
- Executes specific commands based on your selection
- Automatically saves with `copy running-config startup-config`

### Path Handling

- The application correctly handles paths with spaces and special characters (like `Hálpy2.0`)
- Uses `pathlib` for cross-platform path management
- All sound files are referenced using absolute paths

### Known Limitations

- **Windows only** - Uses Windows-specific keyboard automation
- **Requires manual window switching** - You must have the CLI active during countdown
- **Single device at a time** - Cannot configure multiple devices simultaneously
- **No validation** - Input validation is minimal; ensure correct syntax
- **Does not work with password protected devices**

## Troubleshooting

### Sounds Not Playing

1. Ensure `pygame` is installed: `pip install pygame`
2. Check that sound files exist in the `Sounds` folder
3. Verify file names match exactly (case-sensitive)
4. Check that voice assistant is enabled in settings

### Commands Not Executing

1. Ensure `pyautogui` is installed: `pip install pyautogui`
2. Make sure CLI window is active during countdown
3. Check that device is accessible and responsive
4. Verify no dialog boxes or prompts are blocking input

### Configuration Not Saving

1. Check that `config.ini` exists and is writable
2. Ensure the file is not open in another program
3. Verify file permissions

### Path Errors

- If you see path-related errors, ensure all backslashes in paths are handled correctly
- The application uses `pathlib` which automatically handles path separators

## Building Executable

The project includes build artifacts in the `build/` folder, suggesting PyInstaller was used:

```bash
pyinstaller --onefile --icon=pictures/icon.ico main.py
```

The resulting `main.exe` will be in the `dist/` folder.

## Project Structure

```
Hálpy2.0/
├── main.py              # Main application file
├── main.exe             # Compiled executable
├── config.ini           # Configuration file
├── README.md            # This file
├── pictures/
│   ├── icon.ico        # Application icon
│   └── icon.png        # Icon PNG version
├── Sounds/
│   ├── Aszi_voice.wav  # Aszi voice file
│   ├── Bill_voice.mp3  # Bill voice file
│   ├── nyan.wav        # Nyan cat sound
│   └── uwu.wav         # UwU sound effect
└── build/              # PyInstaller build artifacts
```

## Contributing

This is a personal automation tool. If you'd like to contribute or suggest improvements, feel free to fork and modify for your needs.

## Safety Warning

⚠️ **Use with caution!** This tool automates keyboard input and will type commands into whatever window is active. Always ensure:
- You're connected to the correct device
- You have a backup of your configuration
- You understand what commands will be executed
- You're in a safe testing environment

## License

This project is provided as-is for educational and automation purposes.

## Credits

Developed for network automation tasks in Cisco device configuration.

---

**Version**: 2.0  
**Last Updated**: 2025  
**Tested On**: Windows, Python 3.12, Cisco Packet Tracer



# Software support for the ATLAS ITK pixels multi-module cycling box

[![PyPi](https://badge.fury.io/py/mmcb-avt.svg)](https://badge.fury.io/py/mmcb-avt)

![image](https://hep.ph.liv.ac.uk/~avt/pypi/logo.png)

*Particle Physics, University of Liverpool, UK*

----

This repository provides command line tools to monitor and control equipment in the *ATLAS ITK pixels multi-module cycling box* test setup, and includes a Python-importable package to read from environmental sensors. It is used in the test setups for a number of other projects for environmental sensing.

This project expects to be run on a Raspberry Pi, and has a few dependencies - outlined below - that cannot be automatically installed by `pip`.


## Installation (Raspberry Pi OS only)

### Create a Python virtual environment

```shell
mkdir ~/dev && cd ~/dev

python3 -m venv pve
. ~/dev/pve/bin/activate
```

Add `. ~/dev/pve/bin/activate` to the end of `~/.bashrc` to activate the Python virtual environment at login.

### Install package and (most) dependencies

```
python3 -m pip install --upgrade wheel mmcb-avt
```

For the Raspberry Pi 5 you may also need `python3 -m pip install --upgrade gpiod lgpio; sudo apt install libgpiod-dev`

**The above installs all the dependencies required except for the MCP9601 and NAU7802.**

### MCP9601 (manual installation)

The Adafruit MCP9601 API was broken when last tested, so use the Pimoroni MCP9600 API instead. Since the Pimoroni API is for the MCP9600 rather than the MCP9601, we need to make a small change before installation:

```shell
git clone https://github.com/pimoroni/mcp9600-python
cd mcp9600-python
```

In file `library/mcp9600/__init__.py` make these changes:

Change from:

```python
CHIP_ID = 0x40
I2C_ADDRESSES = list(range(0x60, 0x68))
I2C_ADDRESS_DEFAULT = 0x66
I2C_ADDRESS_ALTERNATE = 0x67
```

To:

```python
CHIP_ID = 0x41
I2C_ADDRESSES = list(range(0x65, 0x68))
I2C_ADDRESS_DEFAULT = 0x67
I2C_ADDRESS_ALTERNATE = 0x66
```

Also edit the `PYTHON="..."` line in `install.sh` to point to the correct Python version, which in this case is python3 from the Python virtual environment. Use the full path provided by `which python3`, it'll look something like this:

```shell
#PYTHON="/usr/bin/python3"
PYTHON="/home/ds20k/dev/pve/bin/python3"
```

Then finally:

```shell
sudo ./install.sh --unstable
```

Reboot after the above step.

### NAU7802 (manual installation)

```shell
cd ~/dev
git clone https://github.com/CedarGroveStudios/CircuitPython_NAU7802.git

# copy file into the python virtual environment
# note that the Python version for your environment may be different to those given below

# For 64-bit Raspberry Pi OS (Python virtual environment)
cp ~/dev/CircuitPython_NAU7802/cedargrove_nau7802.py ~/dev/pve/lib/python3.11/site-packages/

# For 32-bit Raspberry Pi OS (distribution's Python)
sudo cp ~/dev/CircuitPython_NAU7802/cedargrove_nau7802.py /usr/local/lib/python3.7/dist-packages/

# For 32-bit Raspberry Pi OS (Python virtual environment)
sudo cp ~/dev/CircuitPython_NAU7802/cedargrove_nau7802.py ~/dev/pve/lib/python3.7/site-packages/
```

### Notes

Make sure I2C is enabled with `sudo raspi-config`.

The installation process will make the following new commands available in the shell:

### Create config file for sensors

```shell
cd ~/dev
git clone https://gitlab.ph.liv.ac.uk/avt/atlas-itk-pmmcb.git

# extract the template configuration file
cp atlas-itk-pmmcb/packaging/src/mmcb/config.txt ~
```

You can now edit the template `config.txt` to match the configuration of your sensor setup.

### Main commands

|Command|Function|
|:---:|:---:|
|[dmm](packaging/src/mmcb/dmm.py)|Reads voltage/current values from the Keithley DMM6500 6.5 digit multimeter.|
|[iv](packaging/src/mmcb/iv.py)|Configurable script to measure IV/IT curves using the Keithley 2410/2614b (RS232). It can operate multiple PSUs concurrently, embed environmental data into log files, and can be easily used in shell scripts to automate tasks such as HV-cycling.|
|`peltier`|Queries and/or sets parameters for the two relay boards that control the polarity of the four Peltier devices, via Raspberry Pi GPIO pins.|
|`psuset`|Sets current/voltage parameters for power supplies (RS232: Keithley 2410/2614b, Hameg HMP4040). Works in both constant voltage and constant current modes.|
|`sense`|Reads environmental sensors connected to the Raspberry Pi by I2C. Hardware setup is specified in a user defined configuration file. Progressively writes data to a human-readable log file, and streams compressed binary data to an [HDF5](https://www.hdfgroup.org/solutions/hdf5/) file. Directly supports the BME680, HYT221, NAU7802, SHTC3 sensors, and various thermocouples via MCP9601. Indirectly supports the [SMC ZSE30A-01-F](https://www.smcpneumatics.com/ZSE30A-01-F.html), [SMC PFM725S-F01-F](https://www.smcpneumatics.com/PFM725S-F01-F.html) and the ATLAS common hybrid module NTC via [ADS1015](https://www.ti.com/product/ADS1015) and PCF8591 ADCs.|
|`ult80`|Queries and/or sets parameters for the ULT80 chiller (RS232).|


### Support commands

|Command|Function|
|:---:|:---:|
|`dat2plot`|From the binary data files generated by `sense`, create two plots featuring all environmental sensors/parameters: the first will contain the raw data acquired vs time, the second contains summary statistics.|
|`dat2root`|Creates a [CERN ROOT](https://root.cern.ch) file containing the raw data from binary data files generated by `sense`, as well as a plot for each parameter.|
|`detect`|Detects equipment attached by RS232, writes a cache file containing identified equipment to `~/.cache.json`. Run *once* after the RS232 configuration has changed.|
|`liveplot`|Companion to `iv`. Displays IV plot in real-time in a graphical window.|
|`log2dat`|Creates a `.dat` file from the log file `sense` creates. Principally used with archived legacy data where binary data files are not available.|
|`psustat`|Provides a single-shot view of the status of all power supply channels (RS232: Keithley 2410/2614b, Hameg HMP4040).|


In addition, once in the Python `venv`, you will be able to do this:

```python
(pve) ds20k@raspberrypi:~ $ cd
(pve) ds20k@raspberrypi:~ $ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import mmcb.configure_environment as ce
>>> testenv = ce.TestEnvironment('config.txt')
>>> measurements = testenv.read_all_sensors()
>>> measurements
{'timestamp': 1653844116.1013656, 'hyt_M1 °C': 21.12342061893426, 'hyt_M1 RH%': 0.0, 'hyt_env °C': 21.324848928767622, 'hyt_env RH%': 0.0, 'hyt_M4 °C': 21.113349203442596, 'hyt_M4 RH%': 0.0, 'ntc_M1 °C': 18.874264620930205, 'smc kPa': -95.29101904000001, 'ntc_M4 °C': -60.849429204693735, 'TC_VC4 °C': 20.3125, 'TC_VC1 °C': 19.375, 'TC_N2 °C': 20.75, 'TC_VC3 °C': 21.0, 'TC_VC2 °C': 21.25, 'sht_ambient °C': 23.43, 'sht_ambient RH%': 31.48, 'bme_ambient °C': 23.924921875, 'bme_ambient RH%': 26.04732304850249, 'bme_ambient hPa': 1014.36410289236}
>>> measurements.get('hyt_M4 °C', None)
21.113349203442596
```

### Python interface for the Keithley DMM6500

```python
(pve) avt@raspberrypi:~ $ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mmcb import dmm_interface
cache: keithley instruments dmm6500 serial number 04592428 on /dev/ttyUSB0
>>> dmm = dmm_interface.Dmm6500()
>>> dmm.
dmm.configure_read_ac_current(   dmm.configure_read_dc_voltage(   dmm.remove(
dmm.configure_read_ac_voltage(   dmm.configure_read_resistance(   dmm.removed
dmm.configure_read_capacitance(  dmm.configure_read_temperature(
dmm.configure_read_dc_current(   dmm.read_value(

>>> dmm.configure_read_capacitance()
>>> c = dmm.read_value()
>>> c
1.0465248938e-07

>>> from mmcb import common
>>> common.si_prefix(v)
'104.652n'
```

## Check the installed version:

```console
(pve) avt@raspberrypi:~ $ python3 -m pip show mmcb-avt
Name: mmcb-avt
Version: 0.0.78
Summary: ATLAS ITK Pixels Multi-Module Cycling Box environmental monitoring/control.
Home-page: https://gitlab.ph.liv.ac.uk/avt/atlas-itk-pmmcb
Author: Alan Taylor, Manex Ormazabal
Author-email: avt@hep.ph.liv.ac.uk
License: None
Location: /home/avt/dev/pve/lib/python3.9/site-packages
Requires: adafruit-circuitpython-shtc3, smbus, adafruit-circuitpython-pcf8591, pandas, zmq, yoctopuce, sparkfun-qwiic-tca9548a, Adafruit-Blinka, adafruit-circuitpython-bme680, tables, matplotlib, numpy, adafruit-circuitpython-ads1x15, pyserial
Required-by:
```

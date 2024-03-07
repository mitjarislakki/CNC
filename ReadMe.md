# Centralized Network Configuration for Time Sensitive Network

The repository contains the basic CNC functionality for TSN network management. This CNC main reponsibilities are:
- Network monitoring (nodes discovery and connection) for topology determination
- Calculate time sensitive related configuration parameters and bridges communication

The project is done in Python, utilizing virtual environment management with Poetry.
## Project structure


```sh
.
├── cnc_main.py             # start CNC functions as separate tasks running in parallel
├── traffic_shaper.py       # switch TSN config calculation
├── switch_discovery
│   ├── frame_handler.py         # get switch basic information from LLDP frame
│   └── process_switch_config.py # YANG LLDP model definition for infomation retrieval
├── network_map
│   └── network_map.py           # network map related models and functions
└── netconf_helper          # NETCONF clients and parameters definition
    ├── tsn_config.xml.py
    ├── nc_get_config.py
    └── nc_edit_config.py
```


## Installation

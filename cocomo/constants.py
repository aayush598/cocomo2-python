# cocomo/constants.py

# Constants for COCOMO II.2000
A = 2.94
B = 0.91
C = 3.67
D = 0.28

# Example default EMs (all nominal = 1.0)
DEFAULT_EMS = {
    'RELY': 1.00, 'DATA': 1.00, 'CPLX': 1.00,
    'RUSE': 1.00, 'DOCU': 1.00, 'TIME': 1.00,
    'STOR': 1.00, 'PVOL': 1.00, 'ACAP': 1.00,
    'PCAP': 1.00, 'PCON': 1.00, 'APEX': 1.00,
    'PLEX': 1.00, 'LTEX': 1.00, 'TOOL': 1.00,
    'SITE': 1.00, 'SCED': 1.00
}

# Scale Factor values
DEFAULT_SFS = {
    'PREC': 3.72, 'FLEX': 3.04, 'RESL': 4.24,
    'TEAM': 3.29, 'PMAT': 4.68
}

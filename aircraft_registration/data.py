PATTERNS_DICT = {
    'YA-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ZA-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '7T-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'C3-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'D2-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VP-A': ['[A-Za-z][A-Za-z]$'],
    'V2-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'LQ-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'LV-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'EK-': ['[0-9][0-9][0-9][0-9][0-9]$'],
    'P4-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VH-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'OE-': ['[A-Za-z][A-Za-z][A-Za-z]$', '[0-9][0-9][0-9][0-9]$'],
    '4K-': ['[A-Za-z][A-Za-z][0-9]$', '[A-Za-z][A-Za-z][0-9][0-9]$', '[0-9][0-9][0-9][0-9][0-9]$'],
    'C6-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'A9C-': ['[A-Za-z][A-Za-z]$', '[A-Za-z][A-Za-z][A-Za-z]$'],
    'S2-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '8P-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'EW-': ['[0-9][0-9][0-9][A-Za-z][A-Za-z]$', '[0-9][0-9][0-9][0-9][0-9]$'],
    'OO-': ['[A-Za-z][A-Za-z][A-Za-z]$', '[0-9][0-9][0-9]$', '[A-Za-z][0-9][0-9]$', '[0-9][0-9]$'],
    'V3-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TY-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VP-B': ['[A-Za-z][A-Za-z]$'],
    'A5-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'CP-': ['[0-9][0-9][0-9][0-9]$'],
    'T9-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'A2-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'PP-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'PR-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'PT-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'PU-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VP-L': ['[A-Za-z][A-Za-z]$'],
    'V8-': ['[A-Za-z][A-Za-z][A-Za-z]$', '[A-Za-z][A-Za-z][0-9]$', '[0-9][0-9][0-9]$'],
    'LZ-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'XT-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9U-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'XU-': ['[0-9][0-9][0-9]$'],
    'TJ-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'CF-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'C-F': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'C-G': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'C-I': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'D4-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VP-C': ['[A-Za-z][A-Za-z]$'],
    'TL-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TT-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'CC-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'B-': ['[0-9][0-9][0-9][0-9][0-9]$'],
    'B-H': ['[A-Za-z][A-Za-z]$'],
    'B-K': ['[A-Za-z][A-Za-z]$'],
    'B-L': ['[A-Za-z][A-Za-z]$'],
    'B-M': ['[A-Za-z][A-Za-z]$'],
    'HJ-': ['[0-9][0-9][0-9][0-9][A-Za-z]$'],
    'HK-': ['[0-9][0-9][0-9][0-9][A-Za-z]$'],
    'D6-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TN-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'E5-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9Q-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TI-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9A-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'CU-T': ['[0-9][0-9][0-9][0-9]$'],
    '5B-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'OK-': ['[A-Za-z][A-Za-z][A-Za-z]$', '[A-Za-z][A-Za-z][A-Za-z][0-9][0-9]$', '[0-9][0-9][0-9][0-9]$', '[A-Za-z][0-9][0-9][0-9]$'],
    'OY-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'OY-H': ['[A-Za-z][A-Za-z]$'],
    'OY-X': ['[A-Za-z][A-Za-z]$'],
    'OY-B': ['[A-Za-z][A-Za-z]$'],
    'J2-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'J7-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'HI-': ['[0-9][0-9][0-9][A-Za-z][A-Za-z]$'],
    'HC-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'SU-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'YS-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '3C-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'E3-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ES-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ET-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VP-F': ['[A-Za-z][A-Za-z]$'],
    'DQ-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'OH-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'F-': ['[A-Za-z][A-Za-z][A-Za-z][A-Za-z]$'],
    'F-OG': ['[A-Za-z][A-Za-z]$'],
    'F-O': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TR-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'C5-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '4L-': ['[0-9][0-9][0-9][0-9][0-9]$', '[A-Za-z][A-Za-z][A-Za-z]$'],
    'D-': ['[A-Za-z][A-Za-z][A-Za-z][A-Za-z]$'],
    '9G-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VP-G': ['[A-Za-z][A-Za-z]$'],
    'SX-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'J3-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TG-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '3X-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'J5-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '8R-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'HH-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'HR-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'HA-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TF-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VT-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'PK-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'EP-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'YI-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'EI-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'M-': ['[A-Za-z][A-Za-z][A-Za-z][A-Za-z]$'],
    '4X-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'I-': ['[A-Za-z][A-Za-z][A-Za-z][A-Za-z]$'],
    'TU-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '6Y-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'JA-': ['[0-9][0-9][0-9][0-9]$', '[0-9][0-9][0-9][A-Za-z]$', '[0-9][0-9][A-Za-z][A-Za-z]$', '[A-Za-z][0-9][0-9][0-9]$'],
    'JY-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'UN-': ['[0-9][0-9][0-9][0-9][0-9]$'],
    '5Y-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'T3-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'P-': ['[0-9][0-9][0-9]$'],
    'HL-': ['[0-9][0-9][0-9][0-9]$'],
    '9K-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'EX-': ['[0-9][0-9][0-9][0-9][0-9]$', '[0-9][0-9][0-9]$'],
    'RDPL-': ['[0-9][0-9][0-9][0-9][0-9]$'],
    'YL-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'OD-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '7P-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'A8-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '5A-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'LY-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'LX-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'Z3-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '5R-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '7Q-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9M-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '8Q-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TZ-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9H-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'V7-': ['[0-9][0-9][0-9][0-9]$'],
    '5T-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '3B-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'XA-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'XB-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'XC-': ['[A-Za-z][A-Za-z][A-Za-z]$', '[A-Za-z][A-Za-z][A-Za-z][0-9][0-9]$'],
    'V6-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ER-': ['[A-Za-z][A-Za-z][A-Za-z]$', '[0-9][0-9][0-9][0-9][0-9]$'],
    '3A-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'JU-': ['[0-9][0-9][0-9][0-9]$'],
    '4O-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'VP-M': ['[A-Za-z][A-Za-z]$'],
    'CN-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'C9-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'XY-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'XZ-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'V5-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'C2-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9N-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'PH-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'PJ-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ZK-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ZL-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ZM-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'YN-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '5U-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '5N-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'LN-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'A4O-': ['[A-Za-z][A-Za-z]$'],
    'AP-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'HP-': ['[0-9][0-9][0-9][0-9][A-Za-z][A-Za-z][A-Za-z]$'],
    'P2-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ZP-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'OB-': ['[0-9][0-9][0-9][0-9]$'],
    'RPC-': ['[0-9][0-9][0-9][0-9]$'],
    'SP-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'CR-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'CS-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'A7-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'F-OD': ['[A-Za-z][A-Za-z]$'],
    'YR-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'RA-': ['[0-9][0-9][0-9][0-9][0-9]$', '[0-9][0-9][0-9][0-9]K$'],
    '9XR-': ['[A-Za-z][A-Za-z]$'],
    'VQ-H': ['[A-Za-z][A-Za-z]$'],
    'V4-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'J6-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'J8-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '5W-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'T7-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'S9-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'HZ-': ['[A-Za-z][A-Za-z][A-Za-z]$', '[A-Za-z][A-Za-z][0-9]$', '[A-Za-z][A-Za-z][0-9][0-9]$', '[A-Za-z][A-Za-z][A-Za-z][0-9]$'],
    '6V-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '6W-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'YU-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'S7-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9L-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9V-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'OM-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'S5-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'H4-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '6O-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ZS-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ZT-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ZU-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'EC-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '4R-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'ST-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'PZ-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '3D-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'SE-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'HB-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'YK-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'F-OH': ['[A-Za-z][A-Za-z]$'],
    'EY-': ['[0-9][0-9][0-9][0-9][0-9]$'],
    '5H-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'HS-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '5V-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'A3-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9Y-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TS-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'TC-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'EZ-': ['[A-Za-z][0-9][0-9][0-9]$'],
    'VQ-T': ['[A-Za-z][A-Za-z]$'],
    'T2-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '5X-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'UR-': ['[0-9][0-9][0-9][0-9][0-9]$', '[A-Za-z][A-Za-z][A-Za-z]$'],
    'A6-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'G-': ['[A-Za-z][A-Za-z][A-Za-z][A-Za-z]$'],
    'N-': ['[0-9]$', '[0-9][0-9]$', '[0-9][0-9][0-9]$', '[0-9][0-9][0-9][0-9]$', '[0-9][0-9][0-9][0-9][0-9]$', '[0-9][A-Za-z]$', '[0-9][0-9][A-Za-z]$', '[0-9][0-9][0-9][A-Za-z]$', '[0-9][0-9][0-9][0-9][A-Za-z]$', '[0-9][A-Za-z][A-Za-z]$', '[0-9][0-9][A-Za-z][A-Za-z]$', '[0-9][0-9][0-9][A-Za-z][A-Za-z]$'],
    'CX-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'UK-': ['[0-9][0-9][0-9][0-9][0-9]$'],
    'YJ-': ['[A-Za-z][A-Za-z][0-9]$', '[A-Za-z][A-Za-z][0-9][0-9]$'],
    'YV-': ['[0-9][0-9][0-9][A-Za-z]$', '[0-9][0-9][0-9][0-9]$', 'O[0-9][0-9][0-9]$', 'KW[0-9]$', 'SATA[0-9]$'],
    'VN-': ['[0-9][0-9][0-9][0-9]$', '[A-Za-z][0-9][0-9][0-9]$'],
    '7O-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    '9J-': ['[A-Za-z][A-Za-z][A-Za-z]$'],
    'Z-': ['[A-Za-z][A-Za-z][A-Za-z]$']
    }

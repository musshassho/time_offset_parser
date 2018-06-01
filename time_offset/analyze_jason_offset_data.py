

# IMPORTS
import os
import json
# import nuke
import re

# CONSTANTS

PATH = "//fbbblue/00_jobs/baj_benjamin/prod/plates/footage_vfx_plates/vfx_plates_QTref/Generic Plate11-01 B.mov"
MOV = "Generic Plate11-01 B.mov"
LOGS = "C:\LOGS"

# MAIN FUNCTIONS

def analyze_data(path):
    in_points = []
    out_points = []
    data = get_json(path)[0]
    for i in data.keys():
        for e in d[i]:
            in_= d[i][e][0]
            out_ = d[i][e][1]
            in_points.append(in_)
            out_points.append(out_)
    min_in= min(in_points)
    max_out = max(out_points)
    return  min_in,max_out


# FUNCTION CALLS

print analyze_data(LOGS)

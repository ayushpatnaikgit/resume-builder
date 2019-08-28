import os
from insert import *
from activate import *
from pages import *
import json
import sys
from build_funcs import *
file = sys.argv[1]
if '.hjson' in file:
    os.system("rm -rf temp_json_from_hjson.json")
    os.system("hjson -j "+sys.argv[1]+" >> temp_json_from_hjson.json") 
    with open("temp_json_from_hjson.json") as json_file:  
        data_file = json.load(json_file)
        os.system("rm -rf temp_json_from_hjson")
else: 
    with open(file) as json_file:  
        data_file = json.load(json_file)
#creating files using headinds
os.system("rm -rf template")
build_website(data_file)

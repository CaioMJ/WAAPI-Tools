#!/usr/bin/env python3
import os
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

#####FUNCTIONS#######
def getAllMusicTrackIDs():
    args = {
        "waql": "$ from type MusicTrack"
    }

    options = {
        "return":["id"]
    }

    return client.call("ak.wwise.core.object.get", args, options=options)
        
def getNumberOfObjects(result_dictionary):
    num_of_objects = 0
    
    for x in result_dictionary.values():
        for i in x: num_of_objects += 1
        
    pprint(num_of_objects)
    return num_of_objects
    
def setMusicTrackSettings(num_of_objects, result_dictionary, zerolatency, noncache):
    count = 0
    
    while (count < num_of_objects):
        object_id = result_dictionary.get("return")[count]["id"]
        
        #streaming
        args = {
            "object":object_id,
            "property":"IsStreamingEnabled",
            "value":True
        }
        
        client.call("ak.wwise.core.object.setProperty", args)
        
        #zero latency
        args = {
            "object":object_id,
            "property":"IsZeroLantency",
            "value":zerolatency
        }
        
        client.call("ak.wwise.core.object.setProperty", args)
        
        #non cache
        args = {
            "object":object_id,
            "property":"IsNonCachable",
            "value":noncache
        }
        
        client.call("ak.wwise.core.object.setProperty", args)
        count = count + 1

def displaySystemMessage(body_Str, title_Str):
        os.system("osascript -e \'Tell application \"System Events\" to display dialog \""+body_Str+"\" with title \""+title_Str+"\"\'")

######EXECUTION#####
try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        input_zerolatency = input("Zero Latency? True or False: ")
        input_noncache = input("Non-cacheable? True or False: ")
        
        get_result = getAllMusicTrackIDs()
        num_of_objects = getNumberOfObjects(get_result)
        pprint("Number of Music Tracks altered: " + str(num_of_objects))
        setMusicTrackSettings(num_of_objects, get_result, input_zerolatency, input_noncache)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

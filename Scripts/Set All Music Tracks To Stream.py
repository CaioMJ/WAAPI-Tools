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
        
        args = {
            "objects":[
                {
                    #Modifies an existing object
                    "object":object_id,
                    "@IsStreamingEnabled":True,
                    "@IsNonCachable":noncache,
                    "@IsZeroLatency":zerolatency
                }
            ]
        }
        client.call("ak.wwise.core.object.set", args)
        count = count + 1
    else:
        displaySystemMessage("Wwise music streaming configuration set!", "WAAPI Message")

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

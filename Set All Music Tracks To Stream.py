#!/usr/bin/env python3

import json
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

def getAllMusicTrackIDs():
    get_args = {
        "waql": "$ from type MusicTrack"
    }

    get_option = {
        "return":["id"]
    }

    return client.call("ak.wwise.core.object.get", get_args, options=get_option)
        
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
        
        set_args = {
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
        client.call("ak.wwise.core.object.set", set_args)
        pprint(count)
        count = count + 1
        
try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        #User settings
        input_zerolatency = input("Zero Latency? True or False: ")
        input_noncache = input("Is it non-cacheable? True or False: ")
        
        #Query to get all music track object ids
        get_result = getAllMusicTrackIDs()
        pprint(get_result)
        wait = input("Wait")
        
        #Get size of result list
        num_of_objects = getNumberOfObjects(get_result)
        wait = input("Wait")

        #Iterate through every object to set properties
        setMusicTrackSettings(num_of_objects, get_result, input_zerolatency, input_noncache)

            
except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

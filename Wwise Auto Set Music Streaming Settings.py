#!/usr/bin/env python3
import os
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

#####FUNCTIONS#######
def getAllMusicTrackIDs():
    #if path is empty, query the whole project for Music Tracks
    if(input_path == ""):
        args = {
            "waql": "$ from type MusicTrack"
        }

        options = {
            "return":["id", "type"]
        }

        return client.call("ak.wwise.core.object.get", args, options=options)
    #if parent path is specified, query only the descendants of that object
    else:
        args = {
            "waql": """$ "{}" select descendants""".format(input_path)
        }

        options = {
            "return":["id", "type"]
        }

        return client.call("ak.wwise.core.object.get", args, options=options)
                
def getNumberOfMusicTracks(result_dictionary):
    num_of_objects = 0
    #gets total number of objects queried
    for x in result_dictionary.values():
        for i in x: num_of_objects += 1
        
    return num_of_objects
    
def setMusicTrackSettings(num_of_objects, result_dictionary, zerolatency, noncache, lookahead, prefetch):
    count = 0
    
    while (count < num_of_objects):
        #if it's a music track, set properties
        if (result_dictionary.get("return")[count]["type"] == "MusicTrack"):
        
            object_id = result_dictionary.get("return")[count]["id"]
            
            setProperty(object_id, "IsStreamingEnabled", True)
            setProperty(object_id, "IsZeroLatency", zerolatency)
            setProperty(object_id, "IsNonCachable", noncache)
            setProperty(object_id, "LookAheadTime", lookahead)
            setProperty(object_id, "PreFetchLength", prefetch)
            
        count = count + 1
    else:
        pprint("Music streaming configuration done!")

def setProperty(object_id, propertyToSet, valueToSet):
    
    if(valueToSet != ""):
        args = {
            "object":object_id,
            "property":propertyToSet,
            "value":valueToSet
        }
        
        client.call("ak.wwise.core.object.setProperty", args)

######EXECUTION#####
try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        input_path = input("Music Hierarchy path (or leave blank): ")
        input_zerolatency = input("Zero Latency? True or False: ")
        input_noncache = input("Non-cacheable? True or False: ")
        input_lookahead = input("Look-ahead time in ms: ")
        input_prefetch = input("Prefetch length in ms: ")
        

        #pprint("Setting streaming configuration...")
        get_result = getAllMusicTrackIDs()
        #pprint(get_result)
        
        num_of_objects = getNumberOfMusicTracks(get_result)

        #input("STOP")
        setMusicTrackSettings(num_of_objects, get_result, input_zerolatency, input_noncache, input_lookahead, input_prefetch)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

import os
import pandas as pd
import numpy as np
import re
import json


def data_cleaner(filepath, savepath, overwrite = False, skip = False, varspath = "vars_of_interest.json",):
    """
    Preprocesses .xlsx files into fennec question-usefull .csv files.

    Args:
        filepath (string): The .xlsx file to process.
        savepath (string): The folder to save the .csv file.
        overwrite (bool): Skips the overwrite checker if true.
        skip (bool): Skips duplicate files instead of checking or overwriting if true.
        varspath (string): The vars-of-interest.json path. Defaults to same folder as THIS script.

    Relies on the vars_of_interest.json file to determine what data is wanted
    """

    # --- FILE & FOLDER CHECKS ---
    if not os.path.isfile(filepath): # does .xlsx file exist?
        raise FileNotFoundError(
            f"Error: Input file '{filepath}' does not exist."
        )

    if not filepath.lower().endswith(".xlsx"): # is the file an .xlsx file?
        raise ValueError(
            f"Error: Input file '{filepath}' is not an .xlsx file."
        )

    if not os.path.isdir(savepath): # does savepath exist?
        raise FileNotFoundError(
            f"Error: Save path '{savepath}' not found. "
            f"Please create the directory before running the function."
        )

    if not os.path.isfile(varspath): # does vars_of_interest.json exist?
        raise FileNotFoundError(
            f"Error: Vars-of-interest file '{varspath}' not found. "
            f"Ensure the JSON file is in the same folder as this script OR pass the filepath via arg: varspath =\" \"."
        )


    inputfile = os.path.basename(filepath) #get the name of the xlsx file
    filename = inputfile[:-5] #remove the ".xlsx" from the end
    
    # --- OVERWRITE CHECKER ---
    if (overwrite == False): #skip is overwrite was set to True
        #check savepath to see if the .xlsx file has already been processed
        for csvfile in os.listdir(savepath):
            if os.path.basename(csvfile) == f"{filename}.csv":
                if(skip == True):
                    print(f"{inputfile} skipped due to existing duplicate.")
                    return False
                
                #if a match is found, prompt the user before overwriting the file
                user_input = ""
                while (user_input != "y") and (user_input != "n"):
                    user_input = input("ARE YOU SURE YOU WANT TO OVERWRITE THIS FILE? (y,n)-->")
                if user_input == "n":
                    print(f"{inputfile} not processed due to user input.")
                    return False
    
    # --- PREPROCESSING ---
    """
    For each sheet, we want to take the relevant data at each timestamp
       and package it together in an 2D array[x][y] where x is each timestamp and y is each datatype

        [[GyrX0, GyrY0, ..., AccZ0],
         [GyrX1, GyrY1, ..., AccZ1],
         [GyrX2, GyrY2, ..., AccZ2], ...]

        Then the arrays for each sheet get combined so EVERY datatype is stored at each timestamp.
        That combined array gets saved as a .csv file.
    """

    xl = pd.ExcelFile(filepath) #load the .xlsx into a pandas array (takes the longest)

    #read the vars_of_interest file
    with open(varspath, "r") as f:
        vars_of_interest = json.load(f) #convert json file to dict

    extracted_data = {key: None for key in vars_of_interest} #stores only the designated data from each xl sheet

    #get the correct data from each sheet in the pandas array
    for sheet, variables in vars_of_interest.items():
        #make sure sheet exist in .xlsx
        if sheet not in xl.sheet_names:
            raise ValueError(
                f"Error: The sheet '{sheet}' was not found in {inputfile}. "
                f"Available sheets: {xl.sheet_names}"
            )
        
        df = xl.parse(sheet) #parse the correct sheet

        #make sure vars exist in sheet
        missing_cols = [col for col in variables if col not in df.columns]
        if missing_cols:
            raise ValueError(
                f"Error: In sheet '{sheet}', the following columns are missing: {missing_cols}. "
                f"Available columns: {list(df.columns)}"
            )        

        extracted_data[sheet] = df[variables].to_numpy(dtype=float) #save the designated data to extracted_data as a numpy array
        
        #FREQUENCY CORRECTION
        if(sheet == "RCOU" or sheet == "RCIN"):
            extracted_data[sheet] = np.repeat(extracted_data[sheet], 40, axis=0).astype(float) #IMU freq. / RCOU/IN freq. = 400Hz / 10Hz = 40

    # --- LENGTH CORRECTION ---
    min_len = min(len(arr) for arr in extracted_data.values()) # Find the minimum length among all the np arrays
    #Truncate all arrays to the minimum length
    for sheet in extracted_data: 
        extracted_data[sheet] = extracted_data[sheet][:min_len] 

    #stack all the data from each sheet into one single 2D array
    csv_data = np.hstack(list(extracted_data.values()))

    # --- SAVE AS .CSV ---
    df = pd.DataFrame(csv_data)
    new_path = os.path.join(savepath, inputfile.replace('xlsx', 'csv')) # Create new path
    df.to_csv(new_path, index=False, encoding='utf_8') # Save to new path

    print(f"{inputfile} processed and saved to {savepath} as {filename}.csv")
    return True
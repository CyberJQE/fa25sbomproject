import json
import datetime
# The generateSBOM() method uses the dictionary data structure relying on user input to fulfill the requirements of a SBOM in SPDX format. The dictionary is converted to json format.

def generateSBOM ():

    sbomList = [] # An empty list.
    while True: # The contents of the dictionary will be appended to the list.
        sbomDictionary = {
        "SPDX Version: ": "2.3",
        "License: ": "CC0-1.0",
        "SPDXID: ": "SPDXRef-Document",
        "createdBy:": input("Enter who created the SBOM: "),
        "suppliedBy:": input("Enter who supplied the SBOM: "),
        "name:": input("Enter the name of the SBOM: "),
        "packageVersion:": input("Enter the package version of the SBOM: "),
        "packageURL:": input("Enter the package URL of the SBOM: "),
        "Relationship:": input("Enter the relationship of the SBOM: "),
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}
        if "/" not in sbomDictionary["packageURL:"] or "github" not in sbomDictionary["packageURL:"]: # checks if a / is in the String. If no / is in the string a URL was not provided.
            print("You need to add a valid open-source package URL.")
        else:
            sbomList.append(sbomDictionary) # Add the SBOM to the list.
            print("The SBOM has been added.")
        inputToAdd = input("\n Do you want to generate further SBOMs? (y/n)") # Checks if the user wants to add more SBOMs.
        if inputToAdd != "y": # If the user does not enter y the loop will break and no further SBOMs will be added.
            break

    return sbomList # returns the generated SBOMs

# todo: Load the saved SBOM to a file as depicted below.
def saveSBOMs(sbomList): # Saves the loaded SBOM.
    try:
        with open('SPDXsbom.json', 'w') as sbomFile:
            json.dump(sbomList, sbomFile, indent=4)
            print("The SBOMs have been saved.")
        return True
    except Exception as e: #If the SBOM was not loaded correctly the contents of it cannot be saved.
        print("The SBOMs were not successfully saved.")
        return False


def loadSBOMs(): #Load the SBOM file.
    try:
        with open("SPDXsbom.json", "r") as sbomFile:
            sbomData = json.load(sbomFile)
            print ("The SBOM has been loaded.") # inform the user the sbom has been loaded.
            return sbomData
    except FileNotFoundError: # If the SBOM file does not exist it means the user needs to leverage the generate method.
        print("The SBOM file was not found.")
        return []
    except Exception as e:
        print("Something went wrong.")

#todo: Improved this method in which it can delete a generated SBOM.
def clearSBOMs(): # Clears the list of SBOMs and writes an empty list if the .json file exists.
    try:
        with open("SPDXsbom.json", "w") as sbomFile:
            json.dump([], sbomFile, indent=4)
        print("The list of SBOMs has been successfully deleted.")
        return True
    except Exception as e:
        print("The list of SBOMs was not successfully deleted.")
        return False

def analyzeSBOMs(sbomList): #todo: method implementation in progress.
    if not sbomList: # If a SBOM has not been generated the user will be informed.
        print("You need to generate SBOMs first before they can be analyzed.")
        return
    print("The SBOM(s) consist of the following: ")
    sbomToAnalyze = json.dumps(sbomList, indent=4)
    print(sbomToAnalyze)


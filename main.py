from SBOMBuilder import generateSBOM
from SBOMBuilder import clearSBOMs
from SBOMBuilder import loadSBOMs
from SBOMBuilder import saveSBOMs
from SBOMBuilder import analyzeSBOMs
import json

"""A CLI SBOM Application that provides the following capabilities:
    - Generate an SBOM in SPDX 2.3 format (https://spdx.github.io/spdx-spec/v2.3/relationships-between-SPDX-elements/).
    - Load an SBOM. - Loads the previously generated SBOM.
    - Save an SBOM. - Saves the generated SBOM
    - Clear an SBOM. - Clears the generated SBOM.
    - Analyze an SBOM. - Analyzes the generated SBOM and reports its components to the CLI.
    - Exit the application.
    
.json is accepted as one of the file formats for SPDX SBOMs and is leveraged.
The generated SBOM is contained in a dictionary which is appended to a list which is saved to a .json file.
"""

def main():

    while True:
        print("Hello User, welcome to an SBOM Builder where you can build SBOMs in SPDX 2.3 format.")
        print("Please select one of the following options: \n 1. Generate an SBOM\n 2. Load a generated SBOM\n 3. Save a SBOM\n 4. Clear a SBOM\n 5. Analyze a SBOM\n 6. Exit the application.")
        userInput = input("Select an option: ")
        if userInput == "1": # Option 1 generates the SBOM and creates the SPDXsbom.json file.
            SPDXsbom = generateSBOM() # Call the generateSBOM method from the SBOMBuilder.py file.
            if not SPDXsbom: # If there are no SBOMs in the list the user should be informed.
                print("There are no SBOMs.")
                continue # if no SBOMs exist return to the menu.
            try: # Try block that writes the list of SBOMs to a json file.
                sbom_json = json.dumps(SPDXsbom, indent=4)
                with open("SPDXsbom.json", "w", encoding="utf-8") as file:
                    file.write(sbom_json)
                print("SBOM generated successfully: SPDXsbom.json")
            except Exception as e:
                print("The SBOM was not generated.")
        if userInput == "2": # Option 2 loads the saved SBOMs and prints the contents to the CLI.
            loadSBOMs()
            print("The SBOM(s) have been loaded.")
        elif userInput == "3": # Option 3 saves the SBOMs and informs the user their SBOMs have been saved.
            saveSBOMs(SPDXsbom)
            print("SBOM saved successfully")
        elif userInput == "4": # Option 4 clears the contents of the SBOMs as an empty list.
            clearSBOMs()
            print("SBOM cleared successfully")
        elif userInput == "5": # Option 5 analyzes the SBOMs and reports their contents.
            analyzeSBOMs(SPDXsbom)
            print("The SBOM was analyzed successfully")
        elif userInput == "6": # Option 6 closes the application.
            print("Exiting the application.")
            break




if __name__ == "__main__":
    main()

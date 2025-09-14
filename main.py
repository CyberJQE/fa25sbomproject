import json
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier


# The generateSBOM() method uses the dictionary data structure relying on user input to fulfill the requirements of a SBOM in SPDX format. Serialization is employed in which the file is written and opened. The dictionary is converted to json format which can be uploaded on FOSSA.
#todo: Leveraging a source that can pull open source projects instead of relying on input would be the eventual goal.

def generateSBOM ():

    # todo: make the dictionary accessible to all methods in the main.py file.
    sbomDictionary = {
        "createdBy:": input(),
        "createdDate:": input(),
        "suppliedBy:": input(),
        "name:": input(),
        "packageVersion:": input(),
        "packageURL:": input(),
        "Relationship:": input()
}
    if "/" not in sbomDictionary["packageURL:"]:
        print("You need to add a valid package URL.")
    return(sbomDictionary)
newSBOM = json.dumps(generateSBOM(), indent=4)
with open("sbom.sbom", "w") as sbomFile:
    sbomFile.write(newSBOM)
SPDXsbom = generateSBOM()

# todo: Load the saved SBOM to a file as depicted below.

def loadSBOM():
    with open("sbom.sbom", "r") as sbomFile:
        sbomData = json.load(sbomFile)

    return sbomData
SPDXLoad = loadSBOM()

#todo: Use Machine Learning for the analyzeSBOM method.
def analyzeSBOM():
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    clf = DecisionTreeClassifier()
    clf.fit(x, y)
    predictions = clf.predict(SPDXLoad)
    print(predictions)

    return SPDXLoad
#todo: Improved this method in which it can delete a generated SBOM.
def deleteSBOM():
    with open("sbom.sbom", "r") as sbomFile:
        sbomData = json.load(sbomFile)
        for sbom in sbomData:
            if sbomData[sbom] is not None:
                del sbomData[sbom]
    return (sbomData)
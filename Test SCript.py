import pandas as pd

def findDuplicates(inputFileName, outputFileName):
    try:
        # Open the input file and use encoding to include all characters in ASCII table
        with open(inputFileName, "r", encoding="utf-8") as infile:
            lines = infile.readlines()  # Read all lines from the file

            # Create list to store the duplicate data
            duplicateData = []

            # Iterate through the lines in the file (start from 1 so the line numbers line up in the output file
            for lineNumber, line in enumerate(lines, 1):
                if "== Dependency" in line:  # Check for keyword
                    nextLine = lines[lineNumber].strip()    # Get next line and .strip() for readability in output file
                    duplicateData.append({
                        "Dependency Line Number": lineNumber,   # Line number of dependency keyword
                        "Next Line Number": lineNumber + 1,     # Line number of the content in the dependency
                        "Dependency Line": line.strip(),        # Dependency line, remove white space
                        "Line Content": nextLine,               # Content of dependency
                    })
            # Create the dataframe
            dataFrame = pd.DataFrame(duplicateData)

            # Checking if dataframe is not empty (dependencies found)
            if not dataFrame.empty:
                # Search for and keep only the duplicate lines
                duplicateDataFrame = dataFrame[dataFrame.duplicated(subset = ["Line Content"], keep=False)]
                # Sort the dataframe by line content (content of dependency)
                duplicateDataFrame = duplicateDataFrame.sort_values("Line Content")

        # Open the output file and use encoding to include all characters in ASCII table
        with open(outputFileName, "w", encoding="utf-8") as outfile:
            # Check for duplicates
            if not duplicateDataFrame.empty:
                # Iterate through each duplicate row of dataframe
                for x, row in duplicateDataFrame.iterrows():
                    # Format of the output file: Line A and B: Dependency Keyword: Dependency Content
                    outfile.write(f"Line {row['Dependency Line Number']} and {row['Next Line Number']}: {row['Dependency Line']}: {row['Line Content']}\n")

                # Print the summary of information for readability
                # len(duplicateData) shows total number of == Dependency lines in deps file
                #print(f"Total Amount of Dependencies in File: {len(duplicateData)}\n"
                      #f"Duplicates found and written to {outputFileName}\n")
            else:
                # If no duplicates were found, output error message and write it into output file
                outfile.write(f"No duplicates found.\n")
                print("No duplicates found.")
    # Error handling case
    except Exception as e:
        print(f"File not found: {e}")

# File names
inputFileName = "deps"
outputFileName = "Keyword Duplicates.txt"

# Function call to process the file
findDuplicates(inputFileName, outputFileName)

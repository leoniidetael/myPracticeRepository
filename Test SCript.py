def findKeyword(inputFileName, outputFileName):
    try:
        # Open the input file and use encoding to include all characters in ASCII table
        with open(inputFileName, "r", encoding="utf-8") as infile:
            lines = infile.readlines()  # Read all lines from the file
        # Open the output file and use encoding to include all characters in ASCII table
        with open(outputFileName, "w", encoding="utf-8") as outfile:
            keywordCount = 0    # Create counter to track keyword
            duplicateCount = 0  # Create counter to track duplicates

            # Iterate through the lines in the file (start from 1 so the line numbers line up in the output file
            for lineNumber, line in enumerate(lines, 1):
                if "== Dependency" in line: # Check for keyword
                    # Clear whitespace for readability in output file
                    currentLine = line.strip()
                    nextLine = lines[lineNumber]    # Get the next line

                    # Write the dependencies and the line under into output file
                    outfile.write(f"Line {lineNumber}: {currentLine}: {nextLine}\n")
                    # Increment keyword count
                    keywordCount += 1

        # Output results after the file is processed
        print(f"Keyword Count : {keywordCount}")
        print(f"Results written to {outputFileName}")

    # Error handling case
    except Exception as e:
        print(f"File not found: {e}")

# File names
inputFileName = "deps"
outputFileName = "Keyword Duplicates.txt"

# Function call to process the file
findKeyword(inputFileName, outputFileName)

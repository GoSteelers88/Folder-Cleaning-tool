# File Organization Tool

## Overview
This File Organization Tool is a Python script designed to automatically sort and organize files in your Windows 10 environment. It efficiently categorizes files from the 'Documents' and 'Downloads' directories into pre-defined folders such as 'Business', 'Personal', 'School', and 'Play'. This is done based on file types and specific keywords in the file names.

## Features
- **Automated Sorting**: Moves files to appropriate categories without manual intervention.
- **Custom Categories**: Sorts files into 'Business', 'Personal', 'School', and 'Play' folders. Additional categories can be added.
- **Error Handling and Logging**: Records actions and errors for easy auditing and troubleshooting.
- **Flexible Categorization**: Uses both file extensions and keywords for categorization.

## Setup and Usage
1. **Prerequisites**:
   - Python 3.x installed on Windows 10.
   - Basic knowledge of Python for any necessary customization.

2. **Installation**:
   - Download the script to your local machine.
   - No additional Python libraries are required.

3. **Configuration**:
   - Edit the script to include your specific paths, keywords, and file types for categorization.

4. **Running the Script**:
   - Execute the script via command line or any Python IDE.
   - Files from 'Documents' and 'Downloads' will be automatically sorted into designated folders.

## Customization
You can customize the script by editing the `file_type_keywords` and `destinations` dictionaries to match your specific organizational needs.

## Safety and Testing
- Always back up your files before running the script.
- Test the script in a controlled environment with sample files.

## Logging
The script generates a log file (`file_organizer.log`) in the same directory, which contains detailed information about the file movements and any encountered errors.

## License
This script is provided "as is", without warranty of any kind. Use at your own risk.

## Author
Nathaniel Brewer

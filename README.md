# Pynance
A program allowing you to import or create a JSON, CSV, or text file for your monthly expenditures. 

Key: "0.1.0" = Alpha, build 1, patch 0

0.1.0 (02/13/2020):
+Uploaded intial files: 
  'main.py', 'mode_json.py'
  
0.2.0 (02/15/2020): 
+Completely overhauled project files -
  Updates: 
1.  'main.py' has been reworked - 
  The file had some light editing done to remove extraneous code and imports that are no longer required. 
  The menu has also been changed -
    a. The menu changes stemmed from functionality changes and the need for simplicity.

2. 'mode_json.py' has been renamed to 'import_handler.py' - 
  The renamed file has been completely overhauled to provide options for what file to import(.JSON, .CSV, .TXT).
    a. It currently ONLY supports JSON importing. Later builds will add support for the other file types.
    b. It works by requesting user input for what file type to import and the path of the file. 
    c. Then returning values for the stored {Key: Value} pairs in the supplied JSON. 

3.  'file_creator.py' has been created -
  This file contains a method to create a new JSON file from user inputs. 
    a. The JSON file is formatted and readable by the newly created and reworked 'mod_json.py' 

4. Current issues or bugs -
  Issues- 
    a. There is no validation that the file supplied is the one expected. 
     1. I will be adding this in the next update. 
    b. It doesn't always handle incorrect inputs nicely. 
     1. I will be adding 'try'...' except' for these cases


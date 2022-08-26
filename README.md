### number-validator

Number validator is a Python program that checks whether a string is a valid Swedish social security number (personnummer), temporary social security number (samordningsnummer) or business registration number (organisationsnummer).

## Prerequisites:

* Make sure to have Python3 installed.


## Getting Started:

1. Clone the repo, or download the project as a zip file and extract it.
2. Open the project in a terminal, and run the following command in **/src**:
```
python main.py <args_1> <args_2> <args_3> ... <args_n>
```

where the input arguments resemble the personnummer, samordningsnummer or organisationsnummer sequence that you want to test. The program will validate whether the string is a personnummer, samordningsnummer or organisationsnummer. Below is an example input and output:

```
python main.py 900118+9811
```

![example](https://user-images.githubusercontent.com/28160364/186970549-7687064f-fb64-405a-9ee9-18d4937c1bb7.PNG)


## To run tests:

1. Navigate to the /test directory in a terminal window and run:
```
python TestSuite.py
```
to run the default test cases provided in the testCases.py file, located under **/tests**.


## Project Structure  
         
    .    
    
    ├── src                    
    │    ├── entities                   
    │    │      ├── Personnummer.py               # Personnummer class containing all logic for personnummer verification
    │    │      ├── Samordningsnummer.py          # Samordningsnummer class inherits Personnummer + contains additional logic
    │    │      └── Organisationsnummer.py        # Organisationsnummer class containing relevant verification logic
    │    │── util           
    │    │      ├── luhnsAlgorithm.py             # helper function for calculating the last digit 
    │    │      └── validPatterns.py              # helper functions for fetching regex-expressions for each verification type 
    │    │   
    │    └── main.py                              # Main point of execution 
    │       
    └── tests        
         ├── entities                   
         │      ├── TestPersonnummer.py           # test cases are tested "in bulk" from the testCases.py file
         │      ├── TestSamordningsnummer.py      # -''-
         │      └── TestOrganisationsnummer.py    # -''-    
         │── util           
         │      └── TestLuhnsAlgorithm.py         # Test class for luhnsAlgorithm.py                 
         │
         │── testCases.py                         # file containing invalid and valid test cases for each number type
         └── TestSuite.py                         # Main point of execution for running all test cases
         
    .

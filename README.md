# number-validator

## Getting Started:

1. Clone the repo, or download the project as a zip file and extract it.
2. Open the project in a terminal, and run the following command in **/src**:
```
python main.py <args_1> <args_2> <args_3> ... <args_n>
```

where the input arguments resemble the personnummer, samordningsnummer or organisationsnummer sequence that you want to test. The program will validate whether the string is a personnummer, samordningsnummer or organisationsnummer.


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
    │    │      ├── luhnsAlgorithm.py             # helper function for calculating the last digit, which is called in the classes above  
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

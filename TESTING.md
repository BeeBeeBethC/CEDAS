# CEDAS
Welcome to the Testing.md document for CEDAS, The Cheesecake Emporium Data Automation System.

This document has been produced due to the extensive testing conducted on this project.

# Contents
* [Full Website Testing](#full-website-testing)
* [Validator Testing](#validator-testing)
* [Debugging](#debugging)
    * [Known bugs](#known-bugs)
    * [Resolved Bugs](#resolved-bugs)
    * [Existing Bugs](#existing-bugs)
* [Further Testing](#further-testing)
## Testing

### PEP8 validation
(INSERT SCREENSHOTS OF PEP8 VALIDATION)

### Bugs
#### API not linking
My API that I had generated using google sheets wasn't connecting I had written google.oauth.service_account when it should have been google.oauth2.service_account.
    
#### Infinite while loop
This was human error as I'd accidentally put my programme into an infinte while loop requesting data due to no 'if' statement even though data had been input. I also forgot to comment out prior code for testing if the API was successfully connected which could have been a contributing factor.

#### Unable to update sales worksheet
This was due to human error not providing correct commands therefore the programme would not run or update and kept throwing an error back(see screenshot) in and not updating the corresponding sheet.

#### Unable to return stock averages
Due to an undefined variable it kept throwing back an error.

(INSERT SCREENSHOTS OF BUGS BEFORE AND AFTER SQUASHING!)

### Solved bugs

#### API not linking 
It turned out I'd missed a numerical value in the command. Once corrected the error was squashed and programme ran as expected.

#### Infinite while loop 
to get myself out of the while loop I sent the command 'exit()' this still didn't work and I'd realized that this command is specific for python shell. I then tried CTRL-C which worked and the while loop stopped. Once stopped I commented out the code that I used to check that the API was connected. On fixing the while loop by removing the partially written loop I had output as expected.

#### Unable to update sales worksheet
by providing correct commands to the programme, it was able to identify what I wanted it to do and update successfully as shown in the screenshot below highlighted by the values in Blue. 

#### Unable to return stock averages
once defining the variables under the main function, code was running as expected and returning stock values to terminal. 

### Remaining bugs

### further testing

further testing was completed on:
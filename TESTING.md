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
Full Manual Testing performed. results as shown
| Website Feature   | Expected Outcome | Testing Performed | Result | Pass or Fail |
| ----- | ----- | ----- | ----- | ----- |
| Menu Selection |
| Displays menu selection when heroku terminal opened | Menu displays on appplication start up | Clicked view from heroku deployment | Terminal opened and displayed menu options | PASS |
| Press 1 | Application runs | Pressed 1, hit enter, followed onscreen prompts | Returned stock to order in terminal, checked spreadsheet and confirmed data had been added. | PASS |
| Press 2 | Shows instructions | Pressed 2, hit enter | Instructions shown | PASS |
| Press 3 | Displays data from a date input from user | Entered a date | Data shown from date input | PASS |
| Press 4 | Fetches all stock data | Pressed 4, hit enter | Stock data shown in terminal | PASS |
| Press 5 | Exit the programme | Pressed 5, Pressed Enter | programme exits | PASS |
| Validation |
| Input validation | Returns an error message to user saying for example "-2 is not valid" | Entered -2, !, /, ., ' ' 2 | returned invalid inputs until 2 was entered | PASS |
| Invalid choice | If users press numbers that aren't the ones declared in choice selection or prematurely given, prior to choice selection being available they automatically recieve an "Invalid choice message" | Entered 66 as a choice and entered it prematurely | Recieved invalid choice please press '1', '2', '3', '4' or 5'. alternatively press 2 for instructions got returned to menu choice. | PASS |
| Date validation | Returns invalid date, please try again | Entered 28/08/2024 | Returned invalid date input error please input as YYYY-MM-DD | PASS |
|  |  |  |  |  |

### PEP8 validation
![pep8-validation-during](/documentation-images/pep8.png)

Before taking this screenshot, I had already started clearing excessive white space and alsoformatting the document correctly.

![pep8-validation-post](/documentation-images/pep8-post.png)

Post validation, no errors were found. The author wanted to provide a before and after for comparison and to show what the pep8 validation looked like during and after validation testing.

### Bugs
#### API not linking
My API that I had generated using google sheets wasn't connecting 
    
#### Infinite while loop
This was human error as I'd accidentally put my programme into an infinte while loop requesting data due to no 'if' statement even though data had been input. I also forgot to comment out prior code for testing if the API was successfully connected which could have been a contributing factor.

#### Unable to update sales worksheet
This was due to human error not providing correct commands therefore the programme would not run or update and kept throwing an error back(see screenshot) in and not updating the corresponding sheet.

#### Unable to return stock averages
Due to an undefined variable it kept throwing back an error.

![throwback-error](/documentation-images/throwback-error.png)

#### No Module Named 
As a result of forgetting to add the requirements.txt doc to enable Heroku to read the programme fully.
![no-module-named-error](/documentation-images/no-module-named.png)

#### No module named
Once requirements.txt doc added and pushed to GitHub, the programme passed another error.
![creds.json-not-configured](/documentation-images/creds.json-not-configured.png)

#### creds.json
Missing curly braces. Due to human error I’d copied and pasted the Creds.json without the curly braces resulting in the wrong format. 

#### typeError
replit pointed out this error which the author had missed

![type-Error](/documentation-images/instance-error.png)

#### Try, Except Statement not working
Broke out of the loop prematurely without fetching the rest of the data for headers.
![try-except-not-working](/documentation-images/try-except-not-work.png)

Rewrote the try and except statement.

### Solved bugs
#### API not linking 
It turned out I'd missed a numerical value in the command. I had written google.oauth.service_account when it should have been google.oauth2.service_account. Once corrected the error was resolved and programme ran as expected.

#### Infinite while loop 
To get myself out of the while loop I sent the command 'exit()' this still didn't work and I'd realized that this command is specific for python shell. I then tried CTRL-C which worked and the while loop stopped. Once stopped I commented out the code that I used to check that the API was connected. On fixing the while loop by removing the partially written loop. The outcome was as expected.

![infinite-while-loop](/documentation-images/infinite-while-loop.png)

#### Unable to update sales worksheet
by providing correct commands to the programme, it was able to identify what I wanted it to do and update successfully as shown in the screenshot below highlighted by the values in Blue. 

![original-data](/documentation-images/original-data.png)

#### Unable to return stock averages
once defining the variables under the main function, code was running as expected and returning stock values to terminal. 

![variable-not-defined](/documentation-images/add-defined.png)

#### creds.json
By replacing the curly braces in the correct place the programme ran as expected. 

![programme-working](/documentation-images/working.png)

#### TypeError
once spelling corrected, the programme worked as expected.

#### Try, Except statement
once the try, Except statement had been reviewed and adjusted, programme worked as expected.

### Remaining Bugs

No remaining bugs are in the project.

### Further Testing

further testing was completed on:

* A huawei laptop

with no issues identified.

Thank you for viewing the testing.md document for CEDAS.
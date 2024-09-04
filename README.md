![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


# CEDAS
The Cheesecake Emporium Data Automation System. 

## What is The Cheesecake Emporium? 
The Cheesecake Emporium is a hypothetical Cheesecake company who have requested a data automation program that helps them to reduce waste and increase their sales numbers. Currently they have a static stock order arriving daily and are loosing sales due to stock not being sold.

## Why use CEDAS?

The aim of CEDAS is to provide an automated program that will assist in monitoring and increasing sales whilst reducing waste by altering stock numbers dynamically rather than static as it currently stands. In turn this should help the owners manage sales, stock and more, efficiently by requesting data stored in an API (Application Programming Interface) that the author has generated based off of the data that has been provided by the company. by Using CEDAS, the Owners can then request and return most recent numbers and any manipulated data for review and replenish stocks more efficiently.

## How to use CEDAS

(STEP BY STEP INSTRUCTIONS FOR HOW TO USE APPLICATION.)

## Existing Features

Before implementing the dynamic system that CEDAS offers, the owners of Cheesecake Emporium were manually tracking data using pen and paper. By implementing CEDAS, this has now taken static stock replenishment to dynamic stock replenishment by analysing the sales data and surplus data and providing stock order numbers to avoid excess waste for the company.

## Future Implementations

## Data Models

## Testing
### bugs
API not linking 
My API that I had generated using google sheets wasn't connecting I had written google.oauth.service_account when it should have been google.oauth2.service_account. 
    
Infinite while loop 
This was human error as I'd accidentally put my programme into an infinte while loop requesting data due to no 'if' statement even though data had been input. I also forgot to comment out prior code for testing if the API was successfully connected which could have been a contributing factor.

### solved bugs

API not linking 
It turned out I'd missed a numerical value in the command. Once corrected the error was squashed and programme ran as expected.

Infinite while loop 
to get myself out of the while loop I sent the command 'exit()' this still didn't work and I'd realized that this command is specific for python shell. I then tried CTRL-C which worked and the while loop stopped. Once stopped I commented out the code that I used to check that the API was connected. On fixing the while loop by removing the partially written loop I had output as expected.

### remaining bugs

### PEP8 validation

## Deployment Instructions

CEDAS was deployed to both Github and Heroku. 

reasons for deploying to Github was to monitor version control.

### Github Clone
To clone a copy of CEDAS from the Github repository, please follow these steps:

1. Go to the repository you wish to clone, project link is as follows. (https://github.com/BeeBeeBethC/CEDAS)

2. Click on the green button that reads 'Code'.

3. On the dropdown menu, please select the 'Copy URL to clipboard' option this button looks like two squares overlaying one another. 

4. Open your favourite code editor, for myself it is Visual Studio Code. on Visual Studio Code, click the 'source control' button from the left hand menu. 
4a. Alternatively, open the terminal and change your working directory to the location of the cloned repository. 

5. Paste the repository URL into the top navigation bar of Visual Studio Code. 
5a. Alternatively type 'git clone' into the terminal and paste the URL link.

6. Save the repository to a localised folder where the repository will be stored on your computer. 

7. Click on select repository location. 

8. Let the repository download and click 'open' when the on screen prompt shows in the lower right corner of the screen.

### Github Fork

To fork the repository of CEDAS, please follow these steps.

1. Sign up or login to Github.

2. Go to the repository for CEDAS (https://github.com/BeeBeeBethC/CEDAS)

3. Click the fork button on the top right hand side of the screen.

PLEASE NOTE: the steps followed above will provide the code only. to access the project from Heroku, please continue to follow the steps below. 

### Heroku Deployment

WRITE OUT HEROKU DEPLOYMENT

## Credits
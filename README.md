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

Unable to update sales worksheet
This was due to human error not providing correct commands therefore the programme wopuld not run or update and kept throwing an error back(see screenshot) in and not updating the corresponding sheet.

unable to return stock averages
due to an undefined variable it kept throwing back an error.

### solved bugs

API not linking 
It turned out I'd missed a numerical value in the command. Once corrected the error was squashed and programme ran as expected.

Infinite while loop 
to get myself out of the while loop I sent the command 'exit()' this still didn't work and I'd realized that this command is specific for python shell. I then tried CTRL-C which worked and the while loop stopped. Once stopped I commented out the code that I used to check that the API was connected. On fixing the while loop by removing the partially written loop I had output as expected.

Unable to update sales worksheet
by providing correct commands to the programme, it was able to identify what I wanted it to do and update successfully as shown in the screenshot below highlighted by the values in Blue. 

unable to return stock averages
once defining the variables under the main function, code was running as expected and returning stock values to terminal. 

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
1. Create your list of requirements by navigating to the requirements.txt file. each package is known as a dependency so therefore should be located in this file when uploading to heroku so that Heroku itself can still open your project. 

2. To create your list of requirements, type in the gitpod (or code terminal of your choice) "pip3 freeze > requitements.txt" ensuring you have the exact same spelling, all lower case for the exact file name or this will not work.

3. Commit and push most recent code upto github.

4. If not done already, sign-up or login to heroku.

5. navigate to your heroku dashboard. 

6. from the heroku dashboard, create a new app and name it. each app name needs to be unique or it wont accept it.
7. select region. 
8. make sure your settings have been set before you deploy! 
9. if settings are not declared, here are the steps for checking settings before deployment. 
    9.1. find the config vars, environmental variables section of the heroku settings. In this tab "Reveal config vars" this is where you put sensitive information for example creds.json that can't be shown publicly.
    for more compatibility, also add another config var to heroku settings which is a port key: PORT value is 8000. this ensures a much smoother deployment as projects may not deploy if not added in.
10. navigate to add build pack. select "python" and click save changes then find "node.js" and click save changes. 

NOTE: If these two packages are the opposite way round you can click and drag them so that python pack is on top and node.js is below python. 

11. For this project there is the choice of automatic deployment or manual. For CEDAS I have chosen to manually deploy it which means that it won't automatically update from pushed changes but it does show deployment logs. 

12. To update the project once deployment has complete, navigate to  

13. Once the project has been deployed you should recieve a message stating that "project was successfully deployed" and you should be able to click a link that takes you to the application terminal where you can run your code in Heroku. 

14. In the heroku terminal there is no need to run python3 run.py as the programme is already running, to restart this programme you can click the red button at the top that states "run programme" and has a play symbol on it.  

## Credits
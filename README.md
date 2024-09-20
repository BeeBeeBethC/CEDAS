# CEDAS
The Cheesecake Emporium Data Automation System.

![responsive](/documentation-images/responsive-design.png)

# Contents

* [What is The Cheesecake Emporium?](#what-is-the-cheesecake-emporium)
    * [Why use CEDAS?](#why-use-cedas)
    * [How to use CEDAS](#how-to-use-cedas)
* [Target Audience]()
* [User Experience]()
* [Existing Features](#existing-features)
    * [Future Implementations](#future-implementations)
    * [Technologies and Libraries Used]()
* [Data Model](#data-model)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Clone The Repository](#how-to-clone-the-repository)
    * [How To Create A Fork](#how-to-fork-the-repository)
    * [Deployment to Heroku](#heroku-deployment)
* [Credits](#credits)
    * [Content](#credits)
    * [Media](#credits)

## What is The Cheesecake Emporium?
The Cheesecake Emporium is a hypothetical Cheesecake company who have requested a data automation program that helps them to reduce waste and increase their sales numbers. Currently they have a set amount of stock arriving daily (static stock) and are loosing sales due to excess stock not being sold.

## Why use CEDAS?

The aim of CEDAS is to provide a semi-automated programme that will assist in monitoring and increasing sales. furthermore, this will also reduce waste by adopting more dynamically generated stock numbers, following user input and in turn replenishing stocks more efficiently.

## Existing Features

By implementing CEDAS, this has now taken static stock replenishment to dynamic stock replenishment by analysing the sales data and stock data to order stock in a much more fluid way dependant on sales numbers which in turn avoids excess waste for the company. existing features go more in depth as I walk you through how to use CEDAS.

please note: some of the following screenshots were taken during the project and once deployed. 

## How to use CEDAS

Welcome to CEDAS. please follow the steps below to use the system correctly.

On application start up, users are asked to select a function from menu options using numbers '1, 2, 3, 4 or 5'. To confirm your choice, Press Enter.

![menu-selection](/documentation-images/menu-selection.png)

When users select Option 1, users can type in latest sales figures for the cheesecake sold. please enter your value and press enter to allow CEDAS to confirm the value. NOTE: CEDAS is designed to continually ask for values correspoding to cheesecake flavours depending on input validity. This validity check also accounts for symbols such as (", !, ., \, %) and negative integers and asks for input to be entered again.

![input-validity](/documentation-images/input-validity.png)

When users select Option 2, CEDAS will bring up Instructions on how to use the application. please allow the application to run until the menu options appear again.

In the Heroku terminal, You need to scroll up to see the instructions but once scrolled up and positioned. All Instructions fit in the terminal window as shwon in the screenshot.

![how-to-use](/documentation-images/how-to.png)

When users select Option 3, Users can fetch data from a set date. 

NOTE: CEDAS returns values after 01-08-2024 no matter what date you put in prior to 01-08-2024.

any data input after the dates declared below will result in an empty table shown in the following screenshot because future data does not exist.

![data-does-not-exist](/documentation-images/data-does-not-exist.png)

the following screenshot shows the before and after date manipulation and input. prior data before is indented to the left of the boxes and data input after date established is indented to the right. 

![data-following-date-manipulation](/documentation-images/data-following-date-manipulation.png)

To search and explore data within the spreadsheet data use dates between 01-08-2024 - 08-09-2024, written in format 'YYYY-MM-DD'. As you can see from the screenshot below, CEDAS will deem any other input invalid. The data updates every time the programme is run. 

Note: As of 20-09-2024, the spreadsheet dates run up until date 20-09-2024. However the output in the spreadsheet is subject to change due to the nature of CEDAS and may be different on review.

![date-validity](/documentation-images/date-not-valid.png)

5. Option 4 retrieves all stock data. Stock data cannot be manipulated. However when run through the programme, the latest stock to order will be shown in the terminal as a result of sales data input.

![stock-shown-in-terminal](/documentation-images/stock-shown.png)

6. Option 5 Exits the programme.
Please note: whilst programme is running, CEDAS will ask for user input until option 5 is selected and exits the programme. 

![exiting-the-application](/documentation-images/exit.png)

## Future Implementations
#### Handling Future Dates. 
As it stands CEDAS returns an empty table if dates put in are dates from sometime in the future (see screenshot for example) simply because they do not exist in the existing database. 

![data-does-not-exist](/documentation-images/data-does-not-exist.png)

Other future implementations may include more opportunities for date manipulation directly from the terminal and more options to retrieve and explore past stock data not just sales data from the API using dates.

another future implementation would be that the instructions under option 2 pop up into a separate space that then has a button to return to normal menu before being able to select another option and move on.

Other future implementations eventually may include the option to intergrate stock replenishment from running the programme.

For this project CEDAS does exactly what the author wanted and has literally brought an idea from imagination to an application.

## Technologies and libraries used in CEDAS
* Gitpod - coding workspace
* Github - storage and commit history
* Heroku - hosting platform for CEDAS
* Replit - used to aid with debugging.

### Languages

For this project, the only language required was python the author has also used compatible libraries that are outlined below. 

This is because our brief was to create a Command - Line - Interface (CLI) application that users can interact with by typing commands or specifics into a terminal or console interface.

### Google Sheets and Libraries used 
Google sheets was used for generating the API or database that directly corresponds to CEDAS

Gspread is used as a Python API to interact with Google Sheets. It is a Python library that enables Python to communicate and retrieve requests directly with an external API straight to the console or terminal output.

PrettyTable was used to generate the table of outcomes as shown in several screenshots in this readme as well as in the actual terminal when using the application.

Datetime was used to generate and add dates to the Google sheet API using the gspread library to add dates to existing data in the spreadsheet.

## Data Models

![data-model](/documentation-images/flowchart.png)

This was the initial data model I had drawn up. 

Over the duration of the project this changed slightly as the project began to evolve and grow. To outline a major change from this data model. The 'surplus' sheet has been removed so the programme just works with sales and stock worksheets. Whilst still calculating, updating and retrieving corresponding data correctly.

## Testing
For testing documentation, see TESTING.md file. 

## Deployment Instructions

CEDAS was deployed to both Github and Heroku.

The reason for deploying to Github as well as Heroku was to monitor version control and commits throughout the project.

### Github Clone
To clone a copy of CEDAS from the Github repository, please follow these steps:

1. Go to the repository you wish to clone, project link is as follows. (https://github.com/BeeBeeBethC/CEDAS)

2. Click on the green button that reads 'Code'.

3. On the dropdown menu, please select the 'Copy URL to clipboard' option this button looks like two squares overlaying one another.

4. Open your favourite code editor, for myself it is Visual Studio Code. on Visual Studio Code, click the 'source control' button from the left hand menu.

(Alternatively, open the terminal and change your working directory to the location of the cloned repository.)

5. Paste the repository URL into the top navigation bar of Visual Studio Code.

(Alternatively type 'git clone' into the terminal and paste the URL link.)

6. Save the repository to a localised folder where the repository will be stored on your computer.

7. Click on select repository location.

8. Let the repository download and click 'open' when the on screen prompt shows in the lower right corner of the screen.

### Github Fork

To fork the repository of CEDAS, please follow these steps.

1. Sign up or login to Github.

2. Go to the repository for CEDAS (https://github.com/BeeBeeBethC/CEDAS)

3. Click the fork button on the top right hand side of the screen.

PLEASE NOTE: The steps followed above will provide the code only. To access the project from Heroku, please continue to follow the steps below.

### Heroku Deployment

The live link to CEDAS can be found here (https://portfolio-project-3-cedas-519829212c7c.herokuapp.com/)

To deploy to Heroku, please follow these steps:

1. Create your list of requirements by navigating to the requirements.txt file. each package is known as a dependency so therefore should be located in this file when uploading to heroku so that Heroku can still open projects.

2. To create your list of requirements, type in the gitpod (or code terminal of your choice) "pip3 freeze > requirements.txt" ensuring you have the exact same spelling, all lower case for the exact file name or this will not work.

3. Commit and push most recent code upto github.

4. If not done already, Sign-up or Login to Heroku.

5. Navigate to your Heroku dashboard.

6. From the Heroku dashboard, create a new app and name it. Each app name needs to be unique or it won't accept it.

7. Select region.

8. Make sure your settings have been set before you deploy.

9. If settings are not declared, here are the steps for checking settings before deployment.
    1. Find the config vars section. (these are environmental variables section found in heroku settings). In this tab "Reveal config vars" this is where you put sensitive information for example creds.json that can't be shown publicly.
    2. (For Code Institute Students only) For more compatibility, also add another config var to heroku settings which is a port key: PORT value is 8000. This ensures a much smoother deployment as projects may not deploy if this is missed out.

10. Navigate to add build pack and Select "Python". Click save changes then find "node.js". select and click save changes.
NOTE: If these two packages are the opposite way round you can click and drag them so that python pack is on top and node.js is below python.
This step is important to ensure the project will be set up properly.

11. For this project there is the choice of automatic deployment or manual. For CEDAS the author has chosen to manually deploy it which means that it won't automatically update from pushed changes but it does show deployment logs along the way.

12. To manually update and re-deploy the project using the main branch:
    1.  Firstly make sure your most recent changes have been pushed to github and confirm these before moving onto the next step.
    
    2.  Navigate back to project overview and select the deploy option from the navigation menu at the top of the page.
    
    3.  Scroll down the deploy page until you reach manual deploy.
    
    4.  Choose branch to deploy, make sure it's the main branch.
    
    5.  Click the deploy button. (return to follow steps 13 onwards)

![final-deployment-stages-to-Heroku](/documentation-images/final-dep-stages.png)

13. Once the project has been deployed you should recieve a message stating that "Your app was successfully deployed" and you should be able to click 'view' that takes you to the application terminal where your code is running in Heroku.

14. In the heroku terminal there is no need to run "python3 run.py" command as the programme is already running. After exiting the application, in order to restart this programme you can click the red button at the top that states "run programme" with a play symbol on it.

## Credits
### Content
Love-sandwiches walkthrough was completed and some of the ways that code was generated was used for inspiration in this project also.

Source code for love sandwiches can be found at: (https://github.com/Code-Institute-Solutions/love-sandwiches-p4-sourcecode)

The authors own love sandwiches walkthrough project can be found here: (https://github.com/BeeBeeBethC/LoveSandwichesWalkthrough)

Gspread information gained from the official gspread documentation found at this link here (https://docs.gspread.org/en/latest/)

Prettytable knowledge and information gained from this link here (https://pypi.org/project/prettytable/)

Datetime knoweledge and information found at this link here (https://docs.python.org/3/library/datetime.html)

To learn a bit more in depth and for more information on google sheets was found at this link here courtesy of youtuber: Tech With Tim (https://www.youtube.com/watch?v=zCEJurLGFRk)

For a deeper understanding of Python following LMS completion and to confirm and learn more knowledge on Python. Youtuber: Bro Code's video (https://www.youtube.com/watch?v=XKHEtdqhLK8&t=1260s) was viewed. 

I also used Replit for debugging purposes specifically spotting a typo error that id completely missed during the creation of this project. 

try, Except statement reviewed from W3Schools here: (https://www.w3schools.com/python/python_try_except.asp)

### Media
screednshots used in this project are all authors own.
### Acknowledgements

I would like to say a huge thank you to my family and friends for the continual support and putting up with my occasional rants whenever things don't go right and the joint celebrations when thing's do play out the right way intended.

I would like to say a huge Thank You to my awesome Mentor Luke Buchanan. for his guidance through out this projects and previous projects completed.

I would like to send a shout out to Kera Cudmore who provides an excellent readme document that I continually to use for guidance for my own readme documents. 

I also would like to thank all staff members at Code Institute.
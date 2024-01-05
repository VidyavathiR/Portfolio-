# Portfolio-

Welcome to my personal portfolio!

## Overview

This personal portfolio is built using HTML, CSS, and JavaScript. It is designed to provide visitors with information about who I am, the projects I've worked on, and the skills I possess. The portfolio also includes an Excel sheet to store additional information.

## Features

- **Responsive Design:**
  - The portfolio is designed to be responsive and accessible across various devices and screen sizes.

- **Portfolio Sections:**
  - Organized sections such as "About Me," "Projects," "Skills," "Education," and "Contact."

- **Skills Matrix:**
  - Visual representation of skills to provide a quick overview.

- **Contact Form:**
  - A contact form for visitors to reach out.

- **Interactive Elements:**
  - JavaScript-powered interactive elements to enhance the user experience.

## Submit a Form to Google Sheets 


## Create an HTML form that stores the submitted form data in Google Sheets using plain 'ol JavaScript (ES6), Google Apps Script, Fetch and FormData.
- **Create a new Google Sheet:**
  - First, go to Google Sheets and Start a new spreadsheet with the Blank template.
  - Rename it abc. Or whatever, it doesn't matter.

- **Create a Google Apps Script:**
  - Click on Tools > Script Editor… which should open a new tab.
  - Rename it Submit Form to Google Sheets. Make sure to wait for it to actually save and update the title before -editing the script.
  - Now, delete the function myFunction() {} block within the Code.gs tab.
  - Paste the googlesheet.js script in it's place and File > Save:

- **3. Run the setup function:**
  - Next, go to Run > Run Function > initialSetup to run this function.
  - In the Authorization Required dialog, click on Review Permissions.
  - Sign in or pick the Google account associated with this projects.
  - You should see a dialog that says Hi {Your Name}, Submit Form to Google Sheets wants to...
  - Click Allow

-**5. Add a new project trigger**
 -Click on Edit > Current project’s triggers.
 -In the dialog click No triggers set up. Click here to add one now.
 -In the dropdowns select doPost
 -Set the events fields to From spreadsheet and On form submit
 -Then click Save

-**5. Publish the project as a web app**
 -Click on Publish > Deploy as web app….
 -Set Project Version to New and put initial version in the input field below.
 -Leave Execute the app as: set to Me(your@address.com).
 -For Who has access to the app: select Anyone, even anonymous.
 -Click Deploy.
 -In the popup, copy the Current web app URL from the dialog.
 -And click OK.

-**Run the index.ḥtml file.**

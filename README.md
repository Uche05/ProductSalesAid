# [Uche's PAS](https://product-sales-aid-a1201459a834.herokuapp.com/)

- A company, Uche's Product Sales Company[imaginative] uses this software to automate having a spreadsheet of the details they need from their customers when their customers want to make a purchase of certain products.
- Uche's PAS(Product Sales Aid) is a Command-Line Interface website itinerary used to register a company's details along with an amount of products they want.


## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

[Mock-up Screenshots](#mockup-screenshots)


[User Stories](#user-stories)

- [User Goals](#user-goals)
- [Returning Site Users](#returning-site-users)



[Features](#features)

- [Existing Features](#existing-features)
- [Future Features](#future-features)

- [Testing](#testing)
- [Features](#features)

[Deployment](#deployment)

  - [Cloning](#cloning)
  - [Forking](#forking)


[Credits](#credits)

- [Content and Code](#content-and-code)
- [Acknowledgments](#acknowledgements)

</details>


User goals:
Get clear instructions on how to use the system in front of them that they can refer to if needed. The ability to input their details including dates of work, days, and hours. Retrieve their employee number. Get an estimate of tax and national insurance due to be paid. Receive a copy of the information inputted via email.

Site owner goals
Provide a program that is easy to use and maintain. Present a program that gives clear instructions each time a contractor visits. Get access to the information inputted by users via email. Develop a program that can have additional features added at a later date. Add the submitted information to Google Sheets with one sheet for information before tax and the other sheet containing tax and national insurance information.

Pre development
I wrote out notes and created a flow chart. All I had to do then is follow my notes and code one area at a time before moving on to the next. I set up projects in GitHub to write out work that needed to be done. The aim is to provide early and continuous delivery of the project.


## Tools & Technologies Used

- [Heroku](https://dashboard.heroku.com/apps) used for hosting the deployed front-end & back-end site.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitPod's Workspace](https://codeinstitute-ide.net/workspaces) used to manage and run the development workspace for the Product Sales Aid project seamlessly.
- [PEP8 CI Linter](https://pep8ci.herokuapp.com/#) used to do checks for errors on my Python Code.
- [Microsoft Visio](https://www.microsoft365.com/launch/Visio/?auth=2&home=1) used as flowchart making tool to make the steps the application would take.
- [VSCode](https://code.visualstudio.com/) used for local IDE for development. It possessed extensions which helped me immensely during my making of the site.
- [W3C HTML Validator](https://validator.w3.org/) used to do checks for errors on HTML elements of the official website.

## Python Packages Used
- ### gspread
- ### re(Regular Expression)
- ## google-auth


## Testing
Testing
The portal has been well tested and the results can be viewed here - TESTING

## Features

### Future Updates
- The ability to actually send automated emails to the given email addresses.
- Improve the UI of the CLI site
- 


Validation
PEP8 - Python style guide checker imported - https://pypi.org/project/pep8/ All code validated and where lines were showing as too long they were adjusted. Some line adjustments caused bugs in the code and it stopped working so they were left as longer lines to avoid this issue. pycodestyle . - was used in Codeanywhere terminal to list any issues.

Deployment


Bugs
After importing the type element so that text can be typed out a line at a time the codes for Fore.WHITE or bold kept showing up e.g. '\033[1m' for bold was typed out. To fix this I had to remove - colorama.init(autoreset=True) - which meant I had to go through each line of code to ensure if one line was red, all subsequent lines didn't turn red.

## Deployment

The site was deployed to GitHub Pages. The steps to deploy are as follows:

### Heroku
The Application has been deployed from GitHub to Heroku by following the steps:

- Create or log in to your account at heroku.com
- Create a new app, add a unique app name ( for example corri-construction-p3) and then choose your region
- Click on create app
- Go to "Settings"
- Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file. Also add a key 'PORT' and value '8000'.
- Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
- Go to "Deploy" and select "GitHub" in "Deployment method"
- To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
- Choose the branch you want to build your app from
- If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
- Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.
- Branching the GitHub Repository using GitHub Desktop and Visual Studio Code
- Go to the GitHub repository.
- Click on the branch button in the left hand side under the repository name.
- Give your branch a name.
- Go to the CODE area on the right and select "Open with GitHub Desktop".
- You will be asked if you want to clone the repository - say yes.
- GitHub desktop will suggest what to do next - select Open code using Visual Studio Code.
- The deployed project live link is HERE - Use Ctrl (Cmd) and click to open in a new window.


#### Cloning

- You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Uche05/ci-p2-Uche's PAS(Product Sales Aid)).
2. Locate the Code button above the list of files and click it.
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard.
4. Open Git Bash or Terminal.
5. Change the current working directory to the one where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/Uche05/ci-p2-Uche's PAS(Product Sales Aid).git`
7. Press Enter to create your local clone.

For Gitpod users, this was not implemented on gitpod, it was from my local PC directly to Github via git and some useful VSCode extensions.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Uche05/ci-p2-Uche's PAS(Product Sales Aid)).
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account.


## Credits

The following are credits to various people and technologies that have directly or otherwise assisted in the creation of the Uche's PAS(Product Sales Aid) site.

### Content and Code

| Source | Location | Notes |
| --- | --- | --- |
|[Javascript Code-Check Aid- ChatGPT](https://chatgpt.com/)| Tool to check javascript code as i wrote it | The JavaScript code I wrote was often quite messy, so I used ChatGPT to help correct and update it. Through this process, I learned how to use arrow functions (=>), the forEach function, and discovered the flexibility JavaScript offers, such as storing objects in arrays— something Python doesn’t do as easily. Thanks to ChatGPT’s guidance, my final JavaScript code was error-free. |
|[Markdown Used](https://github.com/boderg/your-weather)|Markdown| Markdown template was from the given [github repo](https://github.com/boderg/your-weather) for the both "README" and "TESTING"|
|[Code snippets](https://github.com/Uche05/ci-p2-Uche's PAS(Product Sales Aid))|Javascript Code Snippets for loading and using enter key | Javascript code use of loading and use of enter key was inspired from  [Love Math Project](https://github.com/Uche05/love-maths-uche05) taught officially by Code Institute.|


### Acknowledgements

- I would like to thank my Code Institute mentor, [Jubril Akolade](https://github.com/10xOXR) for his support throughout the development of this project and hopes he enjoys his vacation time.
- I would like to thank [Code Institute](https://codeinstitute.net) for giving me the opportunity to complete the P2 course.
- I would like to thank the [Code Institute](https://codeinstitute.net) facilitator team, [Iris Smok](https://github.com/Iris-Smok/Iris-Smok), [the Code Institute Student Care Team](studentcare@codeinstitute.net) and [Irene Neville](
irene.neville@codeinstitute.net) for their advice.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) and [new friend, Darragh_Drennan](https://code-institute-room.slack.com) for the moral support and general information that helps with my studies with Code Institute.
- I would like to appreciate the [W3schools website](https://www.w3schools.com/) and [OpenAI's ChatGPT](https://chatgpt.com/) for their free websites and resources that educate on many technological  and coding concepts intuitively and enabled me understand and learn how to craft needed stuff for my website.
- I would like to thank my family, for their support and understanding, for believing in me, and allowing me to make this transition into software development.
- I personally enjoyed performing this project as it was a chance to both construct and actually program using coding programming techniques and paradigms; to make a functional content myself through research and personal study.
- Written and edited by Uchechukwu Christian Kpadeuwa

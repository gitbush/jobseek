# Jobseek

<a href="">Jobseek</a> serves as a tool for employers to advertise new positions within the company. Jobseekers can view these jobs with information on how to apply.

Jobseek is my DCD (Data Centric Development) milestone project for Code Institutes Full Stack Web Developer course. Project breif below.

I chose to go with my own idea of a job advertisement site while still following the project guidlines and requirements.

### CI breif
- **CREATE AN ONLINE COOKBOOK**
    - Create a web application that allows users to store and easily     access cooking recipes
    - Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
    - Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course)
    - Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation
    - Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes).
    - Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large.
    - Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions.
    - Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.
    - Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure).

- **CREATE YOUR OWN PROJECT**
    - If you choose to create your project outside the brief, the scope should be similar to that of the example brief above. If you want some ideas, please ask your mentor for advice and direction.


## UX

#### Jobseek was created with two users in mind:

  **As an employer I want:**

  1. An easy user interface to post available job opportunites at my company for jobseekers to view.
  2. A way for jobseekers to apply for roles.
  3. To edit any job posts I have made with potential updated content.
  4. To remove/delete a filled or no longer available job post.
  5. Any job posts that I have created are protected from risk of modifying/deleting from anyone other than the creator.
  6. *To see all job posts that I have created*
  7. *To be able to show my company name and logo*
  8. *To be able to update my logo*
  
  **As a jobseeker I want:**

 1. To view any new roles that are available.
 2. To view any roles that are within a certain sector, salary, location and employment type or a mixture of all.
 3. Details on how to apply for any roles of interest.
 4. See how long job posts have been advertised.
 5. *Know how many other jobseekers have applied for certain roles.*
 6. *To order job posts based on different criteria*
  
### Requirements

To acheive the users needs I concluded the following requirements would be needed:

- **Database** - Mysql was used as the RDMS with the following tables:
    - Employer - To store all registered employers
    - Job posts - To store all created job posts
    - Location - To store a list locations for filtering
    - Sector - To store a list sectors for filtering

- **Users** - Flask login was used for easier employer account management

    | Users        | Add/edit/delete posts  | Browse job posts |
    | ------------- |:-------------:|:-------------:| 
    | Anonymous      | No | Yes
    | Registered employer      | Yes      | Yes
    
### Design Choices

**Logo**
  
  <span><img src="jobseek/static/assets/images/Jobseek.png" width=15%></span> was designed using <a href="https://hatchful.shopify.com/">Hatchful</a> free logo maker.
  
**Colors/theme**
- The site color scheme was based off the Jobseek logo above with all button colors fluorescent blue of the logo and the footer and refine section dark blue/grey of the JOBSEEK name.
- These were chosen as they provide a clean aspect and contrast each other well. 

**Icons**
- All icons were chosen to represent to be understood by everyone and compliment the text that follows.

**Backgrounds**
- All backgrounds were chosen to show a proffesional yet inspiring theme.
- The black opacity overlay dulls the bright colours of the background images for a comfortable UX.

### Wireframes
Adobe XD was used to draw up <a href="Jobseek-wireframes.xd">wireframes</a> prior to development.


## Features
### Existing features
- **Pages**
  - **Any page**
    - **Navigation**
      - Jobseek logo links to index
      - Anonymous user menu items:
        - Register
        - Login
        - Home
      - Logged in user menu items:
        - Create Job Post   
        - Logout 
        - Home

    - **Footer**
        - Breif about section 
        - Jobseek logo links to index
        - Logged in user can see their logo and company name displayed as indication of active user.

  - **Home page (index.html)**
    - Show all job posts summaries with:
      - Salary, job type, location, company name, company logo, role summary
      - Logged in user can click edit on their created job posts
    - Filter job posts functionality
    - *Order job posts functionality*
    - Job post job title send user to full detailed view
  
  - **Single full job post**
    - Show user detailed view of job post
      - Role summary
      - Role requirements
      - Role responsibilities 
      - How to apply 
      - Logged in user can click edit or delete on their created job posts
      - *How many applications*
  - **Register**
    - Allows employers to register their company to advertise new roles
      - Employers can link company logo to show on job posts
  - **Login**
    - Registered users can login to add/edit or delete job posts.
  - **Create job post**
    - Allow logged in user to create a new job post under their company name.
    - Font editor on each field eg bullet points, bold, underline etc
    - Select from drop down for location and sector (to allow for easier grouping for filters)
  - **Edit job post**
    -  Logged in users will be sent here if edit is clicked on home page job post.
    - Allow logged in user to edit any field or delete entire post.

**Other features**
1. **Flash messages**
     - Flash messages were used to notify users of successfull/unsuccessfull actions eg, created job posts, incorrect login
2. **Form validation**
    - All forms were created with WTforms. WTforms built in validations provide a much cleaner, desciptive and overall error coverage eg. using invalid credentials, invalid character count.
3. **Responsivenesss**
    - Jobseek is fully responsive across all devices and screen sizes as well cross browser.
4. **Pagination**
    - A limit of X number of job posts are displayed on a single page. Pagination was used to provide a more manigeable UX.
5. **Remember me**
    - A remember token is stored on the users machine so they can stay logged in for a short time if navigating away from the site.
6. **Custom error pages**
    - TBD 


### Features Left to Implement beyond scope of project
1. Further user authentication:
    - Jobseeker - Upload CV, save jobs, rate employers, create profile.
    - Employer - employer profile, company information, social media feed.
    - Admin - monitor job posts and jobseekers, authenticate users before allowing access.
2. Click to apply:
    - Allow jobseekers to send their CV to employers from job post page.

## Technologies Used

HTML, CSS and Javascript were used throught this project as well as:
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Python](https://www.python.org/)
    - Used for application logic
- [Flask](http://flask.pocoo.org/)
    - A python microframework. Used to handle routing and logic.
- [Jinja2](http://jinja.pocoo.org/docs/2.10/)
    - A templating language for python.
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    - Used to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://fontawesome.com/)
    - Used for all icons
- [CKEditor](https://ckeditor.com/)
    - For create job post form field input formating.
- [MYSQL](https://www.mysql.com/)
    - SQL database management system.
- [SQLAlchemy](https://www.sqlalchemy.org/)
    - SQLAlchemy is a Python SQL toolkit and Object Relational Mapper. Use in majority of SQL commands. Simplifies long MYSQL queries and allows for database declaration within code.
- [WTForms](https://wtforms.readthedocs.io/en/stable/)
    - Use for all form creations, handling and validation.

**Tools for testing**
  - [HTML checker](https://validator.w3.org/)
  - [CSS checker](https://jigsaw.w3.org/css-validator/)
  - [PEP8](http://pep8online.com/)
  - [Parallels](https://www.parallels.com/uk/)

**Wireframes**
  - [Adobe XD](https://www.adobe.com/uk/products/xd.html)

## Database

MYSQl was used as the RDBMS. Using the user stories in the UX section the following ER Diagram was created with [Lucid Charts](https://www.lucidchart.com/pages/tour).

<div align="center">
<img width="90%" src="https://i.ibb.co/nCQGRrD/Screenshot-19.png" alt="Screenshot-19" border="0">
</div>

The **employer** table has the following columns:

- **id** – This is both the table’s primary key and a unique identifier for each employer. This ID will be referred to by other tables in the data model.
- **companyName** – This is used for sign in, on authored job posts and as active user.
- **email** – This is also used for sign and forms an alternate key together with companyName.
- **logo_url** - This is to show on authored job posts and active user.

The **job_post** table has the following columns:

- **id** - This is both the table’s primary key and a unique identifier for each job_post. This ID will be referred to by other tables in the data model.
- **date_posted** - This stores the date when the job is posted. By default all job posts are ordered on this column.
- **title** This stores the job title.
- **jobType** -  This column signifies whether the job duration is full-time part-time or temporary (contract).
- **salary** - This specifies the salary of the job post. Groups of £10,000.
- **role_sum** - A brief summary of the job post. Is display on home page and top of full view job post.
- **resp** - This specifies the main responsibilities of the role. 
- **requirements** - This specifies the requirements of the role eg. education, experience etc
- **how_to_apply** - A note on how to contact the company with an application.
- **emp_id** - This column stores the ID of the employer related to the job post. It is a reference to the company table. Referenced as a FK.
- **sector_id** - This refers to an attribute in the sector table that stores the sector/industry of the job eg. IT, Retail etc. Referenced as a FK.
- **location_id** - This refers to an attribute in the location table that stores the actual location of the job: city, country. Referenced as a FK.

The **sector** and **location** tables are similar in design. Both were created as a means to effectively store a large list of sectors and locations for reference in the job_post table.

SQLAlchmey was used for the majority of the interactions with the database and tables. Where SQL was needed, the MYSQL shell and [POPSQL](https://popsql.com/) was used. POPSQL provides an easy UI when working with SQL databases. 

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment and Database Management

Jobseek is hosted on heroku.

If you don't already have an account with heroku you will need to [create one](https://signup.heroku.com/login).

To run your own jobseek on heroku:

1. In your terminal cd into the destination of choice and run:
    -  `git clone https://github.com/gitbush/jobseek.git` 
2. Login to heroku via command line:
    -  `herkou login`
3. Create your app on heroku:
    -  `heroku create [name_of_app]`
    -  Open up heroku in the browser to see you app set up.
4. Back to the terminal and push your master branch to heroku:
    -  `git push heroku master`
5. Go to your Heroku dashboard in the browser to see your app created.

Now we need to connect to a MYSQL database. Heroku only allows connecting to MYSQL databases through add-ons. The easiest way to get this set up is through the GUI.

1. Click on your app on your heroku dashboard and follow resources > find more add-ons > JawsDB MYSQL. (you can use whichever MYSQL add-on you choose but for this we will use JawsDB).
2. Follow JawsDB MYSQL > Install JawsDB MYSQL > Select your app from "app to be provisioned" > Provision add-on. A JawsDB database has now been created for you.
3. Navigate to settings > Reveal Config Vars. You will see a JAWS_URL variable with a mysql connection string. This contains everything needed to connect to the database. The connection string is formed as follows:
   - mysql://USER:PASSWORD@HOST/DB
4. To taylor it to your app you will need to replace "JAWS_URL" with "SQL_ALCHEMY_URI" as this is the environment variable name set in config.py. 
5. Add pymysql connector to connection string. The connection string will  look like "mysql://..[connection string]..". We need to change it to "mysql+pymysql://...[connection string]..." to allow python to connect to the database via your app.

Your jobseek app and database are now set up and connected. The tables have been created and now you can populate with some example data.

Use the JawsDB values in your connection string in the following.

1. Open up your terminal and connect to the JawsDB MYSQL database:
    - `mysql -h < HOST > -u< USER > -p< PASSWORD >` 
2. You will now be in the mysql shell. Now choose the JawsDB database with:
    - `use < DB >;` 
3. With the correct database chosen load the jobseek_data.sql file. Given it is a relatively small number of queries we will use:
    - `source jobseek_data.sql;`
4. Your database should now be populated with some example data. To check use:
    - `select * from < table >;`


In addition, you can also run the code locally.

1. It's recommended when installing packages to work in a virtual environment. Cd into the project root directory and to set up a virtual environment follow this [tutorial](https://www.youtube.com/watch?v=APOPm01BVrk).
2.  With your editor of choice open and virtual env activated; install all dependencies from the requirements.txt with:
    -  `pip install -r requirements.txt` 
    -  (Edit .gitignore `<venv/>` with your virtual env name)
3. Now create an environment variable on your machine with your connection string:
    - Windows: `setx SQL_ALCHEMY_URI = "mysql+pymysql://...[connection string]..."`
    - Mac: 
4. CD into the project root and use:
    - `python app.py` to run the app on local host.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
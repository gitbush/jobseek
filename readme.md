# Jobseek

[Jobseek](https://jobseek-app.herokuapp.com/) serves as a tool for employers to advertise new positions within the company. Jobseekers can view these jobs with information on how to apply.

Jobseek is my DCD (Data Centric Development) milestone project for Code Institutes Full Stack Web Developer course. 

## UX

#### Jobseek was created with two users in mind:

  **As an employer I want:**

  1. An easy user interface to post available job opportunites at my company for jobseekers to view.
  2. A way for jobseekers to apply for roles.
  3. To edit any job posts I have made with potential updated content.
  4. To remove/delete a filled or no longer available job post.
  5. Any job posts that I have created are protected from risk of modifying/deleting from anyone other than the creator.
  6. To be able to show my company name and logo
  
  **As a jobseeker I want:**

 1. To view any new roles that are available.
 2. To view any roles that are within a certain sector, salary, location and employment type or a mixture of all.
 3. Details on how to apply for any roles of interest.
 4. See how long job posts have been advertised.
  
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
Adobe XD was used to draw up wireframes prior to development and can be found in the **docs** folder of this project.

# Features
## Existing features
### Elements of every page
#### **Navigation**
- The navbar features on every page with text menu items for navigation.
- Different menu items are available for authorised or anonymous users:
  - All users:
    - Jobseek logo on the left links to the home page.
    - **Home** 
  - Anonymous users:
    - **Register** 
    - **Login** 
  - Authenticated users:
    - **Create Job Post**   
    - **Logout** 
  
**Footer**
  - Breif about section with a disclaimer about site information
  - Jobseek logo which links to index
  - Logged in user can see their logo and company name displayed as indication of active user.

### **Home page**
  - Shows all job posts summaries with:
    - Salary, job type, location, company name, company logo, role summary
    - Logged in user can click edit on their created job posts
  - Filter job posts functionality
  - *Order job posts functionality*
  - Job post job title sends user to full detailed view
  
### **Single full job post**
  - Shows full detailed view of job post including:
    - Role summary
    - Role requirements
    - Role responsibilities 
    - How to apply 
    - Logged in user can click edit or delete on their created job posts
  
### **Register**
  - Allows employers to register their company to advertise new roles
    - Employers can link company logo to show on job posts
  - Validation is provided for this form and the user will be notified of any invalid inputs after a submit attempt.

### **Login**
  - Registered users can login to add/edit or delete job posts.
  - Validation is provided for this form and the user will be notified of any invalid inputs after a submit attempt.
  - Once logged in a **Create Job Post** button will be available on the navbar.

### **Create job post**
  - Allow logged in user to create a new job post under their company name.
  - Font editor on each field eg bullet points, bold, underline etc
  - Select from drop down for location and sector (to allow for easier grouping for filters)

### **Edit job post**
  -  Logged in users will be sent here if edit is clicked on home page job post.
  - Allows logged in user to edit any field or delete entire post.
  - The form is the same as the create job post page with current details populating form.

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

# Technologies Used

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

All testing was done manually throughout development and at project end.

## User Stories

User stories are taken the UX section.

### **As an employer I want:**

1. **I want to be able to advertise new jobs**
- To be able to post a job an employer must register and/or login:
    - **Register**
      - An employer can register via the register nav item and will redirect to the register page.
      - Register form contains 3 fields to fill in. All are required. 
      - On successfull form submit the employer will be redirected to the login page and greeted with a flash success message "Account created for [company name]"
    - **Login**
      - An employer can login via the login nav item and will redirect to the login page.
      - Login form contains 2 fields both of which are required.
      - On successfull form submit the employer will be redirected to the home page and greeted with a flash success message "Logged in as [company name]".
      - The employer can also see their company name and logo displayed in the footer.

1. **To post available job opportunites at my company for jobseekers to view.**

    - Once logged in a "Create Job Post" button will show sending the registered user to the create job page.
    - The create job form has 9 form fields to fill in detailing the job post.
    - On form submit the author will be redirected to the home page and greeted with a success flash message "Job Post created by [company name]".
    - A breif summary of the newly created job post can be seen on the home page.
  
2. **To edit/remove any job posts I have made with potential updated content.**
    - An edit button will be available on the active users authored job posts.
    - The edit button will redirect the author to the full job post page to view the full post and see which field they would like to edit.
    - From here another edit and delete button will be shown.
    - Clicking edit will take the author to the edit post page and all fields are available for edit.
      - Once the author is happy with renewed job post, they can click the create post to confirm edit.
      - The author will then be redirected to the full job post page and greeted with a flash success message "Job post edited by [company name]"
    - Clicking the delete button will trigger a confirmation modal to confirm that the author wants to delete the job post.
      - On delete confirm the modal will hide and the author will be redirected to the home page and greeted with a flash success message "Job post delete by [company name]".
3. **Any job posts that I have created are protected from risk of modifying/deleting from anyone other than the creator.**
    - Only a registered and logged in user can create posts.
    - Only the author of a job post has access to the edit/delete functionalities.
4. **A way for jobseekers to apply for roles.**
   - A how to apply field can be found on the job post with details of how a jobseeker can apply for a role.
5. *To see all job posts that I have created*
6. *To be able to show my company name and logo*
7.  *To be able to update my logo*

### **As a jobseeker I want:**

1. **To view any new roles that are available.**
      - On arrival to the home page, a jobseeker can see a summary of all available job posts showing job title, company name, date posted, location, salary, type and role summary.
      - The total number of job posts are displayed
      - Clicking on the job title on a job post will take the user to the full view of the job post showing all remaining fields on top of the home page view with responsibilties, requirements and how to apply showing.

2. **To view any roles that are within a certain sector, salary, location and employment type or a mixture of all.**
    - A jobseeker can narrow down their search with the refine form.
    - 4 dropdown menus covering type, salary, location and sector are available.
    - Any combination of the 4 will return a result.
    - The total number of job posts will update and now show the number of filters jobs out of the total number.
    - The selected filters will be displayed as a way of notifying the user of the filters that are currently applied
    - A clear filters button will be available to remove any filters and display all job posts.

3. **Details on how to apply for any roles of interest.**
    - A how to apply field can be found on the job post with details of how a jobseeker can apply for a role.

4. **See how long job posts have been advertised.**
    - The date the job post was created will be shown on the home page view and the full job post view.

## Manual Testing

Jobseek functionality, cross-browser and responsiveness were tested manually and documented in excel spreadsheets located in the **docs** folder of this project.

## Deployment and Database Management

Jobseek is hosted on heroku.

If you don't already have an account with heroku you will need to [create one](https://signup.heroku.com/login).

To run your own jobseek on heroku:

1. In your terminal cd into the destination of choice and run:
    -  `git clone https://github.com/gitbush/jobseek.git` 
2. Login to heroku via command line:
    -  `herkou login`
3. Create your app on heroku:
    -  `heroku create <name_of_app>`
    -  Open up heroku in the browser to see you app set up.
4. Back to the terminal and push your master branch to heroku:
    -  `git push heroku master`

Now we need to connect to a MYSQL database. Heroku only allows connecting to MYSQL databases through add-ons. The easiest way to get this set up is through the GUI.

1. Click on your app on your heroku dashboard and follow resources > find more add-ons > JawsDB MYSQL. (you can use whichever MYSQL add-on you choose but for this we will use JawsDB).
2. Follow JawsDB MYSQL > Install JawsDB MYSQL > Select your app from "app to be provisioned" > Provision add-on. A JawsDB database has now been created for you.
3. Navigate to settings > Reveal Config Vars. You will see a JAWSDB_URL variable with a mysql connection string. This contains everything needed to connect to the database. The connection string is formed as follows:
   - mysql://USER:PASSWORD@HOST/DB 
4. Add pymysql connector to connection string. The connection string will  look like "mysql://..[connection string]..". We need to change it to "mysql+pymysql://...[connection string]..." to allow python to connect to the database via your app.

Your jobseek app and database are now set up and connected. The tables have been created and now you can populate with some example data.

Use the JawsDB values in your connection string in the following.

1. Open up your terminal and connect to the JawsDB MYSQL database:
    - `mysql -h <HOST> -u<USER> -p<PASSWORD>` 
2. You will now be in the mysql shell. Now choose the JawsDB database with:
    - `use <DB>;` 
3. With the correct database chosen load the jobseek_data.sql file. Given it is a relatively small number of queries we will use:
    - `source jobseek_data.sql;`
4. Your database should now be populated with some example data. To check use:
    - `select * from <table>;`


In addition, you can also run the code locally.

1. It's recommended when installing packages to work in a virtual environment. Cd into the project root directory and to set up a virtual environment follow this [tutorial](https://www.youtube.com/watch?v=APOPm01BVrk).
2.  With your editor of choice open and virtual env activated; install all dependencies from the requirements.txt with:
    -  `pip install -r requirements.txt` 
    -  (Edit .gitignore `venv/` with your virtual env name)
3. Now create an environment variable on your machine with your connection string:
    - Windows: `setx JAWSDB_URL "mysql+pymysql://...[connection string]..."`
4. CD into the project root and use:
    - `python app.py` to run the app on local host.


## Credits

### Content
- All job posts and companies are fictional and taken from [Mock Jobs](https://sites.google.com/a/activatelearning.ac.uk/the-employment-shop-at-activate-learning/home/for-students/reading-college/mock-jobs)
- Company logos from [Example logos](https://www.examples.com/design/company-logo.html)

### Media
- All images are from [Unsplash](https://unsplash.com/public-domain-images)

### Acknowledgements

- [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Flask 101 tutorial ](http://www.blog.pythonlibrary.org/2017/12/12/flask-101-getting-started/) 
- [SQLEqualizer](https://sqlizer.io/#/) for converting csv to sql

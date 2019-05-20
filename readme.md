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

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


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

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
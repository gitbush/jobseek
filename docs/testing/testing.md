# Jobseek testing

All testing was done manually throughout development and at project end.

## User Stories

User stories are taken the UX section of [readme.md](readme.md).

### **As an employer I want:**

1. **I want to be able to advertise new jobs**
- To be able to post a job an employer must register and/or login:
    - **Register**
      - TODO (add text on home page)- Employers wanting to advertise a role are prompted to register by the "register". An employer can also register via the register nav item and will redirect to the register page.
      - Register form contains 3 fields to fill in. All are required. 
      - On successfull form submit the employer will be redirected to the login page and greeted with a flash success message "Account created for [company name]"
    - **Login**
      - TODO (add text on home page)- Registered employers wanting to advertise a role are prompted to login by the "login". An employer can also login via the login nav item and will redirect to the login page.
      - Login form contains 2 fields both of which are required.
      - TODO(a unique combination of the two is required)
      - On successfull form submit the employer will be redirected to the home page and greeted with a flash success message "Logged in as [company name]".
      - The employer can also see their company name and logo displayed in the footer.

2. **To post available job opportunites at my company for jobseekers to view.**

    - Once logged in a "Create Job Post" button will show sending the registered user to the create job page.
    - The create job form has 9 form fields to fill in detailing the job post.
    - On form submit the author will be redirected to the home page and greeted with a success flash message "Job Post created by [company name]".
    - A breif summary of the newly created job post can be seen on the home page.
  
3. **To edit/remove any job posts I have made with potential updated content.**
    - An edit button will be available on the active users authored job posts.
    - The edit button will redirect the author to the full job post page to view the full post and see which field they would like to edit.
    - From here another edit and delete button will be shown.
    - Clicking edit will take the author to the edit post page and all fields are available for edit.
      - Once the author is happy with renewed job post, they can click the create post to confirm edit.
      - The author will then be redirected to the full job post page and greeted with a flash success message "Job post edited by [company name]"
    - Clicking the delete button will trigger a confirmation modal to confirm that the author wants to delete the job post.
      - On delete confirm the modal will hide and the author will be redirected to the home page and greeted with a flash success message "Job post delete by [company name]".
4. **Any job posts that I have created are protected from risk of modifying/deleting from anyone other than the creator.**
    - Only a registered and logged in user can create posts.
    - Only the author of a job post has access to the edit/delete functionalities.
5. **A way for jobseekers to apply for roles.**
   - A how to apply field can be found on the job post with details of how a jobseeker can apply for a role.
6. *To see all job posts that I have created*
7. *To be able to show my company name and logo*
8.  *To be able to update my logo*

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

5. *Know how many other jobseekers have applied for certain roles.*
6. *To order job posts based on different criteria*

## Manual Testing

Jobseek functionality, cross-browser and responsiveness were tested manually and documented in excel spreadsheets:

- [Functionality Testing](Functional_testing.xlsx)
- [Cross-browser and device testing](browser_testing.xlsx)

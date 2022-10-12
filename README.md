### **Harvard's CS50W Edx Course: Final Project (Capstone)**

#### **Requirements**

The final project is your opportunity to design and implement a dynamic website of your own. So long as your final project draws upon this course’s lessons, the nature of your website will be entirely up to you, albeit subject to the staff’s approval.
In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

- Your web application must utilize at least two of Python, JavaScript, and SQL.
- Your web application must be mobile-responsive.
- In README.md, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project.
- If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!

Beyond these requirements, the design, look, and feel of the website are up to you!
<br>
<br>

#### **Installation**

- Install project dependencies by running pip install -r requirements.txt.
- Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
- Run server with command 'python manage.py runserver'
- Go to the server address and create an account using an email ending with @corporation.com.
  <br>
  <br>

#### **Built tools:**

-Backend: Django and SQLite.  
-Frontend: Javascript, HTML, CSS.  
-3rd Party: Pillow image library, Paper.JS framework.
<br>
<br>

#### **Project description: BookStation**

[DEMO VIDEO](https://youtu.be/GIein3LbNk0)

My final project for CS50P is a webapp for workstation booking, for employees of a fictional company.  
The user is first required to sign up exclusively with their corporate email before being able to make reservations.

After logging in, the user is presented with a homepage with all the features: Make a new booking, see future bookings, see past bookings, and find coworkers.

The main feature is the booking page, where you can select a date (no past dates accepted), which then prompts to a map of the office with all bookable workstations: the available ones are marked with a green circle and, when hovered over, present a tooltip with the number of seats and monitors available. If the workstation is unavailable/booked, it is shown as red.  
If clicked or touched on, a modal window opens with a full description of the workstation and a picture of it. The user can then confirm their booking, and is redirected to the future bookings page.

There is also a search feature that allows users to find whether their coworkers have bookings for that day and, if so, what workstation they are in. This could be useful in order to facilitate teams to stay closer (or further apart? 😉 ) to one another in the office space. The search allows for first or last names, case-insensitively.


<br>
<br>

#### **Distinctiveness and Complexity**

There were 2 main challenges for me in this project, which in my opinion make this app distinct from the course's projects, and which added a bit more complexity to mine:

- How to display the floorplan and make it clickable?
- How to update in realtime the names in the search feature, without reloading the page?

Regarding the floorplan, the solution was implementing it with Paper.JS, a SVG scripting framework that runs HTML5 canvas. Besides the challenge of reading all the documentation to learn how to properly use its scripting system, it took some time to figure out how to make the PaperJS object responsive without issues.  
All the workstations' data is passed through context to the django view, then parsed with the "json_script" Django template filter, and then drawn on the canvas and stored to use with Javascript.

As for the Search feature, it was a relatively simple solution using jquery/AJAX to update and refresh the results part of the html file inside the main page view, and also toggling the CSS style and animation of the FontAwesome magnifying-glass icon.
<br>
<br>

#### **Files and directories**

- `workstation/` - Project directory.

  - `accounts/` - login/registration directory.
  - `media/` - Contains uploaded images by the workstation model by the admin.
  - `reserve/` - Main application directory

    - `static/`
      - `css/`
        - `floorplan.css` - Styling file for the floorplan canvas.
        - `style.css` - General styling file.
      - `js/`
        - `floorplan.js` - JS file for drawing the floorplan.
        - `main.js` - mains JS file.
        - `paper.js` - Paper.JS framework file.
      - `templates/`
        - `modals/`
          - `delete_confirm_modal.html` - deletion confirmation modal, included in 'reservations_list.html'
          - `reservation_confirm_modal.html` - booking confirmation modal, included in 'workstations_list.html'
          - `reservation_confirm_modal.html`
        - `base.html` - Global template base
        - `find_coworkers.html` - 'Find Coworkers' view template.
        - `find_coworkers_results.html` - search results file, included in 'find_coworkers.html'.
        - `floorplan.html` - workstations search results file, included in 'workstations_list.html.
        - `history.html` - 'Past Bookings' view template.
        - `index.html` - 'Home' view template.
        - `nav.html` - Global navbar template.
        - `reservations_list.html` - 'Future Bookings' view template.
        - `workstations_list.html` - 'New Booking' view template.
    - `admin.py` - Registers models access to Admin.
    - `apps.py` - Registers the main App.
    - `forms.py` - Contains all forms.
    - `models.py` - Contains all models.
    - `urls.py` - Contains all views URLs.
    - `views.py` - Contains all project views.

  - `templates/capstone` - contains all application templates.

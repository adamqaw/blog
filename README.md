# blog
WiP portfolio blog. No bootstrap, no HTML templates, no CSS templates, Flask backend. No external help other than documentation and my own notes.


### Feb 1 2022 Initial Commit notes:

- Added all WiP files for use on other systems
- Padding on some divs need tweaking
- Microservices needs to be moved up on index.html
- Microservices structure needs to be changed
- news.py needs restructuring; would rather not use brute-force list creation
- News API implemented, need to add distinct styling, need to add structure, need to add customizability

### Feb 8 2022 Commit notes:

- Added gridbox for microservices
- Added News and Weather API to the microservices grid
- Adjusted padding and margins for some divs
- Moved microservices higher on the page for easier access

### Feb 9 2022 Commit notes:

- Added forms.py to hold flask wtforms models
- Changed News class on news.py to be without constructor method
- Added db model to main.py (will be moved to a models.py file, along with other db models, if any)
- The program will check if the date of last db entry is equal to today's date. If it is not, it will delete all rows to make way to append the new news headlines.
- Need to expand on weather API page by adding graphics and to display basic info on index.html, then detailed information on weather.html

### Feb 14 2022 Commit notes:
- Changed news.html to include links that open articles in a new tab and also displays a picture from the article (if available).

### March 19 Notes:
 - Fixing the stocks microservice to add new stock info by changing the backend process to "/" and redirecting to "/stocks". (STILL IN PROGRESS)

# Thumbnail Ranker
**This project is all about give your Thumbnail and get the comparing vote of that Thumbnail.**
**Project take a youtube video url and extract its thumbnail.**
**displayed all thumbnail so user give their vote to thumbnail so user get feedback so that they know if their Thumbnail is good or they required some improvement**  
**Project is build using html, css, Vanilla JavaScript, and python-flask for backend and postgresql as database.**

# Installation
## Prerequisites
**Before setting up the project, ensure you have the following installed on your system:**

Python 3.x: The project is built using Python, so make sure you have Python 3.x installed.
PostgreSQL: The project uses PostgreSQL as the database. Make sure PostgreSQL is installed and running.

**Step 1: Clone the Repository**
First, clone the project repository from GitHub to your local machine.
##bash
`git clone git@github.com:MRterrorOP/ThumbnailRanker.git`
`cd ThumbnailRanker`

**Step 2: Set Up a Virtual Environment**
Create and activate a virtual environment to keep dependencies isolated.

##bash
`# Create a virtual environment`
`python3 -m venv venv`

`# Activate the virtual environment`
`# On Windows:`
`venv\Scripts\activate`

`# On macOS/Linux:`
`source venv/bin/activate`
**step 3: Activate the Virtual Environment:**
Before installing any packages, activate the virtual environment to ensure all dependencies are installed locally within the project.
##On macOS/Linux:##
`bash`
`source venv/bin/activate`
##On Windows:##
`venv\Scripts\activate`

**Step 4: Install Required Dependencies**

`pip install blinker==1.7.0 click==8.1.7 Flask==3.0.2 Flask-SQLAlchemy==3.1.1`
`pip install greenlet==3.0.3 itsdangerous==2.1.2 Jinja2==3.1.3 MarkupSafe==2.1.5`
`pip install psycopg2==2.9.9 pytube==15.0.0 SQLAlchemy==2.0.31 typing_extensions==4.12.2 Werkzeug==3.0.1`
**Step 5: Set Up PostgreSQL Database**
1. Create a PostgreSQL Database:

Log in to PostgreSQL and create a database for your project:
`CREATE DATABASE thumbnail_ranker;`


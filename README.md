#TO CREATE USER MANAGEMENT DASHBOARD WITH TWO USER TABS 
#uSER DETAILS- fetch user details from a place holder database and implemet a searchable table dispalying the user details, along with click action in a user in the search result to open a pop up/model generating a report
#Create a tab for account creation , with username and password along with dummy request handling.

1) Create Django Project: used Visual Studio Code
Install Django using pip install django.
Create a new Django project using django-admin startproject projectname.

2) #for setting up vue.jsInstall any necessary Vue.js libraries, like Vue Router (vue add router) for managing tabs. #Install node.js and npm, install vue cli globally . 
    npm install -g@vue/cli
#check versions using
node -v
npm -v
3) #scaffold a new Vue.js project in the project directory
    vue create projectname
4) #cretae app in django and 
   python manage.py startapp appname
5) #create backend- Define a model for the user in Django's models.py.
   Run python manage.py makemigrations and python manage.py migrate to create the database.
6) Create Django REST Framework views and serializers for fetching user data and handling form submissions.
7) create templates for your views
8) Install django-cors-headers using pip install django-cors-headers.
Configure it in your Django settings to allow cross-origin requests.
9) FOR FRONTEND (VUE>JS) we have Installed necessary Vue.js libraries, like Vue Router (vue add router) for managing tabs. 
10) Build Vue components for the User Details tab (searchable table) and the Account Creation tab (form).
11) Use Vue's HTTP library (Axios, for example) to make requests to your Django backend.
12) Create a dashboard layout with tabs for User Details and Account Creation.
13) Apply CSS or use a preferred CSS framework (like Tailwind CSS) for styling the components and dashboard.
14) Implement search functionality in the User Details tab using Vue methods to filter results based on user input
15) Create a reusable Vue component for the popup/modal.
16) Show the modal on clicking a user in the search results.
17) Run Lighthouse audits (npm install -g lighthouse) to analyze and optimize your application.
Address any performance issues reported by Lighthouse.
    


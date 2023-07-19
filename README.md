# **Healty Life Organic Shop - Project Portfolio 5**

Healthy Life Organic Shop is an e-commerce ficticional online store that sells a range of organic goods that are free from pesticides and GMO ingredients. The Organic Shop offers a carefully curated organic items from fresh produce to pantry essentials, cosmetics, and even cleaning supplies. We have a blog that provides valuable insights and tips for maintaining a healthy lifestyle.

This is a fictional website that was created for Portfolio Project 5 - Diploma in Full Stack Software Development at the Code Institute.

Welcome to the live site here: <a href="https://organic-shop.herokuapp.com/" target="_blank">Healthy Life Organic Shop</a>

![Organic Shop responsive design](./static/images/readme/multidevice-organic-shop.jpg)

Table of Content

* [**Project**](<#project>)
    * [Website Goals](<#website-goals>)
    * [Site Users Goal](<#site-users-goal>)
    * [Site Owners Goal](<#site-owners-goal>)
    * [Business Model](<#business-model>)
    * [Marketing Techniques](<#marketing-techniques>)
    * [Project Management](<#project-management>)
* [**User Experience (UX)**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)
* [**Features**](<#features>)
    * [Navbar](<#navbar>)
    * [Home Page](<#home-page>)
    * [Products](<#products>)
    * [Product Details](<#product-details>)
    * [Blog](<#blog>)
    * [My Account](<#my-account>)
    * [Django-allauth Features](<#django-allauth-features>)
    * [Add Product](<#add-product>)
    * [Login](<#login>)
    * [Shopping Bag](<#shopping-bag>)
    * [Checkout](<#checkout>)
    * [Order Confirmation](<#order-confirmation>)
    * [Footer](<#footer>)
    * [Toasts](<#toasts>)
* [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks & Software](<#frameworks--software>)
* [**Testing**](<#testing>)
    * [Testing User Stories](<#testing-user-stories>)
    * [Code Validation](<#code-validation>)
    * [Additional Testing](<#additional-testing>)
    * [Known Bugs](<#known-bugs>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [Content](<#content>)
    * [Media](<#media>)
* [**Acknowledgements**](<#acknowledgements>)


## Website Goals

Healthy Life Organic Shop is a fictional online ecommerce B2C offering a great range of organic products, including fresh produce and groceries. Our goal is to provide a convenient and reliable platform for individuals seeking a healthier lifestyle. 


## Business Model

Healthy Life Organic Shop is a business that only operates online through its ecommerce. We sell fresh produce, groceries and a wide range of products directly to the consumer, B2C business model. We work directly with organic farmers and producers ensuring that our customers have access to a wide range of fresh and sustainable products while supporting local Irish farmers. 

## Marketing Techniques

### Email Marketing

A newsletter is an important marketing technique to keep in touch with clients. Providing the ethos of the organic shop we want to make it in a mindful way to keep connected to our valued customers. At Healthy Life Organic Shop, we understand the importance of staying connected with our valued customers. We utilize the power of the Mailchimp newsletter to keep the customers informed and engaged. Our newsletter brings the latest updates on new products, exclusive deals, and products on season,  and also keeps the customers informed about our blog posts, providing you with valuable insights and tips for maintaining a healthy lifestyle.

### Facebook Page

To establish a strong online presence for Healthy Life Organic Shop, we have chosen Facebook and Instagram. By utilizing these popular social media platforms, we aim to expand our reach and attract a larger customer base to our ecommerce store. We also intend to foster closer connections with our customers through engaging content and personalized interactions.

The Instagram page is still in progress. Both will be alocated as an asset of Facebook Meta Business Suite, which will allows the management of several aspects such as manage posts and also advertising.  

The navlinks for the social media pages can be acessed from the Footer.


<details><summary><b>Healthy Life Organic Shop Facebook Page</b></summary>

<img src="./static/images/readme/facebook-page" alt="Facebook Page"></details>


## Project Management

### GitHub Project

* I have created a kanban project dashboard to manage the project progress. 

![Github Dashboard](media/user-stories-kanban.png)

[Back to top](<#table-of-content>)


## Technologies Used

### Languages

* [Python](https://www.python.org/)
* [HTML 5](https://en.wikipedia.org/wiki/HTML/)
* [CSS 3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)

### Frameworks, supporting libraries and other programs 

* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) was used for authentication, registration, account management.
* [Amazon Web Services](https://aws.amazon.com/) - A service that hosts all static files and images in the project.
* [Bootstrap](https://getbootstrap.com/) was used to style the website, easily add responsiveness and interactivity.
* [CANVA](https://www.canva.com/) to create the logo, color palete (Pro version) 
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style the forms.
* [Django](https://www.djangoproject.com/) as the framework to build the blog.
* [ElephantSQL](https://www.elephantsql.com/) - A PostgreSQL database hosting service.
* [Favicon](https://favicon.io/) - Used to create the favicon.
* [Git](https://git-scm.com/) - Used for version control
* [Gitbash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) to push changes to the GitHub repository.
* [GitHub](https://github.com/) to host the repositories.
* [Gitpod](https://www.gitpod.io/) as the IDE for the application.
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to debug and test responsiveness.
* [Gunicorn](https://gunicorn.org/) as the server for Heroku.
* [Heroku](https://www.heroku.com/) to deploy the project.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
* [PostgreSQL](https://www.postgresql.org/) - Database used for production
* [Psycopg2](https://pypi.org/project/psycopg2/) was used for Python and PostgreSQL databases.
* [PEP8](http://pep8online.com/) for testing and validating the code.
* [Stripe](https://stripe.com/ie) - Used for all the websites payment functionality
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - to validate the CSS.
* [W3C HTML Validator](https://validator.w3.org/) - to validate the HTML.

[Back to top](<#table-of-content>)



## Testing

### Code Validation

Healthy Life Organic Shop ecommerce website has gone through intensive tests throughout its pages and sections/screens.The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) has been used to validate the CSS, [W3C HTML Validator](https://validator.w3.org/) has been used to validate the HTML, [JSHint](https://jshint.com/) to validate JavaScript and [CI Python Linther](https://pep8ci.herokuapp.com/) to validate Python. Additional tests, such as browser tests, manual testing, responsiveness test, testing user stories among others have been carried on as shown below. 

**HTML validation** 

[W3C HTML Validator](https://validator.w3.org/) has been used to validate the HTML. 

![HTML validation image ](./static/images/readme/w3-html-validator.jpg) 


**CSS validation** 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) has been used to validate the CSS. 

![CSS validation image ](./static/images/readme/w3-css-validator-organic-shop.jpg) 

**JavaScript validation image**

![JavaScript validation image ](./static/images/readme/javascript-validation.jpg) 

**PEP8 CI Python Linther**

CI Python Linther [cipythonlinther](https://pep8ci.herokuapp.com/) was used to validate Python code as at the time of this project submission the validator PEP8 [pep8online](http://pep8online.com/) is offline. I have tested the following Python files:


<details><summary><b>Bag App - Python Validation</b></summary>

<img src="./static/images/readme/python-ci-validation-bag-app.jpg" alt="Bag App Python Validation"></details>

<details><summary><b>Blog Python Validation</b></summary>

<img src="./static/images/readme/python-ci-validation-blog-app.jpg" alt="Blog App Python Validation"></details>


**App Checkout**
*  __init__.py - All clear, no errors found.
* admin.py - All clear, no errors found.
* apps.py - All clear, no errors found.
* forms.py - All clear, no errors found.
* models.py - 5 line-too-long errors reported which I decided to keep it according to code style.
* signals.py - All clear, no errors found.
* urls.py - All clear, no errors found.
* views.py - 5 line-too-long errors reported which I decided to keep it according to code style.
* webhook_handler.py - 3 line-too-long errors reported which I decided to keep it according to code style.
* webhooks.py - All clear, no errors found.

**App Home**
* apps.py - All clear, no errors found.
* urls.py - All clear, no errors found.
* views.py - All clear, no errors found.

**App Products**
* admin.py - All clear, no errors found.
* apps.py - All clear, no errors found.
* forms.py - All clear, no errors found.
* models.py - All clear, no errors found.
* urls.py - All clear, no errors found.
* views.py - 4 line-too-long errors reported which I decided to keep it according to code style.

**App Profiles**
* apps.py - All clear, no errors found.
* forms.py - All clear, no errors found.
* models.py - 5 line-too-long errors reported which I decided to keep it according to code style.
* urls.py - All clear, no errors found.
* views.py - 3 line-too-long errors reported which I decided to keep it according to code style.

**organicshop**
* urls.py - All clear, no errors found.
* views.py - All clear, no errors found.

**other**
* custom_storages.py - All clear, no errors found.


[Back to testing](<#testing>)


### Browser Testing

Healthy Life Organic Shop was manually tested on these browsers as table below and design, layout, functionality and, responsiveness were consistent across all browsers both mobile and desktop.

|   Browser   |    Result  | 
| :---------: | :---------:| 
| Chrome      |   pass     | 
| Edge        |   pass     |
| Firefox     |   pass     |
| Safari      |   pass     |
| IE          |   pass     | 

### Responsiveness Test

Healthy Life Organic Shop ecommerce website was manually tested for its responsiveness with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

|        | Nexus 4/5/6 | Galaxy S5/S6/S7 | iPhone 6--12 | iPad |  Display <1200px | Display >1200px |
|--------|-------------|-----------------|--------------|------|------------------|-----------------|
| Render |    pass     |      pass       |     pass     | pass |     pass         |      pass       |
| Images |    pass     |      pass       |     pass     | pass |     pass         |      pass       |
| Links  |    pass     |      pass       |     pass     | pass |     pass         |      pass       |


### Manual Testing

Healthy Life Organic Shop ecommerce website has been extensively tested both on the Gitpod terminal and the Heroku deployed version on the browser. It has been checked features, responsiveness, accessibility, layout, design, texts, buttons and navigation links and form submission on different browsers. 
All tests made aimed to achieve the best user experience in system navigation, so that the user can follow an intuitive and easy flow at all system contact points.

Below are some examples of features tested manually.  

| Test Case              | Description                                                         | Expected Result                                             | Pass/Fail |
|------------------------|---------------------------------------------------------------------|-------------------------------------------------------------|-----------|
| Page 404               | Verify if the 404 page is working                                    | Typing in an incorrect URL loads the 404 error page        | pass      |
| Logo                   | Verify if the logo redirects to the home page                        | Clicking the logo redirects the user to the home page       | pass      |
| Home Button            | Verify if the home button redirects to the home page                 | Clicking the home button redirects the user to the home page | pass      |
| Home Page              | Verify the content and layout of the home page                       | All sections and elements are displayed                    | pass      |
| Play Ideas Button      | Verify if the play ideas button loads the play ideas list            | Clicking the play ideas button displays the play ideas list | pass      |
| Play Ideas Page        | Check if the play ideas are listed correctly                         | Play ideas are displayed in a grid layout                  | pass      |
| Post Detail Page       | Ensure the post detail page shows correct content                    | Post content, comments, and likes are shown                 | pass      |
| User Registration      | Test the user registration process                                   | User can successfully register                              | pass      |
| User Login             | Test the user login process                                          | User can successfully log in                                 | pass      |
| Add Post               | Test the functionality to add a new play idea for logged users       | New play idea is added to the blog                          | pass      |
| Update Post            | Test updating an existing play idea                                  | Play idea is updated successfully                           | pass      |
| Delete Post            | Test deleting a play idea                                            | Play idea is deleted from the blog                          | pass      |
| Nav Links Footer       | Check if the navigation links in the footer are working              | Clicking on a footer nav link redirects to the page         | pass      |
| Social Links           | Test if social links in the footer open in a new window              | Clicking on a social link opens a new window                | pass      |
| Subscribe Newsletter   | Test the subscribe newsletter feature                                | User can submit their email and is redirected to a thank you page | pass |
| Profile Page           | Check if the profile page is loading correctly                       | User can view their profile page                            | pass      |
| Update Profile         | Check if users can update their profile with a bio and picture       | Users can upload a profile picture and add a bio            | pass      |
| Clear Profile          | Check if users can clear their bio and picture from their profile    | Users can remove their profile picture and bio              | pass      |
| User's Posts - Profile | Check if users can see and access their own added play ideas         | Users can view and access their own play ideas              | pass      |
| Feedback Messages      | Check if feedback messages are displayed in relevant submissions     | Users receive appropriate feedback messages                 | pass      |



### Testing User Stories

#### **Site User**

| Expectation                         | Result                          |
| :---------------------------------: | :------------------------------:|
|  As a Site User I can view a list of play ideas so that I can select one to read | **[Play Ideas Page]**  |
|  As a Site User I can click on a play idea that I can read the full play idea | **[Play Idea Detail Page]**| 
|  As a Site User I can view the number of likes on each play idea so that I can see which is the most popular or viral |**[Home, Play Ideas and Detail Pages]**|
| As a Site User I can view comments on an individual play ideas so that I can read the conversation | **[Play Idea Detail Page]**| 
|   As a Site User I can register an account so that I can add, update, delete play ideas, comment and like them and also have a profile | **[Register/Sign Up Page]**| 
| As a Site User | I can create, read, update and delete play ideas so that I can manage my blog content | **[Add, Update, Delete Play Idea page]** |
| As a Site User I can leave comments on a play idea so that I can be involved in the conversation |**[Play Idea Detail Page]** |
| As a Site User I can like or unlike a play idea so that I can interact with the content | **[Play Idea Detail Page]** |
| As a Site User I can access the blog on different devices (mobile, tablet, desktop) for a seamless browsing experience | &check; |
| As a Site User I can create a profile by adding my bio and picture profile so that other users can read about who I am |**[Profile Page]** |
| As a Site User I can update a profile by updating my bio and picture profile so that upload a better bio and/or picture profile, or even remove it. | **[Profile Page]** |
| As a Site User I can see the play ideas I have created so that I can update or delete them | **[Profile Page]**  |
| As a Site User I can subscribe to a newsletter so that I can receive monthly emails with the new play ideas |**[Footer ]**  |
| As a Site User I can log out from the Its4kids blog so that I can feel safe that nobody can access my information | **[Logout page]** |
| As a Site User I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page | **[Flash messages]** |

#### **Site Admin**

| Expectation                         | Result                          |
| :---------------------------------: | :------------------------------:|
| As a Site Admin I can create, read, update and delete play ideas so that I can manage my blog content | **[Add, Update, Delete Play Idea page]**  |
| As a Site Admin I can create draft play ideas so that I can finish writing the content later| **[Add, Update, Delete Play Idea page]**  |
| As a Site Admin I can create new categories through django admin dashboard so that the play ideas are organized by categories | **[Django Dashboard]**  |
| As a Site Admin I can approve or disapprove comments on play ideas so that I can provide a safe environment for the users | **[Django Dashboard]**|


[Back to top](<#contents>)


### Bugs Fixed

Along the development of Its4kids application some error appeared during the debug process which were corrected, for example programming errors due to not running migrations, path errors, among others. Also during the website testing process some smaller errors appeared on the code validation and they were immediately corrected. 

Follow below some examples:

![Home Page - Bugs Fixed ](./static/images/readme/html-bugs-fixed.png) 

![Programming Error - Bugs Fixed ](./static/images/readme/fixed-bugs-programmingError.jpg) 

![Redirect - Bugs Fixed ](./static/images/readme/fixed-bugs-redirect.jpg) 

![IntegrityError - Bugs Fixed ](./static/images/readme/bug-fixed-integrityError.png) 



### Additional Testing

### Acessibility 

The website color accessibility was checked by using [A11y](https://color.a11y.com/).

![Acessibility validation image ](./static/images/readme/a11y-acessibility-validator-organic-shop.jpg) 

### Lighthouse

A test was conducted using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) within Chrome Developer Tools. 

It tests each of the pages for ***performance, accessibility, best practices and, SEO***

The performance score of 73% can be significantly enhanced by simply resizing all the images used on the website.

![Lighthouse test results](./static/images/readme/lighthouse-desktop.jpg)


[Back to top](<#contents>)














## Credits

### Code
[Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) - This project is so far fully based on Boutique Ado walkthrough which will be customized in the next submission.
[Stackoverflow](https://stackoverflow.com/) - helped me along the way with some bugs. 
[Ricardo Maroquio](https://www.youtube.com/watch?v=3dobl8hdeYw) - inspirations for the code for ecommerce organic shop.
[Denis Ivy](https://www.youtube.com/watch?v=_ELCMngbM0E&list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng) - tutorial on Django Ecommerce Website 

### Content 
[Green Earth Organics](https://www.greenearthorganics.ie/) - the description of the products was taken from this ecommerce Green Earth Organics, which was also an inpiration for this project.
[Evergreen](https://evergreen.ie/blogs) - I got the content for the blog posts.

### Media
* [Canva](https://canva.com/) - I got the image for hero home page under the Pro subscription. 
* [The Organic Shop](https://theorganicshop.ie/) - I got all the images for the products from The Organic Shop, which was also an inspiration for this project.

# Acknowledgements

Healthy Life Organic shop was designed and developed for Portfolio 5 project, a requirement of Full Stack Software Developer Diploma Course (Eccommerce) at the [Code Institute](https://codeinstitute.net/). First of all I would like express my gratitude to Bethany from the Student Care, without her huge support, encouragement and understanding I would not be able to complete this project. I also would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/), my Cohort facilitators, my Cohort colleagues, the Slack community and the Tutor Assistance for all guidance and support during this journey. I am also thankful to the ***Mayo, Sligo and Leitrim Education Training Board (msletb)*** for this opportunity. I  would also like to say thank you to my family, my husband Michel and, my children, Alanna, and Peter who is just 17 months old at the time of this project submission. 

[Back to top](<#table-of-content>)

Fabiana Tacco (2023)
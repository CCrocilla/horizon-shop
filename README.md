# **Horizon Shop** Website

### **Developer: Claudio Crocilla**


### **Readme Contents Horizon Shop**
- [Overview](#overview)
- [Project](#project)
  - [User Goal](#user-goal)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Use Cases](#use-cases)
    - [Homepage](#home-page)
    - [Contact Us](#contact-us)
    - [Dashboard](#dashboard)
    - [Sign In/Sign Up](#sign-in-sign-up)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Images and Videos](#images-and-videos)
- [Features](#features)
  - [Database Schema](#database-schema)
  - [Structure](#structure)
  - [Homepage](#home-page-1)
  - [Contact Us](#contact-us-page)
  - [Sign Up/Sign](#sign-upsign-in-page-and-authentication-process)
  - [Dashboard](#dashboard-1)
  - [404 Error Page](#404-error-page)
- [Wireframe](#wireframe)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Testing](#testing)
  - [Lighthouse Validator](#lighthouse-validator)
  - [Test Cases](#test-cases)
  - [Automation Testing](#list-of-automated-test-cases-perfomed)
  - [Additional Tests](#additional-tests)
  - [Bugs](#bugs)
  - [Future Implementation](#future-implementation)
- [Development](#deployment)
  - [Github](#github)
  - [Heroku](#heroku-app)
  - [Github Pages](#github-pages)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Local Clone](#local-clone)
- [Credits](#credits)



## **Overview**

#### The website offers to the user the possibility to buy product and not just that, they can also sell and more!
#### Internet users all around the world love to buy and sell products every day and using website to shop online is part of our life available just at a fingertips. 

#### The website is intuitive and user-friendly! The users can register to the website with a few easy steps by entering Username and Email and have access to all Horizon Shop great services! The users can also subscribe to a newsletter and receive regular updates as well as provide/review feedback, report issues or request support!



<a href="https://horizonshop.herokuapp.com/" target="_blank" rel="noopener noreferrer"><img src="static/images/readme/amiresponsive/" alt="Home Page" width="800px"/></a>
<br/>
Click in the image above to access the Live Website or [click here!](https://parkland.herokuapp.com/ "Parkland")

## **Project** 

### **User Goal**
- Easy, Intuitive and User-Friendly Website!
- Wide compatibility with every Browsers and Devices.
- A fast, easy and intuitive way to buy and sell products.
- Time is precious for everyone and we save yours offering a great buying and selling system.
- High variety of Services offered to the users.
- Possibility to share customer experience via the Dashboard Page.
- Fellow Customer feedback visible to the users in the Home Page.
- Newsletter available to receive updates/offers via email.
- Possibility to report an issue or request assistance/support via Contact Us Page.


---

## **User Experience (UX)**

### **User Stories**
- #### First Time Visitor Goals
    1. As a First Time visitor of a website dedicated to selling products online, I want to have a visual impact on the Landing Page that will attract my attention.  
    2. As a First Time Visitor, I want to be able to easily navigate through the website.
    3. As a First Time Visitor, I want to be able to see the services offered by Horizon Shop website.
    4. As a First Time Visitor, I want to find the website pleasant to the eye, visually intuitive, with catchy colours and images.

- #### Returning Visitor Goals
    1. As a Returning Visitor, I want to be able to register to the website.
    2. As a Returning Visitor, I want to be able to buy products.
    3. As a Returning Visitor, I want to be able to sell products.
    4. As a Returning Visitor, I want to be able to report issues.
    5. As a Returning Visitor, I want to be able to request assistance.
    6. As a Returning Visitor, I want to access the website through my social media accounts.

- #### Frequent User Goals
    1. As a Frequent User, I want to see new products/offers.
    2. As a Frequent User, I want to see new services.
    3. As a Frequent User, I want to be able to change my personal registered information (if necessary).
    4. As frequent User I want to be able to access my personal information via a Dashboard Page.
    5. As a Frequent User, I want to sign up to the Newsletter to receive updates about new offer on Horizon Shop.
    6. As a Frequent User, I want to report issues.
    7. As a Frequent User, I want to share a feedback on the website.

For the User Stories and the Epics please refer to the following links:
- [User Stories](https://github.com/users/CCrocilla/projects/3)
- [Epics](https://github.com/CCrocilla/horizon-shop/milestones)

<!-- Use Cases Area -->
### **Use Cases**

### *_Home Page_*
<details>
    <summary>Description</summary>
    
- Users can use this website to buy and sell products online.
- Users should be able to read the Instructions/FAQ.
- Users should be able to see the available products and services.
- Users should be able to see the latest products added to the website.
- Users should be able to see the offers available.
- Users should be able to see other customers feedback.
- The home page also provides information about the history and rational of the website.


</details>

<details>
    <summary>System & Actors</summary>

**System:** E-commerce Website.

**Actors:** User looking to buy or sell products online.
</details>

<details>
    <summary>Pre-Conditions</summary>

Users should register into the website to be able to sell products.
Users should register into the website to leave a feedback.

</details>

<details>
    <summary>Basic Flow</summary>

- The user browses for buy and/or sell products online and discovers the website. The user navigates to the Home Page, and is attracted by the visual impact of the website.
- The user sees the available products.
- The user sees the available services.
- The user sees the feedback left by the comunity.
- The user can register to the newsletter.

</details>

<details>
    <summary>Alternative/Exception Flow</summary>

- When the user selects a non-existent page, a 404 Error Page will be prompted guiding the user back to Home Page.
- If the user is not logged in, it is not to leave feedbacks/reviews.

</details>
<br/>



### *_Contact Us_*
<details>
    <summary>Description</summary>

- Users can subscribe to the newsletter, report issues or request assistance.
- Users can use this page to see the general info of Horizon Shop Company (including Address, Email address, phone, and a map showing Horizon Shop HQ).
</details>

<details>
    <summary>System & Actors</summary>

**System:** E-commerce Website.

**Actors:** Users who want to report issues, subscribe to a newsletter or request assistance.
</details>

<details>
    <summary>Pre-Conditions</summary>
Users should accept the Terms and Conditions to be able to ask for support/ report issues or for subscribing to the Newsletter.
</details>

<details>
    <summary>Basic Flow</summary>

- The user browses for buy and/or sell products online and discovers the website. The user navigates to the Home Page and then goes into the Contact Us Page.
- The user fills the mandatory fields.
- The user must accept the Terms and Conditions to subscribe to the newsletter and/or report issues/ request support.
- The user can select the available checkboxes to subscribe for the newsletter.
- The user submits the form.
- The user receives a notification indicating that the form has been submitted successfully.

</details>

<details>
    <summary>Alternative/Exception Flow</summary>

- The user can reset the form.
- When the user selects a non-existent page, a 404 Error Page will be prompted guiding the user back to Home Page.
</details>
<br/>


### *_Dashboard_*
<details>
    <summary>Description</summary>

- Users can access the Dashboard page only when they are signed in.
- Users can access a number of services divided into separate subpages listed as follow:

1. My Orders: to review all the shopped products.
2. My Profile: to create or edit their personal profile, change their passwords, register a new car and/or list/delete previously registered cars.
3. My Feedback: to visualise past or add new feedback. Once signed-in the user is presented with the possibility to delete/edit past feedback.

</details>

<details>
    <summary>System & Actors</summary>

**System:** E-commerce Website.

**Actors:** Users that want to access past/present orders, rewards, edit or create their profile and/or provide feedback.
</details>

<details>
    <summary>Pre-Conditions</summary>
User should register into the website to access the page.
</details>

<details>
    <summary>Basic Flow</summary>

- The user browses for buy and/or sell products online and discovers the website. The user sign into the website and navigates to the Dashboard Page. The user is presented with a list of possible options to access the orders, the feedback or their profile page.
- The user clicks into the desired subpage.
- The user is able to perform a list of desired actions of choice.

</details>

<details>
    <summary>Alternative/Exception Flow</summary>

- When the user selects a non-existent page, a 404 Error Page will be prompted guiding the user back to Home Page.
</details>
<br/>


### *_Sign In/ Sign Up_*
<details>
    <summary>Description</summary>

- Users can subscribe to the website.
- Users can sign-in to the website.

</details>

<details>
    <summary>System & Actors</summary>

**System:** E-commerce Website.

**Actors:** Users who want to register/sign-in to the website.
</details>

<details>
    <summary>Pre-Conditions</summary>
Users should be willing to register to the website.
</details>

<details>
    <summary>Basic Flow</summary>

- The user browses for buy and/or sell products online and discovers the website. The user navigates to the Home Page and then goes into the Sign Up Page.
- Users subscribe to the website by filling the mandatory fields.
- Users will receive a confirmation email to their address.
- Users verify the provided email address.
- Users sign-in with the chosen username/email and passwords.


</details>

<details>
    <summary>Alternative/Exception Flow</summary>

- The users can click on the Forgot Password Button if they are not able to sign in.
- The users can click to the Need an Account Button if they need to register.
- When the user selects a non-existent page, a 404 Error Page will be prompted guiding the user back to Home Page.

</details>



---

## **Design**

#### The webpage has been designed to provide a simple, interactive and intuitive view which is able to offer a pleasant experience to customers looking to buy and sell products online.
#### Every page has a minimalistic structure which however contains all the relevant features in order to provide the user with an interactive, clear and effective experience.  

- ### **Colour Scheme**
#### The goal is to use a colour palette that will provide the user with a good and positive impact at a first glance, when opening the website and through the entire navigation experience.
#### The list of colors is chosen to be pleasing to the eyes providing an excellent contrast that will allow the user to have prolonged navigation hours without tiring the eyes.

Colour Source: 
  - #### [Adobe Color](https://color.adobe.com/create/color-wheel)
  - #### [Color Hunt](https://colorhunt.co/) 
#### The main colors are Navy (), White (#FFFFFF) and Black (#1F1534) for text and background, Cyan () with Text White () for the feedback, Orange (FF9900) and Navy (#181D31) for the cards.
#### Navy (#181D31) it has also been used for the background in the Navbar and Footer. These colors are chosen to highlight different components and to make a good contrast providing a better view of those components.
 

- ### **Typography**
#### Google Fonts has been used to select the fonts for the Website.
#### The Main font used is 'Ubuntu' while the Sans-serif has been set up as fall-back in case the main font is not loaded.

Source:
  - [Google Fonts](https://fonts.google.com/)


- ### **Images and Videos**
#### Real and effective images have been used to provide a pleasant visual experience to the user.
#### The developer selected those images from the following source to mimic a full immersive e-commerce website.

Sources:  
  - [Pexels](https://www.pexels.com/)

--- 

## **Features**

- ### *__Database Schema__*:
#### The database schema, representing the structure and organization of Parkland database, has been realized using the Software Wondershare EdrawMax defining the primary and foreign key between tables for optimal definition of parents and child tables. A representation of the used schema can be visualised below. 

<details>
    <summary>Click here for the Database Schema </summary>  
<img src="static/images/readme/database-schema/database-schema.webp" alt="Database Schema" width="800px"/>
</details>


- ### *__Structure__*:
#### The website has been structured in an easy and user-friendly way with 6 main pages. Non-authenticated and authenticated customers are provided with two different page views. The Non-authenticated can visualise and access only the Home Page, Contact Us, Sign-In and Sign-Up pages, while the authenticated customers are also able to access the Booking and the Dashboard pages.

#### The project has been realize creating a single app for each Page:
- Home is the main app that stores the landing page of Horizon Shop.
- Contact App contains the views, urls and forms file for the Contact Us Page
- Dashboard App includes the views, urls and forms for all the Dashboard Sections 

#### The Structure of the website and the components used are listed below:


- ### *__Home Page__*:
#### The Home Page shows the logo of the website on the top left, a navigation bar on the top center and a search on the top right of the page.
#### A small underline animation activates when the user mouse hovers on of the elements in the nav bar, highlighting the content.
#### The active page is in Bold in the navigation bar when selected.
#### Depending on the device used (if laptop, desktop, tablet or smartphone) the position of the nav bar changes, creating a hamburger menu that will be displayed on the top right part of the page to adapt the view for a highly responsive rendering.
#### Those behaviour are consistent in all pages.
#### Following from Logo and the nav bar the user will see an hero carousel that displays all the offers available with images.

#### This is obtained by using a Django Tag with an if else statement to differentiate the content depending on the type of user (non-authenticated vs authenticated).
#### The Feedback Section shows the latest 3 feedbacks provided by other users.
#### The Latest Update Section shows new info about the company or new added services.
#### The Footer section concludes the Home Page, allowing the users to select the different sections of the website or to access Horizon Shop social media with one click.


- ### *__Contact Us Page__*:
#### This page has Header and Footer consistent with the Home Page.
#### The page is characterized by an image extended as background on top of which there is a form that the user can fill with the following information: First, Last Name, Email Address and a Checkbox that will allow the user to subscribe to a newsletter.
#### The user needs to accept the Terms & Conditions Check box to being able to move forward.
#### A Reset and a Submit buttons are included.
#### The Reset Button resets the form.
#### The user will be redirected to the same page and a notification is displayed informing the user that the request has been submitted successfully.
#### Following the form, the page shows a map with Hirozon Shop HQ’s location and details (Company Name, Address, Email, Phone Number and Opening Hours). Hoovering the mouse over the company information boxes a small animation highlights the hoovered icon for an effective visual impact.


- ### *__Sign Up/Sign In Page and Authentication Process__*:
#### This page has Header and Footer consistent with the Home Page.
#### The authentication module used for Horizon Shop is Allauth (a set of Django applications dealing with account authentication, registration, management, and third-party (social) account authentication) add link.
#### The pages have been directly imported from Allauth and customized for the needs of Horizon Shop.   

#### In the Sign Up Page, there is a form that the user can fill with the following information: Email Address (with confirmation), Username and Password (with confirmation).
#### A Reset and a Sign Up buttons are included.
#### The Reset Button resets the form.
#### By clicking on the Sign Up Button (if all mandatory fields have been filled-in correctly) the user will be redirected to the verification email page and a real email is sent to the user requesting validation. The user is not allowed to sign-in in parkland until the verification is completed.
#### If the form is not filled-in correctly, a message appears to the user to request to fill-in the information correctly.

#### In the Sign In Page, there is a form that the user can fill with the following information: Email Address (or Username) and Password.
#### A Sign in and a Forgot Password are included.
#### When clicking on Forgot Password the user is redirected to a Password reset form, where the user is prompted to insert the email address to receive an email with the new password.
#### By clicking on the Sign In Button (if all mandatory fields have been filled-in correctly) the user will be redirected to the Homepage.
#### If the form is not filled in correctly, the user is not able to access the web pages.


- ### *__Dashboard__*:
#### The Dashboard has been structured in an easy and user-friendly way with 
#### The Dashboard shows the logo of the website on the top left and a Hamburger Menu that toggles the opening and closing of a side nav bar.
#### All the forms have been realized with Crispy Forms of Django and Crispy bootstrapp (Details can be found in the following link: https://pypi.org/project/crispy-bootstrap5/)
#### The Dashboard shows also the Logout Button on the top right allowing the user to easily exit the website.
 
#### Depending on the device used (laptop, desktop, tablet or smartphone) the sidebar opens and closes automatically allowing the user to select different options from the hamburger menu and/or have a full visual of the page for a highly responsive rendering.
#### Those behaviours are consistent in all sections of Dashboard.
#### The Logo and the Sidebar are consistent in all sections.

#### All Dashboard's Sections listed below (Open the accordion for more information): 

<details>
    <summary>My Horizon Shop</summary>

#### My Horizon Shop summarises in just one page-view and with different cards all user’s information allowing to access Orders, Feedback and more. A link “View Details” is present in each card and will redirect the users to the selected list.

#### The Function .count() has been used in this section to retrieve the total number of the selected items.
#### A Reward Card displays the Customer Points earned depending on the quantity of Orders (100 points per booking).

</details>


<details>
    <summary>My Profile</summary>

#### “My Profile” is composed of XXX main sub-section (Edit Profile, Change Password) realized using class base views. In Edit Profile (realized using a UpdateView), the users can edit their own profile changing Username, First and Last Name, Email Address and Deactivate the Account (by unchecking the “Account Active” Checkbox).

#### The user can change the password using the “Change Password” Page. This has been realized using the PasswordChangeView and PasswordChangeForm provided by Django auth views/forms. The pages have been customized to match the color schema and layout of Horizon Shop.

</details>


<details>
   <summary>My Feedback</summary>

#### “My Feedback” includes 2 sub-section (Add Feedback and Feedback List).
#### The subsections are consistent in colors and layout with the Sections described above.

#### Add Feedback (realized using a CreateView) allows the user to leave a Feedback to Horizon Shop.
#### The latest 3 feedback added are displayed in the Homepage.

#### In order to realize a better visual impact feedback page a combination between the forms provided by Django and a custom form has been used where each feedback can be rated with a star system (from 1 to 5) for easy-to-use and effective view.
#### In the Feedback List for a consistent display setting through the website, the logged-in user feedback are shown in cards.

#### The Feedback List has been realized using a ListView. The user can review all information as well as Edit or Delete using dedicated buttons.
#### Consistently with all other pages deleting a feedback triggers a pop-up message requesting user’s confirmation.

</details>


- ### *__404 Error Page__*:
#### For any broken or incorrect links, the 404 Error page will be triggered. Here the user will have an image displayed in the background and above text box that will inform the users that the page is not correct.
#### A button is present in the text displayed and highlighted in cyan in order to allow the user to navigate back to the Home Page.  

---

## **Wireframe**
#### Balsamiq has been used in order to create the wireframe.
#### Below you can open the accordions divided by page and by device used (desktop, tablet and smartphone).


- ## Home Page 

<details>
    <summary>Home Page Wireframes</summary> 

<details>
    <summary>Click here for Desktop View - Anonymous </summary>  
<img src="static/images/readme/wireframes/homepage-desktop-anonymous.webp" alt="Desktop View Homepage" width="800px"/>
</details>

<details>
    <summary>Click here for Desktop View - Authenticated </summary>  
<img src="static/images/readme/wireframes/homepage-desktop-authenticated.webp" alt="Desktop View Homepage" width="800px"/>
</details>

<details>
    <summary>Click here for Tablet View</summary>
<img src="static/images/readme/wireframes/homepage-tablet.webp" alt="Tablet View Homepage" width="600px"/>
</details>

<details>
    <summary>Click here for Smartphone View</summary>
<img src="static/images/readme/wireframes/homepage-smartphone.webp" alt="Smartphone View Homepage" width="400px"/>
</details>

</details>


- ## Contact Us Page

<details>
    <summary>Contact Us Page Wireframes</summary>

<details>
    <summary>Click here for Desktop View</summary>
<img src="static/images/readme/wireframes/contact-us-desktop.webp" alt="Desktop View Contact Us Page" width="800px"/>
</details>

<details>
    <summary>Click here for Tablet View</summary>
<img src="static/images/readme/wireframes/contact-us-tablet.webp" alt="Tablet View Contact Us Page" width="600px"/>
</details>

<details>
    <summary>Click here for Smartphone View</summary>
<img src="static/images/readme/wireframes/contact-us-smartphone.webp" alt="Smartphone View Contact Us Page" width="400px"/>
</details>

</details>

- ## Dashboard


<details>
    <summary>Dashboard Pages Wireframes</summary>

- ### My Profile
<details>
    <summary>My Profile Section Wireframes</summary>

<details>
    <summary>Click here for Desktop View - Edit Profile Sub-Section</summary>
<img src="static/images/readme/wireframes/profile-edit-desktop.webp" alt="Desktop View Edit Profile Sub-Section" width="800px"/>
</details>

<details>
    <summary>Click here for Tablet View - Edit Profile Sub-Section</summary>
<img src="static/images/readme/wireframes/profile-edit-tablet.webp" alt="Tablet View Edit Profile Sub-Section" width="600px"/>
</details>

<details>
    <summary>Click here for Smartphone View - Edit Profile Sub-Section</summary>
<img src="static/images/readme/wireframes/profile-edit-smartphone.webp" alt="Smartphone View Edit Profile Sub-Section" width="400px"/>
</details>

<details>
    <summary>Click here for Desktop View - Change Profile Sub-Section</summary>
<img src="static/images/readme/wireframes/profile-change-password-desktop.webp" alt="Desktop View Change Profile Sub-Section" width="800px"/>
</details>

<details>
    <summary>Click here for Tablet View - Change Profile Sub-Section</summary>
<img src="static/images/readme/wireframes/profile-change-password-tablet.webp" alt="Tablet View Change Profile Sub-Section" width="600px"/>
</details>

<details>
    <summary>Click here for Smartphone View - Change Profile Sub-Section</summary>
<img src="static/images/readme/wireframes/profile-change-password-smartphone.webp" alt="Smartphone View Change Profile Sub-Section" width="400px"/>
</details>

</details>


- ### My Feedback
<details>
    <summary>My Feedback Section Wireframes</summary>

<details>
    <summary>Click here for Desktop View - Add Feedback Sub-Section</summary>
<img src="static/images/readme/wireframes/feedback-desktop.webp" alt="Desktop View Add Feedback Sub-Section" width="800px"/>
</details>

<details>
    <summary>Click here for Tablet View - Add Feedback Sub-Section</summary>
<img src="static/images/readme/wireframes/feedback-tablet.webp" alt="Tablet View Add Feedback Sub-Section" width="600px"/>
</details>

<details>
    <summary>Click here for Smartphone View - Add Feedback Sub-Section</summary>
<img src="static/images/readme/wireframes/feedback-smartphone.webp" alt="Smartphone Add FeedbackList Sub-Section" width="400px"/>
</details>

<details>
    <summary>Click here for Desktop View - Feedback List Sub-Section</summary>
<img src="static/images/readme/wireframes/feedback-list-desktop.webp" alt="Desktop View Feedback List Sub-Section" width="800px"/>
</details>

<details>
    <summary>Click here for Tablet View - Feedback List Sub-Section</summary>
<img src="static/images/readme/wireframes/feedback-list-tablet.webp" alt="Tablet View Feedback List Sub-Section" width="600px"/>
</details>

<details>
    <summary>Click here for Smartphone View - Feedback List Sub-Section</summary>
<img src="static/images/readme/wireframes/feedback-list-smartphone.webp" alt="Smartphone View Feedback List Sub-Section" width="400px"/>
</details>

</details>

</details>

- ## 404 Error Page

<details>
    <summary>My Feedback Section Wireframes</summary>
    
<details>
    <summary>Click here for Desktop View</summary>
<img src="static/images/readme/wireframes/error404-desktop.webp" alt="Desktop View Error 404 Page" width="800px"/>
</details>

<details>
    <summary>Click here for Tablet View</summary>
<img src="static/images/readme/wireframes/error404-tablet.webp" alt="Tablet View  Error 404 Page" width="600px"/>
</details>

<details>
    <summary>Click here for Smartphone View</summary>
<img src="static/images/readme/wireframes/error404-smartphone.webp" alt="Smartphone View Error 404 Page" width="400px"/>
</details>


</details>
---

## **Technologies Used**

- ### **Languages**

#### The Languages used are:
 - HTML5
 - CSS3
 - JAVASCRIPT
 - PYTHON + DJANGO

#### Only custom HTML, CSS, JavaScript, Python Code has been used.


- ### **Frameworks, Libraries & Programs Used** 

#### Django Framework has been used.

- #### Google Fonts: 
    - #### Google fonts were used for the font in all pages throughout the project.

- #### Font Awesome:
    - #### Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

- #### Git: 
    - #### Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- #### GitHub: 
    - #### GitHub is used to store the projects code after being pushed from Git.

- #### Balsamiq: 
    - #### Balsamiq was used to create the wireframes during the design process.

- #### TinyPNG
    - #### TinyPNG has been used to compress images.

- #### Convertio
    - #### Convertio has been used to convert the images in webp exxtension.

- #### Heroku
    - #### Heroku is a Platform as a Service (PaaS) and it has been used to run the Parkland website application entirely on the cloud.

- #### PostgreSQL 
    -  #### PostgreSQL is a powerful, open source object-relational database system and it has been used for the Parkland Project. 
  
- #### Bootstrap 5
    -  #### Bootstrap is a framework for building responsive, mobile-first, sites with jsDelivr and a template starter page used in Parkland. 

- #### Wondershare EdrawMax:
    - #### Wondershare EdrawMax has been used to create the Database Schema for the website.

- #### Microsoft Whiteboard:
    - #### This is an infinite, collaborative canvas for effective meetings and engaging learning. Whiteboard was used to summarise the programming steps, the layout and the rationale behind those. Whiteboard has been used together with the Wondershare EdrawMax.

- #### AWS
    - #### Used to store all all the static files. 


---

## **Testing**
The testing phases have been carried out using the **PIP8 Python Validator**. No errors have been identified from the Validators as can be seen in the screenshots below:

- **Python**

<details>
    <summary>PIP8 Python Validator</summary>


<details>
    <summary>Click here for PIP8 Python Validator - Horizon Shop [urls.py]</summary>
<img src="static/images/readme/validation-pip8/Horizon Shop-url.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>

<details>
    <summary>Click here for PIP8 Python Validator - Horizon Shop [settings.py]</summary>
<img src="static/images/readme/validation-pip8/Horizon Shop-settings.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>

<details>
    <summary>Click here for PIP8 Python Validator - Contact [urls.py]</summary>
<img src="static/images/readme/validation-pip8/contact-url.py.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>

<details>
    <summary>Click here for PIP8 Python Validator - Contact [views.py]</summary>
<img src="static/images/readme/validation-pip8/contact-views.py.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>

<details>
    <summary>Click here for PIP8 Python Validator - Contact [forms.py]</summary>
<img src="static/images/readme/validation-pip8/contact-form.py.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>

<details>
    <summary>Click here for PIP8 Python Validator - Dashboard [urls.py]</summary>
<img src="static/images/readme/validation-pip8/dashboard-url.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>

<details>
    <summary>Click here for PIP8 Python Validator - Dashboard [views.py]</summary>
<img src="static/images/readme/validation-pip8/dashboard-views.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>

<details>
    <summary>Click here for PIP8 Python Validator - Dashboard [forms.py]</summary>
<img src="static/images/readme/validation-pip8/dashboard-forms.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>


</details>

The testing phases have been also carried out using the **W3C Javascript Validator**, **W3C CSS Validator** and **W3C Markup Validator**(in all pages). No errors have been identified from the Validators as can be seen in the screenshot below: 

- **JavaScript**

<details>
    <summary>W3C Javascript Validator</summary>

<details>
    <summary>Click here for W3C Javascript Validator - Script.js</summary>
<img src="static/images/readme/validation-js/js-script.js.webp" alt="W3C Javascript Validator - Home Page" width="800"/>
</details>

</details>

- **CSS**

<details>
    <summary>W3C CSS Validator</summary>

<details>
    <summary>Click here for W3C CSS Validator - Custom-style.css</summary>
<img src="static/images/readme/validation-css/css-custom-style.webp" alt="W3C Markup Validator - Home Page" width="800"/>
</details>

<details>
    <summary>Click here for W3C CSS Validator - Rating-stars.css</summary>
<img src="static/images/readme/validation-css/css-rating-stars.webp" alt="W3C Markup Validator - Home Page" width="800"/>
</details>

</details>

- **HTML**

<details>
    <summary>W3C Markup Validator</summary>

<details>
    <summary>Click here for W3C Markup Validator - Home Page</summary>
<img src="static/images/readme/validation-html/html-homepage.webp" alt="W3C Markup Validator - Home Page" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Contact Us</summary>
<img src="static/images/readme/validation-html/html-contact.webp" alt="W3C Markup Validator - Contact Us" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Sign In</summary>
<img src="static/images/readme/validation-html/html-signin.webp" alt="W3C Markup Validator - Sign In" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Sign Up</summary>
<img src="static/images/readme/validation-html/html-signup.webp" alt="W3C Markup Validator - Sign Up" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Sign Out</summary>
<img src="static/images/readme/validation-html/html-signout.webp" alt="W3C Markup Validator - Sign Out" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Dashboard</summary>
<img src="static/images/readme/validation-html/html-dashboard.webp" alt="W3C Markup Validator - Dashboard" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Edit Profile</summary>
<img src="static/images/readme/validation-html/html-profile-edit.webp" alt="W3C Markup Validator - Edit Profile" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Change Password</summary>
<img src="static/images/readme/validation-html/html-profile-changepassword.webp" alt="W3C Markup Validator - Change Password" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Add Feedback</summary>
<img src="static/images/readme/validation-html/html-feedback-add.webp" alt="W3C Markup Validator - Thank You" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Edit Feedback</summary>
<img src="static/images/readme/validation-html/html-feedback-edit.webp" alt="W3C Markup Validator - Error 404" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Details Feedback</summary>
<img src="static/images/readme/validation-html/html-feedback-details.webp" alt="W3C Markup Validator - Error 404" width="800px"/>
</details>

<details>
    <summary>Click here for W3C Markup Validator - Delete Feedback</summary>
<img src="static/images/readme/validation-html/html-feedback-delete.webp" alt="W3C Markup Validator - Error 404" width="800px"/>
</details>

</details>


- ### **Lighthouse Validator**
Below it is possible to taka e look at the result obtained in Lighthouse:

<details>
    <summary>Click here for for Lighthouse Desktop - Homepage</summary>
<img src="static/images/readme/lighthouse/homepage-desktop.webp" alt="Lighthouse Desktop Homepage" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Homepage</summary>
<img src="static/images/readme/lighthouse/homepage-mobile.webp" alt="Lighthouse Mobile Homepage" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Contact Us</summary>
<img src="static/images/readme/lighthouse/contactus-desktop.webp" alt="Lighthouse Desktop Contact Us" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Contact Us</summary>
<img src="static/images/readme/lighthouse/contactus-mobile.webp" alt="Lighthouse Mobile Contact Us" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Sign In</summary>
<img src="static/images/readme/lighthouse/signin-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Sign In</summary>
<img src="static/images/readme/lighthouse/signup-desktop.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Sign Up</summary>
<img src="static/images/readme/lighthouse/signup-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Sign Up</summary>
<img src="static/images/readme/lighthouse/signin-desktop.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Sign Out</summary>
<img src="static/images/readme/lighthouse/sign-out-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Sign Out</summary>
<img src="static/images/readme/lighthouse/sign-out-mobile.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Password Reset Desktop</summary>
<img src="static/images/readme/lighthouse/password-reset-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Password Reset Desktop</summary>
<img src="static/images/readme/lighthouse/password-reset-mobile.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - My Horizon Shop</summary>
<img src="static/images/readme/lighthouse/myHorizon Shop-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - My Horizon Shop</summary>
<img src="static/images/readme/lighthouse/myHorizon Shop-mobile.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Edit Profile</summary>
<img src="static/images/readme/lighthouse/edit-profile-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Edit Profile</summary>
<img src="static/images/readme/lighthouse/edit-profile-mobile.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Change Password Profile</summary>
<img src="static/images/readme/lighthouse/change-password-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Change Password Profile</summary>
<img src="static/images/readme/lighthouse/change-password-mobile.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Add Feedback</summary>
<img src="static/images/readme/lighthouse/add-feedback-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Add Feedback</summary>
<img src="static/images/readme/lighthouse/add-feedback-mobile.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Feedback List</summary>
<img src="static/images/readme/lighthouse/add-feedback-desktop.webp" alt="Lighthouse Desktop Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Feedback List</summary>
<img src="static/images/readme/lighthouse/add-feedback-mobile.webp" alt="Lighthouse Mobile Sign In" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Desktop - Error 404</summary>
<img src="static/images/readme/lighthouse/error404-desktop.webp" alt="Lighthouse Desktop Error 404" width="600px"/>
</details>

<details>
    <summary>Click here for for Lighthouse Mobile - Error 404</summary>
<img src="static/images/readme/lighthouse/error404-mobile.webp" alt="Lighthouse Mobile Error 404" width="600px"/>
</details>



- ### **Test Cases**

- #### List of Manual Test Cases perfomed. 
All the Tests have also been performed in all the Devices and the tests includes also Layout testing. 

| Page | Feature | Expected Result | Status |
| --- | --- | --- | --- |
| Home | Header | Make sure that the Logo and the nav bar are displayed on the top part of the Home Page. |  |
| Home | Header | Make sure that non authenticated users can only access Home, Contact Us, Sign In/Up Pages. |  |
| Home | Header | Make sure that authenticated user can see/access Home, Booking, Contact Us, My Horizon Shop Dashboard. |  |
| Home | Header | Make sure that by clicking on the Logo the user is redirected to the Home Page. |  |
| Home | Horizon Shop Section | Make sure that the Image of Horizon Shop is displayed with no overlap with the Logos, Nav Bar and/or text. |  |
| Home | Horizon Shop Section | Make sure that the Image of Horizon Shop is displayed on the right and does not overlap with the Text Description on the left. |  |
| Home | Service Section | Make sure that the Services are displayed with Image on top and text is centered. |  |
| Home | Services Section | Make sure that only 3 cards are displayed with no overlap between the images and the text included into the cards. |  |
| Home | Story Section | Make sure that the Image is displayed with no overlap with other sections. |  |
| Home | Story Section | Make sure that the Image is displayed on the left side while the text is on the right. |  |
| Home | Feedback Section | Make sure that the feedback area displays a carousel with Users’ Feedback.|  |
| Home | Feedback Section | Make sure that the user can use the arrows to switch between feedbacks. |  |
| Home | Updates Section | Make sure that the cards with the company updates are displayed correctly.|  |
| Home | Footer | Make sure that the footer displays the information of the company |  |
| Home | Footer | Make sure that the footer provides the link to access the social media and when clicking on the icons a new tab is opened |  |
| Home | Footer | Make sure that the user can sign up with an email address to receive the newsletter.|  |
| Home | Footer | Make sure that by clicking on the newsletter form button if no email or an invalid email has been entered an error message is displayed to the user. |  |
| Home | Footer | Make sure that by clicking on the newsletter form button if correct email has been entered a success message notification is displayed to the user |  |
| Contact Us | Images | Make sure that the background image is displayed correctly. |  |
| Contact Us | Form | Make sure all the fields (First Name, Last Name, Email, Text) are editable. |  |
| Contact Us | Form | Make sure all the checkboxes (Newsletter and Terms & Condition) are clickable. |  |
| Contact Us | Form | Make sure all the fields (First Name, Last Name, Email, Text, Terms & Condition) are mandatory. |  |
| Contact Us | Form | Make sure that the Reset Form Button works and deletes all the information entered in the form. |  |
| Contact Us | Form | Make sure that the Submit Button works and provides a clear message to the user. |  |
| Dashboard | My Horizon Shop | Make sure that only authenticated user can access and view the content of the My Horizon Shop Page. |  |
| Dashboard | My Parkland | Make sure that Booking, Cars, Feedback and Rewards Cards are displayed correctly. |  |
| Dashboard | My Parkland | Make sure that the correct value of Bookings, Cars, Feedback and Rewards is displayed in each card. |  |
| Dashboard | My Parkland | Make sure that the from the cards it is possible to access the lists of Bookings, Cars and Feedback. |  |
| Dashboard | My Parkland | Make sure that the any available message is displayed correctly under the messages center.  |  |
| Dashboard | My Profile | Make sure that the My Profile Section includes the Edit Profile, Change word, Add Cars and Cars List Sub-Sections. |  |
| My Profile | Edit Profile | Make sure that by clicking Edit Profile the user is able to access the personal information form. |  |
| My Profile | Edit Profile | Make sure that in the Edit Profile Form the user can edit only his/her own personal information. |  |
| My Profile | Change password | Make sure that by clicking Change word Sub-Section the user is able to successfully access the Change word Page. |  |
| My Profile | Change password | Make sure that in the Change word Form the user can change the word associated to his/her account. |  |
| My Profile | Add Feedback | Make sure that by clicking Add Feedback the user is able to access the Add Feedback Page form. |  |
| My Profile | Add Feedback | Make sure that after filling-in the form, the user is redirected to the Feedback List Page if the form is valid. |  |
| My Profile | Add Feedback | Make sure that after the redirect to the Feedback List Page a Message is displayed to the user confirming the creation of the Feedback. |  |
| My Profile | Add Feedback | Make sure that the user is obliged to fill the mandatory fields correctly. |  |
| My Profile | Feedback List | Make sure that by clicking Feedback List Sub-Section the user is able to access his/her own personal Feedback List. |  |
| My Profile | Feedback List | Make sure that the user can visualise the information of his/her own Feedback. |  |
| My Profile | Feedback List | Make sure that a Delete button is present and that the user can click on the Delete button to delete the entered feedback. |  |
| My Profile | Feedback List | Make sure that by clicking on the Delete Button a modal requesting confirmation to the user in opened. |  |
| My Profile | Feedback List | Make sure that after confirmation the user is redirected to the Feedback List and a message confirm that deletion of the Feedback id displayed. |  |
| My Profile | Feedback List | Make sure that an Edit button is displayed. |  |
| My Profile | Feedback List | Make sure that by clicking on the Edit button the user can update the information of a previous entered Feedback. |  |
| My Profile | Feedback List | Make sure that every page is responsive and that no overlap are presents. |  |


- #### List of Automated Test Cases perfomed:
#### The Automation testing is the process of testing the software (as well as other tech products) to ensure it meets the requirements. In Parkland 10 Automated Tests have been designed and run, all with positive final results. 

#### The Tests have been included in the tests folder and have been divided by type allowing a better visualization of the tests carried out. See below for further details:

- Urls Automation Testing: The urls tests aim to ensure that all the urls in the application are functioning correctly calling the matched View.

- Views Automation Testing: The aim of the Views Automation Testing is to ensure that once the views are called they return a status code 200 meaning that the View is working correctly.

- Forms Automation Testing: The aim of the Forms Automation Testing is to ensure that when filling-in the form (or when trying to send an empty form), only if all the information is populated correctly the form is sent, otherwise it is not possible to proceed. 


### **Additional Tests**
Tests have been performed on Firefox, Microsoft Edge, Chrome and Safari and the result is consistent in all the browsers. 

Additional tests include checks on different devices using the Toggle Device Emulation in Firefox and Microsoft Edge. Below the list of devices used for the tests through the Responsive Design Mode in Firefox is shown:
* iPhone 12 Pro Max
* iPad Pro
* iPad 
* Moto 4G
* Samsung Galaxy S20 Ultra
* Surface Duo

### **Bugs**
- No other bugs could be found in the website during the test phase.


### **Future Implementation**
- Listed here the future implementation:


---

## **Development** 
### Deployment

- ### **Github**
The repository for the project Horizon Shop has been created using Github using the following procedures:
1. Create a Github account [Github.com](https://github.com/)
2. In the top left Github Home Page click on the green New Button in order to create a new repository
3. Select the Template if available (Example: Code-Institute-Org/gitpod-full-template)
4. Choose the Repository name
5. Click on the Create Repository Button in order to create the repository
6. Install the Gitpod Extension in your browser
7. Once Gitpod Extension has been installed, accessing the repository previously created, click on the Gitpod Button
8. A new page will be opened and the Workspace will be created
   

- ### **Heroku App**
Heroku is a platform as a service (PaaS) used to run, operate the Horizon Shop website application entirely in the cloud using the following procedures:
1.	Create an Heroku Account [Heroku.com](https://www.heroku.com/)
2.	In the top right of the “Welcome to Heroku” Screen click on the New drop-down menu
3.	Click on the Create “New App Button”
4.	Select an App Name (Example: Horizon Shop)
5.	Choose the region: “Europe”
6.	Click on the Create App Button
7.	Go in the Settings Tab
8.	In the Config Vars section click on the Reveal Config Vars Button
9.	Enter “PORT” in the Key field, “8000” in the Value field and then press Add
10.	Go in the Buildpacks section and click on the Add Buildpack Button
11.	Select python and press Save Changes
12.	Go in the Deploy Tab 
13.	In the Deployment method section select Github to connect with your repository
14.	In the App connected to Github section type the name of the repository (Example: Horizon Shop) and then press Add
15.	Go in the Manual section, select the correct branch and click on Deploy Branch
16.	Click on the View Button as soon as the deploy is finished and you will be redirected to a new page with your application. 


- ### **GitHub Pages**
The project was deployed to GitHub Pages using the following steps:
1.	Log in to GitHub and locate the GitHub Repository created
2.	Click on the Setting Button
3.	On the left menu bar, click on the "Pages" Tab
4.	Under "Source", click the dropdown called "None" and select "Main"
5.	The page will automatically refresh
6.	When the website is disployed, on top of this page you can see the link of the live website 


<!-- Forking Content from Code Institute Readme File Sample -->
- ### **Forking the GitHub Repository**  
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:
1.	Log in to GitHub and locate the GitHub Repository
2.	At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button
3.	You should now have a copy of the original repository in your GitHub account


- ### **Local Clone**
By creating a Local Clone you will be able to create a copy of the repository that is avilable in your local computer.
In order to create a Local Clone follow the steps below: 
1.	Log in to GitHub and locate the GitHub Repository that you want to clone
2.	Click on the Code Button
3.	To clone the repository using HTTPS, under "Clone with HTTPS", copy the link
4.	Open Git Bash
5.	Change the current working directory to the location where you want the cloned directory to be made
6.	Type git clone as shown in the example below and then paste the URL copied in Step 3
>$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
1. Press Enter 
2. Your local clone will be created


---

## **Credits**

#### Thanks to my Mentor, Narender Singh, for his guide and support in the realization of this project, for his availability and for being willing to talk to me on a Sunday night!!
#### Thanks to the useful references and suggestions derived from sources listed below, I manage to gain a deeper understanding of how Django works and is used, including the integration with HTML. In addition, continuous trial and error tests provided a useful means to further experiment on the usage of these used programming languages for the creation of the site.


- ### Content & Media
#### The landing Page of the website was initially realised using a bootstrap template. This Template has been gradually updated to meet the need of the website. A Django framework has been used for the realization of the site. The content of the application is entirely customised. In order to consolidate the knowledge acquired during the Code Institute Course dedicated to Django (as well as the HTML, CSS and Javascript), I have used the websites listed below studying and focussing on the writing coding procedures and its best practices:
- [Medium.com](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
- [Learn.shayhowe.com](https://learn.shayhowe.com/html-css/writing-your-best-code/)

#### Additional studies for a better understanding of Django have been carried out using the following source and video tutorials:
- [W3School - Django](https://www.w3schools.com/django/) 
- [Javatpoint.com - Django Tutorial](https://www.javatpoint.com/django-tutorial)
- [Django-rest-framework.org - Django Views](https://www.django-rest-framework.org/api-guide/views/)
- [pythonguides.com](https://pythonguides.com/python-django-filter/)
- [Thanks to Codemy.com for the Django Tutorial](https://www.youtube.com/watch?v=B40bteAMM_M)
- [Thanks to CodingEntrepreneurs - Youtube Video Function Based View to Class Based View](https://www.youtube.com/watch?v=SNXn76SI1Ks)
- [Djangoproject.com - Creating Forms from Models](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#controlling-which-fields-are-used-with-fields-and-exclude)


#### Messages Framework has been implemented in Parkland and here is the link source for the studies:
- [Djangoproject.com - Messages](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/)


#### The most complex developing portions of the Parkland Website application were:


#### The following website were inspirational and helped me understanding how to structure the logic on the gravity of the coin entered in the table. I have customized and created my own code taking inspiration from:
- [Djangoproject.com - Making queries](https://docs.djangoproject.com/en/4.1/topics/db/queries/)
- [pythonguides.com](https://pythonguides.com/python-django-filter/)
- [Thanks to StackOverflow and the Comunity - Difference Queryset](https://stackoverflow.com/questions/5945912/how-to-get-the-difference-of-two-querysets-in-django)
- [Thanks to Codemy.com - Youtube Video Fetch Data](https://www.youtube.com/watch?v=H3joYTIRqKk&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=6)
- [Books.agiliq.com - How to use Q](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html)


#### Listed here additional sources of the studies: 

- [Developer.mozilla.org - Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Developer.mozilla.org - Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)


#### Source for the Template of the Landing Page:
- [Thanks to Themewagon for the Bootstrap 5 Template](https://themewagon.com/)


#### Listed here the source of studies for the automation testing: 
- [Djangoproject.com - Testing Overview](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)
- [Djangoproject.com - Testing tools](https://docs.djangoproject.com/en/dev/topics/testing/tools/)
- [Developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)

- [Favicon.io](https://favicon.io/) was used to include the favicon in the website.


#### For the realization of the 404 error page I found a guide on how to create the file here: 
- [Levelup.gitconnected.com](https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317)

#### Thanks to Kasia Bogucka and Narender Singh for suggesting the use of github wiki site to create the Markdown file. They have also provided the link for the Sample Readme of Code Institute.
- [Sample Readme File - Code Institute](https://github.com/Code-Institute-Solutions/SampleREADME)
- [Markdown - Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

#### All the Images as well as the Video included in the Home Page have been taken from [Pexels.com](https://www.pexels.com/)

#### But most of all thanks to my girlfriend Rosi Davi who is always supporting me in this amazing journey!
#### Thank you to the entire Code Institute Team and the Slack Community for their feedback, help and support. 

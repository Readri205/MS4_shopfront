![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/amiresponsive_tulip.png?raw= "WINE SHOP")

[View the live **WINE SHOP**  :wine_glass:  project here.](https://plant-manager-flask-mongodb.herokuapp.com/)

# **WINE SHOP :wine_glass:**


## Site Goals

* This website provides a functionality for users to create a list of plants in collections, either by entering plant details or by uploading from a search. The searches can be made in a number of ways, including by name, image or by filters. Users are able to update the details of plants and collections in their lists. Users are also able to delete plants and collections. A user can also move a plant from one collection to another if so desired. A user can also amend their personal details including email, username and telephone number. A user is also able to fully delete their login and all plants and collections listed on that login. Each users logn and details are specific to that user and cannot be viewed by any other user.

* **NOTE: This site is currently entirely for educational purposes only. Whilst there is an ability to register for the site, any personal details entered are not protected.**

* The website is **'functional'**, allowing users to enter information about **Plants** and to view information on specific plants. The site is designed to show details on **Plants** where required.
* The website concept is to provide a user with a useful list of plants;
  * what is the name of the plant?
  * what are the scientific names and details?
  * what collection do I have the plant in?
  * The structure for the **Plants** is provided by;
    * a list of **plants** entered by and for, a specific user;
    * a list of **collections** entered in which plants can be listed;
    * entering a plant can be made using the following methods;
      * **manual** where a user already has details for a plant, external to the application;
      * **search** to identify a **name** characteristic for a plant;
      * **filter** to identify **colour** characteristics for a plant; and
      * **image** using a computer or mobile device to upload a **file image**.

      * The website sources data from the **[Trefle.io](https://Trefle.io/)** and **[Plant.id](https://plant.id/)**. The website primarily makes use of Application Programming Interfaces (API's) to construct the plant search data. The **[MongoDB](https://www.mongodb.com/cloud/atlas)** is used to store user data and allows for create, read, update and delete data **(CRUD)** for plant details and their user login data. API and other data source details are provided in the **'Application Programming Interfaces (API's) Used'** section below.

* If the site is perceived as successful, it is anticipated that the site could be expanded as;
* there is a significant amount of data in the Trefle database that can be utilised for more specific searches and filtering;
* other API sources could also be utilised to improve the information set;
* other functions could be added such as creating as a calendar for gardening jobs at a particular time of year.

* The site is designed to be responsive and accessible on a range of devices, making it easy to navigate for interested users. The website was designed using **'Mobile First'** principles as the site must be perceived to be quick and easy to use and read as a reference site on a mobile device.

## User Experience (UX)

*   ### User stories

  *   #### First Time Visitor Goals
      * The first time visitor will want to;
        * easily understand the main purpose of the site;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_maininfo.png?raw= "Home")

        * be able to easily navigate throughout the site to find content;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mainmenu.png?raw= "Main Menu")

        * view the carousel images just beneath the header;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_carousel.png?raw= "Carousel")

        * scroll down through the information, read the content, view each of the function cards;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_maininfo.png?raw= "Cards")

        * register for the site and create login credentials;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_register.png?raw= "Register")

        * enter plant details for plants they are interested in;

          * login to the site;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_login.png?raw= "Login")

          * immediately view their plants list;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_myplants.png?raw= "My Plants")

          * immediately view a plant from list;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_viewplant.png?raw= "My Plants")

          * view their collections list;

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mycollections.png?raw= "My Collections")

          * search for plants in one of the search methods;
            * name;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_searchname.png?raw= "Search Name")

            * View plants returned from a search;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_return.png?raw= "Search Name")

            * View individual plant details from a search return;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_plantdeets.png?raw= "Search Name")

            * filter by attribute;

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_filter.png?raw= "search Filter")

            * image upload.

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_image.png?raw= "Image")

            ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_imagesuggestions.png?raw= "Image Suggestions")

          * add a plant to users plant list and a collection.

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_addplant.png?raw= "Add Plant")

        * see their user details and amend if necessary.

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mydetails.png?raw= "My Details")

        * contact us to ask about data projects that they may be interested to have completed as an item of work.

          ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_contact.png?raw= "Contact")

  *   #### Returning Visitor Goals
      * The returning visitor will want to;
        * login to the site;
        * immediately view their plants list;
        * view their collections list.
      * **A returning visitor** may want to go straight to the 'Plant' search function;

          * search for plants in one of the search methods;
            * name;
            * filter by attribute;
            * image upload.
          * on finding a plant the user in they may want to find out more details on that plant by choosing the 'plant details' button;
            * there a number of specific details including in the return;

          * the user may want to add the plant to their plant list and a collection.
      * **A returning visitor** may want to go straight to the 'Contact Us' page;
        * contact us for more information or to provide comments about the site;
        * contact us to ask about projects that they may be interested to have completed as an item of work.

  *   #### Frequent User Goals
      * The frequent user will want to;
        * login to the site;
        * immediately view their plants list;
        * view their collections list.
      * **A returning visitor** may want to go straight to the 'Plant' search function;

          * search for plants in one of the search methods;
            * name;
            * filter by attribute;
            * image upload.
          * on finding a plant the user in they may want to find out more details on that plant by choosing the 'plant details' button;
            * there a number of specific details including in the return;

          * the user may want to add the plant to their plant list and a collection.
      * **A frequent visitor** may want to go straight to the 'Contact Us' page;
        * contact us for more information or to provide comments about the site;
        * contact us to ask about projects that they may be interested to have completed as an item of work.

  *   #### Mobile Menu
        * On mobile devices the menu is shown as a 'hamburger' drop down;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mobile.png?raw= "Mobile")

        * On mobile devices the menu is shown as a 'hamburger' drop down;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mobilemenu.png?raw= "Mobile Menu")

        * On mobile devices the search function operates in the same manner as for larger screens;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_mobilesearch.png?raw= "Mobile Search")

        * On mobile devices an image can be captured and uploaded directly;

        ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/app_capture.png?raw= "Mobile Capture")

*   ### Design
  *   #### colour Scheme
      * The main colour is 'Teal' (#008080), designed to provide a light neutral background to highlight a 'Yellow" (#FFFF00) text. The colours have been manipulated to lighten or darken them using 'Materialize' CSS properties. The various shades of 'Teal' are used to reference the the plant kingdom.
      * The main colours, 'Yellow" (#FFFF00)on a 'Teal' (#008080) background, were potentially a concern for the 'colour blind' fraternity. Some basic tests with colour blind persons did not present any issues, however the spectrum of colour blindness is vast so there may be some issues with some persons. The colour structure is relatively easy to change if there is negative feedback.
  *   #### Typography
      * The site uses the 'Materialize' 'Roboto' default font throughout the whole website. 'Roboto' is a clean font which is both attractive and appropriate.
  *   #### 'Materialize' Card Structure
      * The 'Materialize' card structure is used to return search results. This structures the returns into identifiable components with an image and corresponding details for a return. This keeps each return distinct and independent of each other.
      * The user plant and the collections lists are not constructed in 'Materialize' cards but are shown as accordion lists that the user can access to view more details on each item.
  *   #### Imagery
      * A 'Dark' theme has been intentionally chosen to make it distinct from other numerous 'plant' applications. The dark background provides a clear backdrop to highlight the colours and shapes of plants, and also to highlight clearly the information that is provided in the teal 'card' structure.
      * The header contains a carousel designed to be striking and catch the user's attention and to provide some unique image themes. To provide some context on larger screens each image has a clear title description sourced from the original image provided by the contributor. Note that on some screen sizes the titles can be difficult to read where they blend into the image. As the titles are not fundamental to the website information it has been considered 'acceptable'.
      * Note that the background, carousel and main home page cards all reference  [© Unsplash.com](https://unsplash.com/) for the images. As this is the case there is a risk that an image could be removed from the source and so the site image would fail. Copies of images are retained in the project image folder for backup.
      * The background image is of 'Dark plants ...', designed to provide a dark neutral background yet reference the plant kingdom. The header images are intended to blend into the background image with the 'deep black' backgrounds.

          ![alt text](https://images.unsplash.com/photo-1586990684319-40c14d005de9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1402&q=80)

          *['Dark plants ...'](https://unsplash.com/photos/aDvrHHFGAlE)  By Amir Nyct  [© Unsplash.com](https://unsplash.com/)*


*   ### Wireframes
  *   #### Original Wireframe Design (October 15, 2020).
      * The **'Home'** page includes a basic overall introduction to the purpose of the site. Cards are used to describe the main features of the site. The features are User Plant List, User Collections, Search by a Name, Filter, Image Upload and a  Year Calendar.
      * Once the User has a login these features are accessible from the menu.
      * The menu includes direct links to;
        1. User plant list;
        1. User Collection list;
        1. Search list;
        1. User details.
      * MongoDB to be used as the database core for the user, plant and collection details.
      * The search list is considered to return name and image upload searches as detail page returns.
      * Sources for search data were considered as follows;
        * Trefle.io plant search - [Trefle.io](https://Trefle.io/)
        * Plant.id for image recognition - [Plant.id](https://plant.id/)
      * The contact page uses the following source;
        * Automated Email Response - [Emailjs](https://www.emailjs.com/)
      * All images in the wireframe are by example only.
      *   The **Original Wireframe Design** can be viewed here - [View](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/wireframes/rhcgardenmanager.pdf)
  *  #### Actual Site Design.
      * The developed site uses many of the concepts from the original Wireframe design. Variations are as follows;
        1. The **Home** page has a number of cards explaining the key features of the site, but there is no **'Calendar View'** feature;
        1. The **Calendar Feature** has proven difficult to implement as information to support this appears lacking in the plant world. Most plant and gardening information providers appear to have their own databases to support this kind of feature as a Unique Selling Product (USP). The Trefle.io database has some details such as 'bloom months' and 'sowing months'. However, this data is not complete. The feature could be added as a future feature on the site.
        1. The **'Contact Form'** has its own page. It is accessible from every page either through the main menu or from the footer;
      * The listed API sources, [Trefle.io](https://Trefle.io/), [Plant.id](https://plant.id/) were utilised. [Emailjs](https://www.emailjs.com/) was utilised for email response.

## Features

*   ### Responsive for Device Size
    * Mobile / Smaller screen size
      * The site is designed primarily for use on a mobile. The 'Box Content' structure using Materialize Grid System has been utilised so that the information boxes (search results) will stack vertically on small screens for readability.
      * The menu system uses the Materialize 'navbar' functionality for small screens using the 'toggle' capability for the 'drop down' menu list from a 'hamburger' icon.
      * The navbar is 'fixed' to the top of the screen at all times on page scroll down for easy access.
      * The navbar is coloured 'dark teal' to make it distinctive from the site pages.
      * The 'hamburger' is coloured 'dark yellow' to make it visible yet not intrusive when viewing the site details.
      * See comments above with regard to potential colour blindness impacts of the yellow and green colour mix.
      * The 'drop down' site page options are coloured 'dark yellow' with the current page shown with an 'off-white' background. Note that on a mobile, the drop down lists can prove 'sticky' on selection with touch screen and sometimes go through to the wrong selection.
      * The header image and the carousel images are suitably sized for smaller screens.
    * Desktop / Laptop large screen size
      * The 'Box Content' is effective on wide screens. The Materialize Grid System allows for the 'Box Content' to align horizontally in themes that are consistent on each of the 'Home' and 'Search' pages.
      * The header menu system uses the Materialize 'navbar' functionality with the menu option pages listed to the right.
      * The navbar is coloured 'dark teal' to make it distinctive from the site pages.
      * The menu item list is coloured 'dark yellow' to make it visible yet not intrusive when viewing the site details.
      * The 'drop down' site page options are coloured 'dark yellow' with the current page shown with an 'off-white' background.
      * The header image and carousel images are designed to be larger and 'impactful' on the larger screen size.

*   ### Interactive Elements
    * The first key feature of the site is the ability for the user to;
       * enter their own list of plants;
       * place their listed plants into collections;
       * define their collections.
    * The second key features of the site is the ability for a user to search for plants;
       * by entering a 'name';
       * by using a filter for required 'colours'; or
       * upload an image from file.
    * Each method returns results that the user can;
       * review and choose to see more details on any particular return;
       * add the plant to their list and to a collection.
       * if the search is based on a Trefle.io search the Trefle.io plant id is also added to the list for cross reference to the database.
    * The user is able to contact us via the 'Contact Us' page.
       * This page has an interactive contact form that the user can complete and submit their details through to us.
       * There is an open text box so that the user can submit comments.
       * When the user submits their details by clicking the 'Send Contact Details' button, a modal pops up to confirm that details have been sent.

*   ### Future Features
    * If a user adds a plant to their list from the Trefle.io search , it would be useful to link directly back to the Trefle.io database in order to return more of the details on that plant.
    * Increase the number of filter types in searches. Currently only 'colour' is provided but further filters could be included such as 'edible plants', 'soil types', 'plant height', and 'water conditions'.
    * More complex filters could also be provided to include more than one filter type such as 'colour' and 'soil type'.
    * Improve the quality of data returns for a specific plant in searches, either from updated data submissions in the Trefle.io database or supplement the plant data returns from other available databases.
    * Directly link any search to sources for plant purchase from;
        * local suppliers to the user based on geolocation identifiers; and/or
        * create the ability to online purchase from an identified supplier.
    * Provide an option for the user to image capture a plant and store that image in image form. Links to third party databases are possible for this feature such as AWS, Google and Cloudinary.
    * Provide an option for the user to image capture a plant in their garden which takes them directly to pertinent care details for that particular plant.
    * More sophisticated features include image identifying plants say at a garden centre and being able to compare the plant growing requirements to a users own garden conditions such as light, soil type, water, ph etc.
    * The **Calendar Feature** has proven difficult to implement as information to support this appears lacking in the plant world. Most plant and gardening information providers appear to have their own databases to support this kind of feature as a Unique Selling Product (USP). The Trefle.io database has some details such as 'bloom months' and 'sowing months'. However, this data is not complete. The feature could be added as a future feature on the site.
    * Amend the cards to ensure appropriate rendering on screen sizes at 280px size.
    * Social media icons link to respective social media website home pages. Social media links will in future feature link directly to RMC Ltd social media connections.
    * Note that at present there is no functionality for a user to delete their account. This can be provided as a future feature.

## Technologies Used

### Languages Used

*   [HTML5](https://en.wikipedia.org/wiki/HTML5)
*   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
*   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
*   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Database Used
* [MongoDB](https://www.mongodb.com/cloud/atlas)
* MongoDb was used to store user data, user plant and collection lists for 'CRUD' purposes.
* The database was planned to be as simple as possible with three MongoDB collections;
  1. Users - for user registration and login;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/mongodb_user.png?raw= "Users")
  1. Collections - for users to record their plant lists in their user defined collections;

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/mongodb_collection.png?raw= "Collection")
  1. Plants - for users to record their plants as a complete list and divide these lists into their respective collections. Note that for any images in the database, they are referenced as an HTTP/HTTPS link only.

    ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/mongodb_plant.png?raw= "Plant")

* All plants in the database are directly referenced with the Users ObjectId and a Collection ObjectId.
* All collections are directly referenced to a User ObjectId.

* A key feature of the site is for users to reference the [Trefle.io](https://Trefle.io/) and [Plant.id](https://plant.id/) search capabilities and then upload the data from [Trefle.io](https://Trefle.io/) into their plant list. However, plants can be added to the user list manually, or by utilising the [Trefle.io](https://Trefle.io/) search functionality.
* Images can be uploaded to MongoDB but only in an HTTP/HTTPS referenced form. The database is not designed to hold large images in standard image formats such as JPEG. As such all images are 'referenced' in this way. If a user wishes to upload an image, the user can if the user references a third party website or database.
* Note that at present there is no functionality for a user to delete their account, but will be included as a future feature.


### Frameworks, Databases, Libraries & Programs Used

* [Materialize 1.0.0](https://materializecss.com/)
* Bootstrap was used to assist with the responsiveness and styling of the website.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* Flask was used to generate the front end web page design, using python as the primary back end programming language.
* [MongoDB](https://www.mongodb.com/cloud/atlas)
* MongoDb was used to store user data, user plant and collection lists for 'CRUD' purposes.
* [Hover.css:](https://ianlunn.github.io/Hover/)
* Hover.css was used on the contact details types and for social media icons in the footer to add the float transition while being hovered over.
* [Font Awesome:](https://fontawesome.com/)
* Font Awesome was used for the website to add icons for aesthetic and UX purposes.
* [jQuery:](https://jquery.com/)
* jQuery came with Materialize to make the navbar responsive but was also used to support JavaScript and is loaded from the [CDJNS](https://cdnjs.com/libraries/materialize).
* [GitPod:](https://www.gitpod.io/)
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/)
* GitHub is used to store the projects code after being pushed from Git.
* [Heroku:](https://www.heroku.com/)
  * Heroku is used to host the live site.
* [Atom:](https://atom.io/)
* Atom was used as a Markdown Text Editor for README.md and Testing.md
* [Emailjs:](https://www.emailjs.com/)
* Emailjs is used to send the email from the contact form on the 'Contact Us' page.
* [Favicon.io:](https://favicon.io/)
* Favicon.io was used for Favicon :wine_glass: web page title images.
* [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
* Photoshop was used to resize images and edit photos for the website.
* [GitPod IDE Markup:](https://www.gitpod.io/)
* GitPod IDE markup was used to format HTML files. This easy to use and makes the code very easy to read. I understand this to be VS Code standard.
* [Adobe Stock:](https://stock.adobe.com/uk/)
* Adobe Stock was used as a library source for images.
* [Unsplash:](https://unsplash.com/)
* Unsplash was used as a library source for images.
* [Balsamiq:](https://balsamiq.com/)
* Balsamiq was used to create the [wireframes]() during the design process.
* [Am I Responsive:](http://ami.responsivedesign.is/#)
* Am I Responsive was used to test the page layouts during the build process;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/amiresponsive_succ.png?raw= "Am I Responsive")

### Application Programming Interfaces (API's) Used

* The website sources data from the **[Trefle.io](https://Trefle.io/)** and the **[Plant.id](https://plant.id/)** databases. The API's provide search capabilities for users to identify plants in a number of ways.

* [Trefle.io](https://Trefle.io/)
 * The [Trefle.io](https://Trefle.io/) database was used as the primary search database for a user;
   * entering a 'name'; or
   * by using a filter by 'colour'.

* [Plant.id](https://plant.id/)
 * The [Plant.id](https://plant.id/) database was used as the source for plant searches based on a user image. Images can be captured directly from a mobile device or by file upload.

## Site Construction

* ### Consistent Page Components
 * All pages of the site contain the same 'header', 'navbar', 'carousel' and 'footer';
   * **Header** consists of a title carousel images with titles.
   * **Navbar** is a menu top bar dark yellow coloured lettering. There is a light backdrop highlighting the page that the user is on. The menu allows for easy access to any of the pages at all time. On mobile devices, the menu becomes a 'hamburger' and must be 'touched' in order to select any of the pages.
   * **Carousel** The main 'title' header image is carousel images. These images are large and designed to create visual impact, especially as they scroll through from one to the other. The images are the same for all pages. The images have been selected to represent the 'Plant Kingdom'.
   * **Footer** The footer is displayed on all pages and is consistent. There are three sections **'About'** - describes 'us' as an organisation, **'Data Analysis and Presentation Requirements?'** - describes what we do, and **'Contact'** - describes how to contact **'us'** to discuss what we can do for **'you'**.
* ### Home Page
 * Information Box
   * Contains the details as to the intention of the site and a how it can be used. It contains basic information in each card to explain the key features of the site;
     * User defined plant lists;
     * User defined collections lists;
     * Search functions by name, filter and image upload;
     * Register function for new users;
     * Login for registered users.
* ### Subsequent Pages
* All subsequent pages follow a common theme (using Materialise CSS for font and colours);
  * Main Header Title in 'Yellow';
  * Card in 'Teal' background with information text in 'Dark Teal'.

* ### Contacts Page
 * The Contacts Page contains the 'Contact Form' for a user to supply contact information and to provide comments, questions or to provide a request for some work.
 * The 'Contact Form' will generate an email by referencing the **sendemail.js** file when a user submits their information.

* ### Construction Table
 * The following table provides a summary of how the Site Pages and Sections are compiled;
     Site Page | Page Section | Python File / Code Lines | JS File / Code Lines | API Reference |
     ----------|--------------|-----------------|-----------|---------|
     All | Carousel | N/A  | script.js / 7, 19 - 23 |N/A |
     All | Navbar | N/A  | script.js / 2 - 6 |N/A |
     Home | Card Boxes | app.py / 39 - 43 | N/A |N/A |
     Register | Card Box | app.py / 212 - 236 | N/A |N/A |
     Login | Card Box | app.py / 239 - 266 | N/A |N/A |
     Logout | Card Box | app.py / 281 - 286 | N/A |N/A |
     Plant List | Card Box | app.py / 50 - 53 | N/A  |N/A |
     Add / Update Plant | Add | app.py / 56 - 133 | script.js / 11 - 18 |N/A |
     Collection List | Card Box | app.py / 136 - 151 | N/A |N/A |
     Add / Update Collection | Add | app.py / 154 - 209 | script.js / 11 - 18 |N/A |
     Trefle Search | Search by 'name' | app.py / 320 - 473 | N/A |[Trefle.io](https://Trefle.io/) (Website) |
     Trefle Filter | Filter by 'colour' | app.py / 535 - 678 | script.js / 53 - 63  |[Trefle.io](https://Trefle.io/) (Website) |
     Trefle Plant Details | Search / Filter Return | app.py / 501 - 532 | N/A |[Trefle.io](https://Trefle.io/) (Website) |
     Add Trefle Plant Details | Add | app.py / 476 - 498 | N/A |[Trefle.io](https://Trefle.io/) (Website) |
     Plant.id Search | Plant.id 'image upload' | app.py / 681 - 756 | image_upload.js |[Plant.id](https://plant.id/) (Website) |
     My Details | Card Box | app.py / 289 - 317 | N/A |N/A |
     Contact | Contact Form |N/A| sendemailjs.js | [Emailjs](https://www.emailjs.com/) (Website)|
     Error | Error Messages | app.py / 759 - 775 | N/A | N/A |


## Testing
Testing information can be found in a separate [testing.md](https://github.com/Readri205/MS3_Plant_Manager/blob/master/testing.md) file.
### Known Bugs and Issues
* The python file 'app.py' could be rationalised into key functional items such as 'user, Trefle search and Plant.ID search' to make them more distinct and easier to reference specific functionality in the future.
* Likewise the templates could be rationalised into key functional folders such as 'user, Trefle search and Plant.ID search' to make them more distinct and easier to reference specific functionality in the future.
* Trefle search and filter functionality proved 'difficult' with reference to API pagination. The Trefle database restricts returns to 20 items per page. Identifying distinct pages and presenting them proved difficult even with the 'Shamrock' library, and as such there are a number of Trefle search and filter pages to accommodate pagination from the API return. As the current structure 'works' in terms of presentation (no impact to users), it was decided to submit as is and update the functionality at a later point.
* Note that on a mobile device the 'collections' drop down creates a 'mobile' type drop down selection that can be confusing initially, compared to a desktop drop down. It's a bit clunky but it works.
* Note that on a mobile, the drop down lists can prove 'sticky' on selection with touch screen and sometimes go through to the wrong selection. Again, this can be 'annoying' initially. Further review can look to resolve this for user aesthetics.
* Note that at present there is no functionality for a user to delete their account, but would be provided as a future feature.
* Note that the background, carousel and main home page cards all reference  [© Unsplash.com](https://unsplash.com/) for the images. As this is the case there is a risk that an image could be removed from the source and so the site image would fail. Copies of images are retained in the project image folder for backup.
* GitPod IDE markup was used to format HTML files. This easy to use and makes the code very easy to read. I understand this to be a VS Code standard.
* In the Heroku deployment, and on a mobile device, in the Trefle Search function, if a user enters a name with an apostrophe in it, the search with fail and report an Error (this issue is unique to Heroku deployment on a mobile device. The search will work on a desktop device or in Heroku Chrome Dev tools for mobile device screen sizes). The issue was discussed with CI Tutor Support with the suggestion to record the issue in the README.md file;

* example of type of search;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/problem_search.png?raw= "Mobile Problem Search")

* example of the error return;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/value_error.png?raw= "Mobile Device Error")

* if the user enters a search on mobile with an apostrophe in the name, the following error message is returned (HTTP 500 server error);

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/oops_error_message.png?raw= "Error Message")

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following process;

1. The project was written in [GitPod](https://www.gitpod.io/) and pushed to GitHub Pages ready for deployment by taking the following steps;
1. Logged in to GitHub and located the [GitHub Repository](https://github.com/Readri205/MS3_Plant_Manager);
1. From this point deployment was made linking the Github repository to Heroku;

### Heroku Deployment

1. The application was deployed in Heroku to run the Python Application on the Web front end.
1. An account was created in Heroku and then a new application was setup;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_new_app.png?raw= "Heroku New App")

1. In the 'Deploy' menu the Heroku application is connected to the Github Repository so that it is automatically updated when Github is deployed;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_github_deploy.png?raw= "Github to Heroku Deploy")

1. In the 'Settings' menu, all the relevant API token, Secret Key and config files are entered individually so that the application can run with reference to these inputs;

* The application configs are set in the app.py file for reference;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_configs.png?raw= "Heroku Configs")

* Heroku can reference them once they are set in the Config Vars. All the tokens and secret keys are entered into an environment variable file that is referenced by the offline application and are not uploaded to Github. Any user wishing to copy the application and deploy it will need to obtain and create their own environment variables as listed below;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_app_configs.png?raw= "Heroku App Configs")

1. A requirements file must be set in the Github application which is passed to Heroku so that it knows which libraries to run;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_reqv2.png?raw= "Heroku Deployment")

1. A 'Proc' file must also be set in the Github application which is passed to Heroku so that it knows which programme to run the web application;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_proc.png?raw= "Heroku Deployment")

1. The application is opened on the web by clicking on the "Open app" button;

  ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/heroku_deployment.png?raw= "Heroku Deployment")

- [Click to view site **WINE SHOP** :wine_glass:](https://plant-manager-flask-mongodb.herokuapp.com/ "Heroku Deployed Site")

### Forking the GitHub Repository

A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and  changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository;

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Readri205/MS3_Plant_Manager);
1. At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
   ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/github_fork.png?raw= "Github Fork"); and
1. Click to create a copy of the original repository in your own GitHub account.

### Making a Local Clone

1. Log in to **GitHub** and locate the [GitHub Repository](https://github.com/Readri205/MS3_Plant_Manager)
1. Under the repository name, click "Code".
1. To clone the repository using HTTPS, click the top right hand link click "Use HTTPS";
1. Copy the link under "Clone with HTTPS";
   ![alt text](https://github.com/Readri205/MS3_Plant_Manager/blob/master/static/images/readme/github_clone.png?raw= "Github Clone")
1. Open your Code Editor and access the appropriate process to paste the clone link;
1. Change the current working directory to the location where you want to keep the cloned directory;
1. Paste the URL you copied in step 4 above.

Note that different Code Editors will have different processes for making the clone once the HTTPS link copy is made in step 4 above.

* If using **GitHub Desktop**, the clone can de saved directly into GitHub Desktop from the "Code" dropdown menu by choosing **'Open with GitHub Desktop'**.

A **Zip File** clone can be downloaded from the same "Code" drop down above;
* Select **'Download ZIP'** and the complete zip file will be saved to you local computer.

## Credits

### Code

* My Mentor (Adegbenga Adeye (email:adegbenga.adeye@outlook.com, slack:gbenga_mentor)) for providing help, guidance, inspiration and input on the more challenging components.
* [Code Institute course](https://codeinstitute.net/5-day-coding-challenge/?utm_term=%2Bcode%20%2Binstitute%20%2Bcourses&utm_campaign=a%2526c_BR_IRL_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_tgt=kwd-443742237303&hsa_ad=407017470923&hsa_acc=8983321581&hsa_grp=62188641040&hsa_mt=b&hsa_cam=1578649861&hsa_kw=%2Bcode%20%2Binstitute%20%2Bcourses&hsa_ver=3&hsa_src=g&gclid=CjwKCAjw4MP5BRBtEiwASfwAL3-Oi3uDo1sBfn2KpQVAlLb07T2ndP-Q2mCFxdGgpvoBMoPIAtbg9xoCyZgQAvD_BwE&gclsrc=aw.ds); (the 'Task List' example) by Tim Nelson for the [Flask](https://flask.palletsprojects.com/en/1.1.x/) / [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) / [MongoDB](https://www.mongodb.com/cloud/atlas) / [Materialize](https://materializecss.com/) example which is used for the base construction of this website.
* (the [Emailjs](https://www.emailjs.com/) example) for the 'Contact Form' email return function used in this website.
* Code for the Carousel was from [Learning Simplified](https://youtu.be/re2W7o6IsYo), a youtube channel doing some good things with the [Materialize 1.0.0](https://materializecss.com/) Library.
* [Julian Nash](https://www.youtube.com/channel/UC5_oFcBFlawLcFCBmU7oNZA) provided me with lots of useful tips for Flask and Python programming. The youtube videos are easy to follow and understand and are backed up with useful documentation.

## Content

* All content was written by the developer.

### Media

* All images [© Unsplash.com](https://unsplash.com/) unless otherwise stated;
*   Background image - ['Dark plants ...''](https://unsplash.com/photos/aDvrHHFGAlE) By Amir Nyct [© Unsplash.com](https://unsplash.com/);
*   Carousel image - ['Orchid in Bloom'](https://unsplash.com/photos/1PJnrGd6K1w) By Sanni Sahil [© Unsplash.com](https://unsplash.com/);
*   Carousel image - ['Spring Red Tulips on Moody Background'](https://unsplash.com/photos/gH5ujsvtohE) By Michele Tardivo [© Unsplash.com](https://unsplash.com/);
*   Carousel image - ['Floral Potrait...'](https://unsplash.com/photos/-yYaO0ioyOY) By Abhishek Dhakate [© Unsplash.com](https://unsplash.com/);
*   Carousel image - ['Singapore Botanic Gardens, Singapore'](https://unsplash.com/photos/fQQBArliXGE) Elliot Lowe [© Unsplash.com](https://stock.adobe.com/uk/);
*   Home page card image - ['Hazleton, United States'](https://unsplash.com/photos/Q2dxmAzbUbk) Honey Yanibel Minaya Cruz [© Unsplash.com](https://stock.adobe.com/uk/);
*   Home page card image - ['Mystic Hydrangea'](https://unsplash.com/photos/FOrCwEMIgSI) Natasha Polyakova [© Unsplash.com](https://stock.adobe.com/uk/);
*   Home page card image - ['Deep Red Leaves'](https://unsplash.com/photos/mdNQ3R5dT6w) Jessica Fadel [© Unsplash.com](https://stock.adobe.com/uk/);
*   Home page card image - ['Pink Flowers'](https://unsplash.com/photos/ia1eeRnsbLg) Annie Spratt [© Unsplash.com](https://stock.adobe.com/uk/);
*   Error page image - ['Dying Plant Flower'](https://www.deviantart.com/florapolitis/art/Dying-Plant-Flower-689450996) © 2017 - 2021 florapolitis ['Florapolotis'](https://www.deviantart.com/florapolitis/art/Dying-Plant-Flower-689450996) [Deviant Art](https://www.deviantart.com/);

### Acknowledgements

* My Mentor **Adegbenga Adeye**, (email: adegbenga.adeye@outlook.com, slack:gbenga_mentor) for continuous helpful feedback. Ade has been an amazing in helping and supporting me with this site. It has proven much harder and much more work for me to develop than I ever thought (severe case of 'what you don't know when you start').
* **Tutor support** at Code Institute for their support. When I have requested help, it has come quickly and efficiently when needed.
* **Student assessment** at Code Institute. I have looked to accommodate comments back on MS2 to reduce any re-occurring issues in MS3.
* **Other students** (Slack Code Institute Workspace) on the Full Stack Developer Course, via the [Slack Communication Platform](https://slack.com/intl/en-gb/).
* **Friends and family** providing review and feedback on the site content, navigation and screen size testing. This has been invaluable with two very 'have mobile, will travel' daughters, it is often brutal but effective.

## Version Control

*   All through the development phase of the project, commits have been made from the GitPod Repository to GitHub. The version control list below mirrors the GitHub Commit list. It is designed to provide a direct track on commits in the README file for easy access as to code status in GitPod.

 - V1.0 Initial Commit
 - V1.1 Setup allauth
 - V1.2 Add allauth templates and base template
 - V1.3 Add blocks to base template
 - V1.4 Add home app and templates
 - V1.5 Add home page content and style
 - V1.6 Add main page header profile
 - V1.7 Add home page image and static
 - V1.8 Amend my-account dropdown toggle in css
 - V1.9 Amend css styles for text and shop buttons
 - V2.0 Add mobile and main navbar
 - V2.1 Upload images to media file
 - V2.2 Upload fixtures and amend media images
 - V2.3 Update json files with name fields
 - V2.4 Update product json file for spelling text appellation
 - V2.5 Add models product, appellation, variety, country, type
 - V2.6 Add models to admin and set and ordered fields
 - V2.7 Add products page and layout for products
 - V2.8 Update products and product detail with fields and styles
 - V2.9 Update css for products and product details
 - V3.0 Amend css on products and amend details list
 - V3.1 Add basic product search query
 - V3.2 Add favicons and colour changes to fonts
 - V3.3 Add type filter for products drop down
 - V3.4 Amend main-nav for product views and types
 - V3.5 Update menus with product views and sorts
 - V3.6 Update collections for mixed variety products sort
 - V3.7 Update for sorting and product filter count
 - V3.8 Amend product sort to eliminate sytax errors
 - V3.9 Add jquery script to corejs for product sort function
 - V4.0 Update sort for product sort by product
 - V4.1 Add page return function
 - V4.2 Add cart app for shopping
 - V4.3 Amend fonts and icons on cart page
 - V4.4 Add context to cart
 - V4.5 Add quantity to cart
 - V4.6 Add cart url
 - V4.7 Amend background, formats, fonts and table in cart
 - V4.8 Amend styles for product home link
 - V4.9 Amend cart shop summary for bootsrap text-end
 - V5.0 Add quantity increment decrement script
 - V5.1 Add icons to money and increment decrement to cart
 - V5.2 Add update and remove links in cart
 - V5.3 Amend styles on account and cart links
 - V5.4 Add sub total update and cart quantity amends
 - V5.5 Add toasts
 - V5.6 Amend flag url from countryflag io to flagcdn.com
 - V5.7 Update toasts for shopping add and updates


***

![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/amiresponsive.png?raw= "WINE SHOP")

[View the live **WINE SHOP**  :wine_glass:  project here.](https://winesstore.herokuapp.com/)

# **WINE SHOP :wine_glass:**


## Site Goals

* This website provides a functionality for users to purchase a selection of wines from a wine store. users can select from a number of menu drop-downs for wines that suite their interest across red, white, rose, sparkling and fortified. The user can select the wines and place them in a shopping cart, provide user details for delivery and make credit card payment.

* **NOTE: This site is currently entirely for educational purposes only. Whilst there is an ability to register for the site, any personal details entered are not protected.**

* If the site is perceived as successful, it is anticipated that the site could be expanded as;
  * more wines cold be added to the list for purchase;
  * more products could be added such as cheeses and other foods; and
  * other products related to wines such as glasses, cheeseboards etc.

* The site is designed to be responsive and accessible on a range of devices, making it easy to navigate for interested users. The website was designed using **'Mobile First'** principles as the site must be perceived to be quick and easy to use and read as a reference site on a mobile device.

## User Experience (UX)

*   ### User stories

  *   #### First Time Visitor Goals
      * The first time visitor will want to;
        * easily understand the main purpose of the site;

        ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_homepage.png?raw= "Home")

        * be able to easily navigate throughout the site to find content;

        ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_menubar.png?raw= "Main Menu")

        * register for the site and create login credentials;

        ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_signin.png?raw= "Sign In")

        ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_signup.png?raw= "Sign Up")

        * use the menu dropdown to see a selection;

        ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_dropdown.png?raw= "Search")

        * search for wines by name or description using the search bar;

            ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_search.png?raw= "Search Name")

            * View wines returned from a search;

            ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_sauvignon.png?raw= "Search Name")

            * View wine details from a search return;

            ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_sauvignondetail.png?raw= "Search Detail")

        * see their user details and amend if necessary.

          ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_profile.png?raw= "My Profile")

        * add items to their shopping cart;
          * amend the items in the shopping cart by increasing or decreasing quantity;
          * adding or deleting items completely;

            ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_cart.png?raw= "My Cart")

        * checkout and make payment;
          * go to user details and delivery information;
          * review the shopping cart summary;
          * input credit card payment and submit order.

            ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_checkout.png?raw= "My Checkout")

        * super users can manage product sets in database;
          * add new products to the database;
          * delete products from database; and
          * amend existing products.

            ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_product.png?raw= "Product Management")


  *   #### Returning Visitor Goals
      * The returning visitor will want to;
        * login to the site;
        * view their previous orders;
        * update their contact and delivery details
      * **A returning visitor** may want to go straight to the menu dropdown or search function.

      * **A returning visitor** may be a super user and can manage product sets in database;
        * add new products to the database;
        * delete products from database; and
        * amend existing products.

  *   #### Frequent User Goals
      * The frequent user will want to;
        * login to the site;
        * view their previous orders;
        * update their contact and delivery details
      * **A frequent visitor** may want to go straight to the menu dropdown or search.

      * **A frequent visitor** may be a super user and can manage product sets in database;
        * add new products to the database;
        * delete products from database; and
        * amend existing products.

  *   #### Mobile Menu
        * On mobile devices the menu is shown as a 'hamburger' drop down;

        ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_mobilemenu.png?raw= "Mobile")

        * On mobile devices the menu and search function operates in the same manner as for larger screens;

        ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/app_mobiledrop.png?raw= "Mobile Dropdown")

*   ### Design
  *   #### Colour Scheme
      * the main background uses an image of vines in the Duoro Valley in Portugal. the landing page shows this image distinctly, whilst all other pages use the same image as a 'hazy' backdrop.

        ![alt text](https://images.unsplash.com/photo-1596063093406-321358f23bb1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80)

      * The main colour themes are 'Burgundy' (#722F37) and 'Green' (#4f742f), primarily in reference to 'red' and 'white' wines. 'Burgundy' is used to highlight 'buttons' with 'Green' as a 'hover' effect over 'buttons'.
      * The main colours,  were potentially a concern for the 'colour blind' fraternity. Some basic tests with colour-blind persons did not present any issues, however the spectrum of colour blindness is vast so there may be some issues with some persons. The colour structure is relatively easy to change if there is negative feedback.
  *   #### Typography
      * ...
  *   #### 'Bootstrap' Card Structure
      * The 'Bootstrap' card structure is used to return search results. This structures the returns into identifiable components with an image and corresponding details for a return. This keeps each return distinct and independent of each other.
  *   #### Imagery
      * Note that the background reference is [© Unsplash.com](https://unsplash.com/) for the image. As this is the case there is a risk that an image could be removed from the source and so the site image would fail. Copies of images are retained in the project image folder for backup.
      * The background image is of 'The grapes on the vineyards in Douro Valley, Portugal'.

            ![alt text](https://images.unsplash.com/photo-1596063093406-321358f23bb1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80)

            *['The grapes on the vineyards in Douro Valley, Portugal. The UNESCO World Heritage region where the Porto Wine is produced.'](https://unsplash.com/@qwitka) By Maksym Kaharlytskyi [© Unsplash.com](https://unsplash.com/)*


*   ### Wireframes
  *   #### Original Wireframe Design (October 15, 2020).
      * The **'Home'** page includes a basic overall introduction to the purpose of the site. Cards are used to describe the main features of the site. The features are User Plant List, User Collections, Search by a Name, Filter, Image Upload and a  Year Calendar.
      * Once the User has a login these features are accessible from the menu.
      * The menu includes direct links to wine types;
        1. Reds;
        1. Whites;
        1. Rose;
        1. Sparkling; and
        1. Fortified
      * Amazon S3 to be used as the database for static and media files.
      * The search list is considered to return name and image upload searches as detail page returns.
      * The pages include those for user details entry and checkout from the shopping cart.
      * All images in the wireframe are by example only.
      * Wireframe includes examples for desktop and mobile devices.
      *   The **Original Wireframe Design** can be viewed here - [View](https://github.com/Readri205/MS4_shopfront/blob/master/readme/wireframe/wineshop.pdf).

## Features

*   ### Responsive for Device Size
    * Mobile / Smaller screen size
      * The site is designed primarily for use on a mobile. The 'Box Content' structure using Bootstrap Grid System has been utilised so that the information boxes (search results) will stack vertically on small screens for readability.
      * The menu system uses the Bootstrap 'navbar' functionality for small screens using the 'toggle' capability for the 'drop down' menu list from a 'hamburger' icon.
      * The navbar is 'fixed' to the top of the screen at all times on page scroll down for easy access.
      * The navbar is coloured 'dark teal' to make it distinctive from the site pages.
      * The 'hamburger' is coloured 'dark yellow' to make it visible yet not intrusive when viewing the site details.
      * See comments above with regard to potential colour blindness impacts of the yellow and green colour mix.
      * The 'drop down' site page options are coloured 'burgundy' with the current page shown with an 'white' background.
      * The header image suitably sized for smaller screens.
    * Desktop / Laptop large screen size
      * The 'Box Content' is effective on wide screens. The Bootstrap Grid System allows for the 'Box Content' to align horizontally in themes that are consistent on each of the 'Home' and 'Search' pages.
      * The header menu system uses the Bootstrap 'navbar' functionality with the menu option pages listed to the centre.
      * The menu item list is coloured 'burgundy' to make it visible yet not intrusive when viewing the site details.
      * The 'drop down' site page options are coloured 'burgundy' with the current page shown with an 'white' background.

*   ### Interactive Elements
    * The first key feature of the site is the ability for the user to;
       * enter search by name and description for wines;
       * review their search response details;
       * select menu items for short listed wines by type.
    * The user can register for the site;
        * enter an email and username and password;
        * confirm email and password to confirm accuracy;
        * receive an email to confirm validity of login details;
        * login to the site as a registered user.
    * The user has the ability to;
        * enter search by name and description for wines;
        * review their search response details;
        * select menu items for short listed wines by type.
    * The user has the ability to select wines for purchase;
       * review the returns by menu or search and select a wine to review details;
       * select a wine for entering into the shopping cart; or
       * on wine details page increase or decrease quantity for each wine into shopping cart.
    * A user can enter the shopping cart to review their shopping cart summary;
       * accept the cart for payment;
       * make adjustment by cart entry to increase or decrease quantities.
       * delete an item from the shopping cart if required.
    * The user is able to make an order and make a payment.
       * The user can make a payment and enter their details for delivery;
       * The user will receives a 'toast' confirmation to confirm the order and will receive an email.
    * The super-user is able to make adjustments to te product database;
      * The user can make a payment and enter their details for delivery;
      * The user will receives a 'toast' confirmation to confirm the order and will receive an email.

*   ### Future Features
    * The search function could be improved to be be more specific across appellations, varieties, types and countries.
    * Increase the number of wines.
    * Add other products like foods and other items associated with wines.
    * User functionality for users to delete their account directly.
    * Add marketing tools for product messaging to registered and other users where they 'opt-in' for such material.
    * A more extensive and complete footer will be completed to account for more detailed contact mechanisms and links to core principles and values of the organisation and how it operates
    * make the footer consistently sit at the foot of all pages.
    * Add links to social accounts to provide an easer user experience for users to register and login using their social accounts.


## Technologies Used

### Languages Used

*   [HTML5](https://en.wikipedia.org/wiki/HTML5)
*   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
*   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
*   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Database Used
* [Amazon S3](https://www.Amazon S3.com/cloud/atlas)
* Amazon S3 was used to store user data, user plant and collection lists for 'CRUD' purposes.
* The database was planned to be as simple as possible with three Amazon S3 collections;
  * All static files are housed in s3;
  * All media files for production are housed in S3 (readme media images remain in Github).


### Frameworks, Databases, Libraries & Programs Used

* [Bootstrap 1.0.0](https://Bootstrapcss.com/)
  * Bootstrap was used to assist with the responsiveness and styling of the website.
* [Django](https://www.djangoproject.com/)
  * Django framework was used to construct the website using standard templates and Django pyhton scripts, including the allauth profiles and security mechanisms for user login and registration.
* [Amazon S3](https://www.Amazon S3.com/cloud/atlas)
  * Amazon S3 was used to store user data, user plant and collection lists for 'CRUD' purposes.
* [Stripe](https://www.stripe.com)
  * Stripe was used to facilitate customer payments using credit card information.
* [Hover.css:](https://ianlunn.github.io/Hover/)
  * Hover.css was used on the contact details types and for social media icons in the footer to add the float transition while being hovered over.
* [Font Awesome:](https://fontawesome.com/)
  * Font Awesome was used for the website to add icons for aesthetic and UX purposes.
* [jQuery:](https://jquery.com/)
  * jQuery came with Bootstrap to make the navbar responsive but was also used to support JavaScript and is loaded from the [CDJNS](https://cdnjs.com/libraries/Bootstrap).
* [GitPod:](https://www.gitpod.io/)
  * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/)
  * GitHub is used to store the projects code after being pushed from Git.
* [Heroku:](https://www.heroku.com/)
  * Heroku is used to host the live site.
* [Atom:](https://atom.io/)
  * Atom was used as a Markdown Text Editor for README.md and Testing.md
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

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/amiresponsive.png?raw= "Am I Responsive")

## Site Construction

* ### Consistent Page Components
 * All pages of the site contain the same 'header', 'navbar' and 'footer';
   * **Navbar** is a menu top bar with 'burgundy' lettering. The menu allows for easy access to any of the pages at all time. On mobile devices, the menu becomes a 'hamburger' and must be 'touched' in order to select any of the pages.
   * **Footer** The footer is displayed on all pages and is consistent. There are two sections **'About'** - describes 'us' as an organisation, and **'Contact'** - describes how to contact **'us'**.
* ### Product Pages
 * Information Box
   * Summary pages include details for each wine including;
     * Image;
     * Name;
     * Rating;
     * Variety;
     * Country & Flag;
     * Price
  * Detail wine pages include all the above plus;
     * Description;
     * ability to add product to cart;
     * amend the quantity;
     * click through to the shopping cart.
* ### shopping Cart Page
    * User details;
    * Cart summary;
    * Cart cost and card payment form.

## Testing
* Testing information in the following test schedule;

  * Desktop

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/test_desktop.png?raw= "Desktop Test")

  * mobile

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/test_mobile.png?raw= "Mobile Test")

  The file can be found here;

  [View](https://github.com/Readri205/MS4_shopfront/blob/master/readme/wireframe/testsheet.xlsx)

* The Django programme in Gitpod was tested with python3 manage.py -m flake8 with the following issues remaining;

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/test_flake8_1.png?raw= "Flake8 part 1")

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/test_flake8_2.png?raw= "Flake8 part 2")

  * Items are either line too long which won't effect code, or comments as to 'avoid using 'null' on string fields.

### Known Bugs and Issues
*
* Note that at present there is no functionality for a user to delete their account, but would be provided as a future feature.
* GitPod IDE markup was used to format HTML files. This easy to use and makes the code very easy to read. I understand this to be a VS Code standard.
* The footer on the 'Profile Page' does not fully extend across the width of the page. The error is likely to be easily resolved but time constraints require the fix to be made post submission date.
* The footer on the 'Sign In and sign Out' pages' floats up the page. The error is likely to be easily resolved but time constraints require the fix to be made post submission date.
* Social accounts have not been set up for auto login for users. This would be updated in future amends to the website.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following process;

1. The project was written in [GitPod](https://www.gitpod.io/) and pushed to GitHub Pages ready for deployment by taking the following steps;
1. Logged in to GitHub and located the [GitHub Repository](https://github.com/Readri205/MS4_shopfront);
1. From this point deployment was made linking the Github repository to Heroku;

### Heroku Deployment

1. The application was deployed in Heroku to run the Python Application on the Web front end.
1. An account was created in Heroku and then a new application was setup;

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/heroku_new_app.png?raw= "Heroku New App")

1. In the 'Deploy' menu the Heroku application is connected to the Github Repository so that it is automatically updated when Github is deployed;

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/heroku_github_deploy.png?raw= "Github to Heroku Deploy")

1. In the 'Settings' menu, all the relevant API token, Secret Key and config files are entered individually so that the application can run with reference to these inputs;

* Heroku can reference them once they are set in the Config Vars. All the tokens and secret keys are entered into an environment variable file that is referenced by the offline application and are not uploaded to Github. Any user wishing to copy the application and deploy it will need to obtain and create their own environment variables as listed below;

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/heroku_configs.png?raw= "Heroku App Configs")

1. A requirements file must be set in the Github application which is passed to Heroku so that it knows which libraries to run;

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/heroku_requirements.png?raw= "Heroku Deployment")

1. A 'Proc' file must also be set in the Github application which is passed to Heroku so that it knows which programme to run the web application;

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/heroku_proc.png?raw= "Heroku Deployment")

1. The application is opened on the web by clicking on the "Open app" button;

  ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/heroku_deployment.png?raw= "Heroku Deployment")

- [Click to view site **WINE SHOP** :wine_glass:](https://plant-manager-flask-Amazon S3.herokuapp.com/ "Heroku Deployed Site")

### Forking the GitHub Repository

A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and  changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository;

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Readri205/MS4_shopfront);
1. At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
   ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/github_fork.png?raw= "Github Fork"); and
1. Click to create a copy of the original repository in your own GitHub account.

### Making a Local Clone

1. Log in to **GitHub** and locate the [GitHub Repository](https://github.com/Readri205/MS4_shopfront)
1. Under the repository name, click "Code".
1. To clone the repository using HTTPS, click the top right hand link click "Use HTTPS";
1. Copy the link under "Clone with HTTPS";
   ![alt text](https://github.com/Readri205/MS4_shopfront/blob/master/readme/images/github_clone.png?raw= "Github Clone")
1. Open your Code Editor and access the appropriate process to paste the clone link;
1. Change the current working directory to the location where you want to keep the cloned directory;
1. Paste the URL you copied in step 4 above.

Note that different Code Editors will have different processes for making the clone once the HTTPS link copy is made in step 4 above.

* If using **GitHub Desktop**, the clone can de saved directly into GitHub Desktop from the "Code" dropdown menu by choosing **'Open with GitHub Desktop'**.

A **Zip File** clone can be downloaded from the same "Code" drop down above;
* Select **'Download ZIP'** and the complete zip file will be saved to you local computer.

## Credits

### Code

* [Code Institute course](https://codeinstitute.net/5-day-coding-challenge/?utm_term=%2Bcode%20%2Binstitute%20%2Bcourses&utm_campaign=a%2526c_BR_IRL_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_tgt=kwd-443742237303&hsa_ad=407017470923&hsa_acc=8983321581&hsa_grp=62188641040&hsa_mt=b&hsa_cam=1578649861&hsa_kw=%2Bcode%20%2Binstitute%20%2Bcourses&hsa_ver=3&hsa_src=g&gclid=CjwKCAjw4MP5BRBtEiwASfwAL3-Oi3uDo1sBfn2KpQVAlLb07T2ndP-Q2mCFxdGgpvoBMoPIAtbg9xoCyZgQAvD_BwE&gclsrc=aw.ds); (the 'Boutique Ado' example) by Chris Zielinski for the [Django](https://www.djangoproject.com/) / [Amazon S3](https://aws.amazon.com/s3/) / [Bootstrap](https://getbootstrap.com/) example which is used for the base construction of this website.

## Content

* Content for fixtures was derived from [Laithwaites](https://www.laithwaites.co.uk/) for inspiration.

  * Use of any information in this site is exclusively for the purposes of viewing information only and is entirely for educational purposes.

  * Any interest in content for purchase should be directed to [Laithwaites](https://www.laithwaites.co.uk/).

### Media

*   Background image - ['The grapes on the vineyards in Douro Valley, Portugal. The UNESCO World Heritage region where the Porto Wine is produced.'](https://unsplash.com/@qwitka) By Maksym Kaharlytskyi [© Unsplash.com](https://unsplash.com/);

### Acknowledgements

* **Tutor support** at Code Institute for their support. When I have requested help, it has come quickly and efficiently when needed.
* **Student assessment** at Code Institute. I have looked to accommodate comments back on MS3 to reduce any re-occurring issues in MS4.
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
  - V5.8 Add checkout app and checkout models
  - V5.9 Add forms for checkout
  - V6.0 Update crispy template and base css for checkout
  - V6.1 Amend css in checkout
  - V6.2 Add stripe componant to checkout
  - V6.3 Add stripe variables to gitpod
  - V6.4 Amend clientSecret syntax to fix payment
  - V6.5 Add checkout success page
  - V6.6 Add order detail to checkout page
  - V6.7 Add stripe checkout confirmation
  - V6.8 Add stripe webhook
  - V6.9 Update stripe webhooks for payment types
  - V7.0 Update webhook for client info on submit
  - V7.1 Update webhooks for order redundancy
  - V7.2 Add profiles app
  - V7.3 Add profile model views and url
  - V7.4 Update allauth for styles and crispy forms
  - V7.5 Add profile link and style to profile page
  - V7.6 Add profile update form
  - V7.7 Add profile updates to checkout process
  - V7.8 Add order update via stripe webhook for orders
  - V7.9 Add confirmation email to webhook
  - V8.0 Add product form for product update
  - V8.1 Add add product form
  - V8.2 Update product form for categories
  - V8.3 Add add product style and media context processor
  - V8.4 Add edit product function
  - V8.5 Add delete product function
  - V8.6 Add superuser profile checks
  - V8.7 Add image widget for edit
  - V8.8 Add image js for image load
  - V8.9 Test webhook handler and update profile page styles
  - V9.0 Update confirmation email details
  - V9.1 Setup Heroku delpoyment
  - V9.2 Deploy to heroku
  - V9.3 Amend Procfile
  - V9.4 Further amend on Procfile
  - V9.5 Further amend on Procfile
  - V9.6 Move Procfile to correct location
  - V9.7 Move codes out
  - V9.8 Debug amend and enable heroku auto update
  - V9.9 Deploy files to aws
  - V10.0 Add aws object parameters for cache
  - V10.1 Remove additional media image
  - V10.2 Upload favicon s3 location
  - V10.3 Move favicons to test
  - V10.4 Update favicon location for S3
  - V10.5 Amend for faviconfiles location
  - V10.6 Add stripe keys to heroku
  - V10.7 Amend favicon links in base html
  - V10.8 Return to original base html
  - V10.9 Remove favicons
  - V11.0 New folder for favicons
  - V11.1 Favicons to root
  - V11.2 Remove site manifest file from favicon
  - V11.3 Amend to favicon and mobile menu styles
  - V11.4 Update favicon route in S3
  - V11.5 Further update favicon route for S3
  - V11.6 Test red link on main menu for heroku
  - V11.7 Test red link label
  - V11.8 Test for type all reds
  - V11.9 Reload fixtures files to heroku
  - V12.0 Test for variety monastrell
  - V12.1 Test for allowed hosts
  - V12.2 Test remove import stripe
  - V12.3 Add back import stripe
  - V12.4 Set debug to true for errors
  - V12.5 Test for amends on images access
  - V12.6 Redeploy after amend image names
  - V12.7 Update admin product detail display
  - V12.8 Update debug to production
  - V12.9 Amend mobile css and home page links
  - V13.0 Amend mobile css
  - V13.1 Update mobile page layouts
  - V13.2 Update css on mobile
  - V13.3 Update for product image html error
  - V13.4 Further update for product image error
  - V13.5 Update for product image reference
  - V13.6 Amend checkout buttons page
  - V13.7 Update cart page
  - V13.8 Amend back to shop in empty cart page
  - V13.9 Amend for button on empty cart page
  - V14.0 Amend lint errors
  - V14.1 Test product details page
  - V14.2 Test text positions product details page
  - V14.3 Test product details layout
  - V14.4 Test product details text layout
  - V14.5 Test for product details layout
  - V14.6 Test for product details quantity layout
  - V14.7 Test for details float
  - V14.8 Add detail quantity form
  - V14.9 Update for path error
  - V15.0 Amend to debug true
  - V15.1 Update detail quantity form
  - V15.2 Amend product details template
  - V15.3 Further amend product details template
  - V15.4 Further amend product details page
  - V15.5 Heroku push
  - V15.6 Further product details amends
  - V15.7 Amend to float add cart to right
  - V15.8 Amend to keep shopping
  - V15.9 Update product details page
  - V16.0 Amend error on product details
  - V16.1 Adjust image and quantity block
  - V16.2 Amend columns and icons product detail
  - V16.3 Add email account to settings
  - V16.4 Amend email account settings
  - V16.5 Update fonts on password resets
  - V16.6 Update text in product details
  - V16.7 Add amiresponsive image
  - V16.8 Heroku push
  - V16.9 Further heroku push
  - V17.0 Heroku push for build fails
  - V17.1 Reconnect Heroku
  - V17.2 Further connect heroku
  - V17.3 Load readme amiresponsive
  - V17.4 Style amends on home page
  - V17.5 Further style amend home page
  - V17.6 Add readme images
  - V17.7 Amends in readme
  - V17.8 Amend product model
  - V17.9 Amend products
  - V18.0 Further amend products
  - V18.1 Align all product files
  - V18.2 Amend media image file reference in product json
  - V18.3 Amend sku names for file reference in products
  - V18.4 Further products amends
  - V18.5 Remove mixed products
  - V18.6 Load products to fix image reference
  - V18.7 Amend mixed products in gitpod
  - V18.8 Redeploy to heroku
  - V18.9 Add footer section
  - V19.0 Add css on footer
  - V19.2 Amend css on footer
  - V19.3 Add readme content
  - V19.4 Further readme updates
  - V19.5 Adds to readme
  - V19.6 Fix footer to page foot
  - V19.7 Add footer css and readme amends
  - V19.8 Add footer bootstrap css
  - V19.9 Add images to readme
  - V20.0 Add further images to readme
  - V20.1 Amend body size for footer
  - V20.2 Further amends on footer
  - V20.3 Amends for footer spacing
  - V20.4 Increase footer spacing
  - V20.5 Footer style amend
  - V20.6 Amends on footer
  - V20.7 Final footer style
  - V20.8 Add testing references
  - V20.9 Update readme for profile page footer issue
  - V21.0 Amend footer to relative
  - V21.1 Returned to fixed
  - V21.2 Return to relative
  - V21.3 Debug and secret key removed
  - V21.4 Add and amend content for readme
  - V21.5 Add test images and file for readme
  - V21.6 Add flake8 test
  - V21.7 Remove keys and debug

  ***

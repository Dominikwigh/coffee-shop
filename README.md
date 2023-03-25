# Coffee Shop 
![IMG ALT DESC HERE](IMG PATH HERE)

Coffee shop is a small family run coffee shop serving fresh coffee to people in London.
I have created this full-stack application using the Python, Django framework, Heroku PostgreSQL and front-end technologies, HTML, CSS, and Javascript.

My website can be found here ....

## Goals 
The goal for this project was to allow users to register and confirm their email address, create a profile that would store user order information, order history, and favourited products.

Users also can browse filter and sort products by name and category.

As well as allow purchases of products themed around coffee, making reviews for products, aswell as contacting the store admin via mail. 
Visitors to the site may also subscribe to a newsletter. And receive an confirmation email after purchsing. 

The projects purpose is to enable customers to make purchases, register for an account, and review products while enjoying a nice user experience and user interface.

## User Experience

User experience has been designed with a minimalistic, clean, and professional look. A light-colored background and bold dark colors for text as well as sharp images portray the purpose and goal of the e-commerce-site.
The visitors to Coffee Shop is most likely someone who enjoys making nice coffee at home. Who enjoys a nice espresso, or a pour over coffee from whole beans. A visitor to Coffee shop is also someone who most likely enjoys reading about coffee.


Here is a list of my User Stories...
* 1. As a site user i can view a list of products so that i can select some to purchase.
* 2. As a site user i can view individual products so that i can identify the description.
* 3. As a site user i can have a personal account so that i can view my profile.
* 4. As a site user i can easily login or logout so that i can access my account information.
* 5. As a site user i can have a personalized user profile so that i can view my order history.
* 6. As a site user i can recover my password if i forget it so that i can recover access to my account.
* 7. As a site user i can get an email after registering so that i know that my registration was successful.
* 8. As a site user i can see product reviews so that i can see which product is the most popular.
* 9. As a site user i can add items to my cart so that i can purchase them later.
* 10. As a site user i can view a specific category so that i can quickly find the product iam looking for.
* 11. As a site user i can search for products so that i can easily find what iam looking for.
* 12. As a site user i can delete an item from my cart so that i can change product to buy.
* 13. As a site user i can edit the amount of product in my cart so that i can easily decrement or increment products that i want to buy.
* 14. As a site user i can edit the amount of products in the shopping bag so that its easy to edit.
* 15. As a site user i can view my selected items in the bag so that i know what i am going to purchase.
* 16. As a site user i can enter my payment information easily so that i can checkout quickly.
* 17. As a site user i can view a order confirmation after purchase so that i know that my order went through.
* 18. As a site user i can receive a order confirmation so that i know my purchase went through.
* 19. As a site owner i can provide a contact form so that users can provide feedback or request products.
* 20. As a site owner i can have my customers signing up for a newsletter so that they can receive a emails about site news.
* 21. As a site admin i can add products so that i can update my inventory.
* 22. As a admin i can edit my products so that i can update them in the future.
* 23. As a admin i can be. able to delete products so that i can remove old products.
* 24. As a site user i can be able to see the stores adress so that i can visit them.
* 25. As a site user i can read about the company so that i can get familiar with the company.

## Project Design 

### Color Scheme 
![IMG ALT DESC HERE](IMG PATH HERE)
* The idea for the site is minimalistic and clean, the project is partly inspired by Code Institutes "Boutique Ado" with some finishing styles that i've added. 

* The product images i have taken from Link!!! with permission. 

### Wireframes 
I took a lot of inspiration from Code Institutes Boutique Ado walktrough project. 
Homepage Mockup:
![IMG ALT DESC HERE](IMG PATH HERE)

Product page mockup: 
![IMG ALT DESC HERE](IMG PATH HERE)

### Fonts 
Google Fonts has been used to provide free fonts for commercial use. The fonts selected have been chosen for differing reasons whilst still complementing each other. 

### Database Schema 
The Database schema is as below: 
![IMG ALT DESC HERE](IMG PATH HERE)


### Web Marketing Startegy 

Building on the insights gained as part of the Design Thinking phase. This project has the business model of Business to customer as the business is selling directly to the end user. 

#### Search Engine Optimisation (SEO)

SEO is key to driving traffic from a browser search like Google to the website. To help improve the search engine ranking I ensured each web page has it's own title, and the site carries meta tags for a description and keywords which encapsulate the general content and focus of this B2C site.

#### Sitemap.xml / Robots.txt 
I have created a sitemap.xml and robot.txt to help search engines locate my website. And to keep the website safe. 

#### Newsletter 

To allow the business to communicate with their customers to promote products and events through digital marketing, i have created a newsletter (One of three original models). The newsletter can be found at the bottom of the site, in the footer. Once the emial address is submitted a success message is presented to notify that the user is signed up. If by chance the user trys to sign up agian, the user is notifyied that their emial is already signed up.

#### Coffee shop location 

I have used Google Maps within an iframe inside the footer to promote the physical store location to show customers how they can physicaly experience the businesses coffee.


#### Facebook Page 
To increase traffic to the website, a facebook page has been built that will display information about the products and business.
![IMG ALT DESC HERE](IMG PATH HERE)

## Project Features 

### Navbar
* I have used a Bootstrap 4 fixed navbar that remains on all pages. Its easy to navigate with a clear font and design. While collapsing to mobile view it changes to a burger menu. 
* The navbar includes a shop dropdown menu where you can selelct a specific category to browse through. 
aswell as a about page, and contact page. 
* To the right in the navbar is a dropdown meny for users to register/login and logout. Aswell as a big icon to enter the shooping bag. 
![IMG ALT DESC HERE](IMG PATH HERE)


### Homepage 
* the homepage has several features, a nice background image with a button that is linked to the products page, containing all the products. Its easy for the user to access the products directly after opening th website. 
![IMG ALT DESC HERE](IMG PATH HERE)

### Footer 
* The footer offers a nice dark colour to distinguishing the top from the bottom. The footer enables quick access to key information to improve the users journey on the website. It also includes the businesses socials. 

### Products & Customer reviews 
* Using a Bootstrap grid, the products are set out in rows with each product aligned to a card. 
Each card provides brief info on the product, and the user is able to find out more buy clicking on th eproduct image. 
![IMG ALT DESC HERE](IMG PATH HERE)
* Clicking through provides more information on the specific product with options to add the item to their bag or update quantity. This page also promotes feedback from users through Customer Reviews. Only users who are registered can leave a review so there is a handy link to encourage this feature. Reviews are published immediately to provide a feeling of success to the user. The business assess reviews regularly to ensure there is nothing inflammatory - at which point they could be deleted through Django Admin. (The Reviews feature is the second of the three oginal models).
![IMG ALT DESC HERE](IMG PATH HERE)

### Shopping Bag

The bag page provides an overview of all of the items added by the user. The information aims to confirm what the user has selected with a table of information about the product and a supporting image. The price of all items is calculated and provided as a 'subtotal' with the delivery charge if the price is not over 40 dollars. Users can change quantity of a product or remove a product from the shopping bag, before proceeding to checkout. Users also have the option to keep shooping via a button located at the bottom. 
![IMG ALT DESC HERE](IMG PATH HERE)

### Checkout 

This page enables the user to complete their transaction. It is split in to two sections with delivery and billing on the left side and an overview of the items that are about to be purchased on the right. Here stripe have been implemented to manage transactions and collect payments. The test purchases have been enabled using the following card details. 
![IMG ALT DESC HERE](IMG PATH HERE)
![IMG ALT DESC HERE](IMG PATH HERE)

When completing a transaction, users are automatically navigated to tthe checkout success page. Which provides a confirmation. The confirmation is also emailed to the user. 

![IMG ALT DESC HERE](IMG PATH HERE)

### User Profile 

Accessed through the 'My Account' link in the navbar, a registered and signed-in user can update their saved delivery details and view order history. Each transaction is a row with a table. The 'Order Number' can be clicked to open the order confirmation page.

![IMG ALT DESC HERE](IMG PATH HERE)
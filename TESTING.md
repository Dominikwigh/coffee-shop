# Automated Testing
Automated Unit Testing was done using Django’s testing tools by importing the built in TestCase class from Django. Below is an overview report for testing forms, views and models for each app. The reports are generated when I installed coverage in the terminal using the commands:
- pip3 install covreage
- coverage run --source=(appname) manage.py test
#### To view the reports in the browser:
- coverage report
- coverage html
- python3 -m http.server
#### Bag Testing
 ![Bag app testing report](../coffee-shop/documentation/bagreport.png)
 #### Checkout Testing
 ![Checkout app testing report](../coffee-shop/documentation/checkoutreport.png)
 #### Company Testing
 ![Company app tsting report](../coffee-shop/documentation/companyreport.png)
 #### Products Testing
 ![Products app testing report](../coffee-shop/documentation/productsreport.png)
 #### Profiles Testing
 ![Profiles app testing report](../coffee-shop/documentation/profilesreport.png)

# Manual Testing 

The purpose of this document is to summarise the process, results, bugs and fixes as part of manual testing of the coffee-shop website. 
All test have been performed using the live envioronment deployed from heroku. 

## User Story Testing
The objective of this test is to validate that the user requirements have been delivered for the MVP release.
User story: 
>  1. As a site user i can view a list of products so that i can select some to purchase.
![All products page](../coffee-shop/documentation/productdetail.png)

> 2. As a site user i can view individual products so that i can identify the description.
![Productpage](../coffee-shop/documentation/productpage.png)

> 3. As a site user i can have a personal account so that i can view my profile.
![profile page](../coffee-shop/documentation/profilepage.png)

> 4. As a site user i can easily login or logout so that i can access my account information.
![Login in page](../coffee-shop/documentation/loginpage.png)
![Login out page](../coffee-shop/documentation/logout.png)

> 5. As a site user i can have a personalized user profile so that i can view my order history.
![order history](../coffee-shop/documentation/orderhistory.png)

> 6. As a site user i can recover my password if i forget it so that i can recover access to my account.
![password rest page](../coffee-shop/documentation/passwordreset.png)

> 7. As a site user i can get an email after registering so that i know that my registration was successful.
![confirm email](../coffee-shop/documentation/confirmemail.png)

> 8. As a site user i can see product reviews so that i can see which product is the most popular.
![review section](../coffee-shop/documentation/review.png)

> 9. As a site user i can add items to my cart so that i can purchase them later.
![shoppingbag page](../coffee-shop/documentation/shoppingbag.png)

> 10. As a site user i can view a specific category so that i can quickly find the product iam looking for.
![Category menu](../coffee-shop/documentation/categorysearch.png)


> 11. As a site user i can search for products so that i can easily find what iam looking for.
![Product search page](../coffee-shop/documentation/productsearch.png)

> 12. As a site user i can delete an item from my cart so that i can change product to buy.
![Removed item from bag](../coffee-shop/documentation/removeditemfrombag.png)

> 13. As a site user i can edit the amount of product in my cart so that i can easily decrement or increment products that i want to buy.
![Updated amount in bag](../coffee-shop/documentation/updatedamountbag.png)

> 14. As a site user i can view my selected items in the bag so that i know what i am going to purchase.
![Shopping bag page](../coffee-shop/documentation/shoppingbagpage.png)

> 15. As a site user i can enter my payment information easily so that i can checkout quickly.
![Checkoutpage](../coffee-shop/documentation/checkoutpage.png)

> 16. As a site user i can view a order confirmation after purchase so that i know that my order went through.
![Order confirmation page](../coffee-shop/documentation/orderconfirmation.png)

> 17. As a site owner i can provide a contact form so that users can provide feedback or request products.
![Contact page form](../coffee-shop/documentation/contactpage.png)

> 18. As a site owner i can have my customers signing up for a newsletter so that they can receive a emails about site news.
![Newsletter form](../coffee-shop/documentation/newsletterform.png)

> 19. As a site admin i can add products so that i can update my inventory.
![Add prodcut page](../coffee-shop/documentation/addproductpage.png)

> 20. As a admin i can edit my products so that i can update them in the future.
![Edit product page](../coffee-shop/documentation/editproductpage.png)

> 21. As a admin i can be able to delete products so that i can remove old products.
![Deleted product toast](../coffee-shop/documentation/deleteproduct.png)

> 22. As a site user i can be able to see the stores address so that i can visit them.
![Store contact info](../coffee-shop/documentation/storeaddress.png)

> 23. As a site user i can read about the company so that i can get familiar with the company.
![About page](../coffee-shop/documentation/aboutpage.png)

## Feature Testing

### Navbar

* Links 
    Tested following: 
    * Links are changing colour when hovered over.
    * The shop link drops down and displayes, "All products, Beans and Coffee machines.
    * Once the screen size is collapsed to small the links collapse to a hamburger menu. 
![Nav bar](../coffee-shop/documentation/navbar.png)
* Search bar 
    Tested following:
    * The search bar will search both product title and description. 
    * once the screen size is collapsed to small the search bar turns into a icon and is displayed beside the account icon. 
![Search bar](../coffee-shop/documentation/searchbar.png)
* Account 
    Tested following:
    * Hovering over the account icon, it changes colout. 
    * When clicking the account icon it displays as a dropdown for the user to either register or signin. 
    * When a user is logged in the options change to "My account" and "Signout".
    * When a user is signed in as a super user then a third option of 'Product Management' is available.

![Account icon](../coffee-shop/documentation/accounticon.png)
* Bag
    Tested following:
    * Underneath the bag icon there is a total cost of all the items in the bag displayed. 
    And chnages accordingly. 
    * When the bag icon is clicked, the user gets navigated to the shopping bag. 
    * After an item has been added a pop. up window is shown with the quantity of items and total cost. 
![Bag icon](../coffee-shop/documentation/bagicon.png)

### Home page

* Hero image
    Tested following:
    * The "Shop now" button takes the user to all products page.
![Hero image](../coffee-shop/documentation/heroimage.png)
* Footer
    Tested following:
    * All links in the footer open when clicked.
    * Filling out the newsletter works and sends the email to the admin.
![Footer](../coffee-shop/documentation/footer.png)

### Accounts 

* Registration page 
    Tested following: 
    * Submitting the registration form sends a link to the users email. Then the user has to verify their email. 
    * After filling out he form, these details works to login.
![Registration form](../coffee-shop/documentation/registrationform.png)
    * Then the email adress has to get to verified. By clicking the link and then confirming. Then the user can login
![Email verification](../coffee-shop/documentation/confirmemail.png)
![Login page](../coffee-shop/documentation/loginpage.png)
* Login Page
    Tested following:
    * Logging in, works for users that have already created an account.
    * User can sign in via username and email.
    * Toast messages are displayed correctly.
![Login page](../coffee-shop/documentation/loginpage.png)
* Log out page
    Tested following: 
    * The log out page logs out users. 
    * Toast messages are displayed correctly. 
    * The account icon chnages from "my account" to "sign in". 
![Logout](../coffee-shop/documentation/logout.png)

### Profile 

* Delivery Details / Order history
    Tested following:
    * Every information added by the user matches.
    * Updates to delivery information updates when button is clicked.
    * The saved information will autofill at checkout.
    * Toast messages work when details have been updated.
    * Clicking the order number will send the user to the order confirmation page. 
    * When the screen is displayed as small the order history will be displayed below the delivery information. 
![Profile page](../coffee-shop/documentation/profilepage.png)

### Products 

* All prodcuts page
    Tested following:
    * The product page is responsive, adjusting the amount of products displayed depending on screen size.
    * Each product displays an image, title, price, category and rating.
    * If the user is an admin there will be displayed two buttons, one for edit and one for delete.
![Products page](../coffee-shop/documentation/productpage.png)

* Product Detail
    Tested following:
    * The product detail info shows information about the product, along with buttons to add to cart, and the quantity the user wishes to add to the bag.
    * The product rating is an average and will display result in stars. It is not linked to the review form. 
    * There is a button for keep shopping beneath the add to bag button. 
    * If the user is an admin there will be displayed two buttons, one for edit and one for delete.
![Product detail page](../coffee-shop/documentation/productdetail.png)

### Product review (1 of 3 original models)
    Tested following: 
    * The product review card is located beneath the product detail.
    * Since the leave review button is only valid for logged in users, there will be an sign in and signup button for users that are not authenticated and logged in.
    * The review contains the amount of stars given, the comment they've added, the users name and when it was added.
![Product review logged in](../coffee-shop/documentation/reviewloggedin.png)
![Product review not logged in](../coffee-shop/documentation/review.png)

### Product Management

* Add a product 
    Tested following:
    * The button for adding a product is accessed via the account dropdown menu, under product management.
    * The form can't be submitted with any empty fields besides image url and rating.
    * When a product has been added a success message is shown to alert the user of the action. 
![Add product page](../coffee-shop/documentation/addproductpage.png)

* Edit Product
    Tested following: 
    * The edit button can be accessed both from all products view, and product detail view.
    * Clicking to edit the product button leaves all the forms filled out as is, with options to edit fields. And a alert message is shown to alert the admin that they are editing the product.
    * Clicking the button "Update Product" saves any changes made to the existing item.
    * The edit button can only be accessed from a logged in admin user.
![Edit product page](../coffee-shop/documentation/editproductpage.png)

* Delete Product
    Tested Following: 
    * The delete button can be accessed both from all products view, and product detail view.
    * At the moment there is no warning to show when clicking delete. 
    * When a product is deleted a success message is shown. 
    * When deleteing a product it is deleted completely from the database. 
![Delete product page](../coffee-shop/documentation/deleteproduct.png)

### Bag 

* Items 
    Tested following: 
    * The shopping bag displays the items added to the bag.
    * Clicking the image in the bag will redirect the user to the product detail page.
    * The added item shows the image, name, price and quantity of the product.
    * Each product has a line to change the qty of the item, or delete it from the bag.
![Shopping bag page](../coffee-shop/documentation/shoppingbagpage.png)

* Quantity and Price
    Tested following:
    * The quantity element button has two sides, one to decrease and one to increase the total of items.
    * The minus option will be disabled if the quantity of the item is one.
    * The plus button will disable if the amount added is 99.
    * Clicking remove, will remove the specified product from the bag.

### Checkout 

* Checkout details
    Tested following:
    * If the user is anonymous, a link to create an account or login will be present.
    * Any field with the sign * has to be filled out, if left empty, an error message will be displayed.
    * If the user is logged in, the box for save information can be checked, and the information will then be saved.
    * If the user is signed in and already has added their information, that will be displayed automatically.
![Chekout page](../coffee-shop/documentation/checkoutpage.png)

* Order Summary 
    Tested following:
    * Clicking the image of the product takes the user to the product detail view.
    * This section will show details of everything in the bag, along with quantity and grand total.

* Payment 
    Tested following:
    * Only numbers can be entered in the card payment section. Incorrect card numbers will display an error message.
    * You can make a purchase using a fake card number: 4242 4242 4242 4242 with the expiry date 04/24 and the CVC code 242.
    * You can either make your purchse or go back to the shopping bag via the buttons located beneath the card form. 
![Card form](../coffee-shop/documentation/cardform.png)

* Confirmation 
    Tested following:
    * Once the order has been processed the user is taken to the successpage.
    * An email confirmation will be sent to the users given email.
    * After the summary the user can choose to go back to the shop via a button located at the bottom. 
![Confirmation page](../coffee-shop/documentation/orderconfirmation.png)

* Webhooks 
    Tested following: 
    * After the payment has gone thru, the order shows in the webhooks and confirm the order exists.
![Webhhok page](../coffee-shop/documentation/webhooks.png)


### About Page
    
Tested following:
* Page is accessible from the navbar and when "About" is cliked it directs the user to the about page. 
* Image is responsive and looks good on all screen sizes. 
![About Page](../coffee-shop/documentation/aboutpage.png)


### Contact (1 of 3 original models)
* Contact Info 
    Tested following:
    * Hovering over the social media icons will make them change colour. 
    * When clicking the map, it takes the user to google maps. 

* Contact form
    Tested following:
    * All fields are required to be filled out. 
    * When all fields have been filled out the "Submit" button sends a emial to the store owner. And the user is shown a success message. 
![Contact page](../coffee-shop/documentation/contactpage.png)


### Newsletter (1 of 3 original models)
Tested following:
* Signing up to the newsletter works. 
* When a user has signed up a success message is shown. 
* When a user already have signed up before, a error message is shown that their email is already signed up. 
![Newsletter form](../coffee-shop/documentation/newsletterform.png)
![Newsletter success message](../coffee-shop/documentation/newslettersuccess.png)
![Newsletter error message](../coffee-shop/documentation/newslettererror.png)
![Newsletter signup](../coffee-shop/documentation/newslettesignup.png)


### Toast 
Tested following:
* Toast messages appear in the top right corner and are displayed anytime the user does something on the site. 
* The toast message will be green if it is succeefuf.
* The toast message will be red if it is an error. 


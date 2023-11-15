 Feature: User can log in on the page / buy a product / remove product from shopping cart

	Scenario: Successful Login
		Given a standard_user is a customer
		When they enter their username and password
		Then they click the login button and log in

	Scenario: Buy Product
		Given standard_user logs in successfully
		And selects a product
		When confirm the product
		And fill in the order information
		Then they should be able to complete the purchase

	Scenario: Remove Product from Shopping Cart
		Given standard_user logs in correctly
		And has a product added to the shopping cart
		When they click the remove button for a product they dont want to buy
		Then they will return to the main product page





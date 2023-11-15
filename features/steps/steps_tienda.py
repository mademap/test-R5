from behave import given, when, then
from src.functions.function import Shopping

# Scenario 1
@given('a standard_user is a customer')
def step_login(context):
    context.test = Shopping()


@when('they enter their username and password')
def step_impl(context):
    context.test.login()


@then('they click the login button and log in')
def button_login(context):
    context.test.click_button_login()

# Scenario 2

@given('standard_user logs in successfully')
def login_success(context):
    step_login(context)
    step_impl(context)
    button_login(context)


@given('selects a product')
def select_product(context):
    context.test.list_products()


@when('confirm the product')
def confirm_product(context):
    context.test.confirm_product()


@when('fill in the order information')
def register_info(context):
    context.test.register_info()


@then('they should be able to complete the purchase')
def finish_buy(context):
    context.test.finish_buy()

# Scenario 3

@given('standard_user logs in correctly')
def login_success_2(context):
    step_login(context)
    step_impl(context)
    button_login(context)


@given('has a product added to the shopping cart')
def product_added(context):
    select_product(context)


@when('they click the remove button for a product they dont want to buy')
def product_remove(context):
    context.test.product_remove()


@then('they will return to the main product page')
def return_shopping(context):
    context.test.return_shopping()

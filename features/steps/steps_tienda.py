from behave import given, when, then
from src.functions.function import Shopping


@given('un standard_user es un cliente')
def step_login(context):
    context.test = Shopping()


@when('digita su usuario y contraseña')
def step_impl(context):
    context.test.login()


@then('dara clic en el boton login e iniciara sesion')
def button_login(context):
    context.test.click_button_login()


@given('standard_user inicia sesion correctamente')
def loguin_success(context):
    step_login(context)
    step_impl(context)
    button_login(context)


@given('selecciona un producto')
def select_product(context):
    context.test.list_products()


@when('confirma el producto')
def confirm_product(context):
    context.test.confirm_product()

@when('diligencia la informacion de pedido')
def register_info(context):
    context.test.register_info()


@then('podra realizar la compra')
def finish_buy(context):
    context.test.finish_buy()
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
def login_success(context):
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


@given('standard_user inicia sesion satisfatoriamente')
def login_success_2(context):
    step_login(context)
    step_impl(context)
    button_login(context)


@given('tiene un producto agregado en el carro de compras')
def product_added(context):
    select_product(context)


@when('da click en el boton remove de un producto que no desea comprar')
def product_remove(context):
    context.test.product_remove()


@then('regresara a la pagina principal de productos')
def return_shopping(context):
    context.test.return_shopping()

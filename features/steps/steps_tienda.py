from behave import given, when, then
from src.function import Shopping

@given('un usuario que introduce su {user_name} and su password {password}')
def step_login(context, user_name, password):
    context.test= Shopping(context)
    context.test.login(user_name, password)


@when('da click en el {boton}')
def step_login(context, login):
    context.test.login(login)


@then('debería cargarse la {pagina} junto con los siguientes id de {productos}')
def step_login(context, pagina, productos):
    context.test.login(pagina, productos)


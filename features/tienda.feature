Feature: usuario puede loguearse en la pagina y comprar un producto

#	Scenario: Login correcto
#		Given un standard_user es un cliente
#		When digita su usuario y contraseña
#		Then dara clic en el boton login e iniciara sesion
#
#
#	Scenario: Buy product
#		Given standard_user inicia sesion correctamente
#		And selecciona un producto
#		When  confirma el producto
#		And diligencia la informacion de pedido
#		Then podra realizar la compra

	Scenario: Remove product from shopping cart
		Given standard_user inicia sesion satisfatoriamente
		And tiene un producto agregado en el carro de compras
		When da click en el boton remove de un producto que no desea comprar
		Then regresara a la pagina principal de productos





Feature: usuario puede loguearse en la pagina

	Scenario Outline: Login correcto
	Given un usuario que introduce su <user_name> and su password <password>
	When da click en el <boton>
	Then debería cargarse la <pagina> junto con los siguientes id de <productos>

	Examples:
	| user_name 				| password 			| boton    	| pagina    | productos			|
	| standard_user  			| secret_sauce      | login 	| inventory	| 4, 0, 1, 5, 2, 3	|
	| problem_user 				| secret_sauce      | login 	| inventory | 5, 1, 2, 6, 3, 4	|
	| performance_glitch_user 	| secret_sauce      | login 	| inventory | 4, 0, 1, 5, 2, 3	|
	| error_user 				| secret_sauce      | login 	| inventory | 4, 0, 1, 5, 2, 3	|
	| visual_user 				| secret_sauce      | login 	| inventory | 4, 0, 1, 5, 2, 3	|

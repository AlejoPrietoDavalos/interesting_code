""" - Author: GPTingi"""

# Ejemplo inseguro usando eval
input_string = '["txt_1", "txt_2"]'
result = eval(input_string)
print(result)  # Esto puede parecer seguro, pero...

# Ejemplo de una cadena peligrosa
### dangerous_input = '__import__("os").system("rm -rf /")'
# Si eval se usa con esta cadena, ejecutará un comando de sistema peligroso:
### eval(dangerous_input)

#---> Uso de ast.
# Ejemplo de uso seguro para evaluar un string.
import ast
result = ast.literal_eval('["create_url_payment", "contact_info"]')
print(result)

import win32api 
# Obtener la posición del cursor en una tupla (x, y) 
pos = win32api.GetCursorPos() 
# Mostrar las coordenadas de la posición del cursor en la pantalla 
print(f'Coordenadas del cursor: {pos}')
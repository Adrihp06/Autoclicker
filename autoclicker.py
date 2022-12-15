import time
import win32api
import win32con

# Establecer la posición del clic en la pantalla
x_coord = 0
y_coord = 0

x_coord1 = 0
y_coord1 = 0


# Establecer el tiempo de intervalo entre clics en segundos
interval = 1

while True:
  # Hacer clic en la ubicación establecida
  win32api.SetCursorPos((x_coord, y_coord))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x_coord, y_coord, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x_coord, y_coord, 0, 0)
  
  win32api.SetCursorPos((x_coord1, y_coord1))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x_coord1, y_coord1, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x_coord1, y_coord1, 0, 0)

  # Esperar el intervalo de tiempo establecido antes del próximo clic
  time.sleep(interval)

    
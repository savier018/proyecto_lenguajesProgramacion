import tkinter as tk
from analizador_lexico import analizar_codigoL
from analizador_lexico import checkErrorsL
from analizador_lexico import getErrorsL
from analizador_lexico import deleteErrorsL
from analizador_sintactico1 import analizar_codigoS
from analizador_sintactico1 import checkErrorsSS
from analizador_sintactico1 import getErrorsSS
from analizador_sintactico1 import deleteErrorsSS

erroresText=""
errors=False

def analizar_codigo(entrada_usuario):
    analizar_codigoL(entrada_usuario)
    analizar_codigoS(entrada_usuario)
    ErroresL= []
    ErroresSS= []
    global erroresText
    if (checkErrorsL):
        ErroresL= getErrorsL()
        erroresText = '\n'.join(ErroresL)
    if (checkErrorsSS):
        ErroresSS= getErrorsSS()
        erroresText = '\n'.join(ErroresSS)


def obtener_respuesta():
    global erroresText
    entrada_usuario = entrada_texto.get("1.0", "end-1c")
    analizar_codigo(entrada_usuario)
    respuestaText= ""
    if(checkErrorsL() | checkErrorsSS()):
        respuestaText= "Se han encontrado errores."
    else:
        respuestaText= "No se han encontrado errores"
    texto_respuesta.delete("1.0", "end")
    texto_respuesta.insert("1.0",respuestaText)
    texto_errores.delete("1.0", "end")
    texto_errores.insert("1.0",erroresText)  
    erroresText = ""
    deleteErrorsL()
    deleteErrorsSS()


ventana = tk.Tk()
ventana.title("PROYECTO PARCIAL LP")
ventana.geometry("700x350")  # Ancho x Alto en píxeles

# Etiqueta y cuadro de texto para el cuadro de entrada
label_entrada = tk.Label(ventana, text="Ingrese su texto aquí:")
label_entrada.grid(row=0, column=0, padx=10)

entrada_texto = tk.Text(ventana, height=15, width=40)
entrada_texto.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

# Etiqueta y cuadro de texto para el cuadro de respuesta
label_respuesta = tk.Label(ventana, text="Respuesta y Errores:")
label_respuesta.grid(row=0, column=1, padx=10,)

texto_respuesta = tk.Text(ventana, height=3, width=40)
texto_respuesta.grid(row=1, column=1, padx=10)
texto_errores = tk.Text(ventana, height=10, width=40)
texto_errores.grid(row=2, column=1, padx=10)

# Botón para obtener la respuesta
boton_respuesta = tk.Button(ventana, text="Obtener Respuesta", command=obtener_respuesta)
boton_respuesta.grid(row=3, column=0, columnspan=2, padx=10)


ventana.mainloop()
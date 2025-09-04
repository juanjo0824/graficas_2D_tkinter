from tkinter import *

# ----------------------
# ventana principal
# ----------------------
ventana_principal = Tk()
ventana_principal.title("graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("600x400")
ventana_principal.config(bg="white")

# -------------------------
# frame de graficacion
# -------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="black", width=580, height=380)
frame_graficacion.place (x=10,y=10)

# -----------------------
# lienzo de graficacion 
# -----------------------
c = Canvas(frame_graficacion, width=560, height=360)
c.config(bg="green")
c.place(x=10,y=10)

rectangulo_1 = c.create_rectangle(390,0, 510, 20,fill="blue", outline="white")
rectangulo_2 = c.create_rectangle(370,20, 530, 40,fill="black", outline="white")
rectangulo_3 = c.create_rectangle(400,50, 500, 130, outline="brown", width=20)
rectangulo_4 = c.create_rectangle(210,90, 240, 140, fill="orange", outline="white")
rectangulo_5 = c.create_rectangle(200,70, 250, 90, fill="orange", outline="white")
circulo_1 = c.create_oval(110,150,300, 290, fill= "white")
rectangulo_6 = c.create_rectangle(150,130, 180, 310, fill="black", outline="white")
rectangulo_7 = c.create_rectangle(200,140, 510, 300, fill="red", outline="white")
circulo_2 = c.create_oval(210,250,290, 330, fill= "grey")
circulo_3 = c.create_oval(310,250,390, 330, fill= "grey")
circulo_3 = c.create_oval(410,250,490, 330, fill= "grey")


# ----------------------------
# desplegar ventana principal
# ----------------------------
ventana_principal.mainloop()
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import json
import math

class PrimeraVentana:
    def __init__(self, ventana):
        self.ventana_1 = ventana
        self.ventana_1.title('Hotel Luna')
        self.ventana_1.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.ventana_1.geometry('600x750')

        # Creacion de Frame Contenedor
        self.frame = Frame(self.ventana_1, background='white')
        self.frame.pack(fill=BOTH, expand=True)

        self.crear_imagen()
        self.crear_label_bienvenida()
        self.crear_boton()

    # Crear Imagen
    def crear_imagen(self):
        img = Image.open("Hotel_Luna/Imagenes/Imagen de WhatsApp 2024-04-23 a las 20.21.28_83c25263.jpg") 
        img = img.resize((400, 400))  
        imagen = ImageTk.PhotoImage(img)
        self.label = Label(self.frame, image=imagen)
        self.label.image = imagen 
        self.label.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    # Crear mensaje Bienvenida
    def crear_label_bienvenida(self):
        self.label_bienvenido = Label(self.frame, text='Bienvenido al Hotel Luna', font=('Arial', 18), bg='white')
        self.label_bienvenido.place(relx=0.5, rely=0.75, anchor=CENTER)
    
    # Crear boton
    def crear_boton(self):
        self.boton = tk.Button(self.frame, text='Ingresar', font= ('Arial',15), command=self.abrir_segunda_ventana)  
        self.boton.config(width=10, height=1)
        self.boton.place(relx=0.5, rely=0.9, anchor=CENTER)

    def abrir_segunda_ventana(self):
        self.ventana_1.withdraw() 
        ventana_segunda = SegundaVentana(self.ventana_1)

class SegundaVentana:
    def __init__(self, master):
        self.master = master
        self.ventana_2 = Toplevel(master)
        self.ventana_2.title('Hotel Luna')
        self.ventana_2.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.ventana_2.geometry("800x750")

        ### nuevo self. para direccion de las imagenes ###
        self.imagenes = {
            "Habitación Normal $40.000": "Hotel_Luna/Imagenes/habitacion normal.jpeg",
            "Habitación Mediana $50.000": "Hotel_Luna/Imagenes/habitacion mediana.jpg",
            "Habitación Grande $70.000": "Hotel_Luna/Imagenes/habitacion grande.jpg",
            "Suite $100.000": "Hotel_Luna/Imagenes/haitacion suite.jpg"
        }   
      
        self.frame = Frame(self.ventana_2, bg='white')
        self.frame.pack(fill=BOTH, expand=True)

        self.crear_widgets()

    def crear_widgets(self):

        # Añadimos el titulo de la ventana
        self.titulo_label = tk.Label(self.frame, text="         Reserva de Habitación           ", font=('Arial', 12), bg='white')
        self.titulo_label.pack(pady=20)

        ### boton ver reservas ###
        self.reservar_button = Button(self.frame, text="Ver Reservas", font=('Arial', 10), command=self.ver_reserva)
        self.reservar_button.place(x=220, y=650)

        # Añadimos la imagen (Logo)
        self.img = Image.open("Hotel_Luna/Imagenes/Imagen de WhatsApp 2024-04-23 a las 20.21.28_83c25263.jpg")
        self.img = self.img.resize((300, 300))
        self.logo = ImageTk.PhotoImage(self.img)
        self.logo_label = Label(self.frame, image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.place(relx=0.75, rely=0.5, anchor=CENTER)

        # Agregamos los textos con sus casillas para ingresar la informaci0n
        self.nombre_label = Label(self.frame, text="Nombre/s: ", font=('Arial', 12), bg='white')
        self.nombre_label.place(x=10, y=100)
        self.nombre_entry = Entry(self.frame, fg="black")
        self.nombre_entry.place(x=130, y=100)

        self.apellido_label = Label(self.frame, text="Apellido/s: " ,font = ('Arial', 12), bg='white')
        self.apellido_label.place(x=10, y=200)
        self.apellido_entry = Entry(self.frame, fg="black")
        self.apellido_entry.place(x=130,y=200)

        self.rut_label = Label(self.frame, text="Rut: ", font=('Arial', 12), bg='white')
        self.rut_label.place(x=10, y=300)
        self.rut_entry = Entry(self.frame, fg="black")
        self.rut_entry.place(x=130, y=300)

        self.dias_label = Label(self.frame, text="Día/s: ", font=('Arial', 12), bg='white')
        self.dias_label.place(x=10, y=400)

        # Se crea menu desplegable de los dias
        self.dias_var = StringVar(self.ventana_2)
        self.dias_var.set("1 Día")
        self.dias_opciones = ["1 Día", "2 Días", "3 Días", "4 Días"]
        self.dias_option_menu = OptionMenu(self.frame, self.dias_var, *self.dias_opciones)
        self.dias_option_menu.place(x=100, y=400)

        self.tipo_habitacion_label = Label(self.frame, text="Tipo de Habitación: ", font=('Arial', 12), bg='white')
        self.tipo_habitacion_label.place(x=10, y=500)

        # Se crea menu desplegable de las habitaciones con sus respectivos precios
        self.tipo_habitacion_var = StringVar(self.ventana_2)
        self.tipo_habitacion_var.set("Habitación")
        self.tipo_habitacion_opciones = ["Habitación Normal $40.000", "Habitación Mediana $50.000", "Habitación Grande $70.000", "Suite $100.000"]
        self.tipo_habitacion_option_menu = OptionMenu(self.frame, self.tipo_habitacion_var, *self.tipo_habitacion_opciones)
        self.tipo_habitacion_option_menu.place(x=190, y=500)

        # Agregamos el boton 'Reservar' para guardar toda la informaci0n elegida
        self.reservar_button = Button(self.frame, text="Reservar", font=('Arial', 10), command=self.combinacion_funciones)
        self.reservar_button.place(x=120, y=650)
        self.reservar_button.config(state=DISABLED)

        ### para ver las imagenes ###                    <----------------------------
        self.imagen_label = tk.Label(self.ventana_2)
        self.imagen_label.place(relx=0.75, rely=0.5, anchor=CENTER)
        ### actualiza imagen ###
        self.tipo_habitacion_var.trace_add("write", self.actualizar_imagen)

        # Creamos una función que verifique si los campos de texto están vacíos
        def verificar_campos():
            if self.nombre_entry.get() != "" and self.rut_entry.get() != "" and self.apellido_entry.get() != "":
                self.reservar_button.config(state=NORMAL)
            else:
                self.reservar_button.config(state=DISABLED)

        

        # Asignamos la función 'verificar_campos' a los campos de texto
        self.nombre_entry.bind("<KeyRelease>", lambda event: verificar_campos())
        self.apellido_entry.bind("<KeyRelease>", lambda event: verificar_campos())
        self.rut_entry.bind("<KeyRelease>", lambda event: verificar_campos())

        # Validaciones
        self.nombre_entry.config(validate="key", validatecommand=(self.nombre_entry.register(self.validar_nombre), "%S"))
        self.apellido_entry.config(validate="key", validatecommand=(self.apellido_entry.register(self.validar_apellido), "%S"))

    def combinacion_funciones(self):
        if self.tipo_habitacion_var.get() == "Habitación":
            messagebox.showerror("Error", "Por favor seleccione un tipo de habitación.")
        elif self.validar_rut(self.rut_entry.get()):
            self.reservar()
        else:
            messagebox.showerror("Error", "Rut inválido. Verifique que el rut tenga el formato correcto y que el dígito verificador sea un solo carácter. Ejemplo: '19664581-0'.")

    def reservar(self):
        # Creamos un diccionario para guardar los datos
        datos = {
            "nombre": self.nombre_entry.get(),
            "apellido":self.apellido_entry.get(),
            "rut": self.rut_entry.get(),
            "dias": self.dias_var.get(),
            "tipo_habitacion": self.tipo_habitacion_var.get()
        }
        
        # Crea los precios de las habitaciones
        precio_habitacion = 0
        if datos["tipo_habitacion"] == "Habitación Normal $40.000":
            precio_habitacion = 40000
        elif datos["tipo_habitacion"] == "Habitación Mediana $50.000":
            precio_habitacion = 50000
        elif datos["tipo_habitacion"] == "Habitación Grande $70.000":
            precio_habitacion = 70000
        elif datos["tipo_habitacion"] == "Suite $100.000":
            precio_habitacion = 100000

        # Multiplica el precio de la habitacion por la cantidad de dias a quedar
        total_a_pagar = precio_habitacion * int(datos["dias"].split(" ")[0])

        # Agrega el total a pagar al diccionario con formato de número con puntos
        datos["total_a_pagar"] = "{:,.0f}".format(total_a_pagar).replace(",", "#").replace(".", ",").replace("#", ".")

        # Abrimos el archivo JSON y lo cargamos
        with open("datos.json", "r+") as archivo:
            datos_json = json.load(archivo)

        # Agregamos los nuevos datos al archivo JSON
        datos_json.append(datos)

        # Guardamos los datos en el archivo JSON
        with open("datos.json", "w") as archivo:
            json.dump(datos_json, archivo, indent=4)

        messagebox.showinfo("Reserva", "Reserva Exitosa.")
        self.ventana_2.destroy()

        tercer_ventana = TerceraVentana(self.master)

    def validar_rut(self, rut):
        # Comprobar si el RUT contiene el "-"
        if "-" not in rut:
            return False

        # Separar el RUT en partes utilizando el "-"
        partes = rut.split("-")

        # Comprobar que el RUT tenga exactamente 2 partes
        if len(partes) != 2:
            return False

        # Obtener el número y el dígito verificador (DV)
        numero, dv_ingresado = partes

        # Remover los puntos del número
        numero = numero.replace(".", "")

        # Comprobar que el número tenga entre 7 y 8 caracteres
        if len(numero) < 7 or len(numero) > 8:
            return False

        # Comprobar que el DV sea un solo carácter
        if len(dv_ingresado) != 1:
            return False

        # Convertir el DV ingresado a mayúsculas
        dv_ingresado = dv_ingresado.upper()

        # Calcular el dígito verificador
        factores = [2, 3, 4, 5, 6, 7]
        suma = 0
        factor = 0
        for n in reversed(numero):
            suma += int(n) * factores[factor % len(factores)]
            factor += 1

        # Obtener el resto del módulo 11
        residuo = 11 - (suma % 11)

        # Convertir el residuo en el correspondiente dígito verificador
        if residuo == 11:
            dv_calculado = "0"
        elif residuo == 10:
            dv_calculado = "K"
        else:
            dv_calculado = str(residuo)

        # Comprobar si el dígito verificador calculado es igual al ingresado
        return dv_calculado == dv_ingresado

    # valida que el dato ingresado sea un str 
    # isalpha devuelve true si es un str
    # isspace devuelve true si es espacio en blanco
    def validar_nombre(self, char):
        return char.isalpha() or char.isspace()
    def validar_apellido(self, char):
        return char.isalpha() or char.isspace()
    
    #permite ver las reservas guardadas en la tercera_ventana
    def ver_reserva(self):
        cuarta_ventana = cuartaVentana(self.master)

    ### funcion que nos muestra la imagen con opcion seleccionada ###   <-------------------
    def actualizar_imagen(self, *args):
        opcion_seleccionada = self.tipo_habitacion_var.get()
        ruta_imagen = self.imagenes.get(opcion_seleccionada)  
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((300, 300), Image.LANCZOS) ### esta linea sirve para redimensionar las imagenes ###
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.imagen_label.config(image=imagen_tk)
        self.imagen_label.image = imagen_tk


class TerceraVentana:
    def __init__(self, master):
        self.master = master
        self.ventana_3 = Toplevel(master)
        self.ventana_3.title('Hotel Luna')
        self.ventana_3.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.ventana_3.geometry("600x700")
        self.texto = Label(self.ventana_3, text='Comprobante', font=('Arial', 12), bg='white')
        self.texto.pack()

        self.frame = Frame(self.ventana_3, bg='white')
        self.frame.pack(fill=BOTH, expand=True)

        self.crear_widgets()
        self.mostrar_datos()

    def crear_widgets(self):
        self.text_widget = Text(self.frame, font=('Arial', 12), bg='white')
        self.text_widget.pack(fill=BOTH, expand=True)

        self.regresar_button = Button(self.frame, text="Regresar", font=('Arial', 10), command=self.Regresar)
        self.regresar_button.pack()

        self.cancelar_button = Button(self.frame, text="Cancelar Reserva", font=('Arial', 10), command=self.Cancelar)
        self.cancelar_button.pack()

        self.modificar_button = Button(self.frame, text="Modificar", font=('Arial', 10), command=self.Modificar)
        self.modificar_button.pack()

        self.buscar_button = Button(self.frame, text="Buscar", font=('Arial', 10), command=self.mostrar_ventana_buscar)
        self.buscar_button.pack()

    def Regresar(self):
        self.ventana_3.destroy()
        self.master.deiconify()

    def Cancelar(self):

        try:
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

            datos_json.pop()

            with open("datos.json", "w") as archivo:
                json.dump(datos_json, archivo, indent=4)

            messagebox.showinfo("Cancelar Reserva", "Reserva cancelada exitosamente.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontraron ratos de reservas.")
        self.ventana_3.destroy()
        self.master.deiconify()

    def mostrar_datos(self):
        try:
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)
                for dato in datos_json:
                    self.text_widget.insert(END, f"Nombre/s: {dato['nombre']}\n")
                    self.text_widget.insert(END, f"Apellido/s: {dato['apellido']}\n")
                    self.text_widget.insert(END, f"Rut: {dato['rut']}\n")
                    self.text_widget.insert(END, f"Días: {dato['dias']}\n")
                    self.text_widget.insert(END, f"Tipo de Habitación: {dato['tipo_habitacion']}\n\n")
                    self.text_widget.insert(END, f"Total a Pagar: ${dato['total_a_pagar']}\n\n")
        except FileNotFoundError:
            self.text_widget.insert(END, "No se encontraron datos de reservas.")

    def Modificar(self):
        # Abrimos el archivo JSON y lo cargamos
        with open("datos.json", "r") as archivo:
            datos_json = json.load(archivo)

        # Obtenemos la última reserva
        ultima_reserva = datos_json[-1]

        # Creamos una ventana para modificar la reserva
        self.ventana_3.withdraw()
        ventana_modificar = Modificar_3(self.master, ultima_reserva)

    def mostrar_ventana_buscar(self):
        ventana_buscar = BuscarVentana2(self)

    def buscar_reserva(self, nombre_reserva, apellido_reserva):
        try:
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

            self.ultima_reserva_coincidencia = self.buscar_reserva_ultima(datos_json, nombre_reserva, apellido_reserva)

            if self.ultima_reserva_coincidencia:
                SextaVentana(self.master, self.ultima_reserva_coincidencia)
                self.ventana_3.withdraw()
            else:
                messagebox.showinfo("Buscar Reserva", f"No se encontró ninguna reserva a nombre de {nombre_reserva} {apellido_reserva}.")
        
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontraron datos de reservas.")

    def buscar_reserva_ultima(self, datos_json, nombre_reserva, apellido_reserva):
        ultima_reserva_coincidencia = None
        for dato in reversed(datos_json):
            if dato['nombre'] == nombre_reserva and dato['apellido'] == apellido_reserva:
                ultima_reserva_coincidencia = dato
                break
        return ultima_reserva_coincidencia

class Modificar_3(Toplevel):
    def __init__(self, master, ultima_reserva):
        super().__init__(master)
        self.title('Modificar Reserva')
        self.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.geometry("600x700")

        self.ultima_reserva = ultima_reserva

        self.frame = Frame(self, bg='white')
        self.frame.pack(fill=BOTH, expand=True)

        self.crear_widgets()

    def crear_widgets(self):
        # Agregamos los campos para modificar la reserva
        self.nombre_label = Label(self.frame, text="Nombre/s: ", font=('Arial', 12), bg='white')
        self.nombre_label.pack()
        self.nombre_entry = Entry(self.frame, fg="black")
        nombres_parts = self.ultima_reserva['nombre'].split()
        self.nombre_entry.insert(0, ' '.join(nombres_parts))
        self.nombre_entry.pack()
        self.nombre_entry.bind("<FocusOut>", self.validar_y_actualizar_nombre)

        self.apellido_label = Label(self.frame, text="Apellido/s: ", font=('Arial', 12), bg='white')
        self.apellido_label.pack()
        self.apellido_entry = Entry(self.frame, fg="black")
        apellido_parts = self.ultima_reserva['apellido'].split()
        self.apellido_entry.insert(0, ' '.join(apellido_parts))
        self.apellido_entry.pack()
        self.apellido_entry.bind("<FocusOut>", self.validar_y_actualizar_apellido)

        self.rut_label = Label(self.frame, text="Rut: ", font=('Arial', 12), bg='white')
        self.rut_label.pack()
        self.rut_entry = Entry(self.frame, fg="black")
        self.rut_entry.insert(0, self.ultima_reserva['rut'])
        self.rut_entry.pack()

        self.dias_label = Label(self.frame, text="Días: ", font=('Arial', 12), bg='white')
        self.dias_label.pack()
        self.dias_var = StringVar(self)
        self.dias_var.set(self.ultima_reserva['dias'])
        self.dias_option_menu = OptionMenu(self.frame, self.dias_var, *["1 día", "2 días", "3 días", "4 días"])
        self.dias_option_menu.pack()

        self.tipo_habitacion_label = Label(self.frame, text="Tipo de Habitación: ", font=('Arial', 12), bg='white')
        self.tipo_habitacion_label.pack()
        self.tipo_habitacion_var = StringVar(self)
        self.tipo_habitacion_var.set(self.ultima_reserva['tipo_habitacion'])
        self.tipo_habitacion_option_menu = OptionMenu(self.frame, self.tipo_habitacion_var, *["Habitación Normal $40.000", "Habitación Mediana $50.000", "Habitación Grande $70.000", "Suite $100.000"])
        self.tipo_habitacion_option_menu.pack()

        self.guardar_button = Button(self.frame, text="Guardar", font=('Arial', 10), command=self.Guardar)
        self.guardar_button.pack()

    # ... resto del código ...

    def validar_nombre(self, nombre):
        for char in nombre:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    def validar_y_actualizar_nombre(self, event):
        nombre = self.nombre_entry.get()
        if self.validar_nombre(nombre):
            self.ultima_reserva['nombre'] = nombre
        else:
            self.nombre_entry.delete(0, END)
            self.nombre_entry.insert(0, self.ultima_reserva['nombre'])
        
    def validar_apellido(self, apellido):
        for char in apellido:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    def validar_y_actualizar_apellido(self, event):
        apellido = self.apellido_entry.get()
        if self.validar_apellido(apellido):
            self.ultima_reserva['apellido'] = apellido
        else:
            self.apellido_entry.delete(0, END)
            self.apellido_entry.insert(0, self.ultima_reserva['apellido'])

    def validar_rut(self, rut):
        # Comprobar si el RUT contiene el "-"
        if "-" not in rut:
            return False

        # Separar el RUT en partes utilizando el "-"
        partes = rut.split("-")

        # Comprobar que el RUT tenga exactamente 2 partes
        if len(partes) != 2:
            return False

        # Obtener el número y el dígito verificador (DV)
        numero, dv_ingresado = partes

        # Remover los puntos del número
        numero = numero.replace(".", "")

        # Comprobar que el número tenga entre 7 y 8 caracteres
        if len(numero) < 7 or len(numero) > 8:
            return False

        # Comprobar que el DV sea un solo carácter
        if len(dv_ingresado) != 1:
            return False

        # Convertir el DV ingresado a mayúsculas
        dv_ingresado = dv_ingresado.upper()

        # Calcular el dígito verificador
        factores = [2, 3, 4, 5, 6, 7]
        suma = 0
        factor = 0
        for n in reversed(numero):
            suma += int(n) * factores[factor % len(factores)]
            factor += 1

        # Obtener el resto del módulo 11
        residuo = 11 - (suma % 11)

        # Convertir el residuo en el correspondiente dígito verificador
        if residuo == 11:
            dv_calculado = "0"
        elif residuo == 10:
            dv_calculado = "K"
        else:
            dv_calculado = str(residuo)

        # Comprobar si el dígito verificador calculado es igual al ingresado
        return dv_calculado == dv_ingresado

    def Guardar(self):
        if self.tipo_habitacion_var.get() == "Habitación":
            messagebox.showerror("Error", "Por favor seleccione un tipo de habitación.")
        elif not self.nombre_entry.get().strip():  # Verificar si el nombre está vacío
            messagebox.showerror("Error", "Por favor ingresar nombre/s.")
        elif not self.apellido_entry.get().strip():  # Verificar si el apellido está vacío
            messagebox.showerror("Error", "Por favor ingresar apellido/s.")
        elif not self.validar_nombre(self.nombre_entry.get()):
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
        elif not self.validar_apellido(self.apellido_entry.get()):
            messagebox.showerror("Error", "El apellido solo debe contener letras.")
        elif not self.validar_rut(self.rut_entry.get()):
            messagebox.showerror("Error", "Rut inválido. Verifique que el rut tenga el formato correcto y que el dígito verificador sea un solo carácter. Ejemplo: '19664581-0'.")
        else:
            # leer el archivo JSON
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

                # Actualizamos la reserva con los nuevos datos
                datos_json[-1]['nombre'] = self.nombre_entry.get()
                datos_json[-1]['apellido'] = self.apellido_entry.get()
                datos_json[-1]['rut'] = self.rut_entry.get()
                datos_json[-1]['dias'] = self.dias_var.get()
                datos_json[-1]['tipo_habitacion'] = self.tipo_habitacion_var.get()

                # Calculamos el nuevo total a pagar
                precio_habitacion = 0
                if datos_json[-1]['tipo_habitacion'] == "Habitación Normal $40.000":
                    precio_habitacion = 40000
                elif datos_json[-1]['tipo_habitacion'] == "Habitación Mediana $50.000":
                    precio_habitacion = 50000
                elif datos_json[-1]['tipo_habitacion'] == "Habitación Grande $70.000":
                    precio_habitacion = 70000
                elif datos_json[-1]['tipo_habitacion'] == "Suite $100.000":
                    precio_habitacion = 100000

            total_a_pagar = precio_habitacion * int(datos_json[-1]['dias'].split(" ")[0])
            datos_json[-1]['total_a_pagar'] = "{:,.0f}".format(total_a_pagar).replace(",", "#").replace(".", ",").replace("#", ".")

            # Escribir la lista completa de reservas de vuelta al archivo JSON
            with open("datos.json", "w") as archivo:
                json.dump(datos_json, archivo, indent=4)

            messagebox.showinfo("Modificar Reserva", "Reserva modificada exitosamente.")
            self.destroy()
            self.master.deiconify()


class cuartaVentana:
    def __init__(self, master):
        self.master = master
        self.ventana_4 = Toplevel(master)
        self.ventana_4.title('Hotel Luna')
        self.ventana_4.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.ventana_4.geometry("600x700")
        self.texto = Label(self.ventana_4, text='Comprobante', font=('Arial', 12), bg='white')
        self.texto.pack()

        self.frame = Frame(self.ventana_4, bg='white')
        self.frame.pack(fill=BOTH, expand=True)

        self.crear_widgets()
        self.mostrar_datos()

    def crear_widgets(self):
        self.text_widget = Text(self.frame, font=('Arial', 12), bg='white')
        self.text_widget.pack(fill=BOTH, expand=True)

        self.regresar_button = Button(self.frame, text="Regresar", font=('Arial', 10), command=self.Regresar)
        self.regresar_button.pack()

        self.cancelar_button = Button(self.frame, text="Cancelar Reserva", font=('Arial', 10), command=self.Cancelar)
        self.cancelar_button.pack()

        self.modificar_button = Button(self.frame, text="Modificar", font=('Arial', 10), command=self.Modificar)
        self.modificar_button.pack()

        self.buscar_button = Button(self.frame, text="Buscar", font=('Arial', 10), command=self.mostrar_ventana_buscar)
        self.buscar_button.pack()

    def Regresar(self):
        self.ventana_4.withdraw()


    def Cancelar(self):

        try:
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

            if not datos_json:
                messagebox.showinfo("Cancelar Reserva", "No hay reservas existentes.")

            datos_json.pop()

            with open("datos.json", "w") as archivo:
                json.dump(datos_json, archivo, indent=4)

            messagebox.showinfo("Cancelar Reserva", "Reserva cancelada exitosamente.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontraron datos de reservas.")
        self.ventana_4.destroy()

    def Modificar(self):
        try:
            # Abrimos el archivo JSON y lo cargamos
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

            if not datos_json:
                messagebox.showinfo("Modificar Reserva", "No hay reservas existentes.")
                return
            # Obtenemos la última reserva
            ultima_reserva = datos_json[-1]

            # Creamos una ventana para modificar la reserva
            self.ventana_4.withdraw()
            ventana_modificar = Modificar_4(self.master, ultima_reserva)

        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontraron datos de reservas.")


    def mostrar_datos(self):
        try:
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)
                for dato in datos_json:
                    self.text_widget.insert(END, f"Nombre/s: {dato['nombre']}\n")
                    self.text_widget.insert(END, f"Apellido/s: {dato['apellido']}\n")
                    self.text_widget.insert(END, f"Rut: {dato['rut']}\n")
                    self.text_widget.insert(END, f"Días: {dato['dias']}\n")
                    self.text_widget.insert(END, f"Tipo de Habitación: {dato['tipo_habitacion']}\n\n")
                    self.text_widget.insert(END, f"Total a Pagar: ${dato['total_a_pagar']}\n\n")
        except FileNotFoundError:
            self.text_widget.insert(END, "No se encontraron datos de reservas.")

    def mostrar_ventana_buscar(self):
        ventana_buscar = BuscarVentana1(self)

    def buscar_reserva(self, nombre_reserva, apellido_reserva):
        try:
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

            self.ultima_reserva_coincidencia = self.buscar_reserva_ultima(datos_json, nombre_reserva, apellido_reserva)

            if self.ultima_reserva_coincidencia:
                QuintaVentana(self.master, self.ultima_reserva_coincidencia)
                self.ventana_4.withdraw()
            else:
                messagebox.showinfo("Buscar Reserva", f"No se encontró ninguna reserva a nombre de {nombre_reserva} {apellido_reserva}.")
        
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontraron datos de reservas.")

    def buscar_reserva_ultima(self, datos_json, nombre_reserva, apellido_reserva):
        ultima_reserva_coincidencia = None
        for dato in reversed(datos_json):
            if dato['nombre'] == nombre_reserva and dato['apellido'] == apellido_reserva:
                ultima_reserva_coincidencia = dato
                break
        return ultima_reserva_coincidencia

class Modificar_4(Toplevel):
    def __init__(self, master, ultima_reserva):
        super().__init__(master)
        self.title('Modificar Reserva')
        self.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.geometry("600x700")

        self.ultima_reserva = ultima_reserva

        self.frame = Frame(self, bg='white')
        self.frame.pack(fill=BOTH, expand=True)

        self.crear_widgets()

    def crear_widgets(self):
        # Agregamos los campos para modificar la reserva
        self.nombre_label = Label(self.frame, text="Nombre/s: ", font=('Arial', 12), bg='white')
        self.nombre_label.pack()
        self.nombre_entry = Entry(self.frame, fg="black")
        nombres_parts = self.ultima_reserva['nombre'].split()
        self.nombre_entry.insert(0, ' '.join(nombres_parts))
        self.nombre_entry.pack()
        self.nombre_entry.bind("<FocusOut>", self.validar_y_actualizar_nombre)

        self.apellido_label = Label(self.frame, text="Apellido/s: ", font=('Arial', 12), bg='white')
        self.apellido_label.pack()
        self.apellido_entry = Entry(self.frame, fg="black")
        apellido_parts = self.ultima_reserva['apellido'].split()
        self.apellido_entry.insert(0, ' '.join(apellido_parts))
        self.apellido_entry.pack()
        self.apellido_entry.bind("<FocusOut>", self.validar_y_actualizar_apellido)

        self.rut_label = Label(self.frame, text="Rut: ", font=('Arial', 12), bg='white')
        self.rut_label.pack()
        self.rut_entry = Entry(self.frame, fg="black")
        self.rut_entry.insert(0, self.ultima_reserva['rut'])
        self.rut_entry.pack()

        self.dias_label = Label(self.frame, text="Día/s: ", font=('Arial', 12), bg='white')
        self.dias_label.pack()
        self.dias_var = StringVar(self)
        self.dias_var.set(self.ultima_reserva['dias'])
        self.dias_option_menu = OptionMenu(self.frame, self.dias_var, *["1 Día", "2 Días", "3 Días", "4 Días"])
        self.dias_option_menu.pack()

        self.tipo_habitacion_label = Label(self.frame, text="Tipo de Habitación: ", font=('Arial', 12), bg='white')
        self.tipo_habitacion_label.pack()
        self.tipo_habitacion_var = StringVar(self)
        self.tipo_habitacion_var.set(self.ultima_reserva['tipo_habitacion'])
        self.tipo_habitacion_option_menu = OptionMenu(self.frame, self.tipo_habitacion_var, *["Habitación Normal $40.000", "Habitación Mediana $50.000", "Habitación Grande $70.000", "Suite $100.000"])
        self.tipo_habitacion_option_menu.pack()

        self.guardar_button = Button(self.frame, text="Guardar", font=('Arial', 10), command=self.Guardar)
        self.guardar_button.pack()

    def validar_nombre(self, nombre):
        for char in nombre:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    def validar_y_actualizar_nombre(self, event):
        nombre = self.nombre_entry.get()
        if self.validar_nombre(nombre):
            self.ultima_reserva['nombre'] = nombre
        else:
            self.nombre_entry.delete(0, END)
            self.nombre_entry.insert(0, self.ultima_reserva['nombre'])
        
    def validar_apellido(self, apellido):
        for char in apellido:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    def validar_y_actualizar_apellido(self, event):
        apellido = self.apellido_entry.get()
        if self.validar_apellido(apellido):
            self.ultima_reserva['apellido'] = apellido
        else:
            self.apellido_entry.delete(0, END)
            self.apellido_entry.insert(0, self.ultima_reserva['apellido'])
        
    def validar_rut(self, rut):
        # Comprobar si el RUT contiene el "-"
        if "-" not in rut:
            return False

        # Separar el RUT en partes utilizando el "-"
        partes = rut.split("-")

        # Comprobar que el RUT tenga exactamente 2 partes
        if len(partes) != 2:
            return False

        # Obtener el número y el dígito verificador (DV)
        numero, dv_ingresado = partes

        # Remover los puntos del número
        numero = numero.replace(".", "")

        # Comprobar que el número tenga entre 7 y 8 caracteres
        if len(numero) < 7 or len(numero) > 8:
            return False

        # Comprobar que el DV sea un solo carácter
        if len(dv_ingresado) != 1:
            return False

        # Convertir el DV ingresado a mayúsculas
        dv_ingresado = dv_ingresado.upper()

        # Calcular el dígito verificador
        factores = [2, 3, 4, 5, 6, 7]
        suma = 0
        factor = 0
        for n in reversed(numero):
            suma += int(n) * factores[factor % len(factores)]
            factor += 1

        # Obtener el resto del módulo 11
        residuo = 11 - (suma % 11)

        # Convertir el residuo en el correspondiente dígito verificador
        if residuo == 11:
            dv_calculado = "0"
        elif residuo == 10:
            dv_calculado = "K"
        else:
            dv_calculado = str(residuo)

        # Comprobar si el dígito verificador calculado es igual al ingresado
        return dv_calculado == dv_ingresado

    def Guardar(self):
        if self.tipo_habitacion_var.get() == "Habitación":
            messagebox.showerror("Error", "Por favor seleccione un tipo de habitación.")
        elif not self.nombre_entry.get().strip():  # Verificar si el nombre está vacío
            messagebox.showerror("Error", "Por favor ingresar nombre/s.")
        elif not self.apellido_entry.get().strip():  # Verificar si el apellido está vacío
            messagebox.showerror("Error", "Por favor ingresar apellido/s.")
        elif not self.validar_nombre(self.nombre_entry.get()):
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
        elif not self.validar_apellido(self.apellido_entry.get()):
            messagebox.showerror("Error", "El apellido solo debe contener letras.")
        elif not self.validar_rut(self.rut_entry.get()):
            messagebox.showerror("Error", "Rut inválido. Verifique que el rut tenga el formato correcto y que el dígito verificador sea un solo carácter. Ejemplo: '19664581-0'.")
        else:
            # leer el archivo JSON
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

                # Actualizamos la reserva con los nuevos datos
                datos_json[-1]['nombre'] = self.nombre_entry.get()
                datos_json[-1]['apellido'] = self.apellido_entry.get()
                datos_json[-1]['rut'] = self.rut_entry.get()
                datos_json[-1]['dias'] = self.dias_var.get()
                datos_json[-1]['tipo_habitacion'] = self.tipo_habitacion_var.get()

                # Calculamos el nuevo total a pagar
                precio_habitacion = 0
                if datos_json[-1]['tipo_habitacion'] == "Habitación Normal $40.000":
                    precio_habitacion = 40000
                elif datos_json[-1]['tipo_habitacion'] == "Habitación Mediana $50.000":
                    precio_habitacion = 50000
                elif datos_json[-1]['tipo_habitacion'] == "Habitación Grande $70.000":
                    precio_habitacion = 70000
                elif datos_json[-1]['tipo_habitacion'] == "Suite $100.000":
                    precio_habitacion = 100000

            total_a_pagar = precio_habitacion * int(datos_json[-1]['dias'].split(" ")[0])
            datos_json[-1]['total_a_pagar'] = "{:,.0f}".format(total_a_pagar).replace(",", "#").replace(".", ",").replace("#", ".")

            # Escribir la lista completa de reservas de vuelta al archivo JSON
            with open("datos.json", "w") as archivo:
                json.dump(datos_json, archivo, indent=4)

            messagebox.showinfo("Modificar Reserva", "Reserva modificada exitosamente.")
            self.destroy()
    

class BuscarVentana1:
    def __init__(self, cuarta_ventana):
        self.cuarta_ventana = cuarta_ventana

        self.ventana_buscar = Toplevel(self.cuarta_ventana.ventana_4)
        self.ventana_buscar.title("Buscar Reserva")
        self.ventana_buscar.geometry("300x150")
        self.ventana_buscar.focus_force()


        self.frame = Frame(self.ventana_buscar)
        self.frame.pack()

        self.nombre_label = Label(self.frame, text="Nombre/s y apellido/s de la reserva:", font=('Arial', 10))
        self.nombre_label.pack()

        self.nombre2_label = Label(self.frame, text="Nombre/s:", font=('Arial', 10))
        self.nombre2_label.pack()
        self.nombre_entry = Entry(self.frame, font=('Arial', 10))
        self.nombre_entry.pack()

        self.apellido2_label = Label(self.frame, text="Apellido/s:", font=('Arial', 10))
        self.apellido2_label.pack()
        self.apellido_entry = Entry(self.frame, font=('Arial', 10))
        self.apellido_entry.pack()

        buscar_button = Button(self.frame, text="Buscar", font=('Arial', 10), command=self.buscar_reserva)
        buscar_button.pack()

    def buscar_reserva(self):
        nombre_reserva = self.nombre_entry.get()
        apellido_reserva = self.apellido_entry.get()
        if not nombre_reserva.strip():  # Verificar si el nombre está vacío
            messagebox.showerror("Error", "Por favor ingresar nombre/s.")
        elif not apellido_reserva.strip():  # Verificar si el apellido está vacío
            messagebox.showerror("Error", "Por favor ingresar apellido/s.")
        else:
            self.cuarta_ventana.buscar_reserva(nombre_reserva,apellido_reserva)
            self.ventana_buscar.destroy()

class BuscarVentana2:
    def __init__(self, tercera_ventana):
        self.cuarta_ventana = tercera_ventana

        self.ventana_buscar = Toplevel(self.cuarta_ventana.ventana_3)
        self.ventana_buscar.title("Buscar Reserva")
        self.ventana_buscar.geometry("300x150")

        self.frame = Frame(self.ventana_buscar)
        self.frame.pack()

        self.nombre_label = Label(self.frame, text="Nombre/s y apellido/s de la Reserva:", font=('Arial', 10))
        self.nombre_label.pack()

        self.nombre_entry = Entry(self.frame,text= "Nombre/s" ,font=('Arial', 10))
        self.nombre_entry.pack()

        self.apellido_entry = Entry(self.frame,text="Apellido/s", font=('Arial', 10))
        self.apellido_entry.pack()

        buscar_button = Button(self.frame, text="Buscar", font=('Arial', 10), command=self.buscar_reserva)
        buscar_button.pack()

    def buscar_reserva(self):
        nombre_reserva = self.nombre_entry.get()
        apellido_reserva = self.apellido_entry.get()
        if not nombre_reserva.strip():  # Verificar si el nombre está vacío
            messagebox.showerror("Error", "Por favor ingresar nombre/s")
        elif not apellido_reserva.strip():  # Verificar si el apellido está vacío
            messagebox.showerror("Error", "Por favor ingresar apellido/s")
        else:
            self.cuarta_ventana.buscar_reserva(nombre_reserva,apellido_reserva)
            self.ventana_buscar.destroy()

class QuintaVentana:
    def __init__(self, master, datos_reserva):
        self.master = master
        self.datos_reserva = datos_reserva
        
        self.ventana_5 = Toplevel(master)
        self.ventana_5.title('Detalles de Reserva')
        self.ventana_5.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.ventana_5.geometry("600x400")
        self.ventana_5.focus_force()

        self.frame = Frame(self.ventana_5, bg='white')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.mostrar_datos()

        self.cancelar_button = Button(self.frame, text="Cancelar Reserva", font=('Arial', 10), command=self.cancelar_reserva)
        self.cancelar_button.pack()

        self.regresar_button = Button(self.frame, text="Regresar", font=('Arial', 10), command=self.regresar)
        self.regresar_button.pack()

    def mostrar_datos(self):
        nombre_label = Label(self.frame, text=f"Nombre/s: {self.datos_reserva['nombre']}", font=('Arial', 12), bg='white')
        nombre_label.pack()
        apellido_label = Label(self.frame, text=f"Apellido/s: {self.datos_reserva['apellido']}", font=('Arial', 12), bg='white')
        apellido_label.pack()
        rut_label = Label(self.frame, text=f"Rut: {self.datos_reserva['rut']}", font=('Arial', 12), bg='white')
        rut_label.pack()
        dias_label = Label(self.frame, text=f"Días: {self.datos_reserva['dias']}", font=('Arial', 12), bg='white')
        dias_label.pack()
        tipo_habitacion_label = Label(self.frame, text=f"Tipo de Habitación: {self.datos_reserva['tipo_habitacion']}", font=('Arial', 12), bg='white')
        tipo_habitacion_label.pack()
        total_label = Label(self.frame, text=f"Total a Pagar: ${self.datos_reserva['total_a_pagar']}", font=('Arial', 12), bg='white')
        total_label.pack()

    def cancelar_reserva(self):
        try:
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

            # Obtain the index of the reservation to be deleted
            reservation_index = next((index for index, reservation in enumerate(datos_json) if reservation == self.datos_reserva), None)

            if reservation_index is not None:
                # Remove the reservation from the list
                del datos_json[reservation_index]

                with open("datos.json", "w") as archivo:
                    json.dump(datos_json, archivo, indent=4)

                messagebox.showinfo("Cancelar Reserva.", "Reserva cancelada exitosamente.")
                self.ventana_5.destroy()

        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontraron datos de reservas.")

    def regresar(self):
        self.ventana_5.destroy()

class SextaVentana:
    def __init__(self, master, datos_reserva):
        self.master = master
        self.datos_reserva = datos_reserva
        
        self.ventana_6 = Toplevel(master)
        self.ventana_6.title('Detalles de Reserva')
        self.ventana_6.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.ventana_6.geometry("600x400")
        self.ventana_6.focus_force()

        self.frame = Frame(self.ventana_6, bg='white')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.mostrar_datos()

        self.cancelar_button = Button(self.frame, text="Cancelar Reserva", font=('Arial', 10), command=self.cancelar_reserva)
        self.cancelar_button.pack()

        self.regresar_button = Button(self.frame, text="Regresar", font=('Arial', 10), command=self.regresar)
        self.regresar_button.pack()

    def mostrar_datos(self):
        nombre_label = Label(self.frame, text=f"Nombre/s: {self.datos_reserva['nombre']}", font=('Arial', 12), bg='white')
        nombre_label.pack()
        apellido_label = Label(self.frame, text=f"Apellido/s: {self.datos_reserva['apellido']}", font=('Arial', 12), bg='white')
        apellido_label.pack()
        rut_label = Label(self.frame, text=f"Rut: {self.datos_reserva['rut']}", font=('Arial', 12), bg='white')
        rut_label.pack()
        dias_label = Label(self.frame, text=f"Día/s: {self.datos_reserva['dias']}", font=('Arial', 12), bg='white')
        dias_label.pack()
        tipo_habitacion_label = Label(self.frame, text=f"Tipo de Habitación: {self.datos_reserva['tipo_habitacion']}", font=('Arial', 12), bg='white')
        tipo_habitacion_label.pack()
        total_label = Label(self.frame, text=f"Total a Pagar: ${self.datos_reserva['total_a_pagar']}", font=('Arial', 12), bg='white')
        total_label.pack()

    def cancelar_reserva(self):
        try:
            with open("datos.json", "r") as archivo:
                datos_json = json.load(archivo)

            # Obtain the index of the reservation to be deleted
            reservation_index = next((index for index, reservation in enumerate(datos_json) if reservation == self.datos_reserva), None)

            if reservation_index is not None:
                # Remove the reservation from the list
                del datos_json[reservation_index]

                with open("datos.json", "w") as archivo:
                    json.dump(datos_json, archivo, indent=4)

                messagebox.showinfo("Cancelar Reserva.", "Reserva cancelada exitosamente.")
                self.ventana_6.destroy()
                self.master.deiconify()

        except FileNotFoundError:
            messagebox.showerror("Error.", "No se encontraron datos de reservas.")

    def regresar(self):
        self.ventana_6.destroy()
        self.master.deiconify()

if __name__ == '__main__':
    ventana = Tk()
    app = PrimeraVentana(ventana)
    ventana.mainloop()
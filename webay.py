#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import subprocess
import platform
import os
import re
from Tkinter import * 
from Graphics import * 


def evaluar(status, letra):

	if(letra >= '0' and letra <= '9'):
		return 'N' #Cuando es un numero

	if( status == 'A'):

		if (letra == 'w' or letra == 'W'):
			return 'B'

		elif(letra == 'e' or letra == 'E'):
			return 'E'

		else:
			return 'A'

	elif(status == 'B'):

		if(letra == 'e' or letra == 'E'):
			return 'C'

		elif(letra == 'W' or letra == 'W'):
			return 'B'

		else: 
			return 'A'


	elif(status == 'C'):

		if(letra == 'B' or letra == 'b'):
			return 'D'

		elif(letra == 'w' or letra == 'W'):
			return 'B'

		elif(letra == 'e' or letra == 'E'):
			return 'E'

		else: return 'A'


	elif(status == 'D'):

		if(letra == 'A' or letra == 'a'):
			return 'G'

		elif(letra == 'e' or letra == 'E'):
			return 'E'

		elif(letra == 'w' or letra == 'W'):
			return 'B'

		else: return 'A'


	elif(status == 'E'):

		if(letra == 'B' or letra == 'b'):
			return 'F'

		elif(letra == 'e' or letra == 'E'):
			return 'E'

		elif(letra == 'w' or letra == 'W'):
			return 'B'

		else: return 'A'

	elif(status == 'F'):

		if(letra == 'A' or letra == 'a'):
			return 'G'

		elif(letra == 'e' or letra == 'E'):
			return 'E'

		elif(letra == 'w' or letra == 'W'):
			return 'B'

		else: return 'A'


	elif(status == 'G'):

		if(letra == 'y' or letra == 'Y'):
			return 'H'

		elif(letra == 'e' or letra == 'E'):
			return 'E'

		elif(letra == 'w' or letra == 'W'):
			return 'B'

		else: return 'A'


	elif(status == 'H'):

		if(letra == 'w' or letra == 'W'):
			return 'B'

		elif(letra == 'e' or letra == 'E'):
			return 'E'

		else: return 'A'


	else: 
		return 'A'

def evaluar_cadena(cadena, modo, linea):

	status = 'A'
	palabra = 1

	historial = open("historial.txt", "a")

	if(modo): #Modo uno, evalua solo una cadena
		encontrados = open("Encontrados.txt", "w")

	else: #Evalua multiples cadenas
		encontrados = open("Encontrados.txt", "a")

	cad = re.findall('\w+', cadena)

	for word in (cad):
		historial = open("historial.txt", "a")
		historial.write("\n" + word + "\n\n")

 		palabra+=1

		for l in word:

 			est_ant = status
			status = evaluar(status, l)
			rec_historial(l, status, est_ant)

			
			if status == 'D':

				if(modo):
					print("Se encontró \'web\' en la palabra " + str(palabra))
					encontrados.write("Se encontró \'web\' en la palabra " + str(palabra) + "\n")

				else:
					print("Se encontró \'web\' en la palabra " + str(palabra) + " de la linea " + str(linea))
					encontrados.write("Se encontró \'web\' en la palabra " + str(palabra) + "\n")

			elif status == 'H':

				if(modo):
					print("Se encontro \'ebay\' en la palabra " + str(palabra))
					encontrados.write("Se encontró \'ebay\' en la palabra " + str(palabra) + "\n")

				else:
					print("Se encontro \'ebay\' en la palabra " + str(palabra) + " de la linea " + str(linea))
					encontrados.write("Se encontró la palabra \'ebay\' en la palabra " + str(palabra) + "de la línea" + str(linea) + "\n")


	historial.write("\n\n")
	encontrados.close()

def evaluar_archivo(nombre):

	linea = 0

	try:
		archivo = open(nombre, "r")

	except:
		os.system('clear')
		raw_input("Error archivo no encontrado")
		os.system('clear')
		return

	crear = open("Encontrados.txt", "w+")

	leer = archivo.readline()

	while(leer != ""):
		linea+=1
		evaluar_cadena(leer, 0, linea)
		leer = archivo.readline()

	crear.close()
	archivo.close()

def arco(palabra):
	linea = 0
	evaluar_cadena(palabra,1,linea)

	#Crear ventana 
	tablero = GraphWin("Webay", 900, 600)
	tablero.setBackground(color_rgb(0,0,0))
	

	#Circulos
	A = Circle(Point(80, 270), 30)
	B = Circle(Point(160, 170), 30)
	C = Circle(Point(260, 170), 30)
	D = Circle(Point(360, 170), 30)
	D2 = Circle(Point(360, 170), 35)
	E = Circle(Point(160, 370), 30)
	F = Circle(Point(260, 370), 30)
	G = Circle(Point(360, 370), 30)
	H = Circle(Point(460, 370), 30)
	H2 = Circle(Point(460, 370), 35)

	A.setFill(color_rgb(0,122,255))
	B.setFill(color_rgb(0,122,255))
	C.setFill(color_rgb(0,122,255))
	D.setFill(color_rgb(0,122,255))
	D2.setOutline("white")
	D2.setFill("white")
	E.setFill(color_rgb(0,122,255))
	F.setFill(color_rgb(0,122,255))
	G.setFill(color_rgb(0,122,255))
	H.setFill(color_rgb(0,122,255))
	H.setOutline("white")
	H2.setFill(color_rgb(255,255,255))

	#Lineas
	LBC = Line (Point(190, 165), Point(230, 165))
	LCB = Line (Point(230, 175), Point(190, 175))
	LCD = Line (Point(288, 170), Point(330, 170))
	LEF = Line (Point(188, 365), Point(232, 365))
	LFE = Line (Point(232, 375), Point(188, 375))
	LFG = Line (Point(288,365), Point(330, 365))
	LGH = Line (Point(388, 365), Point(429, 365))

	LBC.setFill("white")
	LCB.setFill("white")
	LCD.setFill("white")
	LEF.setFill("white")
	LFE.setFill("white")
	LFG.setFill("white")
	LGH.setFill("white")

	#Lineas cruzadas 
	CLAB = Line(Point(100, 249), Point(140, 190))
	CLAE = Line(Point(94, 298),  Point(140, 350))
	CLEF = Line(Point(340, 192), Point(180, 344))
	CLCE = Line(Point(240, 192), Point(165, 340))
	CLEB = Line(Point(160, 340), Point(160,197))
	CLFB = Line(Point(260, 340), Point(170, 198))
	CLGB = Line(Point(340 ,350), Point(175,196))
	CLHB = Line(Point(435, 350), Point(185, 192))
	CLBA = Line(Point(130, 180), Point(80, 240))

	CLAB.setFill("white")
	CLAE.setFill("white")
	CLEF.setFill("white")
	CLCE.setFill("white")
	CLEB.setFill("white")
	CLFB.setFill("white")
	CLGB.setFill("white")
	CLHB.setFill("white")
	CLBA.setFill("white")


	#Etiquetas
	TA = Text(Point(80, 270), "A")
	TB = Text(Point(160, 170), "B")
	TC  = Text(Point(260, 170), "C")
	TD = Text(Point(360, 170), "D")
	TE = Text(Point(160, 370), "E")
	TF = Text(Point(260, 370), "F")
	TG = Text(Point(360, 370), "G")
	TH = Text(Point(460, 370), "H")



	TLAB = Text(Point(110,220), "w")
	TLEB = Text(Point(150, 235), "w")
	TLFB = Text(Point(180, 235), "w")
	TLGB = Text(Point(192, 220), "w")
	TLHB = Text(Point(200, 210), "w")
	TLAE = Text(Point(120, 310), "e")

	TCA = Text(Point(30,235), "Σ-e-w")
	TLEF = Text(Point(210,355), "b")
	TLFE = Text(Point(210,385), "e")

	TLFG = Text(Point(310,355), "a")
	TLGH = Text(Point(410,355), "y")

	TLCE = Text(Point(173, 310), "e")
	TLDE = Text(Point(205, 310), "e")

	TLBC = Text(Point(208,160), "e")
	TLCB = Text(Point(208,180), "w")

	TLCD = Text(Point(308,155), "b")

	CLBA = Line(Point(130, 180), Point(80, 240))
	TCLBA = Text(Point(80,210), "Σ-e-w")
	CLBA.setArrow("last")


	#COLORES
	TA.setFill("white")
	TB.setFill("white")
	TC.setFill("white")
	TD.setFill("white")
	TE.setFill("white")
	TF.setFill("white")
	TG.setFill("white")
	TH.setFill("white")

	TLAB.setFill("white")
	TLEB.setFill("white")
	TLFB.setFill("white")
	TLGB.setFill("white")
	TLHB.setFill("white")
	TLAE.setFill("white")
	TCA.setFill("white")
	TLEF.setFill("white")
	TLFE.setFill("white")
	TLFG.setFill("white")
	TLGH.setFill("white")
	TLCE.setFill("white")
	TLDE.setFill("white")
	TLBC.setFill("white")
	TLCB.setFill("white")
	TLCD.setFill("white")
	CLBA.setFill("white")
	TCLBA.setFill("white")
	#Arcos Conectores------------------------------------------------------------

	#Para A
	#A = Circle(Point(80, 270), 30)

	start_line = Line(Point(20, 325), Point(70, 325))
	start_text = Text(Point(40,315),"Start")
	start_line.setArrow("last")
	start_line.draw(tablero)
	start_text.draw(tablero)
	tablero.create_arc(20, 245, 70, 295,  start = 60, extent = 205, style = "arc", outline = "white")
	start_line.setFill("white")
	start_text.setFill("white")

	#Para B---------------------
	#B = Circle(Point(160, 170), 30)
	tablero.create_arc(115, 120, 163, 170,  outline = "white", start = 15, extent = 205, style = "arc")
	CB = Line(Point(125, 160), Point(127, 160))
	CB.setArrow("last")
	CB.setFill("white")
	CB.draw(tablero)
	CTB = Text(Point(120, 120), "w")
	CTB.draw(tablero)
	CTB.setFill("white")

	#Para C---------------------
	#C = Circle(Point(260, 170), 30)
	tablero.create_arc(260, 60, 45, 270, start = 14,outline = "white", extent = 209, style = "arc")
	CA = Line(Point(79, 235), Point(82, 235))
	CA.draw(tablero)
	CA.setFill("white")
	CA.setArrow("last")
	TCLCA = Text(Point(65, 80), "Σ-b-e-w")
	TCLCA.draw(tablero)
	TCLCA.setFill("white")

	#Para D---------------------
	#D = Circle(Point(360, 170), 30)
	tablero.create_arc(360, 15, 15, 270, start = 0, outline = "white", extent = 220, style = "arc")
	DA = Line(Point(60, 225), Point(63, 225))
	DA.draw(tablero)
	DA.setFill("white")
	DA.setArrow("last")
	TCLDA = Text(Point(50, 40), "Σ-a-e-w")
	TCLDA.draw(tablero)
	TCLDA.setFill("white")
	tablero.create_arc(360, 110, 160, 280, start = 35,outline = "white", extent = 105, style = "arc")
	DB = Line(Point(181, 140), Point(177, 140))
	DB.setArrow("last")
	DB.setFill("white")
	DB.draw(tablero)
	TCLDB = Text(Point(260, 100), "w")
	TCLDB.draw(tablero)
	TCLDB.setFill("white")
	CLDG = Line(Point(360, 200),Point(360, 340))
	CLDG.draw(tablero)
	CLDG.setFill("white")
	CLDG.setArrow("last")
	TCLDB = Text(Point(370, 270), "a")
	TCLDB.draw(tablero)
	TCLDB.setFill("white")

	#Para E--------------------------------------
	#E = Circle(Point(160, 370), 30)
	tablero.create_arc(120, 345, 170, 395, start = 92, extent = 175, outline = "white", style = "arc")
	EE = Line(Point(140, 395), Point(143, 395))
	EE.draw(tablero)
	EE.setFill("white")
	EE.setArrow("last")
	TEE = Text(Point(110, 370), "e")
	TEE.draw(tablero)
	TEE.setFill("white")
	CLEA = Line(Point(130, 350), Point(84, 298))
	CLEA.setArrow("last")
	CLEA.setFill("white")
	CLEA.draw(tablero)
	TEA = Text(Point(105, 340), "Σ-w-e")
	TEA.draw(tablero)
	TEA.setFill("white")


	#Para F--------------------------------------
	CLFA = Line(Point(260, 340), Point(110, 270))
	CLFA.draw(tablero)
	CLFA.setFill("white")
	CLFA.setArrow("last")
	TCLFA = Text(Point(140, 270), "Σ-w-e")
	TCLFA.draw(tablero)
	TCLFA.setFill("white")

	#Para G
	CLGA = Line( Point(335, 348), Point(110, 270))
	CLGA.draw(tablero)
	CLGA.setArrow("last")
	CLGA.setFill("white")

	#Para H
	#H = Circle(Point(460, 370), 30)

	CLHA = Line(Point(433, 350), Point(110, 270))
	CLHA.draw(tablero)
	CLHA.setArrow("last")
	tablero.create_arc(460, 15, 160, 395, start = 0, outline = "white", extent = 360, style = "arc")
	CLHA.setFill("white")


	##-------ARCOS SUBTERRANEÓS 

	#Arco FA
	#F = Circle(Point(260, 370), 30)
	#A = Circle(Point(80, 270), 30)
	#E = Circle(Point(160, 370), 30)
	#G = Circle(Point(360, 370), 30)
	#H = Circle(Point(460, 370), 30)




	tablero.create_arc(260, 410, 60, 270, start = 360, outline = "white", extent = -205, style = "arc")
	TDE_FA = Text(Point(230,405), "Σ-a-e-w")
	TDE_FA.setFill("white")
	TDE_FA.draw(tablero)
	Flecha_FA = Line(Point(70,300), Point(70, 310))
	Flecha_FA.setFill("white")
	Flecha_FA.setArrow("first")
	Flecha_FA.draw(tablero)


	tablero.create_arc(360, 440, 55, 260, start = 360, outline = "white", extent = -205, style = "arc")
	TDE_GA = Text(Point(190,430), "Σ-e-w-y")
	TDE_GA.setFill("White")
	TDE_GA.draw(tablero)

	tablero.create_arc(460, 440, 50, 250, start = 360, outline = "white", extent = -205, style = "arc")
	TDE_GA = Text(Point(420,420), "Σ-e-w")
	TDE_GA.setFill("White")
	TDE_GA.draw(tablero)

	#--------------------
	tablero.create_arc(460, 500, 160, 320, start = 360, outline = "white", extent = -205, style = "arc")
	TDE_HE = Text(Point(440,480), "e")
	TDE_HE.setFill("White")
	TDE_HE.draw(tablero)

	tablero.create_arc(360, 500, 160, 290, start = 360, outline = "white", extent = -205, style = "arc")
	TDE_HE = Text(Point(340,480), "e")
	TDE_HE.setFill("White")
	TDE_HE.draw(tablero)

	tablero.create_arc(160, 500, 260, 290, start = 360, outline = "white", extent = -205, style = "arc")
	TDE_FE = Text(Point(250,480), "e")
	TDE_FE.setFill("White")
	TDE_FE.draw(tablero)

	FLECHA_SUB = Line(Point(160, 400), Point(160, 430))
	FLECHA_SUB.setFill("white")
	FLECHA_SUB.setArrow("first")






	#-----------------------DIBUJAR-----------------------s
	A.draw(tablero)
	B.draw(tablero)
	C.draw(tablero)
	D2.draw(tablero)
	D.draw(tablero)
	E.draw(tablero)
	F.draw(tablero)
	G.draw(tablero)
	H2.draw(tablero)
	H.draw(tablero)


	#Lineas
	LBC.draw(tablero)
	LCD.draw(tablero)
	LEF.draw(tablero)
	LFG.draw(tablero)
	LGH.draw(tablero)
	LFE.draw(tablero)
	LCB.draw(tablero)

	#Lineas conectoras
	CLAB.draw(tablero)
	CLAE.draw(tablero)
	CLEF.draw(tablero)
	CLCE.draw(tablero)
	CLEB.draw(tablero)
	CLFB.draw(tablero)
	CLGB.draw(tablero)
	CLHB.draw(tablero)
	CLBA.draw(tablero)


	#Flechas
	LBC.setArrow("last")
	LCD.setArrow("last")
	LEF.setArrow("last")
	LFG.setArrow("last")
	LGH.setArrow("last")
	CLAB.setArrow("last")
	CLAE.setArrow("last")
	CLEF.setArrow("last")
	CLCE.setArrow("last")
	CLEB.setArrow("last")
	CLFB.setArrow("last")
	CLGB.setArrow("last")
	CLHB.setArrow("last")
	LGH.setArrow("last")
	LFE.setArrow("last")
	LCB.setArrow("last")
	#Arcos

	#TAGS
	TA.draw(tablero)
	TB.draw(tablero)
	TC.draw(tablero)
	TD.draw(tablero)
	TE.draw(tablero)
	TF.draw(tablero)
	TG.draw(tablero)
	TH.draw(tablero)
	TLAB.draw(tablero)
	TLEB.draw(tablero)
	TLFB.draw(tablero)
	TLGB.draw(tablero)
	TLHB.draw(tablero)
	TCA.draw(tablero)
	TLEF.draw(tablero)
	TLFG.draw(tablero)
	TLGH.draw(tablero)
	TLCE.draw(tablero)
	TLDE.draw(tablero)
	TLAE.draw(tablero)
	TLBC.draw(tablero)
	TLCD.draw(tablero)
	TCLBA.draw(tablero)
	TLCB.draw(tablero)


	FLECHA_SUB.draw(tablero)

	#Cerrar programa
	TLFE.draw(tablero)


	#Animacion

	if(palabra != "NO"):
		status = 'A'

		A.setFill(color_rgb(255,149,0))
		time.sleep(1)
		A.setFill(color_rgb(0,122,255))

		Evaluando = Text(Point(650, 120), "Ahora evaluando...")
		Evaluando.setFill("white")
		Evaluando.setSize(36)
		Evaluando.draw(tablero)
		Palabra = Text(Point(640,220), palabra)
		Palabra.setFill("white")
		Palabra.setSize(36)
		Palabra.draw(tablero)
		time.sleep(0.5)
		for i in palabra:

			status = evaluar(status, i)

			if(status == 'A' ):
				A.setFill(color_rgb(255,149,0))
				time.sleep(1)
				A.setFill(color_rgb(0,122,255))


				i=0
				j=0

				while(i != 122 and j == 255):
					print(i)
					A.setFill(color_rgb(0,i,j))
					if i != 122:
						i+=1
					j+=1

					time.sleep(1)


			elif(status == 'B'):
				B.setFill(color_rgb(255,149,0))
				time.sleep(1)
				B.setFill(color_rgb(0,122,255))
			
			elif(status == 'C'):
				C.setFill(color_rgb(255,149,0))
				time.sleep(1)
				C.setFill(color_rgb(0,122,255))

			elif(status == 'D'):
				D.setFill(color_rgb(255,149,0))
				time.sleep(1)
				D.setFill(color_rgb(0,122,255))

			elif (status == 'E'):
				E.setFill(color_rgb(255,149,0))
				time.sleep(1)
				E.setFill(color_rgb(0,122,255))

			elif (status == 'F'):
				F.setFill(color_rgb(255,149,0))
				time.sleep(1)
				F.setFill(color_rgb(0,122,255))

			elif(status == 'G'):
				G.setFill(color_rgb(255,149,0))
				time.sleep(1)
				G.setFill(color_rgb(0,122,255))

			elif(status == 'H'):
				H.setFill(color_rgb(255,149,0))
				time.sleep(1)
				H.setFill(color_rgb(0,122,255))



	tablero.getMouse()
	tablero.close()

def rec_historial(letra, estado, est_ante):

	historial = open("historial.txt", "a")


	if(estado == "A"):
		historial.write(est_ante + "(" + letra + ") --> A  \n")
	elif(estado == "B"):
		historial.write(est_ante + "(" + letra + ") --> B  \n")
	elif(estado == "C"):
		historial.write(est_ante + "(" + letra + ") --> C  \n")
	elif(estado == "D"):
		historial.write(est_ante + "(" + letra + ") --> D  \n")
	elif(estado == "E"):
		historial.write(est_ante + "(" + letra + ") --> E  \n")
	elif(estado == "F"):
		historial.write(est_ante + "(" + letra + ") --> F  \n")
	elif(estado == "G"):
		historial.write(est_ante + "(" + letra + ") --> G  \n")
	elif(estado == "H"):
		historial.write(est_ante + "(" + letra + ") --> H  \n")
	else:
		historial.write("\nError")

	historial.close()


def main():

	while(True):

		os.system('clear')
		print("PROGRAMA DE EVALUACIÓN DE PALABRAS WEB Y EBAY\n")
		print("¿Qué desea hacer?\n")
		print("1)Evaluar palabra")
		print("2)Evaluar una cadena")
		print("3)Leer desde archivo")
		print("4)Ver el grafo")
		print("5)Salir")

		opc = raw_input("----->")

		if(opc == "1" or opc == "2" or opc == "3"):
			historial = open("historial.txt", "w")
			historial.close()

		if(opc == "1"):
			cadena = raw_input("Ingrese una palabra: ")
			cad = cadena.split()

			if(len(cad) == 1):
				arco(cadena)

			else:
				raw_input("Solo se puede procesar una palabra")



		elif(opc == "2"):
			cadena = raw_input("Ingrese la cadena: ")
			evaluar_cadena(cadena)
			raw_input()


		elif(opc == "3"):

			file_name = raw_input("Ingrese el nombre del archivo (con extension: ")
			evaluar_archivo(file_name)
			raw_input()

		elif(opc == "4"):
			arco("NO")

		elif (opc == "5"):
			break;

		else:
			raw_input("Opcion no valida, reintentalo de nuevo")

		os.system('clear')

main()

	

graficas.png: graficador.py datos.txt
	python graficador.py

datos.txt: prueba.x
	./prueba.x
	
prueba.x: prueba.cpp
	g++ prueba.cpp -o prueba.x

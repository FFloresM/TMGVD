ejecutar prubas con datos sinteticos

$ python test.py <alg>

donde <alg> puede ser:
"cm" para CountMin, 
"cs" para CountSketch, 
"cmcu" para CountMinCU.

Por ejemplo
$ python test.py cs
ejecuta y calcula tiempos, memoria y heavyhitters para CountSketch


Ejecutar pruebas con datos reales

$ python test_prot.py <alg> <path_to_file>
<alg> es el mismo que el anterior
<path_to_file> es la ruta donde se encuentra el archivo proteinasunicas.fasta que es con el que se hicieron las pruebas

Por ejemplo

$ python test_prot.py cm ~/Descargas/proteinasunicas.fasta

ejecuta y calcula tiempos, memoria y heavyhitters para CountMin usando el archivo ~/Descargas/proteinasunicas.fasta 


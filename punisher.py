#SAVED FROM BLACKHATSERVER.DDNS.NET#
import requests
import threading

requestUrl = 'URL' #URL DONDE SE REALIZA EL REQUEST

#DATOS DEL PROTOCOLO 200 "POST" DE HERRAMIENTAS DE DESARROLLADOR, SIGUIENDO LA MISMA ESTRUCTURA
data = {
	#'sub1': '1i125af10k52f',
	#'pixel': '4607006756020088',
}
 
def sendRequest():
	while True:
		response = requests.post(requestUrl, data = data) 
		print(response.text)

threads = []
#EL NÚMERO 50 SE REFIERE A LA CANTIDAD DE HILOS DE REPETICIÓN DEL SCRIPT
for i in range(50):
	t = threading.Thread(target=sendRequest)
	t.daemon = True
	threads.append(t)

for i in range(50):
	threads[i].start()

for i in range(50):
	threads[i].join()
    #ARRANCAR EL SCRIPT ESCRIBIENDO "PYTHON3 SCRIPT.PY"
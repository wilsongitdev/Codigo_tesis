import requests
import cv2
from datetime import datetime
#url = 'https://wilmcg.000webhostapp.com/proy_control_alc/phpVSC/datauseralcohol.php'
#myobj = {"DNI": 75123454}

#x = requests.post(url, data = myobj)

#print(x.text)
fechahoraactual = datetime.now()
url = 'https://192.164.1.4/proy_control_alc/user/Insertalcoholdata.php'
myobj = {"DNI": 74881892,"Inge_alcohol":"SI","Alc_mgL":0,"Alc_BAC":0,'img': open('../images/test/Arian.jpg', 'rb').read(),
"fechahora":fechahoraactual}
x = requests.post(url, data = myobj)
print(x.text)

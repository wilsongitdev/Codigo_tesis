from ..webcam import *
from ..tcp_ip import *
import pickle
from PIL import Image

def get_image_of_recognized_person(image_webcam_rgb, alcohol, alc_bac):
    
      # cut and resize image
      cropped_image = image_webcam_rgb[60:60 + image_webcam_rgb.shape[0], 80:80 + image_webcam_rgb.shape[1]]# height,width
      
      #imgsercab=bytes("{:<10}".format(len(imgser)),"utf-8")+imgser
      send_image(sock, cropped_image)
      name, prob, id_person, face_locations = receive_confirmation(sock)

      if len(face_locations) == 1:

            prob = str(round(float(prob), 3))
            (top, right, bottom, left) = face_locations[0]
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255, 255, 255)
            line_width = 3
            
            cv2.rectangle(cropped_image, (left, top), (right, bottom), color, line_width)
            cv2.putText(cropped_image, name, (left - 10, top - 10), font, 1.8, color, line_width, cv2.LINE_AA)
            #cv2.putText(cropped_image, prob, (left + 50, top - 50), font, 1, color, line_width, cv2.LINE_AA)
            
            return id_person, cropped_image, True
      else:
            return False, cropped_image, False

def send_image(sock, image):
      # serialize image and send to server
      _, image_data = cv2.imencode('.jpg', image)
      image_data = pickle.dumps(image_data)
      # Envía el tamaño de la imagen en bytes
      size_bytes = len(image_data).to_bytes(4, byteorder='big')
      sock.sendall(size_bytes)
      
      # Envía la imagen al servidor
      image_data = sock.sendall(image_data)

      
def receive_confirmation(sock):
      data = sock.recv(4096)
      message_received = pickle.loads(data)
      print(message_received)
      name = message_received.get('name')
      prob = message_received.get('prob')
      id_person = message_received.get('id')
      face_locations = message_received.get('face_locations')
      return name, prob, id_person, face_locations
      

# 🧠 Breath Alcohol Analyzer with Facial Recognition and Airflow Detection

Este proyecto consiste en el desarrollo de un **equipo electrónico automático de control de alcoholemia** que integra **detección de flujo de aire dirigido** y **reconocimiento facial**, diseñado para optimizar el control de acceso en entornos laborales y reducir riesgos asociados al consumo de alcohol.

## 🚀 Características principales

- **Detección de soplido**: mediante sensor de sonido que supera los 88 dB.
- **Medición de alcohol**: utilizando el sensor MQ3 con una precisión del **91.21%**.
- **Reconocimiento facial**: basado en redes neuronales (FaceNet) con una efectividad del **95.99%**.
- **Estructura adaptable**: altura ajustable entre 120 cm y 180 cm.
- **Interfaz gráfica y aplicación móvil**: para visualización de resultados.
- **Base de datos en tiempo real**: registro de mediciones y identificación de usuarios.

## 🛠️ Tecnologías utilizadas

- **Hardware**:
  - Raspberry Pi 4
  - Sensor de alcohol MQ3
  - Micrófono para detección de sonido (módulo FC04)
  - Cámara web para reconocimiento facial
  - Pantalla LCD
  - Conversor ADS1115 (I2C)

- **Software**:
  - Python
  - OpenCV
  - dlib
  - Face Recognition API
  - Scikit-learn (SVM)
  - TensorFlow / Keras (FaceNet)

- **Estructura**:
  - Impresión 3D con filamento PLA
  - Soporte metálico ajustable

### Estructura del proyecto
```
/
├── Android/ProyectoAlcoholRostro/          # Código AppMovil
├── Conf_Raspberry/            # Configuración empleada en raspberry pi
├── codigo_rpi_proy # Algoritmo de integracion en Raspberry 
├── backend/proy_control_alc              # Backend alojado en un servidor (hosting)
├── codigocomputadoraalcoholrostro # Reconocimiento de rostro basado en CNN y SVM
├── database #base de datos de prueba
└── README.md
```
## 📊 Resultados
- Precisión en medición de alcohol: 91.21%
- Efectividad en reconocimiento facial: 95.99%
- Tiempo de inferencia facial: < 2 segundos
- Error relativo en alcohol: 8.79%
- Correlación de Pearson: 0.937

## 📌 Aplicaciones
- Control de acceso en empresas
- Prevención de accidentes laborales
- Sectores de construcción y transporte
- Entornos donde se requiera sobriedad obligatoria

## 🔮 Trabajos futuros
- Uso de sensores de oxígeno o presión para mejorar la detección de soplido.
- Implementación de iluminación interna para mejorar el reconocimiento facial.
- Sustitución de Raspberry Pi por NVIDIA Jetson Nano para procesamiento embebido.
- Integración de alertas sonoras y visuales personalizables.

## 👥 Autores
Wilson Manuel Chavesta Gonzales
Luis Brandon Merino Rojas

Asesor: Dr. Guillermo Kemper Vásquez

## 📄 Licencia
Este proyecto fue financiado por la Dirección de Investigación de la UPC mediante el IX Concurso Anual de Incentivo a la Investigación (2021).

##📬 Contacto
Si tienes preguntas o sugerencias, no dudes en abrir un issue o contactar a los autores.

### 🔗 Enlaces de referencia

### 🔗 Referencias y patentes

#### 📋 Patentes
- **Patente peruana**: "Desarrollo de un equipo electrónico de control de alcoholemia con capacidad de detección de flujo de aire dirigido y reconocimiento de rostro"  
  *Número de expediente*: 1450  
  *Oficina*: Indecopi - Perú  
  *Enlace de consulta*: [Sistema de Búsqueda de Patentes - Indecopi](https://servicio.indecopi.gob.pe/portalSAE/)
#### 📄 Publicaciones
- [Paper presentado en ICAT 2020](https://link.springer.com/chapter/10.1007/978-3-030-71503-8_14)

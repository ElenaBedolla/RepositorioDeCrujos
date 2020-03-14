**Práctica 1, Revisión 1**

**Integrantes:**

**Computo distribuido**

Lilia Daniela Salazar Herrera -danyliy@icloud.com

María Elena Bedolla Zamudio-maria.elena.bedolla.zamudio@gmail.com

**Introducción a la exploración geofísica**

Jorge Antonio Camarena Pliego

Josué Soto Cortez

Gilberto Carlos Domínguez Aguilar

Salvador Torres Cervantes

Fernando Rodrigo Aguilar Javier

**Licencia: GPL 3.0**



**Definición del proyecto (Planificación):**

Un sistema distribuido, que ayude a detectar sismos, mediante la visualización de espectrogramas, sismogramas y estadísticos, en tiempo real. Dicho sistema también pretende clasificar sismos por magnitud e intensidad. Y si los tiempos lo permiten una clasificación de los sismos por sus ondas _p y s_.

**¿Porque elegimos este proyecto?**

Porque queremos simplificar la visualización de los eventos sísmicos que registra IRIS, pues es una plataforma no muy intuitiva de usar y con datos crudos, que restringe a las personas no muy familiarizadas con las tecnologías computacionales, lo que reduce el aprovechamiento de esta base de datos.

**Objetivos generales**

Generar una herramienta que genere sismogramas y espectrogramas, en tiempo real, de las estaciones sismológicas que están registradas en IRIS (Incorporated Research Institutions for Seismology).

Brindar una herramienta a las personas que trabajan con Sismología u áreas a fines, con el propósito de simplificar su trabajo mediante la visualización de los eventos registrados, así como los estadísticos de los mismos.

**¿Qué se pretende mostrar?**

Los estadísticos, espectrogramas y sismogramas, de las distintas estaciones sísmicas, todo esto en un sistema distribuido que permita monitorear dichos elementos en tiempo real.

Clasificación de los sismos de acuerdo con su magnitud e intensidad.

(Extra) Clasificación en donde se pueda analizar las ondas p y s de los sismogramas obtenidos, para ver si es posible extraer información relevante para las personas que se dedican a estas áreas o bien, para aquellas que la información pueda ser relevante.

**¿Qué hace al proyecto único?**

El conjunto de herramientas que incluye el sistema distribuido, es decir, la combinación de estadísticos, sismogramas y espectrogramas de las distintas estaciones registradas en IRIS, con un monitoreo en tiempo real, y al mismo tiempo la clasificación de los sismos mediante herramientas de Machine Learning, específicamente en aprendizaje supervisado.

**Herramientas de Software**

- Python
- Php
- HTML5
- Lighttpd
- Google Analytics
- Módulo de OBSPY
- Sublime Text
- Kate
- RabbitMQ (Tentativo)

**Diagrama de desarrollo/ Arquitectura general del sistema /Metodologia**
![IRIS](/images/Diapositiva1.JPG)
![IRIS](/images/Diapositiva2.JPG)
![IRIS](/images/Diapositiva3.JPG)


**¿Cuál es el costo aproximado?**
![IRIS](/images/Diapositiva4.JPG)
**Fuente de datos**

- Red de estaciones sísmicas de IRIS.

![IRIS](/images/Diapositiva5.JPG)

                        [https://www.iris.edu/hq/](https://www.iris.edu/hq/)

**Prueba:**
Correr con la linea de comando python template_download.py, para descargar los datos de prueba. Y posteriormente ejecutar python spectrograms.py para observar espectrogramas de prueba.

**Referencias:**

Yanina Muradas. (2020, 13 febrero). Conoce las 3 metodologías ágiles más usadas. Recuperado 14 marzo, 2020, de https://openwebinars.net/blog/conoce-las-3-metodologias-agiles-mas-usadas/

Agilpm. (s.f.). SoftwaReal calcula el costo de tus proyectos en menos de 1 minuto y aporta valor a tus clientes.. Recuperado 14 marzo, 2020, de [https://agilpm.com/softwareal/](https://agilpm.com/softwareal/)

IRIS. (s.f.). IRIS DATA. Recuperado 14 marzo, 2020, de [https://www.iris.edu/hq/](https://www.iris.edu/hq/)

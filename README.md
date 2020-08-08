Practice 1, Revision 1, English Version

15/03/2020


**Team members:**

**Computo distribuido**

María Elena Bedolla Zamudio -maria.elena.bedolla.zamudio@gmail.com

**Introducción a la exploración geofísica**

Jorge Antonio Camarena Pliego

**Introduction**

IRIS is a university research consortium dedicated to explore the earth interior through the collection and distribution of seismologic data and when we saw that they put a lot of this data on Internet and that it is only reachable for People that work at this area so we still do necessary to create a platform that put The processed data online for everyone to understand

**Planification**

We´re going to do a distributed system that helps to detect earthquakes through the visualization of spectrograms, seismograms and statistics in real time. The system also pretends to classify earthquakes by magnitude and intensity and if time allows, we Will be doing a classification by the type of wave too.

**Why we picked this project?**

Because we want to simplify the visualization of earth tremors that IRIS registers, since it&#39;s not a very intuitive platform to use and with the raw data it restricts not so familiar with these technologies which reduce the utilization of this data base

**General Objectives**

- Create a tool that generates seismograms and spectrograms in real time from the seismic stations that are registered in IRIS (Incorporated Research Institutions for Seismology).
- We´re going to provide a tool for people that works in seismology with the purpose to make easier their work through the visualization of the registered events and the statistics of the earthquakes.

**What we want to show?**

We want to display the statistics, seismograms and spectrograms from the distinct seismologic stations all of this with a distributed system that lets us monitor all these data.

**What makes this project unique?**

The set of tools that the distribution system includes meaning the combination of statistics that the stations registered at Iris with a real time monitor at the same time the classification through machine learning instruments specifically supervised learning.

**Software tools:**

- Python
- Php
- HTML5
- Lighttpd
- Google Analytics
- Módulo de OBSPY
- Sublime Text
- Kate
- RabbitMQ (Optional)
- Django

**Metodology:**
![IRIS](/images/1.JPG)

**General Archictecture and development diagram**
![IRIS](/images/2.JPG)
![IRIS](/images/3.JPG)

**Approximate cost of development**

- 132 hours
- 66 days
- 2 weeks
- 3 months
- 6,600 the cost to pay
- 5,940 Net payment

**Sources:**

        IRIS (Incorporated Research Institutions for Seismology)
![IRIS](/images/Diapositiva5.JPG)

**Test:**

Easy testing can be done by running the test_setup.sh file as follows: 
"bash test_setup.sh processor" for a single execution of the processor node in charge of downloading, processing and transferring the data to the server,
or,
"bash test_setup.sh server" for a single execution of the server node in charge of hosting the web server with the updated information on the website.

For this project to run with said file on either the processor or server nodes, you must be running MySQL and Apache2 servers to update the respective databases and for PHP execution to work with the website on the server.

For both the processor and server nodes, custom security credentials are supported and a sample .json credential file (credentials.json) can be found on the repository to specify the user, password and database for MySQL as well as the user and password for the SSH connection with the server, used by the processor.

The final and intended purpose is for this project to be executed periodically with crontab on both the server and processor nodes. As an example, if you would like to download new data every hour on the first minute, you would add the following line to the processor node's crontab file:

00 * * * * cd /Path/To/Repository/RepositorioDeCrujos/ && bash test_setup.sh processor

And, ideally, the server node should be updating it's own data regularly, so it is recommended to set a crontab command on that node to be executed every short period of time. The following is an example of a command executing every 10 minutes:

*/10 * * * * cd /Path/To/Repository/ReposiorioDeCrujos/ && bash test_setup.sh server

You can access the cronjobs file easily through the crontab -e command.

The library requeriments for this project are in the document labeled "Requeriments.txt".

**Conclusions:**

During the acquisition of data, a series of problems arose, since an interpretation of these had to be made, given that it was necessary to evaluate whether what we were downloading would help us achieve our objective when it came to visualizing the information. Practically this part was the one that took us the longest, since several tests were carried out, in addition to a collaboration with students of the subject Introduction to geophysical exploration to support us with geoprocessing and its interpretation. In this practice the points on which they are going to work on this project were established, all this under the methodology of Extreme programming and it is with this that the documentation of it begins.

**References:**

Yanina Muradas. (2020, 13 febrero). Conoce las 3 metodologías ágiles más usadas. Recuperado 14 marzo, 2020, de https://openwebinars.net/blog/conoce-las-3-metodologias-agiles-mas-usadas/

Agilpm. (s.f.). SoftwaReal calcula el costo de tus proyectos en menos de 1 minuto y aporta valor a tus clientes. Recuperado 14 marzo, 2020, de [https://agilpm.com/softwareal/](https://agilpm.com/softwareal/)

IRIS. (s.f.). IRIS DATA. Recuperado 14 marzo, 2020, de [https://www.iris.edu/hq/](https://www.iris.edu/hq/)

SPE. (s.f.). Seismic interpretation. Recuperado 13 marzo, 2020, de https://petrowiki.org/Seismic\_interpretation

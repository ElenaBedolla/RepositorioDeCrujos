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

**What do we want to show?**

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

**Metodology**

![IRIS](/images/1.JPG)

**General Archictecture**

![IRIS](/images/2.JPG)

**Case Diagram**

![Case](/images/case.png)

**State Diagram**

![State](/images/state.jpg)

**Development Diagram**

![IRIS](/images/3.JPG)

**Sequence Diagram**

![Seq](/images/seq.jpg)

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

**User story**

First Increment

1. As a user, I want the system to graph the spectrograms of the most relevant seismic events.
2. As a user, I want the system to graph the seismograms of the most relevant seismic events.
3. As a work team, we want to document the objectives of the project and general information about it.
As a work team, we want to evaluate the operating system in which we are going to develop the project and the technological resources that we have, first individually and then by team.
5. As a technology administrator, we create a repository in GITHUB where we will store everything related to the project.
6. As a Back end 2 developer, I want to develop a Python script that downloads the data from the provider site, IRIS and a script that graphs the seismograms and spectrograms as images.
7. As a Back end 1 developer, I want to develop a database in which I store data such as latitude, longitude, magnitude, duration, seismograms as data series, stations, channels, date and time of the event.
8. As a Back end 1 developer, I want to develop a script that finds the stations and gives you information about the events detected by them.
9. As a Back end 2 developer, I want to generate some scripts that feed the database, once the data is acquired.
10. As a Back end 2 developer, I want to run and test the developed scripts locally.
11. As a Font end 1 developer, I want to generate a simple web template that shows the user the seismograms and spectrograms in real time.
12. As a Font end 1 developer, I want to generate a logo to give the project identity.
13. As a Font end 1 developer, I want to color the web template, according to the colors used in the logo.

Second Increment

1.As a Font end 1 developer, I decided to give the template a more modern look, in addition to making adjustments to the client's main needs and requests. In your case, Bootstrap technology is integrated to make it responsive to all types of devices with internet access, an easy-to-navigate template is also generated, and light colors are used.
2.As a Font end 1 developer, I solve anchoring problems that are shown when testing with the work team.
3.A Java script effect is also integrated into the template, to make browsing more pleasant and innovative.
4.As a Font end 1 developer, I update the navigation menu, now instead of being different pages, navigation is done within the same page, so that the user experience is more pleasant, since the same page makes the information be more accessible than linking to many separate pages.
5. As a work team, we integrate the Back end code with the new Font end template code.
6.As a user, I want the new look of the web template not to be too loaded with colors, since the developer Font end 1 had put one color per section, interspersing between light red and light blue, so I ask you to find another option minimalist but attractive.
7. As a user I also want the navigation bar not to take up much space on the screen, since it takes care of the navigation menu and also a section of the logo, so it makes it a somewhat annoying header.
8.As a Font end 1 developer, I make a bluish-gray body, mixed with a white navigation bar and a white footer. In addition, I integrate the logo to the navigation bar, although it is a little smaller, but it makes the header take up less space when browsing.
9.As a Font end 1 developer, in the footer I integrate some credits of the project.
10. As a user, I require the events that have occurred to be displayed to generate the most relevant seismograms and spectrograms of the day, in addition to allowing me to see some characteristics such as length, latitus, date and time of the event.
11. As a Back end 2 developer, I generate the script to make the queries to the events.
12. How work team integrates the new scripts, both Back end and Font end.
13. As a team we give notice that the software is ready to be mounted on any server, when the user has it. The software is functional locally, so the user can make use of it. The fact of mounting it on a website is to give access to all those users who have access to the internet and are interested in making a query.
Furthermore, the project is still open to modifications if the user so requires, as it is developed so that it can be scalable and upgradeable, that is, give it its relevant maintenance.
15. As a team, we will have another meeting with the user, to evaluate the documented project.

Third Increment:

1.As a fontend 1 developer together with the Back end 2 developer, an interactive map is designed and replaced by the event table that was previously, in this map you can see the location of the event and some relevant data, and it can directly be generated its seismogram and spectrogram.
2. As a Back end 2 developer, a calibration is done in the geoprocessing parameters, since the locations, seismograms and spectrograms presented errors.
3. As a Font end 1 developer, a color modification is made in the spectrogram to make it more attractive to the user.
4.As a technology administrator, the entry tests are made to the LAAD server, and the project administrator is asked to generate a database on said server.
5.As Back end 1 and 2 developers, we started the process of transferring the data from the local database to the LAAD server database, in addition to migrating the scripts to said server.
6.As a technology administrator, tests are carried out to verify that each time the scripts are executed, the local, transfer and server process is carried out.
7.As a technology administrator, a bash script is generated, where all the scripts that must be executed are combined, to save us the work of executing said scripts in just one.
8. As a technology administrator, the crontab is configured every hour so that it executes the script test_setup.sh and we can have updated seismic information.


**Database Class Diagram**
![Class](/images/class.jpg)

**Test:**

Easy testing can be done by running the test_setup.sh file as follows: 
"bash test_setup.sh processor" for a single execution of the processor node in charge of downloading, processing and transferring the data to the server,
or,
"bash test_setup.sh server" for a single execution of the server node in charge of hosting the web server with the updated information on the website.

For this project to run with said file on either the processor or server nodes, you must be running MySQL and Apache2 servers to update the respective databases and for PHP execution to work with the website on the server.

For both the processor and server nodes, custom security credentials are supported and a sample .json credential file (credentials.json) can be found on the repository to specify the user, password and database for MySQL as well as the user and password for the SSH connection with the server, used by the processor. Note that for establishing a local connection, specifying the 127.0.0.1 address is preferred to "localhost" as a potential issue with PHP MySQL connection has been found with the use of "localhost".

The final and intended purpose is for this project to be executed periodically with crontab on both the server and processor nodes. As an example, if you would like to download new data every hour on the first minute, you would add the following line to the processor node's crontab file:

00 * * * * cd /Path/To/Repository/RepositorioDeCrujos/ && bash test_setup.sh processor

And, ideally, the server node should be updating it's own data regularly, so it is recommended to set a crontab command on that node to be executed every short period of time. The following is an example of a command executing every 10 minutes:

*/10 * * * * cd /Path/To/Repository/ReposiorioDeCrujos/ && bash test_setup.sh server

You can access the cronjobs file easily through the crontab -e command.

The library requeriments for this project are in the document labeled "Requeriments.txt".

**Efficiency Results**

The following is a series of execution time measures taken by the processor node to complete all downloading, processing, database creation and data transfer to server steps. Updating times for the server node are not taken into consideration since this is a very light process, so most of the heavy lifting is done on the processor's side.

It should be noted that other variables outside of the experiment's control may have affected the measures directly, such as the processor's specifications, which in this case are decent (Intel Core i7 7700HQ, 8 GB RAM), and the Internet's bandwidth, which are in contrast very poor.

Different values for the minimum magnitude parameter were tested, while leaving the followung parameters fixed:

 * Unlimited number of stations can be detected
 * Maximum distance to include a station is of 5 degrees (1 degree is approximately equal to 111km)
 * The earthquakes ocurred in the last 24 hours
 
Minimum Magnitude: 5, time: 135 seconds (for 4 earthquakes)

Minimum Magnitude: 4.5, time: 885 seconds (for 8 earthquakes)

Minimum Magnitude: 4, time: 2299 seconds (for 10 earthquakes)

**Conclusions:**

During the acquisition of data, a series of problems arose, since an interpretation of these had to be made, given that it was necessary to evaluate whether what we were downloading would help us achieve our objective when it came to visualizing the information. Practically this part was the one that took us the longest, since several tests were carried out, in addition to a collaboration with students of the subject Introduction to geophysical exploration to support us with geoprocessing and its interpretation. In this practice the points on which they are going to work on this project were established, all this under the methodology of Extreme programming and it is with this that the documentation of it begins.

**References:**

Yanina Muradas. (2020, 13 febrero). Conoce las 3 metodologías ágiles más usadas. Recuperado 14 marzo, 2020, de https://openwebinars.net/blog/conoce-las-3-metodologias-agiles-mas-usadas/

Agilpm. (s.f.). SoftwaReal calcula el costo de tus proyectos en menos de 1 minuto y aporta valor a tus clientes. Recuperado 14 marzo, 2020, de [https://agilpm.com/softwareal/](https://agilpm.com/softwareal/)

IRIS. (s.f.). IRIS DATA. Recuperado 14 marzo, 2020, de [https://www.iris.edu/hq/](https://www.iris.edu/hq/)

SPE. (s.f.). Seismic interpretation. Recuperado 13 marzo, 2020, de https://petrowiki.org/Seismic\_interpretation

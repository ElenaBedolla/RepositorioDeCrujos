<?
if (session_status() == PHP_SESSION_NONE) {
    session_start();
    #$_SESSION['post-data'] = $_POST;
}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <title>EARTHQUAIL</title>
    <!-- GOOGLE FONT -->
    <link href="https://fonts.googleapis.com/css2?family=MuseoModerno:wght@300&display=swap" rel="stylesheet"> 
    
    <!-- BOOTSTRAP 4 -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
    
    <!-- SCROOLL REVEAL JS LIBRARY CDN -->
    <script src="https://unpkg.com/scrollreveal/dist/scrollreveal.min.js"></script>

    <!-- CUSTOM CSS -->
    <link rel="stylesheet" href="css/main.css">
    
    <link  rel="icon"   href="img/quail.png" type="image/png" />
  </head>
  
  
  <body>
    <!-- NAVIGATION -->
    <nav class="navbar navbar-expand-lg navbar-light navbar-inverse bg-white fixed-top pt-2">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <a class="navbar-brand" href="#">
    <img src="img/quail.png" height = '55px' width = '150px' loading="lazy">
  </a>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav ml-auto">
          <a class="nav-item nav-link" href="#head">Home</a>
          <a class="nav-item nav-link" href="#defin">Eventos</a>
          <a class="nav-item nav-link" href="#spectro">Espectograma</a>
          <a class="nav-item nav-link" href="#seis">Sismograma</a>
          <a class="nav-item nav-link" href="#cre">Creditos</a>
        </div>
      </div>
    </nav> 
    <br>
    <br>

    <!-- SECTION -->
    <section id="header">
      <p id="head"><br></p>
        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
            <div class="carousel-item active">
            <img src="img/sismo.jpg" class="d-block w-100" height = '700px' width = '400px'>
            </div> 
            <div class="carousel-item">
            <img src="img/sismos2.jpg" class="d-block w-100" height = '700px' width = '400px' style="width: 100%;">
            </div>
            <div class="carousel-item">
            <img src="img/sism.jpg" class="d-block w-100" height = '700px' width = '400px' style="width: 100%;">
            </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
        <br>
        </div>
        </div>
        </section>
        
    <br>
    <section id="map">
      <p id="defin"><br><br><br></p>
        <center><h2>Eventos</h2></center>
            <!--<form method='post'>
                <input type="submit" name="reset" value="Reset"/>
               //<?
                //if(!empty($_POST['reset']))
                    //{
                        //$_SESSION = [];
                        //echo "Reset exitoso";
                    //}
                //?> 
            </form> -->
            <!--<center><iframe id="inlineFrameExample"
                    title="Inline Frame Example"
                    width="700px"
                    height="700px"
                    src="map.html">
            </iframe></center> -->
            
            
            <div class="embed-container">
            <center><iframe width="1200" height="700" src="map.html" frameborder="0" allowfullscreen></iframe></center>
            </div>
            <?
            if(isset($_POST['earthquake']))
            {
                $_SESSION['earthquake'] = json_decode($_POST['earthquake'], true);
                //echo $_SESSION['earthquake'];
            }
            //foreach($_SESSION as $result) {
            //    echo $result, '<br>';
            //}
            ?>
        </div>
        </div>
      </div>
    </section>
            <?
            if(!empty($_SESSION['earthquake']))
            {
                $earthquake_id = $_SESSION['earthquake'][0];
                $date_time = $_SESSION['earthquake'][1];
            ?>
    <section id="station_earthquake_select">
      <div class="container">
      <p id="defin"><br><br><br></p>
        <center><h2>Estaciones</h2></center>
        <div class="row justify-content-center">
        <div class="col-5 text-center">
            <?
                $string = file_get_contents("../credentials.json");
                $json_creds = json_decode($string, true);

                $dbhost = $json_creds['MySQL']['host'];
                $dbuser = $json_creds['MySQL']['user'];
                $dbpass = $json_creds['MySQL']['password'];
                $dbname = $json_creds['MySQL']['database'];
                $conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);

                if(! $conn){
                    die('Could not connect: '. mysqli_error());
                }
                mysqli_set_charset($conn, "utf8");
                ?>
                <form id="form1" name="form1" method="post" action="">  
                    Lista de Estaciones :  
                    <select name='station'>  
                    <option value="">--- Seleccione ---</option>  
                    <?
                    $station_list=mysqli_query($conn, "SELECT DISTINCT s.symbol FROM STATION as s INNER JOIN CHANNEL as c ON s.symbol=c.station INNER JOIN CHANNEL_EARTHQUAKE as ce ON c.station=ce.station");
                    $station = "";
                    if (isset ($station)&&$station!=""){  
                        $station=$_POST ['station'];  
                    }  
                    while($row_list=mysqli_fetch_assoc($station_list)){  
                    ?>  
                        <option value="<? echo $row_list['symbol']; ?>" <? if($row_list['symbol']==$station){ echo "selected"; } ?> > <? echo $row_list['symbol']; ?>  
                        </option>  
                    <?  
                    }
                    ?>
                    </select>
                    <input type="submit" name="select" value="Seleccionar" />
                    <?
                    if(!empty($_POST['select']))
                    {
                        $_SESSION['station'] = $_POST['station'];
                    }
                    ?>
                    </form>
                    <?
                    if(!empty($_SESSION['station']))
                    {
                        #echo $_SESSION['station'];
                        $selection = $_SESSION['station'];
                        /*
                        $sql = "SELECT DISTINCT e.* FROM EARTHQUAKE AS e INNER JOIN CHANNEL_EARTHQUAKE AS ce ON e.id = ce.earthquake_id WHERE ce.station = '$selection' ORDER BY e.id ASC;";
                        #echo $sql;
                        $date_times = array();
                        $result = mysqli_query($conn, $sql);
                        if(mysqli_num_rows($result) > 0)
                        {
                            echo("<table border = 1>");
                            echo("<tr>
                                <th>ID</th>
                                <th>Fecha y Hora</th>
                                <th>Latitud</th>
                                <th>Longitud</th>
                                <th>Profundidad</th>
                                <th>Magnitud</th>
                            </tr>");
                            ?>
                            <form method="post" action="">
                            <?
                                while($row = mysqli_fetch_assoc($result)){
                                    #$temp = new DateTime($row["date_time"]
                                    $date_time = date_format(new DateTime($row["date_time"]),'YmdHis');
                                    array_push($date_times, $date_time);
                                    echo("<tr>
                                        <td>".$row["id"]."</td>
                                        <td>".$row["date_time"]."</td>
                                        <td>".$row["latitude"]."</td>
                                        <td>".$row["longitude"]."</td>
                                        <td>".$row["depth"]."</td>
                                        <td>".$row["magnitude"]."</td>
                                        <td><button name='earthquake' type='submit' value=".json_encode(array(strval($row["id"]), $date_time)).">X</button>
                                        </tr>");
                                }
                                echo("</table>");
                                if(!empty($_POST['earthquake']))
                                {
                                    $_SESSION['earthquake'] = json_decode($_POST['earthquake'], true);
                                }
                                */
                            ?>
                        </form>
            </div>
            </div>
        </div>
      </div>
    </section>
    <br>
    <br>
    <br>
    <br>
    <!-- SECTION -->
    <section id="espectro">
            <p id="spectro"><br><br><br><center><h2>Espectrograma</h2></center></p>
            <?
            /*
            if(!empty($_SESSION['earthquake']))
            {
                $earthquake_id = $_SESSION['earthquake'][0];
                $date_time = $_SESSION['earthquake'][1];
            */
            ?>
            <center><img src="<? echo "../Template/$date_time-$earthquake_id/$selection/spectrograms_plot.png"; ?>" style="width: 40%;" style="height: 40%;"></center>
             <!--<img src="img/f1.png" style="width: 100%;">-->
          
    </section>
    <br>
    <br>
    <br>
    <!-- SECTION -->
    <section id="sismog">
             <!--<a href="https://es.wikipedia.org/wiki/Sismograma" class="btn btn-outline-secondary header-btn btn-lg mt-2">Read More</a>-->
             <p id="seis"><br><br><center><h2>Sismograma</h2></center></p><br>
            <center><img src="<? echo "../Template/$date_time-$earthquake_id/$selection/seismograms_plot.png"; ?>" style="width: 50%;" style="height: 40%;"></center>
            <?
        } # Cierre del if que verifica si ya se selecciono una estacion
    }  # Cierre de los primeros if que verifica si ya se selecciono un sismo
            ?>
              <!--<img src="img/f2.png" style="width: 100%;">-->
    </section>
    <br>
      
    </section>
    
    <footer id="conta">
    <div class="container">
    <br>
    <center><TABLE CELLPADDING=30>
	<TR>
		<TD><img src="img/enes.png" style="width: 100%;" height = '70px' width = '40px'></TD> <TD> <img src="img/iris.jpg" style="width: 100%;" height = '70px' width = '40px'> </TD> <TD><img src="img/obs.png" style="width: 100%;" height = '70px' width = '40px'></TD> <TD><img src="img/quail.png" style="width: 100%;" height = '70px' width = '40px'></TD>
	</TR>
</TABLE ></center>
    <center>
     <p id="cre">Derechos reservados, Jorge Antonio Camarena Pliego - Maria Elena Bedolla Zamudio</p>
    </center>
    </footer>

    <!-- SCRIPTS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>
    <!-- SCROOLL REVEAL SCRIPT -->
    <script>
      window.sr = ScrollReveal();

    sr.reveal('.navbar', {
      duration: 2000,
      origin: 'bottom'
    });

    sr.reveal('.header-content-left', {
      duration: 2000,
      origin: 'top',
      distance: '300px'
    });

    sr.reveal('.header-content-right', {
      duration: 2000,
      origin: 'right',
      distance: '300px'
    });

    sr.reveal('.header-btn', {
      duration: 2000,
      delay: 1000, 
      origin: 'bottom'
    });

    sr.reveal('#testimonial div', {
      duration: 2000,
      origin: 'left',
      distance: '300px',
      viewFactor: 0.2
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
        });
      });
    });
    </script>
  </body>
</html>

<?php
function conectarBD()
{
    $servername = "localhost";
    $username = "id20539402_admin";
    $password = "tv>LPtfs)-H<tKD7";
    $database   = "id20539402_db_tesis_alcros";
    // Create connection
    $mysqli = new mysqli($servername, $username, $password,$database);

    // Check connection
    if ($mysqli->connect_error) {
        die("Fallo de conexion: " . $mysqli->connect_error);
    }
    else
        return $mysqli;
}

?>

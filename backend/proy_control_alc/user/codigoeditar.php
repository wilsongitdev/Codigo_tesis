<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    session_start();
    if(!isset($_SESSION['usuario']) || !isset($_SESSION['admin']))//hecho 
        //hecho a medida de seguridad por q no ingrese a pagina por url
    {
       header("Location: ../../index.php");
    }
    include_once('../basedatos/conectarbd.php');
    $correo = $_SESSION['usuario'];
    $mysqli = conectarBD();
    $result = $mysqli->query("SELECT Name,Lastname FROM tb_user WHERE Email='$correo'");
    if ($result->num_rows == 1) {
            $row = $result->fetch_assoc();
            $_SESSION['nombres']=$row['Name'];
            $_SESSION['apellidos']=$row['Lastname'];

            $cant=0;
            $msjblanco=0;
            foreach ($_POST as $index => $valor) {
              $cant++;
              # code...
              if(empty($valor))
              {
                $msjblanco++;
              }
            }
            if ($msjblanco==3 or $msjblanco==4)
            {
              echo '<script languaje="javascript">
              alert("Todos los campos estan vacios. No hay busqueda posible")
              self.location = "../menuadmin.php"
              </script>';
            }
            if ($cant==4)
            {
              $fec_max="";
              $fec_min="";
              $fec_select=$_POST['date'];
            }
            else
            {
                $fec_max=$_POST['datemax'];
                $fec_min=$_POST['datemin'];
                  if ($fec_max>$fec_min)
                  {
                      
                      $fec_select="";
                  }
                  else
                  {
                      echo '<script language="javascript">
                      alert("El rango de fechas no es válido.Intente nuevamente")
                      self.location="../menuadmin.php"
                      </script>';
                  }
            }
            $radio_btn=$_POST['gridRadios'];
            $nombres=$_POST['nombres'];
            $apellidos=$_POST['apellidos'];
            $arreglo=array('nombres'=>$nombres,'apellidos'=>$apellidos,
                'fec_max'=>$fec_max,'fec_min'=>$fec_min,'fec_select'=>$fec_select,
                'radio_btn'=>$radio_btn);
            
            
           /*
            if ($arreglo['radio_btn']=='fec_rango'){
              if (empty($arreglo['fec_max']) or empty($arreglo['fec_min'])) 
              {
                echo '<script language = javascript>
                alert("No ha seleccionado el intervalo de fechas.Pruebe nuevamente")
                self.location = "../menuadmin.php"
                </script>';
              }
            }
           */ 
    }
    include "timeout.php";
}
else
{
  header("Location: ../../index.php");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="ISO-8859-1">
  <title>Men&uacute; administrativo</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <link href="https://fonts.googleapis.com/css?family=Raleway:100,400,700,900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css">
  <link rel="stylesheet" href="../../css/menu-principal/style_admin.css">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-plomo">
  <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#"><i class="fas fa-map-marker-alt"></i>Av. Javier Prado Este 996 Of 301, San Isidro
Lima Per&uacute; </a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#"><i class="fas fa-phone-alt"></i>Teléfono: 7153800</a>
      </li>
      
    </ul>
  </div>
  <ul class="nav navbar-nav navbar-right gaaa">
        <li><a href="#"><i class="fab fa-youtube"></i></a></li>
        <li><a href="#"><i class="fab fa-facebook-f"></i></a></li>
        <li><a href="#"><i class="fab fa-twitter"></i></a></li>
        <li><a href="#"><i class="fab fa-instagram"></i></a></li>
    </ul>
</nav><!--cierra barra de menu-->


<nav class="navbar navbar-expand-lg navbar-dark bg-morado">
  <a class="navbar-brand" href="#">Menú Administrador</a>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
  </div>

      <!-- As a heading -->
  <ul class="nav navbar-nav navbar-right">
        <li><a><?php echo "Bienvenido/a ".$_SESSION['nombres']."  ";?></a></li>
      <li><a href="../preg1c.php" class="csesion"><i class="fas fa-door-closed"></i> Cerrar Sesi&oacute;n</a></li>
    </ul>
</nav><!--cierra barra de menu-->


<div class="container ancho_tb_alc" id="tbalc" style="width:100%;border:2px solid #000;margin-top:20px">

        <h2 class="text-center">Niveles de alcohol</h2>
        <table class="table table-hover mejoratb">
            <thead class="thead-dark">
                <tr>
                <th scope="col">Nro</th>
                <th scope="col">DNI</th>
                <th scope="col">Apellidos</th>
                <th scope="col">Nombres</th>
                <th scope="col">Correo</th>
                <th scope="col">Tel&eacute;fono</th>
                <th scope="col">Respuesta</th>
                <th scope="col">Alcohol(mg/L)</th>
                <th scope="col">Fecha de Medición</th>
                </tr>
            </thead>
            <tbody>
        
                <?php
                //$arreglo=array('nombres'=>$nombres,'apellidos'=>$apellidos,'radio_btn'=>$radio_btn,
                //'fec_max'=>$fec_max,'fec_min'=>$fec_min);
                 //fec_rango- fec_act---variables del radiobuttton
                if ($arreglo['radio_btn']=='fec_act' and !empty($fec_select))
                {
                    if (empty($nombres) and empty($apellidos))//nombres vacíos
                    {

                      $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                      a.Ing_Alcohol, a.Alc_mgL,a.Date as fecha_medicion from tb_alcohol_measure a 
                      inner join tb_user b on a.DNI=b.DNI where Date='".$fec_select."'
                      order by a.Date desc";
                      
                        
                    }
                    else if(empty($nombres))//nombre vacios
                    {
                      $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                      a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a 
                      inner join tb_user b on a.DNI=b.DNI where Date='".$fec_select."' 
                      and b.Lastname='".$apellidos."' order by a.Date desc";
                    }
                    else if(empty($apellidos))//apellidos vacios
                    {
                      $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                      a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a
                      inner join tb_user b on a.DNI=b.DNI where Date='".$fec_select."'
                      and b.Name='".$nombres."' order by a.Date desc";
                    }
                    else
                    {
                      $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                      a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a 
                      inner join tb_user b on a.DNI=b.DNI where Date='".$fec_select."' 
                      and b.Name='".$nombres."' and b.Lastname='".$apellidos."' order by a.Date desc";
                    }
                }
                else if($arreglo['radio_btn']=='fec_act' and empty($fec_select))
                {
                  if(empty($nombres))
                  {
                    $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                    a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a
                    inner join tb_user b on a.DNI=b.DNI where b.Lastname='".$apellidos."' 
                    order by a.Date desc";
                  }
                  else if(empty($apellidos))
                  {
                    $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                    a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a 
                    inner join tb_user b on a.DNI=b.DNI where b.Name='".$nombres."' order by a.Date desc";
                  }
                  else
                  {
                    $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                    a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a
                    inner join tb_user b on a.DNI=b.DNI where b.Name='".$nombres."' 
                    and b.Lastname='".$apellidos."' order by a.Date desc";
                  }
                }
                else
                {
                    //if ($arreglo['nombres'])
                    if (empty($nombres) and empty($apellidos))//nombres vacíos
                    {
                      $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                      a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a
                      inner join tb_user b on a.DNI=b.DNI where Date between '".$fec_min."' and
                       '".$fec_max." 23:59:59' order by a.Date desc";
                      //echo $sql;
                    }
                    else if(empty($nombres))
                    {
                      $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                      a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a
                      inner join tb_user b on a.DNI=b.DNI where b.Lastname='".$apellidos."' and
                      Date between '".$fec_min."' and '".$fec_max." 23:59:59' order by a.Date desc";
                    }
                    else if(empty($apellidos))
                    {
                      $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                      a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a 
                      inner join tb_user b on a.DNI=b.DNI where b.Name='".$nombres."' and
                      Date between '".$fec_min."' and '".$fec_max." 23:59:59' order by a.Date desc";
                    }
                    else
                    {
                      $sql="Select a.DNI,b.Lastname,b.Name,b.Email as email,b.phoneNumber,
                      a.Ing_Alcohol, a.Alc_mgL,Date as fecha_medicion from tb_alcohol_measure a 
                      inner join tb_user b on a.DNI=b.DNI where b.Name='".$nombres."' and
                      b.Lastname='".$apellidos."' and Date between '".$fec_min."' and '".$fec_max." 23:59:59' 
                      order by a.Date desc";
                      
                    }
                }

                $result=$mysqli->query($sql);
                $itabla=0;
                while ($row=$result->fetch_assoc()){
                    $itabla+=1;
                    echo "<tr>";
                    echo "<th scope='row'>$itabla</th>";
                    foreach ($row as $x=>$valor)
                    {
                        echo "<td>".$valor."</td>";
                    }
                    echo "</tr>";
                }
                echo "</tbody>";
                echo "</table>";
                
                ?>
                
    </div>
          <?php
                echo "<div class='container alignbot' id='regresar'>
                  <i class='fas fa-arrow-left tam'></i>
                </div>"; 
            ?>
  <script src="../../js/jquery-3.5.1.min.js"></script>
  <script src="../../js/menuadmin2.js"></script>  
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>

</body>
</html>
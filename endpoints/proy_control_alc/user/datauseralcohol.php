<?php
header('Content-Type: application/json; charset=utf-8');

    include_once "../basedatos/conectarbd.php";
    include_once "./functions/getcurrentdomain.php";

    if ($_SERVER["REQUEST_METHOD"] == "POST"){
       
        try{
            error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);

            $username=$_POST['username'];
            $numberpage=$_POST['numberpage'];//2
            $sizelist=$_POST['sizelist'];//15
            $offset=$sizelist*($numberpage-1);
            $startdate=$_POST['startdate'];
            $enddate=$_POST['enddate'];
            
            $mysqli=conectarBD();
            
            $res_dni_query = $mysqli->query("select dni from tb_user where email='".$username."'"); 
            $dni_user = mysqli_fetch_array($res_dni_query,MYSQLI_ASSOC)['dni'];
            
            $sql="select * from tb_alcohol_measure ".
            "INNER JOIN tb_user ON tb_user.dni = tb_alcohol_measure.dni
            where tb_alcohol_measure.Date between '".$startdate."' and '".$enddate."' and tb_alcohol_measure.dni='".$dni_user."'  ORDER BY Date DESC  limit ". $sizelist. " offset ".$offset;

            $sql1="select count(*) as total from tb_alcohol_measure where DNI='".$dni_user."' and Date between '".$startdate."' and '".$enddate."'";
            mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
            $res=$mysqli->query($sql);
            $res1=$mysqli->query($sql1);
            
            $totalelem=round(mysqli_fetch_array($res1,MYSQLI_ASSOC)['total']);
            $numberpages=ceil($totalelem/$sizelist);
            $array=array();
            $domain=getcurrentdomain();
            if ($res){

                while ($fila = mysqli_fetch_array($res,MYSQLI_ASSOC)){
                    $array[]=array(   "id"      =>  intval($fila['id_measure']),
                                    "Alc_mgL"   =>  doubleval($fila['alc_mgl']),
                                    "Alc_BAC"   =>  doubleval($fila['alc_bac']),
                                    "Ing_Alcohol"   =>  intval($fila['ing_alcohol']),
                                    "Picture"      =>  'https://'.$domain['host'].'/proy_control_alc/fotos/medicionesalc/'.$fila['dni']."/".$fila['picture'],
                                    "Date"     =>  date("c", strtotime($fila['date'])),
                                    "User"     =>  array ("DNI" => $fila['dni'], "Name" => $fila['name'],
                                                           "Lastname" => $fila['lastname'] )
                    );

                }
                
                if (count($array)>0){
                    $response['status']=1;
                    $response['description']='Transaction Succesfully';
                    $response['objModel']['numberpages']=$numberpages;
                    $response['objModel']['totalelements']=$totalelem;
                    $response['objModel']['elements']=$array;
                }
                elseif ((count($array)===0)){
                    $response['status']=0;
                    $response['description']='No hay datos';
                    $response['objModel']=$array;
                }
                echo json_encode($response);
            }
            
        }
        catch(Exception $e)
        {
            $response['status']=-1;
            $response['description']=$e->getMessage();
            $response['objModel']=[];
            echo json_encode($response);
        }
    }
    

?>
<?php
header('Content-Type: application/json; charset=utf-8');

    include_once "../basedatos/conectarbd.php";
    include_once "./functions/getcurrentdomain.php";
    if ($_SERVER["REQUEST_METHOD"]==="POST"){
        try{
            error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);

            $numberpage=$_POST['numberpage'];//2
            $sizelist=$_POST['sizelist'];//15
            $offset=$sizelist*($numberpage-1);
            $startdate=$_POST['startdate'];
            $enddate=$_POST['enddate'];
            
            $mysqli=conectarBD();
            $sql="select * from tb_alcohol_measure INNER JOIN tb_user ON tb_alcohol_measure.DNI = tb_user.DNI  where tb_alcohol_measure.Date between '".$startdate."' and '".$enddate."'  ORDER BY Date DESC  limit ". $sizelist. " offset ".$offset;
            $sql1="select count(*) as total from tb_alcohol_measure where Date between '".$startdate."' and '".$enddate."'";
            mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
            $res=$mysqli->query($sql);
            $res1=$mysqli->query($sql1);
            
            $totalelem=round(mysqli_fetch_array($res1,MYSQLI_ASSOC)['total']);
            $numberpages=ceil($totalelem/$sizelist);
            $array=array();
            $domain=getcurrentdomain();
            if ($res){

                while ($fila = mysqli_fetch_array($res,MYSQLI_ASSOC)){
                    $array[]=array(   "id"      =>  intval($fila['IdMeasure']),
                                    "Alc_mgL"   =>  intval($fila['Alc_mgL']),
                                    "Alc_BAC"   =>  intval($fila['Alc_BAC']),
                                    "Picture"      =>  'https://'.$domain['host'].'/proy_control_alc/fotos/medicionesalc/'.$fila['DNI']."/".$fila['Picture'],
                                    "Date"     =>  date("c", strtotime($fila['Date'])),
                                    "User"     =>  array ("DNI" => $fila['DNI'], "name" => $fila['Name'],
                                                           "Apellidos" => $fila['Lastname'] )
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
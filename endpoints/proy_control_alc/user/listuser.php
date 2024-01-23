<?php
header('Content-Type: application/json; charset=utf-8');

    include_once "../basedatos/conectarbd.php";
    include_once "./functions/getcurrentdomain.php";
    if ($_SERVER["REQUEST_METHOD"]==="POST"){
        try{
            error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);

            $numberpage = $_POST['numberpage'];//2
            $sizelist = $_POST['sizelist'];//15
            $offset = $sizelist*($numberpage-1);

            $mysqli = conectarBD();
            $sql = "SELECT * FROM tb_user INNER JOIN tb_loggin ON tb_user.email = tb_loggin.Username
            limit ". $sizelist. " offset ".$offset;
            
            $sql1 = "SELECT count(*) as total from tb_loggin";
            
            mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
            $res = $mysqli -> query($sql);
            $res1 = $mysqli ->  query($sql1);
            $totalelem = round(mysqli_fetch_array($res1,MYSQLI_ASSOC)['total']);
            $numberpages = ceil($totalelem/$sizelist);
            $array = array();
            $domain = getcurrentdomain();
            if ($res){
                while ($fila = mysqli_fetch_array($res,MYSQLI_ASSOC)){
                    $array[] = array(
                            "DNI"   =>  $fila['dni'],
                            "email" =>  $fila['email'],
                            "name"  =>  $fila['name'],
                            "lastname"  =>    $fila['lastname'],
                            "phonenumber"   =>  $fila['phone_number'],
                            "userimage" =>  'https://'.$domain['host'].'/proy_control_alc/fotos/usuarios/'.$fila['dni']."/".$fila['user_image'],        
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
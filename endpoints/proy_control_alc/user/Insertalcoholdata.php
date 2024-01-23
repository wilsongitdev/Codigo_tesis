<?php
header('Content-Type: application/json; charset=utf-8');
    
    error_reporting(E_ERROR | E_WARNING | E_PARSE);
    include_once "../basedatos/conectarbd.php";
    date_default_timezone_set('America/Lima'); //
    if ($_SERVER["REQUEST_METHOD"]==="POST"){
        try{
            // echo $_POST["nombre"];
            $datenow = date('Y-m-d H:i:s');
            $DNI = $_POST["dni"];
            $Inge_alcohol = $_POST["ing_alcohol"];
            $Alc_mgL = $_POST["alc_mgl"];
            $img = $_FILES["img"];
            $Alc_BAC = $_POST["alc_bac"];
            $mysqli = conectarBD();
            $filenewname = uniqid("pruebaalc").".jpg";
            $sql="Insert into tb_alcohol_measure (`dni`, `ing_alcohol`, `alc_mgl`, `alc_bac`, `picture`, `date`) values 
                                                ('".$DNI."','".$Inge_alcohol."',".$Alc_mgL.",".$Alc_BAC.",'".$filenewname."','".$datenow."')";

            mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
            $mysqli->query($sql);
            
            if (!is_dir('../fotos/medicionesalc/'.$DNI)){
                mkdir('../fotos/medicionesalc/'.$DNI); 
            }
            $filedestination="../fotos/medicionesalc/".$DNI."/".$filenewname;
            move_uploaded_file( $img["tmp_name"], $filedestination );
            $response['status']=1;
            $response['description']='Transaction Succesfully';
            $response['objModel']=[];
            echo json_encode($response);

        }
        catch(Exception $e){
            $response['status']=0;
            $response['description']=$e->getMessage();
            $response['objModel']=[];
            echo json_encode($response);
        }
    }
    
    
?>
<?php
header('Content-Type: application/json; charset=utf-8');

    include_once "../basedatos/conectarbd.php";
    include_once "./functions/getcurrentdomain.php";
    if ($_SERVER["REQUEST_METHOD"]==="POST"){
        try{
            error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);
            $dni = $_POST["dni"];
            $email = $_POST["email"];
            $name = $_POST["name"];
            $lastname = $_POST["lastname"];
            $phone_number = $_POST["phone_number"];
            $city = $_POST["city"];
            $country = $_POST["country"];
            $user_image = $_FILES["user_image"];
            $splt_lastname = explode(" ", $lastname);
            $mysqli = conectarBD();
            
            $domain = getcurrentdomain();
            $img_name =  uniqid("user");
            
            $sql_loggin = "INSERT INTO tb_loggin(`Username`, `Password`) VALUES ('".$email."','12345')";
            $sql_user = "INSERT INTO tb_user (`dni`, `email`, `name`, `lastname`, `phone_number`,`city`, `country`, `user_image`) VALUES ('".$dni."','".$email."','".$name."','".$lastname."','".$phone_number."', '".$city."','".$country."','".$img_name.".jpg')";
            
            mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
            $res = $mysqli -> query($sql_loggin);
            $res1 = $mysqli ->  query($sql_user);
            
            if ($res and $res1){
                if (!is_dir('../fotos/usuarios/'.$dni)){
                    mkdir('../fotos/usuarios/'.$dni); 
                }
            
                #clear folder
                $folder = '../fotos/usuarios/'.$dni.'/*'; // Note the use of the * wildcard to match all files in the folder
                $files = glob($folder); // Get a list of all files in the folder
                foreach ($files as $file) {
                    if (is_file($file)) { // Only delete files, not subdirectories
                        unlink($file); // Delete the file
                    }
                }
                #add file
                $filedestination="../fotos/usuarios/".$dni."/".$img_name.".jpg";
                move_uploaded_file( $user_image["tmp_name"], $filedestination );
                
                #show response
                $response['status']=1;
                $response['description']='Transaction Succesfully';
                $response['objModel']=[];

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
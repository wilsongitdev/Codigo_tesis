<?php
	header('Content-Type: application/json; charset=utf-8');
    require_once("../basedatos/conectarbd.php");
	
	try{
		error_reporting(E_ALL);
		
		// error_log("Failed to connect to database!", 0);
		
		if (isset($_POST["Username"],$_POST["Password"])){
			
			$usuario = $_POST["Username"];
			$clave = $_POST["Password"];
			$key = "omasmas";
			$mysqli=conectarBD();
			mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
			$sql="select * from tb_loggin where Username='".$usuario."' and Password='".$clave."'";
			$rs = $mysqli->query($sql);
			if($rs->num_rows==1){
					$response['status']=1;
					$response['description']='Transaction Succesfully';
					// $ivlen = openssl_cipher_iv_length("aria-128-gcm");
					// $iv = openssl_random_pseudo_bytes($ivlen);
					// $ciphertxt = openssl_encrypt("u*".$usuario."*key*".$clave, "aria-128-gcm", $key,$options=0,$iv,$tag);
					// $response['objModel']['token']=$ciphertxt;
					//$original_plaintext = openssl_decrypt($ciphertext, $cipher, $key, $options=0, $iv,$tag);
					//$response['objModel']['desencypted']=$original_plaintext;
					echo json_encode($response);
			}
			else{
				http_response_code(400);
				$response['status']=0;
				$response['description']='Usuario no registrado';
				echo json_encode($response);
			}
			$mysqli->close();
		}
		else{
			http_response_code(400);
			$response['status']=0;
			$response['description']="No se ha ingresado usuario o clave";
			echo json_encode($response);
			
		}
		
	}
	catch(Exception $e){
		http_response_code(400);
		$response['status']=-1;
		$response['description']=$e->getMessage();
		echo json_encode($response);
	}
	
?>
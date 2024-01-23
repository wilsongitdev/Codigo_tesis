<?php
    function getcurrentdomain(){
        
        $uri = $_SERVER['REQUEST_URI'];
        $protocol = ((!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] != 'off') || $_SERVER['SERVER_PORT'] == 443) ? "https://" : "http://";
        $url = $protocol . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
        $domain = parse_url($url);
        return $domain;
    }
?>
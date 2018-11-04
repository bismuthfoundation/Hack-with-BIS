<?php
header('Content-type: image/png');

$address = $_GET['address'];

function generate_and_save($address, $cache_file) {
    $url = 'http://bismuth.online/api/address/'.$address;    
    $info = json_decode(file_get_contents($url), true);    
    if (!isset($info['address'])) {
        return;
    }
    $amount = round($info['balance']*100)/100;       
    $short = substr($address,0,5).'...'.substr($address,51,5);    
    $text = "Balance of $short is $amount \$BIS";
    
    $im = imagecreatetruecolor(400, 30);
    $white = imagecolorallocate($im, 255, 255, 255);
    imagefilledrectangle($im, 0, 0, 399, 29, $white);

    $black = imagecolorallocate($im, 0, 0, 0);
    $font = 'assets/fonts/DroidSans.ttf';
    imagettftext($im, 12, 0, 40, 21, $black, $font, $text);

    $logo = imagecreatefrompng('assets/images/BIS30.png');
    imagecopy($im, $logo, 0, 0, 0, 0, 30, 30);

    imagepng($im, $cache_file);
    imagedestroy($im);
}

$cache_file = "./cache/$address.png";
if (!file_exists($cache_file)) {
    generate_and_save($address, $cache_file);
} elseif (time() - filemtime($cache_file) > 60 * 10) {
    // No more than 1 request to the API per address and per 10 minutes.
    generate_and_save($address, $cache_file);
}

print(file_get_contents($cache_file));

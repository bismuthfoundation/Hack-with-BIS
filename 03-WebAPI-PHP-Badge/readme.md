# Creating a blockchain aware Badge with PHP and the Web API

Bismuth comes with many interfaces to choose from.  
In this tutorial, we'll use the public http API provided by the official explorers:  
No need to run a node, a few lines of code and you're good to go.

We'll use PHP as a backend to show how easily you can play with Bismuth, even if you don't know a word of Python.

## The initial need

We run some bounties from time to time, or can publish tip jars for several projects (so can you!).  
**I felt the need for a way to show, right on a github page, the current balance of any address.**

Since those are static markdown pages, no python nor php could help in a quick approach.  
Then, I thought of the badges we can see on some github, showing build status or extra info.  

How does that work?  
Very simply, it's a dynamic image that is generated from an external script, and embedded into the static page.  
No JS, no nothing. Just an auto magically updating image.

**Requirements**
PHP installed with GD support and FreeType support enabled.

## What we will code together

We will built a short PHP script - hosted on a server of ours - that takes a Bismuth address as a param and produces a valid png image, with the matching BIS balance.

**Example URL**
http://localhost/index.php?address=437b30a2ea780cffb67cc220428d462cf2bedcbd3aab094aa7d4df9c
Changing the BIS address within the URL automatically changes the badge data.

Example with the address `437b30a2ea780cffb67cc220428d462cf2bedcbd3aab094aa7d4df9c`, one of my tip jar:

![TipJar](https://eggpool.net/balance/index.php?address=437b30a2ea780cffb67cc220428d462cf2bedcbd3aab094aa7d4df9c)

## Other uses

Of course, this can be used to include any Bismuth related data into any website, even fully static ones.  
You can use it to display BIS price, your latest incoming transactions, the current block height, whatever you need from the bismuth chain.  

Please surprise us by using it for something unexpected!

## Step by Step

### Architecture

- The script will take a single "address" get parameter as input
- Images will be cached on disk for some time to avoid cpu load
- Data will be obtained by the http api, "address" endpoint 
- We will prepend the Bismuth logo

### Core script

An important task in developement is to cut tasks into smaller ones that are easily coded and maintained.

Let's just imagine we know how to create the image, and we just need the plumbing to cache and deliver it.

- Get the address param
- Does a cache file for it already exists? if no, create and save
- Is the cache fresh enough? If yes, send it, else create and save

In php 101, this is the following:

```php
$address = $_GET['address'];

$cache_file = "./cache/$address.png";
if (!file_exists($cache_file)) {
    generate_and_save($address, $cache_file);
} elseif (time() - filemtime($cache_file) > 60 * 10) {
    // No more than 1 request to the API per address and per 10 minutes.
    generate_and_save($address, $cache_file);
}

print(file_get_contents($cache_file));
```

> time() returns the current unix timestamp, and filemtime() the timestamp of the last file modification. The difference (in seconds, then) is compared to 60 * 10, that is 10 minutes. This is to avoid hammering the API server, and your balance does not change that fast anyway.

**Generate and save**

Now, we miss a `generate_and_save` function that takes an `$address` and the location of the `$cache_file`.

Again, we'll split this task in several easy ones:
- get the balance of the address
- assemble the text to print
- create the image from its parts
- save it

### Get the balance of an address

The API doc tells us to query `http://bismuth.online/api/address/our_bismuth_address`.  
Let's fetch that in a browser to see what the result contains:
http://bismuth.online/api/address/437b30a2ea780cffb67cc220428d462cf2bedcbd3aab094aa7d4df9c

Result is 
```
{"address": "437b30a2ea780cffb67cc220428d462cf2bedcbd3aab094aa7d4df9c", "alias": "", "credits": "0.12300000", "debits": "0.00000000", "rewards": "0.00000000", "fees": "0.00000000", "balance": "0.12300000"}
```
A neat json, with our address back, as well as a "balance" key.

The required php to get the balance amount is an easy one:  
```php
$url = 'http://bismuth.online/api/address/'.$address;    
$info = json_decode(file_get_contents($url), true);    
if (!isset($info['address'])) {
    return;
}
$amount = round($info['balance']*100)/100;  
```
We get the content, json_decode it, and check it contains an "address" key. If not, the server may be broken.  
Then, we round the amount to 2 digits after the decimal point, because our space is scarce.

### Get the text to print

As you saw above, the badge only shows parts of the address (first and last 5 chars) so its size is shorter.

Let's do that:

```php
$short = substr($address,0,5).'...'.substr($address,51,5);    
$text = "Balance of $short is $amount \$BIS";
```
We now have the text part of the badge, now to the image!

### Assemble the image

We'll use the GD image library, part of PHP.  
Basic steps are:
- Create an empty image with white background
- write our text in black
- paste the logo
- save the whole

The matching php code is the following:  
```php
// Create an empty image
$im = imagecreatetruecolor(400, 30);
$white = imagecolorallocate($im, 255, 255, 255);
imagefilledrectangle($im, 0, 0, 399, 29, $white);

// Write text with given ttf font
$black = imagecolorallocate($im, 0, 0, 0);
$font = 'assets/fonts/DroidSans.ttf';
imagettftext($im, 12, 0, 40, 21, $black, $font, $text);

// Paste the 30x30 logo
$logo = imagecreatefrompng('assets/images/BIS30.png');
imagecopy($im, $logo, 0, 0, 0, 0, 30, 30);

// Save image as png to cache
imagepng($im, $cache_file);
// Free the image object
imagedestroy($im);
```

### Final code

That's it, almost done!!! 
Only missing thing is to send the proper mime-type in headers so that the browsers know it's a png image:

```php
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
```

> Now, it's your turn to play with this simple script and amaze us!

### Give us a hand!

You like this tutorial? Learned something? Give us a hand!  
You can:

- Star this repo
- Post a link to that tutorial in a forum you use (no spam ever!), explaining what you liked/learned in it
- Tweet about it: [Tweet: "A blockchain aware badge for any website, with #Bismuth and #PHP"](https://twitter.com/intent/tweet?text=A%20blockchain%20aware%20badge%20for%20any%20website,%20with%20%23Bismuth%20and%20%23PHP&amp;url=https://github.com/bismuthfoundation/Hack-with-BIS/tree/master/03-WebAPI-PHP-Badge&amp;via=Eggpoolnet)

## Resources

- Full code and assets for this tuto: https://github.com/bismuthfoundation/Hack-with-BIS/tree/master/03-WebAPI-PHP-Badge/code

- Detail of the available Bismuth http API commands: http://bismuth.online/apihelp
- The explorers and API code: https://github.com/maccaspacca/BismuthToolsWeb

## Licence

This tutorial is (c) EggdraSyl and the Bismuth Foundation and released under a MIT licence.  
In a nutshell, you can do what you want with it provided you keep this notice intact and hold no responsability against the authors.

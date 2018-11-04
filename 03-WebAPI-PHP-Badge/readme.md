# Creating a blockchain aware Badge with PHP and the Web API

Bismuth comes with many interfaces to choose from.  
In this tutorial, we'll use the public http API provided by the official explorers:  
No need to run a node, a few lines of code and you're good to go.

We'll use PHP as a backend to show how easily you can play with Bismuth, even if you don't know a word of Python.

## The initial need

We run some bounties from time to time, or can publish tip jars for several projects (so can you!).  
**I felt the need for a way to show, right on a github page, the current balance of the pot.**

Since those are static markdown pages, no python nor php could help in a quick approach.  
Then, I thought of the badges we can see on some github, showing build status or extra info.  

How does that work?  
Very simply, it's a dynamic image that is generated from an external page, and embedded into the static page.  
No JS, no nothing. Just an auto magically updating image.

## What we will code together

We will built a short PHP script - hosted on a server of ours - that takes a Bismuth address as a param and produces a valid png image, with the matching Bis balance.

Exemple with the address `437b30a2ea780cffb67cc220428d462cf2bedcbd3aab094aa7d4df9c`, one of my tip jar:  
![TipJar](https://eggpool.net/balance/index.php?address=437b30a2ea780cffb67cc220428d462cf2bedcbd3aab094aa7d4df9c)

## Other uses

Of course, this can be used to include any Bismuth related data into any website, even fully static ones.  
You can use it to display Bis price, your latest incoming transactions, the current block height, whatever you need from the bismuth chain.  

Please surprise us by using it for something unexpected!


## Resources

- The explorers and API code: xx

## Licence

This tutorial is (c) EggdraSyl and the Bismuth Foundation and released under a MIT licence.  
In a nutshell, you can do what you want with it provided you keep this notice intact and hold no responsability against the authors.

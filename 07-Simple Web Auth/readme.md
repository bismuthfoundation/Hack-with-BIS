# A Simple Web auth with Bismuth

Here is a little known use case I was astonished to see at first, that can have quite a lot of variations.

I saw it first on https://pokapoka.biz. I asked the dev if she could write some tuto, but she prefered that I do it and gave me the related code so I could explain.

## The goal

Pokapoka runs a - beta - poker website and wanted to achieve several things at once:

- Anonymous or rather pseudonymous players (no email)
- Account creation needs a confirmation from the user
- User has to prove he owns, and link a Bismuth address

Pokapoka's minimalist approach does all that with very few trouble as you will see.

## Account info

Here is all you are required to enter to create a new account:
- Player name
- password
- bis address

That's all the website will record of you.

Now, the website owner wants you to confirm your account, and make sure you entered your bismuth address, not a random one or your friend's.

## Account confirmation

To achieve that, Pokapoka only requires that you send a 0 bis transaction to an address of hers.  
It costs you only the minimal fees (so you prove you have a working wallet, you can't spam the service for free)  

When the website sees an incoming transaction to that address, it validates the matching account.

## Possible improvements

More could be added that we won't discuss here:

- Lost password (show a new password, encoded with your pubkey, so only you can decode)
- Destroy account via a specific message
- Send BIS to credit your account on the website or pay for a specific feature

## Server side

Pokapoka handled that with very few code.  
In fact, she is not really at ease with python, so she copied a demo plugin and coded the rest in PHP.

Bismuth plugins are an incredibly easy way to get events from the chain.  
You just need to place the plugin file in the "plugins" directory of a bismuth node, and voila!

Pokapoka used the generic webhook, as is, nothing modified:
https://github.com/bismuthfoundation/BismuthPlugins/blob/master/plugins/010_webhook/__init__.py

This plugin adds a "webhook" action to the node and other plugins. Just drop it to your plugins dir and you'll be able to trigger any webhook, in its thread - no node slow down - as you want.

Then she used the "on transactions" plugin:  
https://github.com/bismuthfoundation/BismuthPlugins/blob/master/plugins/201_on_transactions/__init__.py
This plugin generates an event on every block, passing the block info and every transaction.  
If a transaction matches the target address, it triggers... the webhook plugin!

Only things to edit there were 2 config variables:
- the URL of the php webhook to call
- the bismuth address to target (pokapoka's)

```
# Hook definition - Edit to your specific hook
TYPE = 'GET'
URL = 'http://127.0.0.1/transaction.php'

# The bismuth address you want to watch
TARGET_ADDRESS = '679a5ef3ad5e75d9ba7773bc5986e6d390556a85e92a78db55aa2471'
```

The rest is simple PHP: transaction.php then gets a "data" param filled with a php array:
```
[
block_height,   // block # of the matching transaction
timestamp,      // timestamp (with 2 decimals) of the transaction
from,           // sender => this is the account we want to active
to,             // no surprise, this is our target address
amount,         // should be 0, but we may have nice surprises :)
signature,      // signature of the tx, can be ignored
pubkey,         // pubkey of the sender. we can store it with the account to send him encrypted messages.
blockhash,      // hash of the block , you can ignore
fees,           // fees for that tx, should be 0.01 BIS, fixed.
reward          // 0 for regulat tx
operation       // Should be empty for regular tx
openfield       // extra data field, unused here.
]
```

Pokapoka then just has to match the 4th field to its unactivated users list and switch it on.

## Two strings...

Two strings to edit, that's all it took to add an innovative, blockchain based, pseudonymous account validation to an existing website...

Let meditate on that...


# Resources

- Full code for this tuto:  
  (actually, it's just the 2 related plugins, as is...)
- The Bismuth plugins repo with sample plugins: https://github.com/bismuthfoundation/BismuthPlugins

# Licence

This tutorial is (c) EggdraSyl and the Bismuth Foundation and released under a MIT licence.
In a nutshell, you can do what you want with it provided you keep this notice intact and hold no responsability against the authors.

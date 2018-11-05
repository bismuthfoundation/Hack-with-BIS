# Offchain but secure post storage and distribution

A proof of concept dApp to show how Bismuth dApps can use private channels to exchange and store html articles, but still benefit from the chain safety.

## Goal

A steemit like dApp, where anyone with a Bismuth address can publish html or markdown content.  
Content is linked to the author address.  
Real content is stored on participating users drives, only content hashes are stored on chain.  

## Architecture

- A client dApp  
  Runs a webserver, connects to an online wallet server or local node

- A custom dApp protocol  
  So (most recent/last required) content can be cached and synced across clients, available even if the author app is not online
  
- A bismuth protocol  
  For apps to register their external ip on chain so they are reachable, and for authors to announce/sign new content.
  

# Flows

## John registers its client

- At launch, the client checks its external ip, and verifies if it's registered.  
- if it's not, John has the choice to register it to make his own content available to the world.
- The dApp sends a "html:register" transaction with John's external IP

## John publishes a new post

- The post is available from John's webserver on his external ip. 
- It can embed some structured properties like title, tags, version, history (use available html structured data format)
- Its url (network wide) can be something like "bis://html/john_s_address/content_hash"
- The hash of the post content is stored as a "html:publish" transaction

## John deletes a post

- The post is deleted from John's webserver
- The hash of the post content is stored as a "html:delete" transaction so other dApps clients can remove it also.

## John edits a post

- The url of the post will change, since the hash will
- Title will stay the same
- History can be used to keep track of revisions, past hashes and dates
- John's index is updated
- can be handled by "html:delete" + "html:publish" or better, a single "html:update" with old hash and new hash so the edit history is safe, on chain.
- This way, when a hash disappears (old revision), then chain has the new hash and can automatically "redirect" to the current revision.

## Sarah reads John's content

- Sarah "follows" john from her dApp client, she gets a notification when John posts or updates a content.
- Her dApp client fetches the content from John's webserver and caches it locally, or tries to get it from other registered nodes if not available.
- Option: who you follow can be stored on chain, so Sarah can specifically ask John's followers for his content.
- Sarah's dApp client automatically checks the validity of the content via the on chain hash and history.

"""
Demo Script, send a Bismuth transaction
"""

from bismuthclient.bismuthclient import BismuthClient

if __name__ == "__main__":
    client = BismuthClient(wallet_file='wallet.der')
    if not client.address:
        client.new_wallet()
        client.load_wallet()
    """
    BismuthClient does the heavy lifting of finding and connecting to a working wallet server.
    """
    print(f"My address is {client.address}")  #
    txid = client.send(recipient=client.address, amount=0)  # sends 0 to self
    print(f"Txid is {txid}")

    # client.send(recipient="9ba0f8ca03439a8b4222b256a5f56f4f563f6d83755f525992fa5daf", operation='dragg:transfer', data='draggon_adn')

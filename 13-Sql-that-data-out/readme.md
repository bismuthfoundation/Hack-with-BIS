# SQL That data!

Bismuth blockchain and associated extra index are stored in a SQLite db.

You can directly access that data anytime, even when the node is running, to extract any kind of valuable info.

## Sqlite client

### Linux

* `apt install sqlite3` will install the default command line sqlite client.
* `sqlite3 Bismuth/static/ledger.db` opens the ledger (blockchain registry)

* You can also use SQLite Studio if you prefer a full featured GUI  
  https://sqlitestudio.pl/index.rvt
  
### Windows

* You can use SQLite Studio for a full featured GUI  
  https://sqlitestudio.pl/index.rvt
  
## Developers

Every language has bindings for SQLite.  
You can easily access the .db in PHP for instance.

# DB Structure
/static/ledger.db

| DATABASE |
|----------|
| ledger   |
|----------|

TABLE:	misc
|  COLUMN       |  DATA TYPE   |
|---------------|--------------|
| block_height  | INTEGER      |
| difficulty    | TEXT         |

TABLE:	transactions
|  COLUMN       |  DATA TYPE   |
|---------------|--------------|
| block_height  | INTEGER      |
| timestamp     | NUMERIC      |
| address       | TEXT         |
| recipient     | TEXT         |
| amount        | NUMERIC      |
| signature     | TEXT         |
| public_key    | TEXT         |
| block_hash    | TEXT         |
| fee           | NUMERIC      |
| reward        | NUMERIC      |
| operation     | TEXT         |
| openfield     | TEXT         |


# Example Queries

Here are a few useful example queries you can try  
Number of txs during the last hour:  
sqlite> `select count(*) from transactions where block_height in (SELECT block_height from transactions WHERE timestamp > strftime('%s', 'now', '-1 hour') and reward > 0) and reward <= 0;`  

Number of txs during the last 24 hours:  
sqlite> `select count(*) from transactions where block_height in (SELECT block_height from transactions WHERE timestamp > strftime('%s', 'now', '-24 hour') and reward > 0) and reward <= 0;`  

Number of txs during the last month (excluding coinbase txs):  
sqlite> `SELECT count(*) FROM transactions WHERE  timestamp > strftime('%s', 'now', '-1 month') AND reward=0;`  

Last 5 block rewards:  
sqlite> `select block_height,reward from transactions order by block_height desc limit 5;`  

WIP

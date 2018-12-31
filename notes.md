# Submitting a file

* User submits file to network
* File is given unique ID
* File is sharded in 16Kb chunks
    * Each chunk is given order ID
* Each shard is received by other peers
* Final shard is marked with special code to determine last shard
* Maximum capacity on disk for shards is 1Gb
    * User can manually change this to take up as much space

# Downloading a file
* User can search for available files
    * TODO::Determine best method for searching
* Query converted to unique ID
* Ask available peers if they have shard
    * No peers have shards -- Drop peers and find new ones
* Request shards from all available peers
* Wait until all shards are received
* Rebuild shards in order to give file
* Write out to disk

# Command Tags

* UPDT -- Update list of known peers from random peer in list
* SHRD -- File shard
* CHCK -- Check if node has shard

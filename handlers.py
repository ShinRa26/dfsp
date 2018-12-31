import pickle

ACCEPTED_TAGS = {
    "UPDT": update_peer_list,
    "SHRD": process_shard,
    "CHCK": check_for_shard
}

def update_peer_list(client, peers):
    peers = pickle.dumps(peers)
    client.send(peers.encode("utf-8"))

def process_shard(client, data):
    # TODO::Implement
    pass

def check_for_shard(client, shard_info):
    # TODO::Implement
    pass

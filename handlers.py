import pickle

SERVER_TAGS = {
    "UPDT": s_update_peer_list,
    "SHRD": s_process_shard,
    "CHCK": s_check_for_shard
}

CLIENT_TAGS = {
    "UPDT": c_update_peer_list,
    "SHRD": c_process_shard
}

def s_update_peer_list(client, peers):
    peers = pickle.dumps(peers)
    client.send(peers.encode("utf-8"))

def s_process_shard(client, data):
    # TODO::Implement
    pass

def s_check_for_shard(client, shard_info):
    # TODO::Implement
    pass


def c_update_peer_list(peers):
    return pickle.loads(peers)

def c_process_shard(shard):
    # TODO::Implement
    pass

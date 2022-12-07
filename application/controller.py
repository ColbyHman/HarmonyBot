"""Controller Module for the Discord Bot"""
import json

def json_to_dict(json_str):
    """Converts a JSON payload to a dictionary"""
    if json_str is not None:
        return json.loads(json_str)
    return {}

def add_server(server_id, channel):
    """Adds a Discord server to the DB"""
    # db.add_discord_server({
    #     "server_id":server_id,
    #     "channel":channel.name,
    #     "subs":[]
    # })

def remove_server(server_id):
    """Removes a given server from the DB"""
    db.remove_discord_server({"server_id":server_id})


def update_discord_channel(server_id, channel):
    """Updates a discord server's channel preference"""
    # query = {"server_id":server_id}
    # server_info = db.list_server_info(query)
    # server_info['channel'] = channel
    # db.update_discord_server(query, server_info)
    return f"I will now send channel updates to **#{channel}**"


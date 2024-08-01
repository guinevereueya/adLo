def channel_def_without_condition(channel):
    # Process the channel configuration without any conditions
    print(f"Channel {channel['name']} defined without condition.")

my_channel = {"name": "myChannel", "frequency": 100}
channel_def_without_condition(my_channel)

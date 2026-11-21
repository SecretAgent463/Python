
class Television:
    # Constant variables
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3
    def __init__(self):
        status = False
        muted = False
        volume = min_volume
        channel = min_channel
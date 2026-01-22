from gravity_core import BlackHole

class EventHorizon:
    def __init__(self, black_hole):
        self.black_hole = black_hole

    def check(self, distance):
        return self.black_hole.is_inside_event_horizon(distance)
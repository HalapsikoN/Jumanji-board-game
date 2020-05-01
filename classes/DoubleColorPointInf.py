class DoubleColorPointInf:

    def __init__(self, pointAddress, colors, thread, eventToStop):
        self.pointAddress = pointAddress
        self.colors = colors
        self.thread = thread
        self.eventToStop = eventToStop

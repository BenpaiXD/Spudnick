class Buffer:
    def __init__(self, frames):
        self._totalFrames = frames
        self._frames = 0

    def tick(self):
        if self._frames != 0:
            self._frames -= 1

    def check(self):
        return self._frames == 0

    def reset(self):
        self._frames = self._totalFrames
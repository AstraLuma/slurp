import ppb
import time


class AnimationSprite(ppb.BaseSprite):
    def __init__(self, *p, anchor, pos=None, **kw):
        self.anchor = anchor
        if pos is None:
            pos = self.aposition
        super().__init__(*p, pos=pos, **kw)
        self._start_time = time.monotonic()
        self._last_time = None

    @property
    def aposition(self) -> ppb.Vector:
        """
        The anchor position.
        """
        if isinstance(self.anchor, ppb.BaseSprite):
            return self.anchor.position
        else:
            return self.anchor

    def do_start(self, signal):
        """
        Set initial conditions
        """

    def do_frame(self, dt: float, t: float, signal) -> bool:
        """
        Update the animation based on the given frame.

        Returns if there is more frame to do: True if so, False if not
        """
        return False

    def do_finish(self, signal):
        """
        Do any cleanup and trigger anything else
        """

    # We seperate these tasks on the assumption that an Update might not happen
    # every frame, and we should keep the work we do during a frame to a minimum

    def on_idle(self, update, signal):
        if self._last_time is None:
            self.do_start(signal)
            self._last_time = time.monotonic() - self._start_time
        elif self._last_time is ...:
            update.scene.remove(self)
            self.do_finish(signal)

    def on_pre_render(self, pr, signal):
        t = time.monotonic() - self._start_time
        if self._last_time is None:
            pass
        elif self._last_time is ...:
            pass
        else:
            dt = t - self._last_time
            more = self.do_frame(dt, t, signal)
            if more:
                self._last_time = t
            else:
                self._last_time = ...


class FlyUpEffect(AnimationSprite):
    line = ppb.Vector(0, 1)
    duration = 3

    def do_start(self, signal):
        self.position = self.aposition

    def do_frame(self, dt, t, signal):
        self.position = self.line * (t / self.duration) + self.aposition
        return t < self.duration

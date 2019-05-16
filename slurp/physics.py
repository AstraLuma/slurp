from ppb import Vector, keycodes, BaseSprite


class WasdMixin:
    wasd_motion = Vector(0, 0)

    motions = {
        keycodes.W: Vector(0, 1),
        keycodes.A: Vector(-1, 0),
        keycodes.S: Vector(0, -1),
        keycodes.D: Vector(1, 0),
    }

    def on_key_pressed(self, event, signal):
        if event.key in self.motions:
            self.wasd_motion += self.motions[event.key]
        else:
            try:
                super().on_key_pressed
            except AttributeError:
                pass
            else:
                super().on_key_pressed(event, signal)

    def on_key_released(self, event, signal):
        if event.key in self.motions:
            self.wasd_motion -= self.motions[event.key]
        else:
            try:
                super().on_key_released
            except AttributeError:
                pass
            else:
                super().on_key_released(event, signal)


class Region(BaseSprite):
    @staticmethod
    def get_vector(other):
        if isinstance(other, BaseSprite):
            return other.position
        else:
            return other

    def contains(self, other):
        return False

# FIXME: Do overlap

class CircularRegion(Region):
    @property
    def radius(self):
        return max(self.right - self.left, self.top - self.bottom) / 2

    def contains(self, other):
        """
        Returns if other's position overlaps our region
        """
        pos = self.get_vector(other)
        return (self.position - pos).length < self.radius


class RectangularRegion(Region):
    def contains(self, other):
        """
        Returns if other's position overlaps our region
        """
        pos = self.get_vector(other)
        return (
            self.left <= pos.x <= self.right
            and
            self.bottom >= pos.y >= self.top
        )

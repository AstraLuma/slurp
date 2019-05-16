from ppb_mutant import MutantSprite
from .physics import WasdMixin


class PlayerSlime(MutantSprite, WasdMixin):
    emoji = 'slime'

    strength = 1
    

    def on_update(self, event, signal):
        self.position += self.wasd_motion * event.time_delta

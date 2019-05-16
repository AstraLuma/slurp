from ppb_mutant import MutantSprite
from .physics import CircularRegion
from .effects import FlyUpEffect


class BoostItem(MutantSprite, CircularRegion):
    stat = None
    amount = 0
    icon = None

    def can_apply_boost(self, target):
        return hasattr(target, self.stat)

    def apply_boost(self, target):
        value = getattr(target, self.stat)
        value += self.amount
        setattr(target, self.stat, value)

    def on_idle(self, event, signal):
        for player in event.scene.get(tag='player'):
            if self.contains(player) and self.can_apply_boost(player):
                self.apply_boost(player)
                event.scene.remove(self)
                event.scene.add(BoostedEffect(emoji=self.icon, anchor=self.position))


class BoostedEffect(MutantSprite, FlyUpEffect):
    size = 0.5

import ppb
from slurp.player import PlayerSlime
from slurp.items import BoostItem


def setup(scene):
    scene.add(PlayerSlime(), tags=['player'])
    scene.add(BoostItem(
        stat='strength',
        amount=1,
        emoji='red_potion',
        icon='muscle_hmn_g2',
        position=(3, 3),
    ))


ppb.run(setup)

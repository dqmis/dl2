# SET

This folder contains the data for the [SET card game](https://en.wikipedia.org/wiki/Set_(card_game)).

The `asp` folder contains a script version of the card game, written in ASP these can be executed using a ASP solver, such as `clingo`.

The `images` folder contains images of 12 cards. These are generated using code from the `abstractor` repository, which is included as a submodule. To use this repository to generate the images, a small change needs to be made within `experiments\set\setGame.py`, by replacing the first lines with:

```
import os
# other imports


class SetGame():

    def __init__(self, verbose=0):
        dirname = os.path.dirname(__file__)
        im = mpimg.imread(os.path.join(dirname, 'all-cards.png'))
```



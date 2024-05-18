"""
Generating images with SET cards. Uses the `abstractor` repository.
The code is adapted from the notebook file
`experiments/set/set_classification.ipynb` within this repository.
"""

import numpy as np
import random
import matplotlib.pyplot as plt

from abstractor.experiments.set.setGame import SetGame

np.random.seed(0)
random.seed(0)

amount_images = 10

setgame = SetGame()
num_cards = 12
num_rows = 3
num_cols = int(np.ceil(num_cards / num_rows))

for idx in range(amount_images):
    _ = setgame.init_state(num_cards=num_cards, shuffle=True)
    hand = setgame.state.dealt_cards
    fig, axarr = plt.subplots(nrows=num_rows, ncols=num_cols)
    pi = np.random.choice(range(len(hand)), size=len(hand), replace=False)

    strings = []

    for i in range(len(hand)):
        card = hand[i]
        row = i // num_cols
        col = i % num_cols
        strings.append(str(setgame.attributes_of_card(*card)).replace("'", ""))
        axarr[row, col].imshow(setgame.image_of_card(card[0], card[1]))
        axarr[row, col].axis('off')

    with open(f"data/text/{idx}.asp", mode="w") as f:
        f.write("\n".join(strings) + "\n")

    plt.savefig(f"data/images/{idx}.png")

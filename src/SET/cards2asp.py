"""
Adds the card attributes from the txt files to a template
Answer Set Programming (ASP) file.
"""

import os
import numpy as np

# Constants to denote the card attributes
NUMBER = "number"
SHAPE = "shape"
COLOR = "color"
SHADING = "shading"

def create_asp_file(cards,
                    input_use_numerical_numbers=False,
                    output_use_numerical_numbers=False,
                    card_proposition= "card_in_play",
                    input_order=[NUMBER, COLOR, SHADING, SHAPE],
                    output_order=[NUMBER, COLOR, SHADING, SHAPE],
                    ):
    """
    Creates an ASP file with the card attributes from the input list of cards.
s
    Parameters
    ----------
    cards : list of str
        List of strings with the card attributes. Each string should have the
        format following `input_order`

    input_use_numerical_numbers : bool
        If True, the input cards use numerical numbers.

    output_use_numerical_numbers : bool
        If True, the output cards use numerical numbers.

    card_proposition : str
        Name of the card proposition.

    input_order : list of str (using the constants NUMBER, COLOR, SHAPE, SHADING)
        Order of the card attributes in the input.

    output_order : list of str (using the constants NUMBER, COLOR, SHAPE, SHADING)
        Order of the card attributes in the output.


    Returns a list of strings which can be written to a .asp file.
    """
    strings = []

    if output_use_numerical_numbers:
        strings.append("number(1; 2; 3).")
    else:
        strings.append("number(one; two; three).")

    strings.append("shape(oval; squiggle; diamond).")
    strings.append("color(red; green; purple).")
    strings.append("shading(solid; striped; empty).")

    capital_props = [name.capitalize() for name in output_order]
    propositions = ", ".join([f"{name}({cname})" for name, cname in zip(output_order, capital_props)])
    string_capitals = ", ".join(capital_props)
    strings.append(f"card(C) :- {propositions}, C = ({string_capitals}).")

    # strings.append("""
    # card(C) :-
    #     number(Number),
    #     shape(Shape),
    #     color(Color),
    #     shading(Shading),
    #     C = (Number, Shape, Color, Shading).
    # """)

    # String of variables for the card attributes, e.g. "Number1, Shape1, Color1, Shading1".
    # The order can be changed based on `output_order`.
    capital_variables = lambda i: ", ".join([name + str(i) for name in capital_props])

    strings.append(f"""
    all_same_or_all_different(A, B, C) :- A = B, B = C, number(A), number(B), number(C).
    all_same_or_all_different(A, B, C) :- A < B < C, number(A), number(B), number(C).

    all_same_or_all_different(A, B, C) :- A = B, B = C, shape(A), shape(B), shape(C).
    all_same_or_all_different(A, B, C) :- A != B, A != C, B != C, shape(A), shape(B), shape(C).

    all_same_or_all_different(A, B, C) :- A = B, B = C, color(A), color(B), color(C).
    all_same_or_all_different(A, B, C) :- A != B, A != C, B != C, color(A), color(B), color(C).

    all_same_or_all_different(A, B, C) :- A = B, B = C, shading(A), shading(B), shading(C).
    all_same_or_all_different(A, B, C) :- A != B, A != C, B != C, shading(A), shading(B), shading(C).

    valid_set(C1, C2, C3) :-
        card(C1), card(C2), card(C3), C1 != C2, C1 != C3, C2 != C3,
        C1 = ({capital_variables(1)}),
        C2 = ({capital_variables(2)}),
        C3 = ({capital_variables(3)}),
        all_same_or_all_different(Number1, Number2, Number3),
        all_same_or_all_different(Shape1, Shape2, Shape3),
        all_same_or_all_different(Color1, Color2, Color3),
        all_same_or_all_different(Shading1, Shading2, Shading3).

    valid_set_in_play(C1, C2, C3) :-
        {card_proposition}(C1), {card_proposition}(C2), {card_proposition}(C3),
        valid_set(C1, C2, C3).

    #show valid_set_in_play/3.
    """)

    # Change the input's order and names of the attributes
    for card in cards:
        if input_use_numerical_numbers != output_use_numerical_numbers:
            from_list = ["1", "2", "3"] if input_use_numerical_numbers else ["one", "two", "three"]
            to_list = ["1", "2", "3"] if output_use_numerical_numbers else ["one", "two", "three"]
            # Switch text and numerical numbers
            for f, t in zip(from_list, to_list):
                card = card.replace(f, t)

        # Change the order of the card attributes to match with the card proposition.
        attrs = card.replace("(", "").replace(")", "").replace(" ", "").split(",")

        index_mapping = {element: idx for idx, element in enumerate(input_order)}
        indices = [index_mapping[element] for element in output_order]

        ordered_card = [attrs[index] for index in indices]

        string_card = ", ".join(ordered_card)

        strings.append(f"{card_proposition}(({string_card})).")

    return strings

if __name__ == "__main__":
    cards_folder = os.path.join("data","text")
    output_folder = os.path.join("data","asp")

    for i, file in enumerate(os.listdir(cards_folder)):
        with open(os.path.join(cards_folder, file)) as f:
            cards_attributes = [line.strip() for line in f.readlines()]

        strings = create_asp_file(cards_attributes)

        filename, _ = os.path.splitext(file)
        output_file = os.path.join(output_folder, filename + ".asp")

        with open(output_file, mode="w") as f:
            f.write("\n".join(strings) + "\n")

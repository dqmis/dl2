number(1; 2; 3).
shape(oval; squiggle; diamond).
color(red; green; purple).
shading(solid; striped; open).

card(C) :-
    number(Number),
    shape(Shape),
    color(Color),
    shading(Shading),
    C = (Number, Shape, Color, Shading).


card_in_play((2, diamond, green, open)).
card_in_play((2, squiggle, purple, solid)).
card_in_play((1, diamond, purple, open)).
card_in_play((3, diamond, purple, striped)).
card_in_play((3, diamond, red, striped)).
card_in_play((3, diamond, green, open)).
card_in_play((3, diamond, red, open)).
card_in_play((2, squiggle, red, striped)).
card_in_play((1, oval, green, striped)).
card_in_play((1, oval, red, striped)).
card_in_play((1, diamond, purple, striped)).
card_in_play((2, diamond, purple, solid)).

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
    C1 = (Number1, Shape1, Color1, Shading1),
    C2 = (Number2, Shape2, Color2, Shading2),
    C3 = (Number3, Shape3, Color3, Shading3),
    all_same_or_all_different(Number1, Number2, Number3),
    all_same_or_all_different(Shape1, Shape2, Shape3),
    all_same_or_all_different(Color1, Color2, Color3),
    all_same_or_all_different(Shading1, Shading2, Shading3).


valid_set_in_play(C1, C2, C3) :-
    card_in_play(C1), card_in_play(C2), card_in_play(C3),
    valid_set(C1, C2, C3).

#show valid_set_in_play/3.


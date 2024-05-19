number(one; two; three).
shape(oval; squiggle; diamond).
color(red; green; purple).
shading(solid; striped; empty).
card(C) :- number(Number), color(Color), shading(Shading), shape(Shape), C = (Number, Color, Shading, Shape).

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
        C1 = (Number1, Color1, Shading1, Shape1),
        C2 = (Number2, Color2, Shading2, Shape2),
        C3 = (Number3, Color3, Shading3, Shape3),
        all_same_or_all_different(Number1, Number2, Number3),
        all_same_or_all_different(Shape1, Shape2, Shape3),
        all_same_or_all_different(Color1, Color2, Color3),
        all_same_or_all_different(Shading1, Shading2, Shading3).

    valid_set_in_play(C1, C2, C3) :-
        card_in_play(C1), card_in_play(C2), card_in_play(C3),
        valid_set(C1, C2, C3).

    #show valid_set_in_play/3.
    
card_in_play((two, green, solid, squiggle)).
card_in_play((three, purple, solid, diamond)).
card_in_play((two, red, striped, diamond)).
card_in_play((two, red, striped, oval)).
card_in_play((three, green, striped, squiggle)).
card_in_play((two, green, empty, diamond)).
card_in_play((three, purple, empty, oval)).
card_in_play((two, green, striped, squiggle)).
card_in_play((one, green, empty, diamond)).
card_in_play((two, red, solid, squiggle)).
card_in_play((two, green, empty, oval)).
card_in_play((one, red, solid, squiggle)).

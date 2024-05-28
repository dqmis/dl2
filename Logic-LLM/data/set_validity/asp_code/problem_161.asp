% Defining all possible numbers, shapes, colors, and shadings.
number(one; two; three).
shape(oval; squiggle; diamond).
color(red; green; purple).
shading(solid; striped; empty).


% Defining the card ids.
card_id(1..4).
% Defining the card object. Card has number of objects, shape, color, and shading.
card(C) :- card_id(Id), number(Number), color(Color), shading(Shading), shape(Shape), C = (Id, Number, Color, Shading, Shape).

% All cards in a set must have the same number or all different numbers.
all_same_or_all_different(A, B, C) :- A = B, B = C, number(A), number(B), number(C).
all_same_or_all_different(A, B, C) :- A < B < C, number(A), number(B), number(C).

% All cards in a set must have the same shape or all different shapes.
all_same_or_all_different(A, B, C) :- A = B, B = C, shape(A), shape(B), shape(C).
all_same_or_all_different(A, B, C) :- A != B, A != C, B != C, shape(A), shape(B), shape(C).

% All cards in a set must have the same color or all different colors.
all_same_or_all_different(A, B, C) :- A = B, B = C, color(A), color(B), color(C).
all_same_or_all_different(A, B, C) :- A != B, A != C, B != C, color(A), color(B), color(C).

% All cards in a set must have the same shading or all different shadings.
all_same_or_all_different(A, B, C) :- A = B, B = C, shading(A), shading(B), shading(C).
all_same_or_all_different(A, B, C) :- A != B, A != C, B != C, shading(A), shading(B), shading(C).

% A set is valid if the cards have the same number or all different numbers, the same shape or all different shapes,
% the same color or all different colors, and the same shading or all different shadings.
valid_set(C1, C2, C3) :-
card(C1), card(C2), card(C3), C1 != C2, C1 != C3, C2 != C3,
C1 = (_, Number1, Color1, Shading1, Shape1),
C2 = (_, Number2, Color2, Shading2, Shape2),
C3 = (_, Number3, Color3, Shading3, Shape3),
all_same_or_all_different(Number1, Number2, Number3),
all_same_or_all_different(Shape1, Shape2, Shape3),
all_same_or_all_different(Color1, Color2, Color3),
all_same_or_all_different(Shading1, Shading2, Shading3).

% A set is valid if the cards have the same number or all different numbers, the same shape or all different shapes,
valid_set_in_play(C1, C2, C3) :-
card_in_play(C1), card_in_play(C2), card_in_play(C3),
valid_set(C1, C2, C3).


% The cards in play.
card_in_play((1, one, purple, striped, oval)).
card_in_play((2, two, green, striped, diamond)).
card_in_play((3, one, purple, striped, oval)).
card_in_play((4, one, red, empty, oval)).


% The set is valid if there is a valid set in play. 

:- not valid_set_in_play(_, _, _).
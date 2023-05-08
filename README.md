# mtg-curve

This is a collection of scripts to compute the number of colored lands you need to play your spells on curve.

## Basic script

This is mostly the same script as Frank Karsten's, with similar results




| lands | C  | 1C | CC | 2C | 1CC | CCC | 3C | 2CC | 1CCC | CCCC | 4C | 3CC | 2CCC | 1CCCC | 5C | 4CC | 3CCC | 5CC | 4CCC |
|-------|----|----|----|----|-----|-----|----|-----|------|------|----|-----|------|-------|----|-----|------|-----|------|
| 20    | 12 | 12 | 18 | 10 | 15  | 19  | 9  | 13  | 17   | 20   | 8  | 12  | 15   | 18    | 7  | 11  | 14   | 10  | 12   |
| 21    | 12 | 12 | 18 | 10 | 16  | 20  | 9  | 14  | 18   | 21   | 8  | 12  | 16   | 19    | 7  | 11  | 14   | 10  | 13   |
| 22    | 13 | 12 | 19 | 11 | 17  | 21  | 9  | 15  | 19   | 22   | 8  | 13  | 17   | 20    | 8  | 12  | 15   | 11  | 14   |
| 23    | 13 | 13 | 20 | 11 | 17  | 22  | 10 | 15  | 19   | 23   | 9  | 13  | 17   | 21    | 8  | 12  | 16   | 11  | 14   |
| 24    | 14 | 13 | 20 | 11 | 18  | 23  | 10 | 16  | 20   | 24   | 9  | 14  | 18   | 21    | 8  | 13  | 16   | 12  | 15   |
| 25    | 14 | 13 | 21 | 12 | 18  | 23  | 11 | 16  | 21   | 24   | 9  | 15  | 19   | 22    | 9  | 13  | 17   | 12  | 16   |
| 26    | 14 | 13 | 21 | 12 | 19  | 24  | 11 | 17  | 21   | 25   | 10 | 15  | 19   | 23    | 9  | 14  | 18   | 13  | 16   |
| 27    | 15 | 14 | 22 | 12 | 19  | 25  | 11 | 17  | 22   | 26   | 10 | 16  | 20   | 24    | 9  | 14  | 18   | 13  | 17   |
| 28    | 15 | 14 | 22 | 13 | 20  | 26  | 11 | 18  | 23   | 27   | 10 | 16  | 21   | 25    | 10 | 15  | 19   | 14  | 18   |
| 29    | 15 | 14 | 23 | 13 | 20  | 26  | 12 | 18  | 23   | 28   | 11 | 17  | 21   | 25    | 10 | 15  | 20   | 14  | 18   |
| 30    | 15 | 14 | 23 | 13 | 21  | 27  | 12 | 19  | 24   | 29   | 11 | 17  | 22   | 26    | 10 | 16  | 20   | 15  | 19   |

## Tapped lands

This is a script to take into account taplands, assuming they tap for the color you're trying to cast.

The process is a bit more CPU intensive, and  also harder to present, so here is the data for 24 and 25 lands only.

### 24 lands



Here  is how the data should be read: If you want to cast a 2C spell, you need 11 sources of the color, and this can accomodate 0 taplands.
If you have 12 sources of that color, you can accomodate 4 taplands..
The row for C is not interesting: turn 1, any tapland is the same as a land of a bad color, so you shouldn't count taplands as sources of the relevant color.


| mana cost | lands (tapped)                                                     |
|-----------|--------------------------------------------------------------------|
| C         | 14(0) 15(1) 16(2) 17(3) 18(4) 19(5) 20(6) 21(7) 22(8) 23(9) 24(10) |
| 1C        | 13(4) 14(6) 15(8) 16(9) 17(10) 20(11)                              |
| CC        | 20(2) 21(6) 22(8) 23(10) 24(11)                                    |
| 2C        | 11(0) 12(4) 13(7) 14(8) 15(9) 16(10) 19(11)                        |
| 1CC       | 18(4) 19(7) 20(9) 21(10) 22(11)                                    |
| CCC       | 23(7) 24(11)                                                       |
| 3C        | 10(1) 11(3) 12(5) 13(6) 14(7) 15(8) 24(9)                          |
| 2CC       | 16(2) 17(5) 18(6) 19(7) 20(8) 23(9)                                |
| 1CCC      | 20(1) 21(5) 22(7) 23(8)                                            |
| CCCC      | 24(8)                                                              |
| 4C        | 9(0) 10(2) 11(3) 12(4) 13(5)                                       |
| 3CC       | 14(0) 15(2) 16(4) 18(5)                                            |
| 2CCC      | 18(1) 19(3) 20(4) 21(5)                                            |
| 1CCCC     | 21(0) 22(3) 23(5)                                                  |
| 5C        | 8(0) 9(1) 10(2) 11(3)                                              |
| 4CC       | 13(1) 14(2) 16(3)                                                  |
| 3CCC      | 16(0) 17(1) 18(2) 19(3)                                            |
| 5CC       | 12(0) 13(1) 14(2)                                                  |
| 4CCC      | 15(0) 16(1) 17(2)                                                  |




Some rows might be surprising, like the 4C row. It means that I can
accomodate at most 5 taplands, even if all 24 lands tap for my color.
Why is that ? Suppose you have 24 lands, 6 of them tapped. That's 25%
of your lands tapped.  5 lands is a lot, and it's pretty difficult to
get 5 lands by turn 5. So you're almost always topdecking your 5th
land, and it will be tapped 25% of the time, so you won't be able to
cast your spell. That's not a rigorous proof, but that's the idea.

The moral of the story is that you shouldn't expect to be able to play
your 5 and 6 mana cards on curve even with one tapland.


### 25 lands

| mana cost | lands (tapped)                                                            |
|-----------|---------------------------------------------------------------------------|

| C     | 14(0) 15(1) 16(2) 17(3) 18(4) 19(5) 20(6) 21(7) 22(8) 23(9) 24(10) 25(11) |
| 1C    | 13(2) 14(6) 15(8) 16(9) 17(10) 19(11) 22(12)                              |
| CC    | 21(4) 22(7) 23(9) 24(10) 25(12)                                           |
| 2C    | 12(3) 13(6) 14(8) 15(9) 16(10) 17(11) 22(12)                              |
| 1CC   | 18(1) 19(6) 20(8) 21(10) 22(11) 24(12)                                    |
| CCC   | 23(1) 24(8) 25(12)                                                        |
| 3C    | 10(0) 11(2) 12(5) 13(6) 14(7) 15(8) 16(9)                                 |
| 2CC   | 16(0) 17(4) 18(6) 19(7) 20(8) 21(9)                                       |
| 1CCC  | 21(3) 22(6) 23(8) 24(9)                                                   |
| CCCC  | 24(0) 25(9)                                                               |
| 4C    | 9(0) 10(2) 11(3) 12(4) 13(5) 15(6)                                        |
| 3CC   | 15(2) 16(3) 17(4) 18(5) 19(6)                                             |
| 2CCC  | 19(2) 20(4) 21(5) 22(6)                                                   |
| 1CCCC | 22(1) 23(4) 24(6)                                                         |
| 5C    | 9(1) 10(2) 11(3) 15(4)                                                    |
| 4CC   | 13(0) 14(1) 15(2) 16(3) 19(4)                                             |
| 3CCC  | 17(0) 18(2) 19(3) 21(4)                                                   |
| 5CC   | 12(0) 13(1) 14(2)                                                         |
| 4CCC  | 16(1) 18(2)                                                               |


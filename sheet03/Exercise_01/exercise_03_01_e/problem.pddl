(define (problem kami-prob)
    (:domain kami-dom)

    (:objects
        tile00 tile10 tile20 tile30 tile40 tile50 tile01 tile11 tile21 tile31 tile41 tile51 tile02 tile12 tile22 tile32 tile42 tile52 tile03 tile13 tile23 tile33 tile43 tile53 tile04 tile14 tile24 tile34 tile44 tile54 tile05 tile15 tile25 tile35 tile45 tile55 tile06 tile16 tile26 tile36 tile46 tile56 tile07 tile17 tile27 tile37 tile47 tile57 tile08 tile18 tile28 tile38 tile48 tile58 tile09 tile19 tile29 tile39 tile49 tile59 - tile
        blue yellow - color
        true - bool)

    (:init
(= (total-cost) 0)
(color_value tile00 blue)
(is_neighbour tile00 tile10)
(is_neighbour tile00 tile01)
(color_value tile10 blue)
(is_neighbour tile10 tile20)
(is_neighbour tile10 tile00)
(is_neighbour tile10 tile11)
(color_value tile20 blue)
(is_neighbour tile20 tile30)
(is_neighbour tile20 tile10)
(is_neighbour tile20 tile21)
(color_value tile30 blue)
(is_neighbour tile30 tile40)
(is_neighbour tile30 tile20)
(is_neighbour tile30 tile31)
(color_value tile40 blue)
(is_neighbour tile40 tile50)
(is_neighbour tile40 tile30)
(is_neighbour tile40 tile41)
(color_value tile50 blue)
(is_neighbour tile50 tile40)
(is_neighbour tile50 tile51)
(color_value tile01 blue)
(is_neighbour tile01 tile11)
(is_neighbour tile01 tile02)
(is_neighbour tile01 tile00)
(color_value tile11 blue)
(is_neighbour tile11 tile21)
(is_neighbour tile11 tile01)
(is_neighbour tile11 tile12)
(is_neighbour tile11 tile10)
(color_value tile21 blue)
(is_neighbour tile21 tile31)
(is_neighbour tile21 tile11)
(is_neighbour tile21 tile22)
(is_neighbour tile21 tile20)
(color_value tile31 blue)
(is_neighbour tile31 tile41)
(is_neighbour tile31 tile21)
(is_neighbour tile31 tile32)
(is_neighbour tile31 tile30)
(color_value tile41 blue)
(is_neighbour tile41 tile51)
(is_neighbour tile41 tile31)
(is_neighbour tile41 tile42)
(is_neighbour tile41 tile40)
(color_value tile51 blue)
(is_neighbour tile51 tile41)
(is_neighbour tile51 tile52)
(is_neighbour tile51 tile50)
(color_value tile02 yellow)
(is_neighbour tile02 tile12)
(is_neighbour tile02 tile03)
(is_neighbour tile02 tile01)
(color_value tile12 yellow)
(is_neighbour tile12 tile22)
(is_neighbour tile12 tile02)
(is_neighbour tile12 tile13)
(is_neighbour tile12 tile11)
(color_value tile22 yellow)
(is_neighbour tile22 tile32)
(is_neighbour tile22 tile12)
(is_neighbour tile22 tile23)
(is_neighbour tile22 tile21)
(color_value tile32 yellow)
(is_neighbour tile32 tile42)
(is_neighbour tile32 tile22)
(is_neighbour tile32 tile33)
(is_neighbour tile32 tile31)
(color_value tile42 yellow)
(is_neighbour tile42 tile52)
(is_neighbour tile42 tile32)
(is_neighbour tile42 tile43)
(is_neighbour tile42 tile41)
(color_value tile52 yellow)
(is_neighbour tile52 tile42)
(is_neighbour tile52 tile53)
(is_neighbour tile52 tile51)
(color_value tile03 yellow)
(is_neighbour tile03 tile13)
(is_neighbour tile03 tile04)
(is_neighbour tile03 tile02)
(color_value tile13 blue)
(is_neighbour tile13 tile23)
(is_neighbour tile13 tile03)
(is_neighbour tile13 tile14)
(is_neighbour tile13 tile12)
(color_value tile23 blue)
(is_neighbour tile23 tile33)
(is_neighbour tile23 tile13)
(is_neighbour tile23 tile24)
(is_neighbour tile23 tile22)
(color_value tile33 blue)
(is_neighbour tile33 tile43)
(is_neighbour tile33 tile23)
(is_neighbour tile33 tile34)
(is_neighbour tile33 tile32)
(color_value tile43 blue)
(is_neighbour tile43 tile53)
(is_neighbour tile43 tile33)
(is_neighbour tile43 tile44)
(is_neighbour tile43 tile42)
(color_value tile53 yellow)
(is_neighbour tile53 tile43)
(is_neighbour tile53 tile54)
(is_neighbour tile53 tile52)
(color_value tile04 yellow)
(is_neighbour tile04 tile14)
(is_neighbour tile04 tile05)
(is_neighbour tile04 tile03)
(color_value tile14 blue)
(is_neighbour tile14 tile24)
(is_neighbour tile14 tile04)
(is_neighbour tile14 tile15)
(is_neighbour tile14 tile13)
(color_value tile24 yellow)
(is_neighbour tile24 tile34)
(is_neighbour tile24 tile14)
(is_neighbour tile24 tile25)
(is_neighbour tile24 tile23)
(color_value tile34 yellow)
(is_neighbour tile34 tile44)
(is_neighbour tile34 tile24)
(is_neighbour tile34 tile35)
(is_neighbour tile34 tile33)
(color_value tile44 blue)
(is_neighbour tile44 tile54)
(is_neighbour tile44 tile34)
(is_neighbour tile44 tile45)
(is_neighbour tile44 tile43)
(color_value tile54 yellow)
(is_neighbour tile54 tile44)
(is_neighbour tile54 tile55)
(is_neighbour tile54 tile53)
(color_value tile05 yellow)
(is_neighbour tile05 tile15)
(is_neighbour tile05 tile06)
(is_neighbour tile05 tile04)
(color_value tile15 blue)
(is_neighbour tile15 tile25)
(is_neighbour tile15 tile05)
(is_neighbour tile15 tile16)
(is_neighbour tile15 tile14)
(color_value tile25 yellow)
(is_neighbour tile25 tile35)
(is_neighbour tile25 tile15)
(is_neighbour tile25 tile26)
(is_neighbour tile25 tile24)
(color_value tile35 yellow)
(is_neighbour tile35 tile45)
(is_neighbour tile35 tile25)
(is_neighbour tile35 tile36)
(is_neighbour tile35 tile34)
(color_value tile45 blue)
(is_neighbour tile45 tile55)
(is_neighbour tile45 tile35)
(is_neighbour tile45 tile46)
(is_neighbour tile45 tile44)
(color_value tile55 yellow)
(is_neighbour tile55 tile45)
(is_neighbour tile55 tile56)
(is_neighbour tile55 tile54)
(color_value tile06 yellow)
(is_neighbour tile06 tile16)
(is_neighbour tile06 tile07)
(is_neighbour tile06 tile05)
(color_value tile16 blue)
(is_neighbour tile16 tile26)
(is_neighbour tile16 tile06)
(is_neighbour tile16 tile17)
(is_neighbour tile16 tile15)
(color_value tile26 blue)
(is_neighbour tile26 tile36)
(is_neighbour tile26 tile16)
(is_neighbour tile26 tile27)
(is_neighbour tile26 tile25)
(color_value tile36 blue)
(is_neighbour tile36 tile46)
(is_neighbour tile36 tile26)
(is_neighbour tile36 tile37)
(is_neighbour tile36 tile35)
(color_value tile46 blue)
(is_neighbour tile46 tile56)
(is_neighbour tile46 tile36)
(is_neighbour tile46 tile47)
(is_neighbour tile46 tile45)
(color_value tile56 yellow)
(is_neighbour tile56 tile46)
(is_neighbour tile56 tile57)
(is_neighbour tile56 tile55)
(color_value tile07 yellow)
(is_neighbour tile07 tile17)
(is_neighbour tile07 tile08)
(is_neighbour tile07 tile06)
(color_value tile17 yellow)
(is_neighbour tile17 tile27)
(is_neighbour tile17 tile07)
(is_neighbour tile17 tile18)
(is_neighbour tile17 tile16)
(color_value tile27 yellow)
(is_neighbour tile27 tile37)
(is_neighbour tile27 tile17)
(is_neighbour tile27 tile28)
(is_neighbour tile27 tile26)
(color_value tile37 yellow)
(is_neighbour tile37 tile47)
(is_neighbour tile37 tile27)
(is_neighbour tile37 tile38)
(is_neighbour tile37 tile36)
(color_value tile47 yellow)
(is_neighbour tile47 tile57)
(is_neighbour tile47 tile37)
(is_neighbour tile47 tile48)
(is_neighbour tile47 tile46)
(color_value tile57 yellow)
(is_neighbour tile57 tile47)
(is_neighbour tile57 tile58)
(is_neighbour tile57 tile56)
(color_value tile08 blue)
(is_neighbour tile08 tile18)
(is_neighbour tile08 tile09)
(is_neighbour tile08 tile07)
(color_value tile18 blue)
(is_neighbour tile18 tile28)
(is_neighbour tile18 tile08)
(is_neighbour tile18 tile19)
(is_neighbour tile18 tile17)
(color_value tile28 blue)
(is_neighbour tile28 tile38)
(is_neighbour tile28 tile18)
(is_neighbour tile28 tile29)
(is_neighbour tile28 tile27)
(color_value tile38 blue)
(is_neighbour tile38 tile48)
(is_neighbour tile38 tile28)
(is_neighbour tile38 tile39)
(is_neighbour tile38 tile37)
(color_value tile48 blue)
(is_neighbour tile48 tile58)
(is_neighbour tile48 tile38)
(is_neighbour tile48 tile49)
(is_neighbour tile48 tile47)
(color_value tile58 blue)
(is_neighbour tile58 tile48)
(is_neighbour tile58 tile59)
(is_neighbour tile58 tile57)
(color_value tile09 blue)
(is_neighbour tile09 tile19)
(is_neighbour tile09 tile08)
(color_value tile19 blue)
(is_neighbour tile19 tile29)
(is_neighbour tile19 tile09)
(is_neighbour tile19 tile18)
(color_value tile29 blue)
(is_neighbour tile29 tile39)
(is_neighbour tile29 tile19)
(is_neighbour tile29 tile28)
(color_value tile39 blue)
(is_neighbour tile39 tile49)
(is_neighbour tile39 tile29)
(is_neighbour tile39 tile38)
(color_value tile49 blue)
(is_neighbour tile49 tile59)
(is_neighbour tile49 tile39)
(is_neighbour tile49 tile48)
(color_value tile59 blue)
(is_neighbour tile59 tile49)
(is_neighbour tile59 tile58))

    (:goal (and (not (curr_color true))
                (or 
                   (forall (?t - tile) (color_value ?t blue))
                   (forall (?t - tile) (color_value ?t yellow))
                )))

    (:metric minimize (total-cost))
)

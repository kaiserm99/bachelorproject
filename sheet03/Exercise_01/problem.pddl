(define (problem kami-prob)
   (:domain kami-dom)

   (:objects
      tile11 tile12 tile13 tile21 tile22 tile23 tile31 tile32 tile33 tile43 - tile
      red green brown - color
      true - bool)

   (:init
        (color_value tile11 brown)
        (color_value tile12 brown)
        (color_value tile13 green)
        (color_value tile21 red)
        (color_value tile22 brown)
        (color_value tile23 red)
        (color_value tile31 green)
        (color_value tile32 brown)
        (color_value tile33 red)
        (color_value tile43 red)
      
        (is_neighbour tile11 tile12)
        (is_neighbour tile11 tile21)
        
        (is_neighbour tile12 tile11)
        (is_neighbour tile12 tile22)
        (is_neighbour tile12 tile23)

        (is_neighbour tile13 tile12)
        (is_neighbour tile13 tile23)
    
        (is_neighbour tile21 tile11)
        (is_neighbour tile21 tile22)
        (is_neighbour tile21 tile31)
        
          
        (is_neighbour tile22 tile12)
        (is_neighbour tile22 tile21)
        (is_neighbour tile22 tile32)
        (is_neighbour tile22 tile23)

        (is_neighbour tile23 tile13)
        (is_neighbour tile23 tile22)
        (is_neighbour tile23 tile33)
        
        (is_neighbour tile31 tile21)
        (is_neighbour tile31 tile32)
        
        (is_neighbour tile32 tile22)
        (is_neighbour tile32 tile31)
        (is_neighbour tile32 tile33)

        (is_neighbour tile33 tile32)
        (is_neighbour tile33 tile23)
        (is_neighbour tile33 tile43)

        (is_neighbour tile43 tile33)


   )
   
   (:goal (and (or (forall (?t - tile) (color_value ?t green))
                   (forall (?t - tile) (color_value ?t red))
                   (forall (?t - tile) (color_value ?t brown)))
                (not (curr_color true))
   )))
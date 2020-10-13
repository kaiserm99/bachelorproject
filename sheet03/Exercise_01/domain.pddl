(define (domain kami-dom)
    (:requirements :strips :typing :disjunctive-preconditions :negative-preconditions :conditional-effects)

    (:types tile color bool
    )

    (:predicates
        (color_value ?t - tile ?c - color)
        (is_neighbour ?fir_t ?sec_t - tile)
        (change_to_color ?t - tile ?c - color)  ;; a tile can get this value when it is in a floodfill and should get colored next
        (mark_tile ?t - tile)  ;; mark the tile explicit so it will get colored in the next step
        (curr_color ?b - bool)  ;; this is a general variable which is set to true when a floodfill is activated
    )
    
    (:action start_action
        :parameters (?t - tile ?old_c ?new_c - color)
        :precondition  (and (not (color_value ?t ?new_c)) (color_value ?t ?old_c) (not (curr_color true)))  ;; get the old and the new color, make sure there is no floodfill yet
        :effect (and
            (curr_color true)  ;; set this to true, so the floodfill is now in action
            (color_value ?t ?new_c) (not (color_value ?t ?old_c))  ;; the color value of the tile should get changed right away
            
            (forall (?acc - tile)  ;; loop through every tile
                
                (when (and (is_neighbour ?t ?acc) (color_value ?acc ?old_c))  ;; check if the current tile is the neighbour of the acc tile and has the same color
                
                    (and (change_to_color ?acc ?new_c)  ;; mark the neighbour whith the color it will get changed to afterwards
                         (mark_tile ?acc)
                    )
            
                ) ;; when end
            )  ;; forall end
        )  ;; effect end
    )  ;; action end
    
    
    ;; at this point the current tile has already the right color marked, just the neighbours should get colored in the same color
    (:action -->
        :parameters (?t - tile ?old_c ?new_c - color)
        :precondition (and (color_value ?t ?old_c) (change_to_color ?t ?new_c) (curr_color true))  ;; current color, color wich it will get changed to, and only the marked tile, there must be a floodfill
        :effect (and
            (not (change_to_color ?t ?new_c))  ;; set back the marking
            (not (mark_tile ?t))
            (color_value ?t ?new_c) (not (color_value ?t ?old_c))  ;; the color value of the tile should get changed right away
            
            (forall (?acc - tile)  ;; loop through every tile
                
                (when (and (is_neighbour ?t ?acc) (color_value ?acc ?old_c))  ;; unsure for infinite loop
                
                    (and (change_to_color ?acc ?new_c)  ;; mark the neighbour whith the color it will get changed to afterwards
                         (mark_tile ?acc)
                    )
                   
                ) ;; when end
            )  ;; forall end
        )  ;; effect end
    )  ;; action end



    (:action end_action
        :parameters ()
        :precondition (and (curr_color true) (forall (?t - tile) (not (mark_tile ?t))))
        :effect (not (curr_color true))
    )  
)
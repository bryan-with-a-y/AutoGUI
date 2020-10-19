
path = [
        [(959, 548), (959, 548)], #south door1 from south door1
        [(959, 611), (959, 570)], #south chest1 from south door1
        [(872, 503), (959, 548)], #south door2 from south chest1
        [(959, 548),#south chest2 from south door2
        [(872, 503), (959, 548)],   #south door3 from south chest2
            #south chest3 from south door3
        [(960, 415), (960, 520)]    #north door1 from south chest3
            #north door2 from north door1
            #north door3 from north door2
            #starting position from north door 3
        [(960, 425), #north door from south chest. Repeat bottom pixel of door on fail
        [(1052, 503), #next north door from north door. This click only happens on success of door.
        [(961, 520), #same door from north position (if fail repeat this click)
        ]


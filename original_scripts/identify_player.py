def identify_hands(wrist_coords, hand_labels):

    #grabs y coordinate from wrist
    def sort_by_y(hand):
        return hand[0][1]

    #zip combines wrist coord and labels into tuples e.g.(0.5, 0.8), "rock")...
    #key = sort_by_y means sort by the y coordinate of the wrist
    #hands_with_labels is now sorted by y coordinate of wrist from lowest to highest
    hands_with_labels = sorted(zip(wrist_coords, hand_labels), key=sort_by_y) 
    my_hands = hands_with_labels[2:] #we know highest y cords are mine
    opponent_hands = hands_with_labels[:2] #lowest y cords are opponent's

    #sort my hands ascending to determine left and right
    my_hands = sorted(my_hands, key=lambda hand: hand[0][0])
    my_left = my_hands[0][1]
    my_right = my_hands[1][1]

    #sort opponent hands ascending to determine left and right
    opponent_hands = sorted(opponent_hands, key=lambda hand: hand[0][0])
    opponent_left = opponent_hands[0][1]
    opponent_right = opponent_hands[1][1]

    return {
        'my_left': my_left,
        'my_right': my_right,
        'opponent_left': opponent_left,
        'opponent_right': opponent_right
    }
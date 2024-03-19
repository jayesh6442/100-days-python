bid={}
def high_bidding(bidding_record):
    high_bid = 0
    winner = ""
    for bidder in bidding_record:
        bidding_prise = bidding_record[bidder]
        if bidding_prise > high_bid:
            high_bid = bidding_prise
            winner = bidder
    print(f"the winner in {winner} with {high_bid}")


is_bid_over= False
while not is_bid_over:
    name = input("Enter the name: ")
    biding = int(input("Enter the prise: "))
    bid[name] = biding
    over = input("Is bidding over: ")
    if over =="over":
        is_bid_over=True
        high_bidding(bid)

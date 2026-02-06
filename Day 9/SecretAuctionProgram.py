# Secret Auction Program
import logo

print(logo.logo)

def find_highest_bidder(bidding_dictionary):
  winner = ''
  highest_bid = 0
  
  max(bidding_dictionary)
  
  for bidder in bidding_dictionary:
    bid_amount = bidding_dictionary[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  
  
  print(f'The winner is {winner} with a bid of ${highest_bid}.')

bids = {}
continue_bidding = True
while continue_bidding:
  name = input('What is your name?: ')
  price = int(input('What is your bid?: $')) 
  bids[name] = price
  schould_continue = input('Are there any other bidders? Type "yes" or "no".\n').lower()
  if schould_continue == 'no':
    continue_bidding = False
    find_highest_bidder(bids)
  elif schould_continue == 'yes':
    print('\n' * 20)



# Nesting Lists and Dictionarys
# List{
#   Key: [List],
#   Key2: {Dict},
# }

capitals = {
  'France': 'Paris',
  'Germany': 'Berlin',
}

# Nested List in Dictionary
travel_log = {
  'France': ['Paris', 'Lille', 'Dijon'],
  'Germany': ['Stuttgart', 'Berlin'],
}

# print Lille
print(travel_log['France'][1])

# print D
nested_list = ['A', 'B', ['C', 'D']]
print(nested_list[2][1])

# list nested in dictionary
travel_log = {
  'France': {
    'cities_visited': ['Paris', 'Lille', 'Dijon'],
    'total_visits': 8,
    },
  'Germany': {
    'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
    'total_visits': 5
    },
}

# print Stuttgart
print(travel_log['Germany']['cities_visited'][2])
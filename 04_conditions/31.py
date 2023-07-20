
# *Ex31 - Develop a program that asks for the distance of a trip in kilometers. Calculate the ticket price, charging R$0.50 per Km for trips up to 200Km and R$0.45 for longer trips.

distance = int(input('Enter how many kilometers is the trip? '))
print(
    'The ticket price will cost R${:.1f}'.format(distance*0.5)
    if distance <= 200
    else 'O preço vai custar R${:.1f}'.format(distance*0.45)
)

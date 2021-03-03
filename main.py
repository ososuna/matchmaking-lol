#%%
import numpy as np
import matplotlib.pyplot as plt
import random
from progress.bar import ChargingBar
import time
from classes import *

p1 = Player('pinguinodelanasa', 150, 55, 'Bronze', 1, True, 'adc', 'jg')
p2 = Player('Charls Alonso', 146, 50, 'Bronze', 2, False, 'sup', 'top')
p3 = Player('Johiliwisky18', 98, 58, 'Silver', 3, True, 'jg', 'mid')
p4 = Player('nigaalan', 159, 56, 'Gold', 4, True, 'top', 'jg')
p5 = Player('Osiris', 365, 60, 'Gold', 1, True, 'mid', 'adc')

q1 = Queue('Silver')

t1 = Team(1)

users = ['Edgar', 'Pablo', 'Gerardo', 'Diego', 'Mariana', 'Carolina', 'Catherine', 'Gabo', 'Ivan', 'Luisa', 'Nahibi', 'Isabella', 'Brenda']
lanes = ['top', 'jg', 'mid', 'adc', 'sup']
mmr = 1350 + 320 * np.random.randn(100000)
wr = 50 + 8 * np.random.randn(100000)

k = int(np.ceil(1+np.log2(100000)))
plt.hist(mmr, bins=k)
plt.xlabel('MMR')
plt.ylabel('Players number')
plt.title('Rank distribution of players online')

# %%
def generate_rand_player():

    rand_mmr = round(np.random.choice(mmr), 2)
    rand_wr = round(np.random.choice(wr), 2)
    rand_rank = random.randint(1,4)
    rand_user = '{}{}{}'.format(np.random.choice(users), random.randint(0,9), random.randint(0,9))
    rand_level = random.randint(30, 550)
    rand_p_lane = np.random.choice(lanes)

    while(True):
        rand_s_lane = np.random.choice(lanes)
        if rand_p_lane != rand_s_lane:
            break
    
    if rand_mmr < 800:
        p = Player(rand_user, rand_level, rand_wr, 'Iron', rand_rank, True, rand_p_lane, rand_s_lane)
    elif 800 <= rand_mmr < 1000:
        p = Player(rand_user, rand_level, rand_wr, 'Bronze', rand_rank, True, rand_p_lane, rand_s_lane)
    elif 1000 <= rand_mmr < 1200:
        p = Player(rand_user, rand_level, rand_wr, 'Silver', rand_rank, True, rand_p_lane, rand_s_lane)
    elif 1200 <= rand_mmr < 1500:
        p = Player(rand_user, rand_level, rand_wr, 'Gold', rand_rank, True, rand_p_lane, rand_s_lane)
    elif 1500 <= rand_mmr < 1800:
        p = Player(rand_user, rand_level, rand_wr, 'Platinum', rand_rank, True, rand_p_lane, rand_s_lane)
    elif 1800 <= rand_mmr < 2200:
        p = Player(rand_user, rand_level, rand_wr, 'Diamond', rand_rank, True, rand_p_lane, rand_s_lane)
    elif 2200 <= rand_mmr < 2400:
        p = Player(rand_user, rand_level, rand_wr, 'Master', None, True, rand_p_lane, rand_s_lane)
    elif 2400 <= rand_mmr < 2600:
        p = Player(rand_user, rand_level, rand_wr, 'Grand Master', None, True, rand_p_lane, rand_s_lane)
    elif rand_mmr >= 2600:
        p = Player(rand_user, rand_level, rand_wr, 'Challenger', None, True, rand_p_lane, rand_s_lane)
    return p

for i in range(0,10000):
    p = generate_rand_player()
    if 1000 <= p.mmr < 1200:
        q1.insert_end(p)

t1 = Team(1)
t2 = Team(2)

q1.form_team(t1)
q1.form_team(t2)

m1 = Match(1, t1, t2)

def charge_bar(text):
    bar = ChargingBar(text, max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.05))
        bar.next()
    bar.finish()

print('\n\tLeague of Legends Matchmaking System\n')
charge_bar('Generating 10,000 random players')
time.sleep(1.5)
print('\nLooking for a match')
time.sleep(.5)
print('Estimated time: 00:{}\n'.format(random.randint(11,18)))

for i in range(0, random.randint(11,18)):
    if(i < 10):
        print('00:0{}'.format(i))
    else:
        print('00:{}'.format(i))
    time.sleep(1)

time.sleep(.5)
print('\nMatch founded!')
charge_bar('Feeding the Baron Nashor')
time.sleep(1)
print()
m1.print_match_stats()
print(m1)


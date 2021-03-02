
class Player:

    def __init__(self, user, level, winrate, division, rank, autofill, primary_lane, secondary_lane):
        self.__user = user
        self.__level = level
        self.__winrate = winrate
        self.__division = division
        self.__rank = rank
        self.__autofill = autofill
        self.__primary_lane = primary_lane
        self.__secondary_lane = secondary_lane
        self.__mmr = self.calculate_mmr()

    @property
    def user(self): 
        return self.__user
    
    @property
    def level(self): 
        return self.__level
    
    @property
    def winrate(self): 
        return self.__winrate
    
    @property
    def division(self): 
        return self.__division
    
    @property
    def rank(self): 
        return self.__rank

    @property
    def autofill(self): 
        return self.__autofill
    
    @property
    def primary_lane(self): 
        return self.__primary_lane
    
    @property
    def secondary_lane(self): 
        return self.__secondary_lane
    
    @property
    def mmr(self): 
        return self.__mmr
    
    @mmr.setter 
    def mmr(self, mmr):
        self.__mmr = mmr

    def calculate_mmr(self):
        if self.division == 'Iron':
            self.mmr = 200
            if self.rank == 1:
                self.mmr += 400
            elif self.rank == 2:
                self.mmr += 300
            elif self.rank == 3:
                self.mmr += 200
            elif self.rank == 4:
                self.mmr += 100
            self.mmr += (self.mmr*.1) * (self.winrate*.01)
        elif self.division == 'Bronze':
            self.mmr = 800
            if self.rank == 1:
                self.mmr += 160
            elif self.rank == 2:
                self.mmr += 120
            elif self.rank == 3:
                self.mmr += 80
            elif self.rank == 4:
                self.mmr += 40
        elif self.division == 'Silver':
            self.mmr = 1000
            if self.rank == 1:
                self.mmr += 160
            elif self.rank == 2:
                self.mmr += 120
            elif self.rank == 3:
                self.mmr += 80
            elif self.rank == 4:
                self.mmr += 40
        elif self.division == 'Gold':
            self.mmr = 1200
            if self.rank == 1:
                self.mmr += 200
            elif self.rank == 2:
                self.mmr += 150
            elif self.rank == 3:
                self.mmr += 100
            elif self.rank == 4:
                self.mmr += 50
        elif self.division == 'Platinum':
            self.mmr = 1500
            if self.rank == 1:
                self.mmr += 200
            elif self.rank == 2:
                self.mmr += 150
            elif self.rank == 3:
                self.mmr += 100
            elif self.rank == 4:
                self.mmr += 50
        elif self.division == 'Diamond':
            self.mmr = 1800
            if self.rank == 1:
                self.mmr += 240
            elif self.rank == 2:
                self.mmr += 180
            elif self.rank == 3:
                self.mmr += 120
            elif self.rank == 4:
                self.mmr += 60
        elif self.division == 'Master':
            self.mmr = 2200
        elif self.division == 'Grand Master':
            self.mmr = 2400
        elif self.division == 'Challenger':
            self.mmr = 2600
        
        if self.winrate >= 50:
            self.mmr += (self.mmr*.2) * (self.winrate*.01)
        else:
            self.mmr -= (self.mmr*.2) * ((50 - self.winrate) *.01)
        
        return self.mmr
    
    def __str__(self):
        return '\n{}\n{} {}\nLevel {}\nWin Rate: {}%\nPrimary lane: {}\nSecondary lane: {}'.format(self.user, self.division, self.rank, self.level, self.winrate, self.primary_lane, self.secondary_lane)

class Team:

    def __init__(self, id):
        self.__id = id
        self.__top = None
        self.__jg = None
        self.__mid = None
        self.__adc = None
        self.__sup = None
        self.__avg_mmr = None
    
    @property
    def id(self): 
        return self.__id
    
    @property
    def top(self): 
        return self.__top

    @top.setter 
    def top(self, top):
        self.__top = top
    
    @property
    def jg(self): 
        return self.__jg

    @jg.setter 
    def jg(self, jg):
        self.__jg = jg

    @property
    def mid(self): 
        return self.__mid

    @mid.setter 
    def mid(self, mid):
        self.__mid = mid
    
    @property
    def adc(self): 
        return self.__adc

    @adc.setter 
    def adc(self, adc):
        self.__adc = adc
    
    @property
    def sup(self): 
        return self.__sup

    @sup.setter 
    def sup(self, sup):
        self.__sup = sup
    
    @property
    def avg_mmr(self): 
        return self.__avg_mmr
    
    @avg_mmr.setter 
    def avg_mmr(self, avg_mmr):
        self.__avg_mmr = avg_mmr

    def calculate_avg_mmr(self):
        if self.top and self.jg and self.mid and self.adc and self.sup:
            total_mmr = self.top.mmr + self.jg.mmr + self.mid.mmr + self.adc.mmr + self.sup.mmr
            self.avg_mmr = total_mmr / 5
            return self.avg_mmr
    
    def __str__(self):
        return '\ntop: {}\njg: {}\nmid: {}\nadc: {}\nsup: {}'.format(self.top.user, self.jg.user, self.mid.user, self.adc.user, self.sup.user)

class Match:
    
    def __init__(self, id, red_team, blue_team):
        self.__id = id
        self.__red_team = red_team
        self.__blue_team = blue_team
    
    @property
    def id(self): 
        return self.__id
    
    @property
    def red_team(self): 
        return self.__red_team

    @red_team.setter 
    def red_team(self, red_team):
        self.__red_team = red_team

    @property
    def blue_team(self): 
        return self.__blue_team

    @blue_team.setter 
    def blue_team(self, blue_team):
        self.__blue_team = blue_team
    
    def print_match_stats(self):
        print('Red Team\n{}\n{}\n{}\n{}\n{}\nBlue Team\n{}\n{}\n{}\n{}\n{}\n'.format(self.red_team.top, self.red_team.mid, self.red_team.jg, self.red_team.adc, self.red_team.sup, self.blue_team.top, self.blue_team.mid, self.blue_team.jg, self.blue_team.adc, self.red_team.sup))

    def __str__(self):
        return '\nRed Team\nAverage MMR: {}{}\n\nBlue Team\nAverage MMR: {}{}'.format(self.red_team.calculate_avg_mmr(), self.red_team, self.blue_team.calculate_avg_mmr(), self.blue_team)

class Link:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_end(self, newdata):
        new_link = Link(newdata)
        if self.head is None:
            self.head = new_link
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=new_link

    def remove(self, key):
        head_value = self.head

        if (head_value is not None):
            if (head_value.value == key):
                self.head = head_value.next
                head_value = None
                return

        while (head_value is not None):
            if head_value.value == key:
                break
            prev = head_value
            head_value = head_value.next

        if (head_value == None):
            return

        prev.next = head_value.next
        head_value = None

    def print_list(self):
        printval = self.head
        while printval is not None:
            print (printval.value)
            printval = printval.next
    

class Queue(SLinkedList):
    
    def __init__(self, elo):
        super().__init__()    
        self.server = 'LAN'
        self.__elo = elo
    
    def form_team(self, team):
        player = self.head
        found_top = False
        found_jg = False
        found_mid = False
        found_adc = False
        found_sup = False
        
        while(player.next):
            if player.value.primary_lane == 'top' and (not found_top):
                team.top = player.value
                found_top = True
            elif player.value.primary_lane == 'jg' and (not found_jg):
                team.jg = player.value
                found_jg = True
            elif player.value.primary_lane == 'mid' and (not found_mid):
                team.mid = player.value
                found_mid = True
            elif player.value.primary_lane == 'adc' and (not found_adc):
                team.adc = player.value
                found_adc = True
            elif player.value.primary_lane == 'sup' and (not found_sup):
                team.sup = player.value
                found_sup = True
            
            self.remove(player.value)

            if found_top and found_jg and found_mid and found_adc and found_sup:
                break
            else:    
                player = player.next


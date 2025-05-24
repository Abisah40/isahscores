import requests


api_key = 'c64VNZpc1sCivJFW'
secret = 'awYDHbZUTgSG8wklCogqoGCq8eJDYoA9'
# the above free livescore Api expires after 14 days
print('ISAH_SCORES')

def livescore(live):
    
    if game == 'today':
        def today():

            print('Today')
            '''retrive today  matches''' 
            
            url = f'https://livescore-api.com/api-client/fixtures/list.json?/fixtures/list.json?&key={api_key}&secret={secret}'

            response = requests.get(url)
            #print(response)

            if response.status_code == 200:
                data = response.json()
                #print(data)
                data_1 = data.get('data')
                data_2 = data_1.get('fixtures')
                #print(data_2)
                for data_3 in data_2:
                    # print(data_3)

                    if data_3:
                        if data_3['federation'] == None:
                                
                            print(f'COUNTRY : {data_3.get('country', {}).get('name', 'none')}')
                            print(f'LEAGUE : {data_3.get('competition', {}).get('name', 'none')}')
                            print(f'TEAM : {data_3.get('home', {}).get('name', 'none')} vs {data_3.get('away', {}).get('name', 'none')}') 
                            print(f"Score : {data_3.get('scores', {}).get('score', 'none')}")
                            print(f'status : {data_3.get('status')}') 
                            print(f'schedule : {data_3.get('date')}')
                            print(f'time : {data_3.get('time')}')
                            print('')

                        else:
                            print(f'FEDERATION : {data_3.get('federation', {}).get('name', 'none')}')
                            print(f'LEAGUE : {data_3.get('competition', {}).get('name', 'none')}')
                            print(f'TEAM : {data_3.get('home', {}).get('name', 'none')} vs {data_3.get('away', {}).get('name', 'none')}') 
                            print(f"Score : {data_3.get('scores', {}).get('score', 'none')}")
                            print(f'status : {data_3.get('status')}') 
                            print(f'schedule : {data_3.get('date')}')
                            print(f'time : {data_3.get('time')}')
                            print(f"{data_3.get('score')}")

                    else:
                        print('no match available currently...')
        today()
    elif game == 'live':
        
        def live():
                        
            print('Live')
            '''retrive live  matches and results''' 
            url = f'https://livescore-api.com/api-client/matches/live.json?key={api_key}&secret={secret}&lang=ar'
            response = requests.get(url)
            if response.status_code == 200:

                data = response.json()
                #print(data)
                data_1 = data.get('data')
                data_2 = data_1.get('match')
                #print(data_2)
                if data_2 != []:
                        
                    for data_3 in data_2:
                        #print(data_3)
                        home = data_3.get('home', [])
                        away = data_3.get('away', [])
                        matches = data_3.get('data')
                        #print(matches)
                        if matches != []:
                            if data_3['status'] == 'IN PLAY':

                                
                                if data_3['federation'] == None:
                                    print(' ')
                                    print(f'COUNTRY :  {data_3.get('country', {}).get('name', 'none')}')
                                    print(f'LEAGUE :   {data_3.get('competition', {}).get('name', 'none')}')
                                    print(f'TEAM :     {home.get('name')}  vs {away.get('name')}')
                                    print(f"Score :    {data_3.get('scores', {}).get('score', 'none')}")
                                    print(f'status :   {data_3.get('status')}') 
                                    print(f'schedule : {data_3.get('scheduled')}')
                                    print(f'time :     {data_3.get('time')}')
                                    print(' ')
                                    
                                
                                else:
                                    print(f'FEDERATION : {data_3.get('federation', {}).get('name', 'none')}')
                                    print(f'LEAGUE :     {data_3.get('competition', {}).get('name', 'none')}')
                                    print(f'TEAM :       {home.get('name')}  vs {away.get('name')}')
                                    print(f"Score :      {data_3.get('scores', {}).get('score', 'none')}")
                                    print(f'status :     {data_3.get('status')}') 
                                    print(f'schedule :   {data_3.get('scheduled')}')
                                    print(f'time :       {data_3.get('time')}')

                    gam =input((('enter statistics / live / no: ').title()).strip()).lower()
                    if gam == 'statistics':
                        url = f'https://livescore-api.com/api-client/matches/live.json?key={api_key}&secret={secret}&lang=ar'
                        response = requests.get(url)
                        if response.status_code == 200:

                            data = response.json()
                            #print(data)
                            data_1 = data.get('data')
                            data_2 = data_1.get('match')
                           
                            if data_2 != []:
                                match = input(('select team statistics: ').title()).strip()

                                for data_3 in data_2:
                                
                                    home = data_3.get('home', [])
                                    away = data_3.get('away', [])
                                
                                    team_1 = home.get('name','none')
                                    team_2 = away.get('name','none')
                                
                                    team_1_id = data_3.get('id','none')
                                    team_2_id = data_3.get('id','none')
                                
                                    if match == team_1 or match == team_2:
                                    
                                        url = f'https://livescore-api.com/api-client/matches/stats.json?match_id={team_1_id}&key={api_key}&secret={secret}'
                                        response = requests.get(url)
                                        data = response.json()
                                        #print(data)
                                        d = data.get('data','none')
                                        print('STATISTICS')
                                        print(f'TEAM :            {home.get('name')}  vs {away.get('name')}')
                                        print(f"Score :                         {data_3.get('scores', {}).get('score', 'none')}")
                                        print(f"Yellow Cards:                   {d.get('yellow_cards','none')}")
                                        print(f"Red Cards:                      {d.get('red_cards','none')}")
                                        print(f"Substitutions:                  {d.get('substitutions','none')}")
                                        print(f"Possesion                       {d.get('possesion','none')}")
                                        print(f"free_kicks:                     {d.get('free_kicks','none')}")
                                        print(f"goal_kicks:                     {d.get('goal_kicks','none')}")
                                        print(f"offsides:                       {d.get('offsides','none')}")
                                        print(f"corners:                        {d.get('corners','none')}")
                                        print(f"shots_on_target:                {d.get('shots_on_target','none')}")
                                        print(f"shots_off_target:               {d.get('shots_off_target','none')}")
                                        print(f"saves:                          {d.get('saves','none')}")
                                        print(f"fauls:                          {d.get('fauls','none')}")
                                        print(f"penalties:                      {d.get('penalties','none')}")
                                        print(f"shots_blocked:                  {d.get('shots_blocked','none')}")
                    elif gam == 'live':
                        live()
                    else:
                        return
                                                     
            else:
                print('no live match available currently...')
        live()

    elif game == 'stand':
        print('Standings')
        '''retrive league standings''' 
        #from tabulate import tabulate

        def standings():
            menu = {
                'germany':1,'england':2,'spain':3,'italy':4,'france':5,'turkey':6,'russia':7,'portugal':8,'greece':9,'iceland':10,'ireland':11,'Luxembourg':12,
                'norway':13,'sweden':14,'switzerland':15,'belarus':16,'croatia':17,'estonia':18,'hungary':19,'latvia':20,'montenegro':21,'slovenia':22,'argentina':23,
                'brasil':24,'chile':25,'china':26,'indonesia':27,'japan':28,'singapore':29,'thailand':30,'azerbaijan':31,'georgia':32,'kuwait':33,'iran':34,'algeria':35,
                'egypt':36,'kanya':37,'morocco':38,'vietnam':39,'denmark':40,'south africa':41,'tunisia':42,'austria':43,'cyprus':44,'maxico':45,'venezuela':46,'peru':47,
                'urugua':48,'ecuador':50,'finland':57,'korea':66,'australia':67,'belgium':68,'northern ireland':69,'czech':72,'isreal':73,'scotland':75,'usa':76,
                'england championship':77,'nigeria':78
            }
            name = menu[competition]

            url = f'https://livescore-api.com/api-client/competitions/table.json?competition_id={name}&key={api_key}&secret={secret}'
            response = requests.get(url)
            #print(response)
            if response.status_code == 200:
                data = response.json()
                #print(data)
                data_1 = data.get('data', {}).get('stages', {})
                league = data.get('data', {}).get('competition',{}).get('name','none')
                print(league)
                print(' postion    T   P   GF   GA   GD   L   D   W')
                print(' ')
                # headers = ['position','Teams','Points','GF','GA','GD','L','D','W']
                # print(headers)
                for i in data_1:
                    #print(i)
                    data_2 = i.get('groups',{})
                    for x in data_2:
                        data_3 = x.get('standings',[])
                        for y in data_3:
                            a = y.get('rank', 'none')
                            b = y.get('matches', 'none')
                            c = y.get('points', 'none')
                            d = y.get('goals_scored', 'none')
                            e = y.get('goals_conceded', 'none')
                            f = y.get('goal_diff', 'none')
                            g = y.get('lost', 'none')
                            h = y.get('drawn', 'none')
                            j = y.get('won', 'none')
                            k = y.get('team', 'none').get('name','none')
                            print(f'{a}: {k}  {b}  {c}  {d}  {e}  {f}  {g}  {h}  {j}')
                            print(' ')
                            # tab = [
                            #     {'position' :a,'Teams': k, 'matches' :b, 'points':c, 'GF': d, 'GA' :e, 'GD' :f, 'L' :g, 'D' :h, 'W' :j}
                            #     ]
                            # table = tabulate(tab,headers = 'keys',tablefmt='pipe',colalign=('left'))
        
                            # print(table)

        competition = input('enter country: ').lower()
        standings()

    elif game == 'yesterday':
        print('Yesterday')

        '''retrive yesterday matches and their results''' 
        url = f'https://livescore-api.com/api-client/matches/history.json?&key={api_key}&secret={secret}'

        response = requests.get(url)
        #print(response)
        if response.status_code == 200:
            data = response.json()
            #print(data)
            data_1 = data['data']
            data_2 = data_1.get('match', [])
            #print(data_2)
            for data_3 in data_2:
                #print(data_3)
                if data_3:
                    #print(data_3['country']['name'])
                    print(f"COUNTRY : {data_3.get('country', {}).get('name', 'none')}")
                    print(f"LEAGUE: {data_3.get('competition', {}).get('name', 'none')}")
                    print(f"DATE: {data_3.get('date',{})}")
                    print(f'TEAMS: {data_3.get('home',{}).get('name','none')} vs {data_3.get('away',{}).get('name','none')}')
                    print(f"SCORES: {data_3.get('scores',{}).get('score','none')}")
                    print(f"SCHEDULED: {data_3.get('scheduled','none')}")
                    print(f"STATUS: {data_3.get('status','none')}")
                    print(f"TIME: {data_3.get('time','none')}")
                    print(' ')
                else:
                    print('no match is available...')
            gam =input((('enter statistics / no: ').title()).strip()).lower()
            if gam == 'statistics':
                url = f'https://livescore-api.com/api-client/matches/history.json?&key={api_key}&secret={secret}'
                response = requests.get(url)
                #print(response)
                if response.status_code == 200:

                    data = response.json()
                    #print(data)
                    data_1 = data.get('data')
                    data_2 = data_1.get('match')
                    
                    match = input(('select team statistics: ').title()).strip()

                    for data_3 in data_2:
                    
                        home = data_3.get('home', [])
                        away = data_3.get('away', [])
                    
                        team_1 = home.get('name','none')
                        team_2 = away.get('name','none')
                        
                        team_1_id = data_3.get('id','none')
                        team_2_id = data_3.get('id','none')
                    
                        if match == team_1 or match == team_2:
                        
                            url = f'https://livescore-api.com/api-client/matches/stats.json?match_id={team_1_id}&key={api_key}&secret={secret}'
                            response = requests.get(url)
                            data = response.json()
                            # print(data)
                            d = data.get('data','none')
                            print('STATISTICS')
                            print(f'TEAM :            {home.get('name')}  vs {away.get('name')}')
                            print(f"Score :                         {data_3.get('scores', {}).get('score', 'none')}")
                            print(f"Yellow Cards:                   {d.get('yellow_cards','none')}")
                            print(f"Red Cards:                      {d.get('red_cards','none')}")
                            print(f"Substitutions:                  {d.get('substitutions','none')}")
                            print(f"Possesion                       {d.get('possesion','none')}")
                            print(f"free_kicks:                     {d.get('free_kicks','none')}")
                            print(f"goal_kicks:                     {d.get('goal_kicks','none')}")
                            print(f"offsides:                       {d.get('offsides','none')}")
                            print(f"corners:                        {d.get('corners','none')}")
                            print(f"shots_on_target:                {d.get('shots_on_target','none')}")
                            print(f"shots_off_target:               {d.get('shots_off_target','none')}")
                            print(f"saves:                          {d.get('saves','none')}")
                            print(f"fauls:                          {d.get('fauls','none')}")
                            print(f"penalties:                      {d.get('penalties','none')}")
                            print(f"shots_blocked:                  {d.get('shots_blocked','none')}")

        
game = input((('enter live / today / stand / yesterday:  ').title()).strip()).lower()
livescore('live')





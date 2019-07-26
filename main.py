from RiotApi import RiotApi
import RiotConst as Consts
import pprint

def main():
    api = RiotApi('RGAPI-1cfcbc31-b14b-48aa-a083-e387b72474f2')
    summoners = []

    for value in Consts.NAMES:
        summoner = api.get_summoner_by_name(value['name'], value['region'])
        
        formattedSummoner = {
            'accountId': summoner['accountId'],
            'name': value['name'],
            'region': value['region']
        }

        summoners.append(formattedSummoner)

    for value in summoners: 
        print(value)
        

    pp = pprint.PrettyPrinter()
    pp.pprint(summoners)


    #data = api.get_match_history(summoner['accountId'])
    
    #matchList = []

    #for value in data['matches']:
    #    matchList.append(api.get_individual_match(value['gameId']))

    #print(matchList)

if __name__ == "__main__":
    main()
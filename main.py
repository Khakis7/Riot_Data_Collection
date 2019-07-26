from RiotApi import RiotApi
from Excel import Excel

def main():
    api = RiotApi('RGAPI-ed88f27a-3734-4174-add0-d7b790f684ac')
    accountId = api.get_summoner_by_name('C9 Sneaky')['accountId']
    data = api.get_match_history(accountId)
    
    matchList = []

    for value in data['matches']:
        matchList.append(api.get_individual_match(value['gameId']))

    print(matchList)

if __name__ == "__main__":
    main()
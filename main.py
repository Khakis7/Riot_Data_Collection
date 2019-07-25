from RiotApi import RiotApi

def main():
    api = RiotApi('RGAPI-c3577aa9-cf34-464c-8fc0-98c4d4c71644')
    r = api.get_summoner_by_name('C9 Sneaky')

if __name__ == "__main__":
    main()
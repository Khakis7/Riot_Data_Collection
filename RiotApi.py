import RiotConst as Consts
import requests

class RiotApi(object) :
    def __init__(self, api_key, region = Consts.REGION['north-america']):
        self.api_key = api_key
        self.region = region
        
    def _request(self, api_url, params = {}):
        args = {'api_key': self.api_key}

        for key, value in params.items():
            if key not in args:
                args[key] = value
        
        response = requests.get(
            Consts.URL['base'].format(
                region=self.region,
                url=api_url
                ),
            params=args
            )
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSION['summoner'],
            names=name
        )

        return self._request(api_url)

    def get_match_history(self, accountId):
        api_url = Consts.URL['match_history'].format(
            version=Consts.API_VERSION['summoner'],
            accountId=accountId
        )

        return self._request(api_url)

    def get_individual_match(self, matchId):
        api_url = Consts.URL['individual_match'].format(
            version=Consts.API_VERSION['summoner'],
            matchId=matchId
        )

        return self._request(api_url)

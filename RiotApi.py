import RiotConst as Consts
import requests

class RiotApi(object) :
    def __init__(self, api_key, region = Consts.REGION['north-america']):
        self.api_key = api_key
        self.region = region
        
    def _request(self, api_url, params = {}):
        args = {'api_ley': self.api_key}

        for key, value in params.items():
            if key not in args:
                args[key] = value
        
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
                ),
            params=args
            )
        print response.url
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSION['summoner'],
            names=name
        )

        return self._request(api_url)
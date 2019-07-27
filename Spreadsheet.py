import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Spreadsheet(object):
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
        client = gspread.authorize(creds)

        self.sheet = client.open('McGee Analytics - Dashboard').sheet1

    def insertPlayer(self):
        playerRow = ['Chovy - Griffen']
        headerRow = ['Champion', 'Opponent Champion', 'Summoner Spells', 'Major Rune', 'Minor Runes 1-5', 'The three stat runes (atk speed etc)', 'Starting Item', 'First Item', 'Final Build']
        statsRow = ['Lucian', 'Ashe', 'Flash / Heal', 'Lethal Tempo', 'Random Runes', 'Random Stats', 'Doran Shield', 'Rapid Fire Cannon', 'Some Bullshit Tear Build']
        
        self.sheet.insert_row(playerRow, 1)
        self.sheet.insert_row(headerRow, 2)
        self.sheet.insert_row(statsRow, 3)
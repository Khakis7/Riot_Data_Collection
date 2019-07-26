import pygsheets

def main():
    scopes = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    gc = pygsheets.authorize()

def other():
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scopes)
    client = gspread.authorize(creds)

    sheet = client.open('Data Collection').sheet1

    playerRow = ['Chovy - Griffen']
    headerRow = ['Champion', 'Opponent Champion', 'Summoner Spells', 'Major Rune', 'Minor Runes 1-5', 'The three stat runes (atk speed etc)', 'Starting Item', 'First Item', 'Final Build']
    statsRow = ['Lucian', 'Ashe', 'Flash / Heal', 'Lethal Tempo', 'Random Runes', 'Random Stats', 'Doran Shield', 'Rapid Fire Cannon', 'Some Bullshit Tear Build']
    
    sheet.insert_row(playerRow, 1)
    sheet.insert_row(headerRow, 2)
    sheet.insert_row(statsRow, 3)

if __name__ == '__main__':
    main()
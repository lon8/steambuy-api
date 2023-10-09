import requests
from src.selenium.getsessionid import get_cookies, get_sessionid
from db.tables.funcs import get_bot_steamid


headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'timezoneOffset=10800,0; browserid=2712913428713093758; steamLoginSecure=76561199161845250%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQ1RF8yMzQ2M0Q4OV84OTc1OSIsICJzdWIiOiAiNzY1NjExOTkxNjE4NDUyNTAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5Njg3OTI5NywgIm5iZiI6IDE2ODgxNTI3NzAsICJpYXQiOiAxNjk2NzkyNzcwLCAianRpIjogIjBENDlfMjM0NjNEOERfMzA0NDMiLCAib2F0IjogMTY5Njc5Mjc2OSwgInJ0X2V4cCI6IDE3MTQ4NzA4NjksICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxOTguMTYuNzguNDUiLCAiaXBfY29uZmlybWVyIjogIjE5OC4xNi43OC40NSIgfQ.jt1ST6o0IhsONV0Ry2Xex7MzQW-qlVTAx7geCqGDFFcHZ5kPj1cIoq6p2__rAQsvx3E8Dw3R9UfcST8fKi56CQ; sessionid=7c27b57e2f6331c779f6bedc; steamCountry=RU%7C877da95dd6f9e5eeb7666f16247f4f4e; rgTopicView_General_4009259_30=%7B%22864973577904147767%22%3A1696847986%7D',
    'Origin': 'https://steamcommunity.com',
    'Referer': 'https://steamcommunity.com/id/Cree7',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.962 YaBrowser/23.9.1.962 Yowser/2.5 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

data = {
    'sessionID': '7c27b57e2f6331c779f6bedc',
    'steamid': '76561198079962421', # Также здесь будем менять SteamID на ID бота, которого выбрала программа   
    'accept_invite': '0',
}

def add_in_friends(bot_id : int):
    
    steam_id = get_bot_steamid(bot_id=bot_id)
    
    data['steamid'] = steam_id

    cookies = get_cookies()
    # Меняем куки на новые, на заголовки пофиг
    headers['Cookie'] = '; '.join([f'{cookie["name"]}={cookie["value"]}' for cookie in cookies])

    session_id = get_sessionid(cookies=cookies)
    # Меняем sessionID
    data['sessionID'] = session_id

    response = requests.post('https://steamcommunity.com/actions/AddFriendAjax', headers=headers, data=data)

    print(response.status_code)

    print(response.text)
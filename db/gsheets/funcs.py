# Engine imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread import Spreadsheet, Client
from decouple import config


URL = config("GTABLE_URL") # Ссылка на таблицу
credentials_path = 'db/gsheets/res/credits.json'

# Область видимости
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)

client : Client = gspread.authorize(credentials)

worksheet : Spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/14vw2GQZ8BGQGoOOG8qcCOCrEDRB-ZEZM-VSLEJUnHjQ/edit#gid=0').get_worksheet(0)

# Дальше будут функции, которые будем использовать для записи в Таблицу

# Для создания столбцов в таблице
def start(worksheet : Spreadsheet) -> None:
    new_headers = [
        "Лир в сутки",
        "Лир в неделю",
        "Лир в месяц",
        "Рублей в сутки",
        "Рублей в неделю",
        "Рублей в месяц",
        "Комиссия в зависимости от способа оплаты (эквайринг)",
        "Торговая наценка или цена  в виде фикс значения в рублях",
        "Налоговая ставка",
        "Общая история покупок в ботах"
    ]

    # Обновляем заголовки
    for i, header in enumerate(new_headers):
        worksheet.update_cell(1, i+1, header)
    
    return



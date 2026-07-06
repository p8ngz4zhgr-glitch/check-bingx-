import requests
import json

# Endpoint lấy danh sách tất cả các cặp Perpetual Futures trên BingX
url = "https://open-api.bingx.com/openApi/swap/v2/quote/symbols"

try:
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        # Tìm tất cả các mã có chứa từ khóa 'XAU'
        gold_symbols = [
            item['symbol'] 
            for item in result['data']['symbols'] 
            if 'XAU' in item['symbol']
        ]
        
        if gold_symbols:
            print("--- CÁC MÃ VÀNG TÌM ĐƯỢC TRÊN BINGX ---")
            for symbol in gold_symbols:
                print(f"Mã chính xác: {symbol}")
        else:
            print("Không tìm thấy mã nào chứa 'XAU'. Thử tìm với 'XAUT'...")
            # Thử tìm với XAUT nếu không thấy XAU
            xaut_symbols = [
                item['symbol'] 
                for item in result['data']['symbols'] 
                if 'XAUT' in item['symbol']
            ]
            print(f"Kết quả tìm XAUT: {xaut_symbols}")
    else:
        print(f"Lỗi kết nối API: {response.status_code}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

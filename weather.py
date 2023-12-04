import requests
import json
import time

# OpenWeatherMap API 설정
apikey = "8043ad19fc304c6deb2651297b9b1bdc"
city = "Busan"
lang = "kr"

# 아두이노 wemos IP 주소
node_mcu_ip = '192.168.0.5'  

def send_command_to_nodemcu(command):
    """NodeMCU로 HTTP GET 요청을 보내는 함수"""
    requests.get(f'http://{node_mcu_ip}/motor?state={command}')

while True:
    # 날씨 API 
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
    result = requests.get(api_url)
    data = json.loads(result.text)

    # 날씨 정보 
    print(data["name"],"의 날씨입니다.")
    weather_condition = data["weather"][0]["main"]
    print(weather_condition)
    
    
    if weather_condition.lower() == 'clear':
        send_command_to_nodemcu('close')
        print("Closed")
    else:
        send_command_to_nodemcu('open')
        print("Opened")
    
    # 2분마다 반복
    time.sleep(120)




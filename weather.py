import requests
def get_weather(city):
    api_key="https://wttr.in"
    url=f"{api_key}/{city}?format=%c+%t"
    
    response=requests.get(url)
    
    if response.status_code==200:
        return response.text
    else:
        return "error"
    
if __name__ =="__main__":
    city=input("enter city: ")
    weather=get_weather(city)
    print(f"weather in {city}: {weather}")
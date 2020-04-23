import requests


def Covidapi(country):
    url = "https://coronavirus-map.p.rapidapi.com/v1/summary/region"

    querystring = {"region": country}

    headers = {
        'x-rapidapi-host': "coronavirus-map.p.rapidapi.com",
        'x-rapidapi-key': "93cc996576mshe334962bc994652p141711jsnf9a80f8be139"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = response.json()
    country_data = json_data['data']["summary"]

    total_cases = country_data['total_cases']
    active_cases = country_data['active_cases']
    deaths = country_data['deaths']
    recovered = country_data['recovered']

    response = f"Total Number of cases in {country} are: \nTotal Cases: {total_cases} \nActive Cases: {active_cases} \nDeaths: {deaths} \nRecovered: {recovered}\nStay Home, Stay Safe, and keep SocialDistancing "

    return response


def world_info():

    url = "https://api.covid19api.com/summary"
    res = requests.get(url)
    data = res.json()
    world_data = data['Global']

    total_cases = world_data['TotalConfirmed']
    new_cases = world_data['NewConfirmed']
    deaths = world_data['TotalDeaths']
    recovered = world_data['TotalRecovered']
    respo = f"\nTotal Cases: {total_cases} \nNw Cases: {new_cases} \nTotal Deaths: {deaths} \nTotal Recovered: {recovered}\nStay Home, Stay Safe, and keep SocialDistancing "

    return respo


def indiastate(statename):
    url = "https://coronavirus-tracker-india-covid-19.p.rapidapi.com/api/getStatewise"

    headers = {
        'x-rapidapi-host': "coronavirus-tracker-india-covid-19.p.rapidapi.com",
        'x-rapidapi-key': "93cc996576mshe334962bc994652p141711jsnf9a80f8be139"
    }

    res = requests.request("GET", url, headers=headers)
    data = res.json()
    state = []
    statename = statename.title()
    for i in range(len(data)):
        if data[i]["name"] == statename:
            state.append(data[i]['cases'])
            state.append(data[i]['recovered'])
            state.append(data[i]['deaths'])

    total_cases = state[0]
    recovered = state[1]
    deaths = state[2]

    respo = f"\nTotal Number of cases in {statename} are: \nTotal Cases: {total_cases} \nTotal Deaths: {deaths} \nTotal Recovered: {recovered}\nStay Home, Stay Safe, and keep SocialDistancing "

    return respo


import requests

def search_movies(title=None, 
                imdb_id=None, 
                year=None, 
                r_type='movie',
                plot='short', 
                api_key=None
    ):
    parameters = {'apikey': api_key}
    if title:
        parameters['t'] = title
    # if imdb_id:
    #     parameters['i'] = imdb_id
    if year:
        parameters['y'] = year
    # if r_type:
    #     parameters['type'] = r_type
    # if plot:
        # parameters['plot'] = plot
        
    response = requests.get('http://www.omdbapi.com/', params=parameters)

    if response.status_code != 200:
        print(f'Ошибка запроса {response.status_code}')
        return None
    
    response_data = response.json()
    
    if response_data['Response'] == 'False':
        print(response_data['Error'])
        return None
    
    return response_data
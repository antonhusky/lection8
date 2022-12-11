import requests

api_host = 'https://akabab.github.io/superhero-api/api'
api_endpoint = '/all.json'


class Superhero:
    def get_superhero_by_name(name):
        response = requests.get(api_host + api_endpoint)
        if response.status_code == 200:
            for superhero in response.json():
                if superhero['name'] == name:
                    return superhero
        return None

    def get_powerstats(superhero):
        return superhero['powerstats']


hulk = Superhero.get_superhero_by_name('Hulk')
Captain_America = Superhero.get_superhero_by_name('Captain America')
Thanos = Superhero.get_superhero_by_name('Thanos')

hulk_powerstats = Superhero.get_powerstats(hulk)
Captain_America_powerstats = Superhero.get_powerstats(Captain_America)
Thanos_powerstats = Superhero.get_powerstats(Thanos)

hulk_intelligence = hulk_powerstats['intelligence']
Captain_America_intelligence = Captain_America_powerstats['intelligence']
Thanos_intelligence = Thanos_powerstats['intelligence']

print('Hulk intelligence: ', hulk_intelligence)
print('Captain_America intelligence: ', Captain_America_intelligence)
print('Thanos intelligence: ', Thanos_intelligence)

if hulk_intelligence > Captain_America_intelligence and hulk_intelligence > Thanos_intelligence:
    print('Hulk is the most intelligent')
elif Captain_America_intelligence > hulk_intelligence and Captain_America_intelligence > Thanos_intelligence:
    print('Captain America is the most intelligent')
elif Thanos_intelligence > hulk_intelligence and Thanos_intelligence > Captain_America_intelligence:
    print('Thanos is the most intelligent')
else:
    print('There is no most intelligent')

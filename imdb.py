import requests, json, time
import os.path
class tvdbAPI():
  URL_base = 'https://api.thetvdb.com'
  favorites = 'favorites.txt'
  def __init__(self,apiKey,username,userkey):
    print("Generating new connection with tvdb. Logging in...")
    self.token = ''
    self.apiKey = apiKey
    self.username = username
    self.userkey = userkey
    self.sesh = requests.session()
    self.generateHeader()
    response = self.sesh.post(tvdbAPI.URL_base+'/login', headers = self.headers, data = json.dumps({
      "apikey":self.apiKey,
      "username":self.username,
      "userkey":self.userkey
      }))
    if response.status_code == requests.codes.ok:
      self.token = response.json()['token']
      self.generateHeader()
      print('successfully retrieved token. Token: '+self.token)
    else:
      print("Unable to retrieve token.")

  def generateHeader(self):
    self.headers = {'Content-type': 'application/json',
      'Authorization': "Bearer " + self.token,
      'Accept-Language':'en'}

  def refreshToken(self):
    response = self.sesh.get(tvdbAPI.URL_base+'/refresh_token', headers = self.headers)
    if response.status_code == requests.codes.ok:
      self.token = response.json()['token']
      print("successfully refreshed token. Token: "+ self.token)
      self.generateHeader()
    else:
      print("could not refresh token.")
  def addSeries(self, name, season, episode):
    response = self.sesh.get(tvdbAPI.URL_base+'/search/series', headers = self.headers, params = {"name":name})
    if response.status_code == requests.codes.ok:
      print("found requested TV series.")
      seriesID =response.json()["data"][0]["id"]
      with open(tvdbAPI.favorites,'a+') as file:
        file.write(str(seriesID) + '\n')
      return True
    else:
      print("something went wrong here...")
      print(response.text)
      return False
  def getInfo(self,name):
    print("looking for info about: "+ str(name))
    response = self.sesh.get(tvdbAPI.URL_base+'/series/'+str(name), headers=self.headers, params=({id:name}))
    print(response.text)

newSesh = tvdbAPI(apiKey,username,userkey)
#time.sleep(2)
#print('requesting new token...')
#newSesh.refreshToken()
if not os.path.isfile(tvdbAPI.favorites):
  newSesh.addSeries("Halt and Catch Fire", 3, 0)
  newSesh.addSeries("Silicon Valley", 4, 0)
  newSesh.addSeries("Westworld" 1, 0)
else:
  with open(tvdbAPI.favorites,'r') as favs:
    for line in favs:
      newSesh.getInfo(line.rstrip())


#print(headers)
#result = client.post(loginURL, data=login_data,headers=headers)
#result = client.get(refreshURL, headers=headers, data = json.dumps({}))
#print(result.text)
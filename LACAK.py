import sys
import requests
import json
import time

def banner():
	print('''
  ______ _          ______ _       
 |  ____(_)        |  ____| |      
 | |__   _ _ __ ___| |__  | |_   _ 
 |  __| | | '__/ _ \  __| | | | | |
 | |    | | | |  __/ |    | | |_| |
 |_|    |_|_|  \___|_|    |_|\__, |
                              __/ |
                             |___/ 
	Author: Lexxrt
	Github: https://github.com/Lexxrt             
	''')

def main():
	banner()
	number = input('\33[m[\033[93m?\33[m] MASUKKAN NOMER TELEPON COK > \x1b[1;92m')
	output = requests.get(f'http://phone-number-api.com/json/?number={number}').text
	obj = json.loads(output)
		
	query = obj['query']
	status = obj['status']
	numberType = obj['numberType']
	numberCountryCode = obj['numberCountryCode']
	numberAreaCode = obj['numberAreaCode']
	ext = obj['ext']
	dialFromCountryCode = obj['dialFromCountryCode']
	carrier = obj['carrier']
	continent = obj['continent']
	continentCode = obj['continentCode']
	country = obj['country']
	countryName = obj['countryName']
	lat = obj['lat']
	lon = obj['lon']
	timezone = obj['timezone']
	offset = obj['offset']
	currency = obj['currency']
		
	print('[+] Information Output')
	print('--------------------------------------')
	print(' - Phone number:', query)
	print(' - Status:', status)
	print(' - Number type:', numberType)
	print(' - Number Country Code:', numberCountryCode)
	print(' - Number Area Code:', numberAreaCode)
	print(' - ext:', ext)
	print(' - dial country:', dialFromCountryCode)
	print(' - carrier:', carrier)
	print(' - continent:', continent)
	print(' - continent code:', continentCode)
	print(' - country:', country)
	print(' - countryname:', countryName)
	print(' - Latitude:', lat)
	print(' - Longitude:', lon)
	print(' - timezone:', timezone)
	print(' - offset:', offset)
	print(' - currency:', currency)

if __name__ == '__main__':
	main()

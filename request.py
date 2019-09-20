import requests

r = requests.get('https://report.khconf.com/api.php/info', auth=('1ParadisN', 'pw'))

Status_Code = r.status_code
output = r.json()

print(Status_Code)
print(output)




# r.json()

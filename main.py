import requests

url= 'https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P189&aid=VisaWaitTimesHomePage'

ses = requests.session()

headers= {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'cookie': '_ga=GA1.2.1735239109.1646023241; _rdt_uuid=1646023240941.8a85a7ae-bf8c-4c3e-abbf-5ebd24466c96; _ga=GA1.3.1735239109.1646023241; visasStateGovPost=P189%3ASingapore; ADRUM=s=1657597764622&r=https%3A%2F%2Fceac.state.gov%2FGenNIV%2FDefault.aspx%3F0; _gid=GA1.2.210332381.1657856386; _gid=GA1.3.210332381.1657856386; _gat=1; _gat_GSA_ENOR0=1; _gat_gtag_UA_161656342_1=1'}

req = ses.get(url,headers=headers)

print(req.text)
import requests
from bs4 import BeautifulSoup as bs
from models import session, Server

BASE_URL = 'http://register.start.bg/'
r = requests.get(BASE_URL).content
html_page = bs(r, 'html.parser')


def get_all_links(html_page):
    servers = {}

    for link in html_page.find_all('a'):
        link = link.get('href')
        if link:
            try:
                if link.startswith('http'):
                    r = requests.head(link, allow_redirects=True)
                else:
                    r = requests.head(BASE_URL + link, allow_redirects=True)

                if 'Server' in r.headers:
                    if 'Apache' in r.headers['Server']:
                        server = 'Apache'
                    else:
                        server = r.headers['Server']

                if server not in servers.keys():
                    servers[server] = 1
                else:
                    servers[server] += 1

            except:
                pass

    print(servers)
    return servers

servers = get_all_links(html_page)

for server, number in servers.items():
    session.add(Server(name=server, number=number))
session.commit()

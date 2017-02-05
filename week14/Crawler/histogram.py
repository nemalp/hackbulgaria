import matplotlib.pyplot as plt
from models import session, Server

servers = (server for server in session.query(Server))
D = {s.name.split('/')[0]: s.number for s in servers if 'NULL' not in s.name}

fig = plt.figure()
fig.suptitle('Most common servers in bg', fontsize=16)

plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), D.keys(), rotation=20, fontsize=10)
plt.show()

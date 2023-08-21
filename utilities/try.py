import requests

base_urls = [
    'https://papers.gceguide.com/A%20Levels/Afrikaans%20(9679)/',
    'https://papers.gceguide.com/A%20Levels/Afrikaans%20-%20First%20Language%20(AS%20Level%20only)%20(8779)/',
    'https://papers.gceguide.com/A%20Levels/Afrikaans%20-%20Language%20(AS%20Level%20only)%20(8679)/',
    'https://papers.gceguide.com/A%20Levels/Applied%20Information%20and%20Communication%20Technology%20(9713)/',
    'https://papers.gceguide.com/A%20Levels/Arabic%20(9680)/',
    'https://papers.gceguide.com/A%20Levels/Arabic%20-%20Language%20(AS%20Level%20only)%20(8680)/',
    'https://papers.gceguide.com/A%20Levels/Art%20%26%20Design%20(9479)/',
    'https://papers.gceguide.com/A%20Levels/Art%20%26%20Design%20(9704)/',
    'https://papers.gceguide.com/A%20Levels/Biblical%20Studies%20(9484)/',
    'https://papers.gceguide.com/A%20Levels/Biology%20(9700)/',
    'https://papers.gceguide.com/A%20Levels/Cambridge%20International%20Project%20Qualification%20(9980)/',
    'https://papers.gceguide.com/A%20Levels/Chinese%20(A%20Level%20only)%20(9715)/',
    'https://papers.gceguide.com/A%20Levels/Chinese%20-%20Language%20(AS%20Level%20only)%20(8681)/',
    'https://papers.gceguide.com/A%20Levels/Classical%20Studies%20(9274)/',
    'https://papers.gceguide.com/A%20Levels/Design%20%26%20Textiles%20(9631)/',
    'https://papers.gceguide.com/A%20Levels/Design%20and%20Technology%20(9705)/',
    'https://papers.gceguide.com/A%20Levels/Digital%20Media%20%26%20Design%20(9481)/',
    'https://papers.gceguide.com/A%20Levels/Divinity%20(9011)/',
    'https://papers.gceguide.com/A%20Levels/Divinity%20(AS%20Level%20only)%20(8041)/',
    'https://papers.gceguide.com/A%20Levels/Drama%20(9482)/',
    'https://papers.gceguide.com/A%20Levels/English%20-%20Literature%20(9695)/',
    'https://papers.gceguide.com/A%20Levels/English%20General%20Paper%20(AS%20Level%20only)%20(8021)/',
    'https://papers.gceguide.com/A%20Levels/English%20Language%20(9093)/',
    'https://papers.gceguide.com/A%20Levels/Environmental%20Management%20(AS%20only)%20(8291)/',
    'https://papers.gceguide.com/A%20Levels/Food%20Studies%20(9336)/',
    'https://papers.gceguide.com/A%20Levels/French%20(A%20Level%20only)%20(9716)/',
    'https://papers.gceguide.com/A%20Levels/French%20-%20Language%20(AS%20Level%20only)%20(8682)/',
    'https://papers.gceguide.com/A%20Levels/French%20-%20Literature%20(AS%20Level%20only)%20(8670)/',
    'https://papers.gceguide.com/A%20Levels/General%20Paper%208004%20(AS%20Level%20only)%20(8004)/',
    'https://papers.gceguide.com/A%20Levels/Geography%20(9696)/',
    'https://papers.gceguide.com/A%20Levels/German%20(A%20Level%20only)%20(9717)/',
    'https://papers.gceguide.com/A%20Levels/German%20-%20Language%20(AS%20Level%20only)%20(8683)/',
    'https://papers.gceguide.com/A%20Levels/Global%20Perspectives%20%26%20Research%20(9239)/',
    'https://papers.gceguide.com/A%20Levels/Hindi%20(A%20Level%20only)%20(9687)/',
    'https://papers.gceguide.com/A%20Levels/Hindi%20-%20Language%20(AS%20Level%20only)%20(8687)/',
    'https://papers.gceguide.com/A%20Levels/Hindi%20-%20Literature%20(AS%20Level%20only)%20(8675)/',
    'https://papers.gceguide.com/A%20Levels/Hinduism%20(9014)/',
    'https://papers.gceguide.com/A%20Levels/Hinduism%20(9487)/',
    'https://papers.gceguide.com/A%20Levels/Hinduism%20(AS%20level%20only)%20(8058)/',
    'https://papers.gceguide.com/A%20Levels/History%20(9389)/',
    'https://papers.gceguide.com/A%20Levels/History%20(9489)/',
    'https://papers.gceguide.com/A%20Levels/History%20(for%20final%20examination%20in%202021)%20(9389)/',
    'https://papers.gceguide.com/A%20Levels/Information%20Technology%20(9626)/',
    'https://papers.gceguide.com/A%20Levels/Islamic%20Studies%20(9013%20%26%208053)/',
    'https://papers.gceguide.com/A%20Levels/Islamic%20Studies%20(9013)/',
    'https://papers.gceguide.com/A%20Levels/Islamic%20Studies%20(9488)/',
    'https://papers.gceguide.com/A%20Levels/Islamic%20Studies%20(AS%20Level%20only)%20(8053)/',
    'https://papers.gceguide.com/A%20Levels/Japanese%20Language%20(AS%20Level%20only)%20(8281)/',
    'https://papers.gceguide.com/A%20Levels/Law%20(9084)/',
    'https://papers.gceguide.com/A%20Levels/Marine%20Science%20(9693)/',
    'https://papers.gceguide.com/A%20Levels/Media%20Studies%20(9607)/',
    'https://papers.gceguide.com/A%20Levels/Music%20(9483)/',
    'https://papers.gceguide.com/A%20Levels/Music%20(9703)/',
    'https://papers.gceguide.com/A%20Levels/Music%20(AS%20Level%20only)%20(8663)/',
    'https://papers.gceguide.com/A%20Levels/Nepal%20Studies%20(AS%20Level%20only)%20(8024)/',
    'https://papers.gceguide.com/A%20Levels/Physical%20Education%20(9396)/',
    'https://papers.gceguide.com/A%20Levels/Portuguese%20(A%20Level%20only)%20(9718)/',
    'https://papers.gceguide.com/A%20Levels/Portuguese%20-%20Language%20(AS%20Level%20only)%20(8684)/',
    'https://papers.gceguide.com/A%20Levels/Portuguese%20-%20Literature%20(AS%20Level%20only)%20(8672)/',
    'https://papers.gceguide.com/A%20Levels/Psychology%20(9698)/',
    'https://papers.gceguide.com/A%20Levels/Psychology%20(9990)/',
    'https://papers.gceguide.com/A%20Levels/Sociology%20(9699)/',
    'https://papers.gceguide.com/A%20Levels/Spanish%20(A%20Level%20only)%20(9719)/',
    'https://papers.gceguide.com/A%20Levels/Spanish%20-%20First%20Language%20(AS%20Level%20only)%20(8665)/',
    'https://papers.gceguide.com/A%20Levels/Spanish%20-%20Language%20(AS%20Level%20only)%20(8685)/',
    'https://papers.gceguide.com/A%20Levels/Spanish%20-%20Literature%20(AS%20Level%20only)%20(8673)/',
    'https://papers.gceguide.com/A%20Levels/Tamil%20(9689)/',
    'https://papers.gceguide.com/A%20Levels/Tamil%20-%20Language%20(AS%20Level%20only)%20(8689)/',
    'https://papers.gceguide.com/A%20Levels/Thinking%20Skills%20(9694)/',
    'https://papers.gceguide.com/A%20Levels/Travel%20%26%20Tourism%20(9395)/',
    'https://papers.gceguide.com/A%20Levels/Urdu%20(A%20Level%20only)%20(9676)/',
    'https://papers.gceguide.com/A%20Levels/Urdu%20-%20Language%20(AS%20Level%20only)%20(8686)/',
    'https://papers.gceguide.com/A%20Levels/Urdu%20-%20Pakistan%20only%20(A%20Level%20only)%20(9686)/'
]


for url in base_urls:
    response = requests.get(url)
    if response.status_code == 404:
        print(f"URL {url} returned a 404 error.")
    else:
        print(f"URL {url} is accessible.")


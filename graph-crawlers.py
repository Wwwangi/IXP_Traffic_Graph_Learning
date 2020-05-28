import requests
import urllib.request
import threading
import arrow
import re
import json
import random
import time
from bs4 import BeautifulSoup
import base64
from time import sleep
from selenium import webdriver

def load_img(url,targ):
    if(targ in [31,102,109,124,162,163,170]):
        url = 'https://' + url
    else:
        url = 'http://' + url
    if(targ in [88,95,100,150]):
    	response = requests.get(url,verify=False)
    else:
    	response = requests.get(url)
    data = response.content
    return data

def get_graph(url):
    targ = url
    get_images=[]
    if(targ == 1):
        det=0
        index='1'
        print('Downloading from IXP: MIXP')
        get_images.append("www.mixp.org/stats/aggregate-traffic-day.png")
        get_images.append("www.mixp.org/stats/aggregate-traffic-week.png")
        get_images.append("www.mixp.org/stats/aggregate-traffic-month.png")
        get_images.append("www.mixp.org/stats/aggregate-traffic-year.png")
        scale=[32,192,840,8760]
    elif(targ == 2):
        det=0
        index='2'
        print('Downloading from IXP: IXPN Lagos')
        get_images.append("rt1.ixp.net.ng/mrtg/totalixpnlagos-day.png")
        get_images.append("rt1.ixp.net.ng/mrtg/totalixpnlagos-week.png")
        get_images.append("rt1.ixp.net.ng/mrtg/totalixpnlagos-month.png")
        get_images.append("rt1.ixp.net.ng/mrtg/totalixpnlagos-year.png")
        scale=[50,312,1176,13680]
    elif(targ == 3):
        index='3'
        det=0
        print('Downloading from IXP: angonix')
        resp = requests.get('http://angonix.net/about-angonix/statistics/')
        des = r'ixp.angonix.net/statistics/ixp_peering-angonix-bits-[.*\S]*.png'
        pattern = re.compile(des)
        get_images = re.findall(pattern,repr(resp.content))
        scale = [33,192,840,10080]
    elif(targ == 7):
        index='7'
        det=1
        print('Downloading from IXP: Rheintal IX')
        content = urllib.request.urlopen('https://ixp.rheintal-ix.net/statistics/ixp').read()
        soup = BeautifulSoup(content,features='html.parser')
        graph = soup.findAll('img',class_='img-fluid')
        for i in range(len(graph)):
            get_images.append(graph[i].get('src').split('data:image/png;base64,')[1])
        scale=[33,192,840,8740]
    elif(targ == 8):
        det=0
        index='8'
        print('Downloading from IXP: SAIX')
        get_images.append("www.saix.at/ixp_peering-aggregate-bits-month.png")
        scale=[4200]
    elif(targ == 9):
        det=0
        index='9'
        print('Downloading from IXP: DIX')
        get_images.append("info.net.deic.dk/traffic/dix-day.png")
        get_images.append("info.net.deic.dk/traffic/dix-week.png")
        scale=[24,168]
    elif(targ == 10):
        det=0
        index='10'
        print('Downloading from IXP: R_iX')
        get_images.append("www.nl-ix.net/graphs/metro/rotterdam")
        scale=[168]
    elif(targ ==11):  #json file
    	det=2
    	index='11'
    	print('Downloading from IXP: MSK-IX')
    	get_images.append('https://www.msk-ix.ru/data/json/traffic/ix.all/daily/?0.8529540869671604')
    	get_images.append('https://www.msk-ix.ru/data/json/traffic/ix.all/weekly/?0.7386478444598312')
    	get_images.append('https://www.msk-ix.ru/data/json/traffic/ix.all/monthly/?0.42161254369326717')
    	get_images.append('https://www.msk-ix.ru/data/json/traffic/ix.all/yearly/?0.5237254237342213')
    	scale=[36,216,696,8760]
    elif(targ == 16):
        det=0
        index='16'
        print('Downloading from IXP: PIRIX')
        get_images.append("pirix.ru/img/pirix-1w")
        get_images.append('pirix.ru/img/pirix-1m')
        scale=[168,720]
    elif(targ == 18):
        det=0
        index='18'
        print('Downloading from IXP: W-IX')
        get_images.append("www.w-ix.ru/i/w-ix-g.png")
        scale=[24]
    elif(targ == 19):
        det=0
        index='19'
        print('Downloading from IXP: SIX.SK')
        get_images.append("www.six.sk/stats/aggregated-day.png")
        get_images.append("www.six.sk/stats/aggregated-week.png")
        get_images.append("www.six.sk/stats/aggregated-month.png")
        get_images.append("www.six.sk/stats/aggregated-year.png")
        scale=[32,192,840,8760]
    elif(targ == 20):
        det=0
        index='20'
        print('Downloading from IXP: RIX')
        get_images.append("www.rix.is/status/rix/galag/galag-day.png")
        get_images.append("www.rix.is/status/rix/galag/galag-week.png")
        get_images.append("www.rix.is/status/rix/galag/galag-month.png")
        get_images.append("www.rix.is/status/rix/galag/galag-year.png")
        scale=[32,192,840,8760]
    elif(targ == 21):
        det=0
        index='21'
        print('Downloading from IXP: SIX.SK Košice')
        get_images.append("www.six.sk/statske/aggregated-ke-day.png")
        get_images.append("www.six.sk/statske/aggregated-ke-week.png")
        get_images.append("www.six.sk/statske/aggregated-ke-month.png")
        get_images.append("www.six.sk/statske/aggregated-ke-year.png")
        scale=[32,192,840,8760]
    elif(targ == 22):
        det=0
        index='22'
        print('Downloading from IXP: LyonIX')
        get_images.append("vm-monitoring-1.rezopole.net/stats-services/all_traffic_exchanged_lyonix/lyonix-day.png")
        get_images.append("vm-monitoring-1.rezopole.net/stats-services/all_traffic_exchanged_lyonix/lyonix-week.png")
        get_images.append("vm-monitoring-1.rezopole.net/stats-services/all_traffic_exchanged_lyonix/lyonix-month.png")
        get_images.append("vm-monitoring-1.rezopole.net/stats-services/all_traffic_exchanged_lyonix/lyonix-year.png")
        scale=[40,216,1008,11520]
    elif(targ == 23):
        det=0
        index='23'
        print('Downloading from IXP: LONAP')
        get_images.append("www.lonap.net/mrtg/lonap-total-day.png")
        get_images.append("www.lonap.net/mrtg/lonap-total-week.png")
        get_images.append("www.lonap.net/mrtg/lonap-total-month.png")
        get_images.append("www.lonap.net/mrtg/lonap-total-year.png")
        scale=[48,264,1176,13680]
    elif(targ ==24):  #json file
    	det=2
    	index='24'
    	print('Downloading from IXP: LINX LON1')
    	get_images.append('https://portal.linx.net/api/throughput/lan/lon1')
    	scale=[24]
    elif(targ ==25):  #json file
    	det=2
    	index='25'
    	print('Downloading from IXP: LINX LON2')
    	get_images.append('https://portal.linx.net/api/throughput/lan/lon2')
    	scale=[24]
    elif(targ ==26):  #json file
    	det=2
    	index='26'
    	print('Downloading from IXP: LINX Manchester')
    	get_images.append('https://portal.linx.net/api/throughput/lan/man1')
    	scale=[24]
    elif(targ ==27):  #json file
    	det=2
    	index='27'
    	print('Downloading from IXP: LINX Scotland')
    	get_images.append('https://portal.linx.net/api/throughput/lan/sco1')
    	scale=[24]
    elif(targ == 28):
        det=0
        index='28'
        print('Downloading from IXP: VIX')
        get_images.append("www.vix.at/typo3conf/ext/vix_public/Classes/Resource/Traffic/Daily.php")
        get_images.append("www.vix.at/typo3conf/ext/vix_public/Classes/Resource/Traffic/Weekly.php")
        get_images.append("www.vix.at/typo3conf/ext/vix_public/Classes/Resource/Traffic/Monthly.php")
        get_images.append("www.vix.at/typo3conf/ext/vix_public/Classes/Resource/Traffic/Yearly.php")
        scale=[24,168,720,7200]
    elif(targ == 29):
        det=0
        index='29'
        print('Downloading from IXP: BiX')
        get_images.append("stats.bix.hu/graph.cgi?type=Octets&portid=aggregated&start=1576733058&end=1576819458")
        get_images.append("stats.bix.hu/graph.cgi?type=Octets&portid=aggregated&start=1576214658&end=1576819458")
        get_images.append("stats.bix.hu/graph.cgi?type=Octets&portid=aggregated&start=1574141058&end=1576819458")
        get_images.append("stats.bix.hu/graph.cgi?type=Octets&portid=aggregated&start=1545197058&end=1576819458")
        get_images.append('stats.bix.hu/graph.cgi?type=Octets&portid=aggregated&start=1481952258&end=1576819458')
        scale=[24,168,720,8760,26280]
    #elif(targ == 30):
        #det=0
        #index='30'
        #print('Downloading from IXP: NIX')
        #get_images.append("www.nix.cz/mrtg/NIX/n-all-day.png")
        #get_images.append("www.nix.cz/mrtg/NIX/n-all-week.png")
        #get_images.append("www.nix.cz/mrtg/NIX/n-all-month.png")
        #get_images.append("www.nix.cz/mrtg/NIX/n-all-year.png")
        #scale=[36,216,1008,10080]
    elif(targ == 31):
        det=0
        index='31'
        print('Downloading from IXP: GigaPIX')
        get_images.append("193.137.196.180:8001/")
        get_images.append("graf.gigapix.pt:8001/semanal")
        get_images.append("graf.gigapix.pt:8001/mensal")
        get_images.append("graf.gigapix.pt:8001/anual")
        scale=[32,192,840,8760]
    elif(targ == 32):
        det=0
        index='32'
        print('Downloading from IXP: CIX')
        get_images.append("www.srce.unizg.hr/multimedia/CIX-stat/ixp001-bits-day.png?1576821010")
        get_images.append("www.srce.unizg.hr/multimedia/CIX-stat/ixp001-bits-week.png?1576821161")
        get_images.append("www.srce.unizg.hr/multimedia/CIX-stat/ixp001-bits-month.png?1576821167")
        get_images.append("www.srce.unizg.hr/multimedia/CIX-stat/ixp001-bits-year.png?1576821171")
        scale=[32,192,840,8760]
    elif(targ == 33):
        det=0
        index='33'
        print('Downloading from IXP: GR-IX::Athens')
        get_images.append("portal.gr-ix.gr/grapher/infrastructure?id=1&period=day")
        get_images.append("portal.gr-ix.gr/grapher/infrastructure?id=1&period=week")
        get_images.append("portal.gr-ix.gr/grapher/infrastructure?id=1&period=month")
        get_images.append("portal.gr-ix.gr/grapher/infrastructure?id=1&period=year")
        scale=[32,192,840,8760]
    elif(targ == 34):
        det=0
        index='34'
        print('Downloading from IXP: GR-IX::DE-CIX Istanbul')
        get_images.append("www.de-cix.net/traffic_IST-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_IST-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_IST-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_IST-2years-1170-400.png")
        scale=[48,720,8760,17520]
    elif(targ == 35):
        det=0
        index='35'
        print('Downloading from IXP: BALT-IX')
        get_images.append("stats.balt-ix.net/day.png")
        get_images.append("stats.balt-ix.net/week.png")
        get_images.append("stats.balt-ix.net/month.png")
        scale=[32,192,840]
    elif(targ == 36):
        det=0
        index='36'
        print('Downloading from IXP: GR-IX::Thessaloniki')
        get_images.append("portal.gr-ix.gr/grapher/infrastructure?id=3&period=day")
        get_images.append("portal.gr-ix.gr/grapher/infrastructure?id=3&period=week")
        get_images.append("portal.gr-ix.gr/grapher/infrastructure?id=3&period=month")
        get_images.append("portal.gr-ix.gr/grapher/infrastructure?id=3&period=year")
        scale=[32,192,840,8760]
    elif(targ == 37):
        det=0
        index='37'
        print('Downloading from IXP: B-IX')
        get_images.append("www.b-ix.net/traffic_graph_daily.png")
        get_images.append("www.b-ix.net/traffic_graph_weekly.png")
        get_images.append("www.b-ix.net/traffic_graph_monthly.png")
        scale=[24,168,720]
    elif(targ == 38):
        det=0
        index='38'
        print('Downloading from IXP: BIX.BG')
        get_images.append("www.bix.bg/assets/templates/bix/images/bixtotal-days.png")
        get_images.append("www.bix.bg/assets/templates/bix/images/bixtotal-years.png")
        scale=[48,8760]
    elif(targ == 39):
        det=0
        index='39'
        print('Downloading from IXP: CIXP')
        get_images.append("netstat.cern.ch/monitoring/network-statistics/ext/graphit.php?title=CIXP-Total-Traffic&custom=EXT&rrdpath=CIXP_CIXP-Total-Traffic")
        get_images.append("netstat.cern.ch/monitoring/network-statistics/ext/graphit.php?title=CIXP-Total-Traffic&custom=EXT&rrdpath=CIXP_CIXP-Total-Traffic&t=Weekly")
        get_images.append("netstat.cern.ch/monitoring/network-statistics/ext/graphit.php?title=CIXP-Total-Traffic&custom=EXT&rrdpath=CIXP_CIXP-Total-Traffic&t=Monthly")
        get_images.append("netstat.cern.ch/monitoring/network-statistics/ext/graphit.php?title=CIXP-Total-Traffic&custom=EXT&rrdpath=CIXP_CIXP-Total-Traffic&t=Yearly")
        scale=[24,168,720,8760]
    elif(targ == 40):
        index='40'
        det=1
        print('Downloading from IXP: SwissIX')
        browser = webdriver.Chrome()
        browser.get('https://www.swissix.ch/infrastructure/traffic')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img',class_='img-responsive')
        for i in range(len(graph)):
            get_images.append(graph[i].get('src').split('data:image/png;base64,')[1])
        scale=[33,192,840,8740]
        browser.quit()
    elif(targ == 41):
        det=0
        index='41'
        print('Downloading from IXP: DE-CIX Frankfurt')
        get_images.append("www.de-cix.net/traffic_FRA-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_FRA-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_FRA-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_FRA-5years-1170-400.png")
        scale=[48,720,8760,43800]
    elif(targ == 42):
        det=0
        index='42'
        print('Downloading from IXP: DE-CIX Hamburg')
        get_images.append("www.de-cix.net/traffic_HAM-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_HAM-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_HAM-1year-1170-400.png")
        scale=[48,720,8760]
    elif(targ == 43):
        det=0
        index='43'
        print('Downloading from IXP: BCIX')
        get_images.append("www.bcix.de/ixp/bcix/ixp001-bits-day.png")
        get_images.append("www.bcix.de/ixp/bcix/ixp001-bits-week.png")
        get_images.append("www.bcix.de/ixp/bcix/ixp001-bits-month.png")
        get_images.append("www.bcix.de/ixp/bcix/ixp001-bits-year.png")
        scale=[32,192,840,8760]
    elif(targ == 44):
        det=0
        index='44'
        print('Downloading from IXP: DE-CIX Munich')
        get_images.append("www.de-cix.net/traffic_MUC-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MUC-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MUC-1year-1170-400.png")
        scale=[48,720,8760]
    elif(targ == 45):
        det=0
        index='45'
        print('Downloading from IXP: DE-CIX Dusseldorf')
        get_images.append("www.de-cix.net/traffic_DUS-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_DUS-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_DUS-1year-1170-400.png")
        scale=[48,720,8760]
    elif(targ == 46):
        det=0
        index='46'
        print('Downloading from IXP: Community-IX')
        get_images.append("www.community-ix.de/ixp/grapher/ixp?period=day")
        get_images.append("www.community-ix.de/ixp/grapher/ixp?period=week")
        get_images.append("www.community-ix.de/ixp/grapher/ixp?period=month")
        get_images.append("www.community-ix.de/ixp/grapher/ixp?period=year")
        scale=[32,192,840,8760]
    elif(targ == 48):
        det=0
        index='48'
        print('Downloading from IXP: DE-CIX Madrid')
        get_images.append("www.de-cix.net/traffic_MAD-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MAD-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MAD-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MAD-2years-1170-400.png")
        scale=[48,720,8760,17520]
    elif(targ == 49):
        det=0
        index='49'
        print('Downloading from IXP: France-IX Paris')
        get_images.append("tools.franceix.net/static/images/observium/all-par-1d_from0.png")
        get_images.append("tools.franceix.net/static/images/observium/all-par-1w_from0.png")
        get_images.append("tools.franceix.net/static/images/observium/all-par-1m_from0.png")
        get_images.append("tools.franceix.net/static/images/observium/all-par-3m_from0.png")
        get_images.append("tools.franceix.net/static/images/observium/all-par-1y_from0.png")
        scale=[24,168,720,2160,8760]
    elif(targ == 50):
        det=0
        index='50'
        print('Downloading from IXP: France-IX Marseille')
        get_images.append("tools.franceix.net/static/images/observium/all-mrs-1d_from0.png")
        get_images.append("tools.franceix.net/static/images/observium/all-mrs-1w_from0.png")
        get_images.append("tools.franceix.net/static/images/observium/all-mrs-1m_from0.png")
        get_images.append("tools.franceix.net/static/images/observium/all-mrs-3m_from0.png")
        get_images.append("tools.franceix.net/static/images/observium/all-mrs-1y_from0.png")
        scale=[24,168,720,2160,8760]
    elif(targ == 51):
        det=0
        index='51'
        print('Downloading from IXP: AuvernIX')
        get_images.append("traf.auvernix.net/traffic.png")
        scale=[12]
    elif(targ == 52):
        det=0
        index='52'
        print('Downloading from IXP: DE-CIX Marseille')
        get_images.append("www.de-cix.net/traffic_MRS-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MRS-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MRS-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MRS-2years-1170-400.png")
        scale=[48,720,8760,17520]
    elif(targ == 53):
        index='53'
        det=1
        print('Downloading from IXP: INEX LAN1')
        browser = webdriver.Chrome()
        browser.get('https://www.inex.ie/ixp/statistics/infrastructure/1/bits')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img',class_='img-fluid')
        for i in range(len(graph)):
            get_images.append(graph[i].get('src').split('data:image/png;base64,')[1])
        scale=[32,192,672,8760]
        browser.quit()
    elif(targ == 54):
        index='54'
        det=1
        print('Downloading from IXP: INEX LAN2')
        browser = webdriver.Chrome()
        browser.get('https://www.inex.ie/ixp/statistics/infrastructure/2/bits')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img',class_='img-fluid')
        for i in range(len(graph)):
            get_images.append(graph[i].get('src').split('data:image/png;base64,')[1])
        scale=[32,192,672,8760]
        browser.quit()
    elif(targ == 55):
        det=0
        index='55'
        print('Downloading from IXP: TOP-IX')
        get_images.append("mrtg.top-ix.org/cgi-bin/14all.cgi?log=exchangedtraffic&cfg=exchangedtraffic.cfg&png=daily")
        get_images.append("mrtg.top-ix.org/cgi-bin/14all.cgi?log=exchangedtraffic&cfg=exchangedtraffic.cfg&png=weekly")
        get_images.append("mrtg.top-ix.org/cgi-bin/14all.cgi?log=exchangedtraffic&cfg=exchangedtraffic.cfg&png=monthly")
        get_images.append("mrtg.top-ix.org/cgi-bin/14all.cgi?log=exchangedtraffic&cfg=exchangedtraffic.cfg&png=yearly")
        scale=[34,192,792,8760]
    elif(targ == 56):
        det=0
        index='56'
        print('Downloading from IXP: VSIX')
        get_images.append("www.vsix.it/stat.php?m=t&f=stats0.png")
        get_images.append("www.vsix.it/stat.php?m=t&f=stats1.png")
        get_images.append("www.vsix.it/stat.php?m=t&f=stats2.png")
        get_images.append("www.vsix.it/stat.php?m=t&f=stats3.png")
        scale=[24,168,840,8760]
    elif(targ == 57):
        det=0
        index='57'
        print('Downloading from IXP: DE-CIX Palermo')
        get_images.append("www.de-cix.net/traffic_PMO-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_PMO-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_PMO-1year-1170-400.png")
        scale=[48,720,8760]
    elif(targ == 58):
        index='58'
        det=1
        print('Downloading from IXP: NL-ix')
        browser = webdriver.Chrome()
        browser.get('https://www.nl-ix.net/traffic.php')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        for i in range(len(graph)):
            if(graph[i].get('alt')=='Daily graph'):
                get_images.append(graph[i].get('src').split('data:image/jpeg;base64,')[1])
        scale=[24]
        browser.quit()
    elif(targ == 59):
        det=0
        index='59'
        print('Downloading from IXP: TPIX')
        get_images.append("stats.tpix.pl/img/day.png")
        get_images.append("stats.tpix.pl/img/month.png")
        get_images.append("stats.tpix.pl/img/year.png")
        scale=[24,744,8760]
    elif(targ == 60):
        index='60'
        det=1
        print('Downloading from IXP: InterLAN')
        browser = webdriver.Chrome()
        browser.get('https://ixpm.interlan.ro/statistics/ixp')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        for i in range(len(graph)):
            if(graph[i].get('border')=='0'):
                get_images.append(graph[i].get('src').split('data:image/png;base64,')[1])
        scale=[33,192,792,8760]
        browser.quit()
    elif(targ == 61):
        det=0
        index='61'
        print('Downloading from IXP: YAR-IX')
        get_images.append("yar-ix.net/graph/total-yarix-daily.png")
        get_images.append("yar-ix.net/graph/total-yarix-weekly.png")
        get_images.append("yar-ix.net/graph/total-yarix-monthly.png")
        scale=[24,168,720]
    elif(targ == 62):
        det=0
        index='62'
        print('Downloading from IXP: Netnod Stockholm')
        get_images.append("www.netnod.se/ix-stats/sums/Stockholm_day_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Stockholm_week_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Stockholm_month_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Stockholm_year_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Stockholm_twoyear_sum.png")
        scale=[24,168,720,8760,17520]
    elif(targ == 63):
        det=0
        index='63'
        print('Downloading from IXP: Netnod Gothenburg')
        get_images.append("www.netnod.se/ix-stats/sums/Gothenburg_day_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Gothenburg_week_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Gothenburg_month_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Gothenburg_year_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Gothenburg_twoyear_sum.png")
        scale=[24,168,720,8760,17520]
    elif(targ == 64):
        det=0
        index='64'
        print('Downloading from IXP: Netnod Lulea')
        get_images.append("www.netnod.se/ix-stats/sums/Lulea_day_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Lulea_week_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Lulea_month_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Lulea_year_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Lulea_twoyear_sum.png")
        scale=[24,168,720,8760,17520]
    elif(targ ==65):  #json file
    	det=2
    	index='65'
    	print('Downloading from IXP: MegaIX Sofia')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Sofia%20IX')
    	scale=[24]
    elif(targ == 66):
        det=0
        index='66'
        print('Downloading from IXP: STHIX - Copenhagen')
        get_images.append("www.sthix.net/stats/sthix_total_hour.png")
        get_images.append("www.sthix.net/stats/sthix_total_day.png")
        get_images.append("www.sthix.net/stats/sthix_total_week.png")
        get_images.append("www.sthix.net/stats/sthix_total_month.png")
        get_images.append("www.sthix.net/stats/sthix_total_year.png")
        scale=[1,24,168,720,8760]
    elif(targ ==67):  #json file
    	det=2
    	index='67'
    	print('Downloading from IXP: Asteroid Amsterdam')
    	get_images.append('https://sputnik.asteroidhq.com/exchange/1/1d')
    	get_images.append('https://sputnik.asteroidhq.com/exchange/1/4w')
    	get_images.append('https://sputnik.asteroidhq.com/exchange/1/52w')
    	scale=[24,672,8760]
    elif(targ ==73):  #json file
    	det=2
    	index='73'
    	print('Downloading from IXP: MegaIX Melbourne')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Melbourne%20IX')
    	scale=[24]
    elif(targ ==74):  #json file
    	det=2
    	index='74'
    	print('Downloading from IXP: MegaIX Sydney')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Sydney%20IX')
    	scale=[24]
    elif(targ ==75):  #json file
    	det=2
    	index='75'
    	print('Downloading from IXP: MegaIX Brisbane')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Brisbane%20IX')
    	scale=[24]
    elif(targ ==77):  #json file
    	det=2
    	index='77'
    	print('Downloading from IXP: MegaIX Perth')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Perth%20IX')
    	scale=[24]
    elif(targ ==78):  #json file
    	det=2
    	index='78'
    	print('Downloading from IXP: MegaIX Auckland')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Auckland%20IX')
    	scale=[24]
    elif(targ == 79):
        det=0
        index='79'
        print('Downloading from IXP: UAE-IX')
        get_images.append("www.uae-ix.net/traffic_DXB-1year-1170-400.png")
        get_images.append("www.uae-ix.net/traffic_DXB-5years-1170-400.png")
        scale=[8760,17520]
    elif(targ == 80):
        det=0
        index='80'
        print('Downloading from IXP: TWIX')
        get_images.append("www.twix.net/twix-traffic/summary-day.png")
        get_images.append("www.twix.net/twix-traffic/summary-week.png")
        get_images.append("www.twix.net/twix-traffic/summary-month.png")
        get_images.append("www.twix.net/twix-traffic/summary-year.png")
        scale=[26,192,720,8760]
    elif(targ == 81):
        det=0
        index='81'
        print('Downloading from IXP: HKIX')
        get_images.append("portal.hkix.net/customer/cgi-bin/mrtg-rrd-customer.cgi?log=hkix-aggregate&png=daily&u=")
        get_images.append("portal.hkix.net/customer/cgi-bin/mrtg-rrd-customer.cgi?log=hkix-aggregate&png=weekly&u=")
        get_images.append("portal.hkix.net/customer/cgi-bin/mrtg-rrd-customer.cgi?log=hkix-aggregate&png=monthly&u=")
        get_images.append("portal.hkix.net/customer/cgi-bin/mrtg-rrd-customer.cgi?log=hkix-aggregate&png=yearly&u=")
        scale=[48,168,840,8760]
    elif(targ == 82):
        det=0
        index='82'
        print('Downloading from IXP: NIXI Kolkata')
        get_images.append("180.179.222.68/mrtg/Total_Agg/nixi-day.png")
        scale=[32]
    elif(targ == 86):
        det=0
        index='86'
        print('Downloading from IXP: btIX')
        get_images.append("www.btix.bt/ixp/grapher")
        get_images.append("www.btix.bt/ixp/grapher?id=1&period=week&type=png")
        get_images.append("www.btix.bt/ixp/grapher?id=1&period=month&type=png")
        get_images.append("www.btix.bt/ixp/grapher?id=1&period=year&type=png")
        scale=[30,192,792,8760]    
    elif(targ == 88):
        det=0
        index='88'
        print('Downloading from IXP: Mumbai IX')
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-day.png")
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-week.png")
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-month.png")
        scale=[24,168,744]
    elif(targ == 89):
        det=0
        index='89'
        print('Downloading from IXP: AMS-IX India')
        get_images.append("stats-mum.ams-ix.net/cgi-bin/stats/16all?imgformat=png;target=totalall;interval=daily")
        get_images.append("stats-mum.ams-ix.net/cgi-bin/stats/16all?imgformat=png;target=totalall;interval=weekly")
        get_images.append("stats-mum.ams-ix.net/cgi-bin/stats/16all?imgformat=png;target=totalall;interval=monthly")
        get_images.append("stats-mum.ams-ix.net/cgi-bin/stats/16all?imgformat=png;target=totalall;interval=yearly")
        scale=[24,192,840,11520]
    elif(targ == 90):
        det=0
        index='90'
        print('Downloading from IXP: JPIX TOKYO')
        get_images.append("www.jpix.ad.jp/en/img/TOTAL.In_e.png")
        scale=[24]
    elif(targ == 91):
        det=0
        index='91'
        print('Downloading from IXP: JPIX OSAKA')
        get_images.append("www.jpix.ad.jp/en/img/TOTAL-OSK.In_e.png")
        scale=[24]
    elif(targ == 92):
        det=0
        index='92'
        print('Downloading from IXP: PhOpenIX-Manila')
        get_images.append("phopenix.net/images/hourly.png")
        get_images.append("phopenix.net/images/daily.png")
        get_images.append("phopenix.net/images/weekly.png")
        get_images.append("phopenix.net/images/monthly.png")
        get_images.append("phopenix.net/images/yearly.png")
        scale=[4,24,168,744,8760]
    elif(targ == 93):
        det=0
        index='93'
        print('Downloading from IXP: SGIX')
        get_images.append("www.sgix.sg/statistics/sgix-aggregate-daily.png")
        get_images.append("www.sgix.sg/statistics/sgix-aggregate-weekly.png")
        get_images.append("www.sgix.sg/statistics/sgix-aggregate-monthly.png")
        get_images.append("www.sgix.sg/statistics/sgix-aggregate-yearly.png")
        scale=[24,168,792,8760]
    elif(targ == 94):
        det=0
        index='94'
        print('Downloading from IXP: BKNIX')
        get_images.append("bknix.co.th/data/images/traffic/current_total_ix.png")
        get_images.append("bknix.co.th/data/images/traffic/current_total_ix-week.png")
        get_images.append("bknix.co.th/data/images/traffic/current_total_ix-month.png")
        get_images.append("bknix.co.th/data/images/traffic/current_total_ix-year.png")
        scale=[24,168,744,8760]
    elif(targ == 95):
        det=0
        index='95'
        print('Downloading from IXP: DE-CIX Delhi')
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-day.png")
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-week.png")
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-month.png")
        scale=[24,168,720]
    elif(targ == 99):
        det=3
        index='99'
        print('Downloading from IXP: CAIX')
        get_images.append("www.caix.net.eg/images/stories/graphs/graph_22_1.png")
        get_images.append("www.caix.net.eg/images/stories/graphs/graph_22_2.png")
        get_images.append("www.caix.net.eg/images/stories/graphs/graph_22_3.png")
        get_images.append("www.caix.net.eg/images/stories/graphs/graph_22_4.png")
        scale=[24,168,744,8760]
    elif(targ == 100):
        det=0
        index='100'
        print('Downloading from IXP: TPIX-TW')
        get_images.append("mrtg.chief.com.tw/outputPNG.php?P=MjAxNDAxMjQwMDo6ZGF5")
        get_images.append("mrtg.chief.com.tw/outputPNG.php?P=MjAxNDAxMjQwMDo6d2Vlaw==")
        get_images.append("mrtg.chief.com.tw/outputPNG.php?P=MjAxNDAxMjQwMDo6bW9udGg=")
        get_images.append("mrtg.chief.com.tw/outputPNG.php?P=MjAxNDAxMjQwMDo6eWVhcg==")
        scale=[33,192,792,8760]
    elif(targ ==101):  #json file
    	det=2
    	index='101'
    	print('Downloading from IXP: MegaIX Singapore')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Singapore%20IX')
    	scale=[24]
    elif(targ == 102):
        det=0
        index='102'
        print('Downloading from IXP: NYIIX Los Angeles')
        get_images.append("www.nyiix.net/LA-mrtg/graph_587.png")
        get_images.append("www.nyiix.net/LA-mrtg/graph_587_9.png")
        get_images.append("www.nyiix.net/LA-mrtg/graph_587_10.png")
        get_images.append("www.nyiix.net/LA-mrtg/graph_587_11.png")
        scale=[24,168,1344,8760]
    elif(targ == 103):
        det=0
        index='103'
        print('Downloading from IXP: TahoeIX')
        get_images.append("www.tahoeix.org/mrtg/ix_traffic-day.png")
        get_images.append("www.tahoeix.org/mrtg/ix_traffic-week.png")
        get_images.append("www.tahoeix.org/mrtg/ix_traffic-month.png")
        get_images.append("www.tahoeix.org/mrtg/ix_traffic-year.png")
        scale=[40,240,840,11520]
    elif(targ == 104):
        det=0
        index='104'
        print('Downloading from IXP: TorIX')
        get_images.append("www.torix.ca/img/torix-day.png")
        get_images.append("www.torix.ca/img/torix-week.png")
        get_images.append("www.torix.ca/img/torix-month.png")
        get_images.append("www.torix.ca/img/torix-year.png")
        scale=[32,192,768,8760]
    elif(targ == 105):
        det=0
        index='105'
        print('Downloading from IXP: QIX')
        get_images.append("www.qix.ca/assets/images/network-daily.png")
        get_images.append("www.qix.ca/assets/images/network-monthly.png")
        scale=[24,744]
    elif(targ == 106):
        det=0
        index='106'
        print('Downloading from IXP: YYCIX')
        get_images.append("yycix.ca/graphs/e_day.png")
        get_images.append("yycix.ca/graphs/e_week.png")
        get_images.append("yycix.ca/graphs/e_month.png")
        get_images.append("yycix.ca/graphs/e_year.png")
        scale=[36,168,744,8760]
    elif(targ == 107):
        det=0
        index='107'
        print('Downloading from IXP: MBIX')
        get_images.append("www.mbix.ca/cacti/graph_image.php?action=view&local_graph_id=745&rra_id=5")
        get_images.append("www.mbix.ca/cacti/graph_image.php?action=view&local_graph_id=745&rra_id=2")
        get_images.append("www.mbix.ca/cacti/graph_image.php?action=view&local_graph_id=745&rra_id=3")
        get_images.append("www.mbix.ca/cacti/graph_image.php?action=view&local_graph_id=745&rra_id=4")
        scale=[24,168,744,8760]
    elif(targ == 108):
        det=0
        index='108'
        print('Downloading from IXP: SIX Seattle')
        get_images.append("www.seattleix.net/statistics/agg.cfg-agg-d-y3.png")
        get_images.append("www.seattleix.net/statistics/agg.cfg-agg-w-y3.png")
        get_images.append("www.seattleix.net/statistics/agg.cfg-agg-m-y3.png")
        get_images.append("www.seattleix.net/statistics/agg.cfg-agg-y-y3.png")
        scale=[34,168,816,8760]
    elif(targ == 109):
        det=0
        index='109'
        print('Downloading from IXP: NYIIX')
        get_images.append("www.nyiix.net/mrtg/graph_4469.png")
        get_images.append("www.nyiix.net/mrtg/graph_4469_9.png")
        get_images.append("www.nyiix.net/mrtg/graph_4469_11.png")
        get_images.append("www.nyiix.net/mrtg/graph_4469_12.png")
        scale=[24,168,1344,8760]
    elif(targ == 110):
        det=0
        index='110'
        print('Downloading from IXP: SFMIX')
        get_images.append("sfmix.org/static/img/daily.gif")
        get_images.append("sfmix.org/static/img/week.gif")
        scale=[24,168]
    elif(targ == 111):
        det=0
        index='111'
        print('Downloading from IXP: MICE')
        get_images.append("micelg.usinternet.com/export/graphs/graph_1430_5.png")
        get_images.append("micelg.usinternet.com/export/graphs/graph_1430_1.png")
        get_images.append("micelg.usinternet.com/export/graphs/graph_1430_2.png")
        get_images.append("micelg.usinternet.com/export/graphs/graph_1430_3.png")
        get_images.append("micelg.usinternet.com/export/graphs/graph_1430_4.png")
        scale=[4,24,168,744,8760]
    elif(targ == 113):
        det=0
        index='113'
        print('Downloading from IXP: MASS-IX')
        get_images.append("portal.mass-ix.net/mass-ixp64-day.png")
        get_images.append("portal.mass-ix.net/mass-ixp64-week.png")
        get_images.append("portal.mass-ix.net/mass-ixp64-month.png")
        get_images.append("portal.mass-ix.net/mass-ixp64-year.png")
        scale=[34,192,792,8760]
    elif(targ == 114):
        det=0
        index='114'
        print('Downloading from IXP: DE-CIX Dallas')
        get_images.append("www.de-cix.net/traffic_DFW-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_DFW-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_DFW-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_DFW-2years-1170-400.png")
        scale=[48,720,8760,17520]
    elif(targ ==115):  #json file
    	det=2
    	index='115'
    	print('Downloading from IXP: MegaIX Toronto')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Toronto%20IX')
    	scale=[24]
    elif(targ == 116):
        det=0
        index='116'
        print('Downloading from IXP: ChIX')
        get_images.append("unitedix.net/stats/chicago-agg.png")
        scale=[192]
    elif(targ ==117):  #json file
    	det=2
    	index='117'
    	print('Downloading from IXP: MegaIX Seattle')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Seattle%20IX')
    	scale=[24]
    elif(targ ==118):  #json file
    	det=2
    	index='118'
    	print('Downloading from IXP: MegaIX Los Angeles')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Los%20Angeles%20IX')
    	scale=[24]
    elif(targ ==119):  #json file
    	det=2
    	index='119'
    	print('Downloading from IXP: MegaIX Dallas')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Dallas%20IX')
    	scale=[24]
    elif(targ == 120):
        index='120'
        det=1
        print('Downloading from IXP: IX-Denver')
        browser = webdriver.Chrome()
        browser.get('https://portal.ix-denver.org/statistics/ixp')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        for i in range(len(graph)):
            if(graph[i].get('border')=='0'):
                get_images.append(graph[i].get('src').split('data:image/png;base64,')[1])
        scale=[33,192,792,8760]
        browser.quit()
    elif(targ ==121):  #json file
    	det=2
    	index='121'
    	print('Downloading from IXP: MegaIX Las Vegas')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Las%20Vegas%20IX')
    	scale=[24]
    elif(targ == 122):
        det=0
        index='122'
        print('Downloading from IXP: NAP Colombia')
        get_images.append("www.nap.co/wp-content/uploads/2020/04/%C3%9Altima-semana.jpg")
        get_images.append("www.nap.co/wp-content/uploads/2020/04/%C3%9Altimo-a%C3%B1o.jpg")
        scale=[24,8760]
    elif(targ == 124):
        det=0
        index='124'
        print('Downloading from IXP: TTIX2')
        get_images.append("ttix2.airlinktt.co/graphs/last1d.png")
        scale=[1]
    elif(targ == 125):
        det=0
        index='125'
        print('Downloading from IXP: IX.br (PTT.br) Porto Alegre')
        get_images.append("old.ix.br/stats/133b7f1cd0adde227ab9f48e68a4b82f/rs/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/4185e82b8327da2c082b64b7908ea1d8/rs/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/2c750bed5973b759ffabdcbcdf2b7507/rs/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/1d1a3da389fafaf7d154f04eb605a7fa/rs/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/ee9f4e3c38954321570d0233d94c5eb3/rs/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,78840]
    elif(targ == 126):
        det=0
        index='126'
        print('Downloading from IXP: IX.br (PTT.br) Florianópolis')
        get_images.append("old.ix.br/stats/be779630c4bfd20baffc23b9b9a513ac/sc/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/f2ab5cebc4c482bb99b237c63b2f74f1/sc/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/122c12f775cb9e23d12e589e7b156540/sc/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/f78d6973d140f41a2a381597b14aaa76/sc/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/f5f613c9f71ac7b6dfbc6dd92a11dea1/sc/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 127):
        det=0
        index='127'
        print('Downloading from IXP: IX.br (PTT.br) Belo Horizonte')
        get_images.append("old.ix.br/stats/bbaec3801638d06029a23d912c2a2e3c/mg/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/791a46315816d1645b8687910d92826c/mg/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/fa2d7b6631b242dc7563f41f874dd616/mg/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/73576366be65f66156c87ff2c4d7c9b0/mg/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/e1090fc2aa4dc0f8278fe7ae7eeb8f1c/mg/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 128):
        det=0
        index='128'
        print('Downloading from IXP: IX.br (PTT.br) Rio de Janeiro')
        get_images.append("old.ix.br/stats/b7fb718114f447c323641f962a7be869/rj/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/e18815450e1904c724cbf61d415c1674/rj/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/9e308c8511fbf9e13f9815ee081e68ef/rj/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/8b3ae630ef7370de3261afa2d12746c0/rj/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/b1fc9245d1e9cb4d00c3801d22bbd233/rj/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 129):
        det=0
        index='129'
        print('Downloading from IXP: IX.br (PTT.br) Brasília')
        get_images.append("old.ix.br/stats/297842eef685fa1b41fa156842cdf32c/df/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/546b1ad23c677f118515fc57f8c5ea49/df/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/dffd05d408a2b1f4a477351df9820656/df/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/57efe8fa9022e7ce77412f7f47d22aef/df/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/3cc3b494cb80fffda7341f6908a31a46/df/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 130):
        det=0
        index='130'
        print('Downloading from IXP: IX.br (PTT.br) Londrina')
        get_images.append("old.ix.br/stats/7137e5d6e862f9e5d47b6eb3c6693922/lda/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/c98b3ff768e12344a286730f43939e89/lda/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/4f3ec7febc32d5ca81b89d5c02b926aa/lda/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/bec4ff9b7baa8cf8a2ca9d6ad3a4fc68/lda/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/ecd4cf1fe231349330d57cb03d7528df/lda/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 131):
        det=0
        index='131'
        print('Downloading from IXP: IX.br (PTT.br) Campinas')
        get_images.append("old.ix.br/stats/64d04c470b3b2cfd6a8baaa2326ddefa/cas/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/663f3f72a31c3528c05b8a8fed1b1796/cas/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/80f83eeb6ac6d1ebaa436ca5f22bf925/cas/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/481cdf1c402c2702ecbb6637a779b843/cas/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/a4e44007b76594b611ee06ae2d687d1c/cas/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 132):
        det=0
        index='132'
        print('Downloading from IXP: IX.br (PTT.br) Salvador')
        get_images.append("old.ix.br/stats/fd6bf1772c30a428a00c015b76c83d65/ba/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/a11fded4aa7cafd4e66148b705a6dd2c/ba/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/6ddeda7e79276297de70089dc6941a58/ba/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/bc51b484e909dab3d531fd0f4fa75ae8/ba/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/3e50d59d6a10966e1a38ac84d96520c3/ba/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 133):
        det=0
        index='133'
        print('Downloading from IXP: IX.br (PTT.br) Caxias do Sul')
        get_images.append("old.ix.br/stats/1ca8748e6672014e5862c1eda1e19c97/cxj/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/f0778d14de5c32afe63b11314d29b9e7/cxj/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/d5b4ceced963d0981527655e51b27920/cxj/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/8fcf0f3ab0d652f3169ff940416f1110/cxj/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/b98c3e60cf0c0f34dcf220115a845faa/cxj/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 134):
        det=0
        index='134'
        print('Downloading from IXP: IX.br (PTT.br) Goiânia')
        get_images.append("old.ix.br/stats/e1100a9487a40dac85dc59754ba070e8/gyn/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/baf01de293cda7e11b9f17fcd34ae408/gyn/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/3e819be3ef16142fa1b4b2a566844e39/gyn/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/33237d0ac2fbcff05c276f1b1d4dbaba/gyn/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/493a6e4f6b78799a19467b979d5e34c7/gyn/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 135):
        det=0
        index='135'
        print('Downloading from IXP: IX.br (PTT.br) Campina Grande')
        get_images.append("old.ix.br/stats/56bd40ebacb261ea9079e570301057b6/cpv/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/09e21fcef95a990f862237f19af36b17/cpv/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/40900fe67ed3982c37752d5b335107a6/cpv/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/4e3479e59df6ec67f9146d140e878cc1/cpv/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/4b5c453bcdbf56259d15216ebed3bedd/cpv/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 136):
        det=0
        index='136'
        print('Downloading from IXP: IX.br (PTT.br) Sao José dos Campos')
        get_images.append("old.ix.br/stats/e3012aaf82b9f4310854c5e54aa02512/sjc/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/90fcfb92076d49e19737eda9a5f4e4b9/sjc/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/4f9ee81b0ce7966c112b1e3b826d6b54/sjc/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/0acd2ed2859998369f9b07467a032b34/sjc/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/fb0eddd31b0cff57116d18b55d182a92/sjc/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 137):
        det=0
        index='137'
        print('Downloading from IXP: IX.br (PTT.br) Recife')
        get_images.append("old.ix.br/stats/f4a27f4bb8f3c1600fa87f7ba51f95d5/pe/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/1af2a4eb82df82e086d08012c6735d03/pe/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/46d00ae9025237446713cc95f813baa3/pe/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/4b8b891e0d5f3540634f354837a86014/pe/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/745fb2a41c8e961e34a102098d198c32/pe/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 138):
        det=0
        index='138'
        print('Downloading from IXP: IX.br (PTT.br) Vitória')
        get_images.append("old.ix.br/stats/92d46ba66e511a9ce784d1dab41911f7/vix/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/b12d7ba8eeed2f6c82a38077e44407ec/vix/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/5162fc9642d86ed6cd4d238f4ccb7465/vix/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/43ea5750eeaf18311baa1e712ddb1891/vix/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/a2460191e129e723b3e7330529a34d9f/vix/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 139):
        det=0
        index='139'
        print('Downloading from IXP: IX.br (PTT.br) Manaus')
        get_images.append("old.ix.br/stats/95cde10d825361b3d70a5973ed4a6c91/mao/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/27142cfb8a89e10b9732675757a2dcab/mao/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/04b58183d64badf8ea68ee8547c8e19c/mao/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/5838e44d8a19c60717d5c6a76ff2d3be/mao/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/c7283ac14397afa386d7b92b5098547d/mao/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 140):
        det=0
        index='140'
        print('Downloading from IXP: IX.br (PTT.br) São José do Rio Preto')
        get_images.append("old.ix.br/stats/8ae6bb843462f9afeaad741bc2119183/sjp/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/99efb61d7a2c9917f0107a4a3180a12b/sjp/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/753a3cc69194607d0fe5b72fce5759e4/sjp/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/bd613943cb3f35b750e77fb55903f36f/sjp/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/7dcf61e86d9bee9d906c995d633341ce/sjp/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 141):
        det=0
        index='141'
        print('Downloading from IXP: IX.br (PTT.br) Fortaleza')
        get_images.append("old.ix.br/stats/dd851cb5bcb8b5ed4ee7231a0cc6a5ec/ce/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/f0f2f2898654c1861ef48b917fa2c4ec/ce/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/f0fa54448245736402675cffdc254d03/ce/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/fc82c3e2a81d46d3db0f9feaf4ce4145/ce/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/4e2b862704f711f8ed315e1a817d630c/ce/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 142):
        det=0
        index='142'
        print('Downloading from IXP: IX.br (PTT.br) Belém')
        get_images.append("old.ix.br/stats/ff3d72ee5bf5de680178c1a0e28b8c64/bel/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/c48c4a9aa3156caf3d58960e6d71623a/bel/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/23eb74c6d5a7481d0c39f7f612599fef/bel/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/dd95a6f2faa732fc56c9eda4c5d8ef70/bel/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/4a1bd4f792540648705dc263c2347cbd/bel/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 143):
        det=0
        index='143'
        print('Downloading from IXP: IX.br (PTT.br) Lajeado')
        get_images.append("old.ix.br/stats/91edce7194e571c167cbb8ec1adc2e89/laj/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/858eac4901044b95959ca11549bb50a8/laj/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/2415fe5ebbc77237cd4549549ac6930c/laj/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/786a9d3e63eda45997d566c8e6208925/laj/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/6fc346d949de3468c22eada689659043/laj/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 144):
        det=0
        index='144'
        print('Downloading from IXP: IX.br (PTT.br) Cuiabá')
        get_images.append("old.ix.br/stats/dd9ca9df6af28c1b48bd5d0d1168b1d8/cgb/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/030427e93e80e5325a86c429b6eb9281/cgb/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/957502212437042299fab3fd33df1c00/cgb/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/e2ef0fb3e22476cf0c767a3260c5ebd7/cgb/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/fb79fe92c1ad7c379f57726575635947/cgb/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 145):
        det=0
        index='145'
        print('Downloading from IXP: IX.br (PTT.br) Foz do Iguaçu')
        get_images.append("old.ix.br/stats/8f8d8931daca452b21d22b0843f5035c/igu/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/0b123add96cec63d2a818f69097d9289/igu/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/477738493b9c73feeeb28009264b6a2f/igu/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/5d62a360dccca38c0840fbae3350bb79/igu/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/cf0d57a47c824707650d4b5907e479db/igu/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 146):
        det=0
        index='146'
        print('Downloading from IXP: IX.br (PTT.br) Aracaju')
        get_images.append("old.ix.br/stats/9f19207684abc9efd2554cb8a9799afe/se/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/c708bb5c3fe29877ade751f68a5bc40e/se/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/856a98f2cef1313d211e3984de52cf97/se/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/a7d54d58220b8814f49fba0b21e0e483/se/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/89b52cf633eeb477cd2875e45a5c091b/se/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 147):
        det=0
        index='147'
        print('Downloading from IXP: PIT Santiago - PIT Chile')
        get_images.append("www.pitchile.cl/graficos/SCL-day.png")
        scale=[32]
    elif(targ == 148):
        det=0
        index='148'
        print('Downloading from IXP: IX.br (PTT.br) Curitiba')
        get_images.append("old.ix.br/stats/1f549208241a2c4624bec5c0f82f9a1e/pr/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/bf9f2a267995aed2a79e64f1ce74fd6e/pr/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/29c3a32b01b9ec646a61726debacc649/pr/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/9bba14908596b3a96ce08561c333e6bb/pr/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/6a37992d0d1091a3df6107844eb24db4/pr/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,840,8760,43800]
    elif(targ == 149):
        det=0
        index='149'
        print('Downloading from IXP: Netnod Sundsvall')
        get_images.append("www.netnod.se/ix-stats/sums/Sundsvall_day_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Sundsvall_week_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Sundsvall_month_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Sundsvall_year_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Sundsvall_twoyear_sum.png")
        scale=[24,168,720,8760,17520]
    elif(targ == 150):
        det=0
        index='150'
        print('Downloading from IXP: GigaNET')
        get_images.append("customer.giganet.ua/ix-daily-en.php")
        scale=[24]
    elif(targ == 151):
        index='151'
        det=1
        print('Downloading from IXP: UIXP')
        browser = webdriver.Chrome()
        browser.get('https://portal.uixp.co.ug/public-statistics/public')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        for i in range(len(graph)):
            if(graph[i].get('border')=='0'):
                get_images.append(graph[i].get('src').split('data:image/png;base64,')[1])
        scale=[33,192,792,8760]
        browser.quit()
    elif(targ == 152):
        det=0
        index='152'
        print('Downloading from IXP: RINEX')
        get_images.append("nmrtg.rinex.org.rw/mrtg/aggregate_traffic-day.png")
        get_images.append("nmrtg.rinex.org.rw/mrtg/aggregate_traffic-week.png")
        get_images.append("nmrtg.rinex.org.rw/mrtg/aggregate_traffic-month.png")
        get_images.append("nmrtg.rinex.org.rw/mrtg/aggregate_traffic-year.png")
        scale=[32,192,792,8760]
    elif(targ == 155):
        det=0
        index='155'
        print('Downloading from IXP: SIX SI')
        get_images.append("ixp.six.si/graphs/six-graph-1.png")
        get_images.append("ixp.six.si/graphs/six-graph-2.png")
        get_images.append("ixp.six.si/graphs/six-graph-4.png")
        scale=[24,168,8760]
    elif(targ == 156):
        det=0
        index='156'
        print('Downloading from IXP: LIX-LV')
        get_images.append("mans.oneit.lv/lix/graph1?period=86400&width=390")
        get_images.append("mans.oneit.lv/lix/graph1?period=604800&width=390")
        get_images.append("mans.oneit.lv/lix/graph1?period=2592000&width=390")
        get_images.append("mans.oneit.lv/lix/graph1?period=31536000&width=390")
        scale=[24,168,744,8760]
    elif(targ == 157):
        det=0
        index='157'
        print('Downloading from IXP: ArmIX')
        get_images.append("mrtg.armix.am/mrtg1/total-day.png")
        get_images.append("mrtg.armix.am/mrtg1/total-week.png")
        get_images.append("mrtg.armix.am/mrtg1/total-month.png")
        get_images.append("mrtg.armix.am/mrtg1/total-year.png")
        scale=[32,216,840,8760]
    elif(targ == 158):
        det=0
        index='158'
        print('Downloading from IXP: BR-IX')
        get_images.append("br-ix.cz/stats.png")
        scale=[33]
    elif(targ == 159):
        det=0
        index='159'
        print('Downloading from IXP: Netnod Copenhagen')
        get_images.append("www.netnod.se/ix-stats/sums/Copenhagen_day_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Copenhagen_week_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Copenhagen_month_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Copenhagen_year_sum.png")
        get_images.append("www.netnod.se/ix-stats/sums/Copenhagen_twoyear_sum.png")
        scale=[24,168,720,8760,17520]
    elif(targ ==160):  #json file
    	det=2
    	index='160'
    	print('Downloading from IXP: LINX Cardiff')
    	get_images.append('https://portal.linx.net/api/throughput/lan/car1')
    	scale=[24]
    elif(targ == 161):
        det=0
        index='161'
        print('Downloading from IXP: MIX-IT')
        get_images.append("www.mix-it.net/wp-content/statistics_mix/global-statistics.png")
        get_images.append("www.mix-it.net/wp-content/statistics_mix/weekly-statistics.png")
        get_images.append("www.mix-it.net/wp-content/statistics_mix/monthly-statistics.png")
        get_images.append("www.mix-it.net/wp-content/statistics_mix/yearly-statistics.png")
        scale=[36,264,792,8760]
    elif(targ == 162):
        det=0
        index='162'
        print('Downloading from IXP: NaMeX Rome IXP')
        get_images.append("my.namex.it/grapher/ixp?id=1&type=png")
        get_images.append("my.namex.it/grapher/ixp?id=1&type=png&period=week")
        get_images.append("my.namex.it/grapher/ixp?id=1&type=png&period=month")
        get_images.append("my.namex.it/grapher/ixp?id=1&type=png&period=year")
        scale=[33,192,792,8760]
    #elif(targ == 163):
        #det=0
        #index='163'
        #print('Downloading from IXP: POZIX')
        #get_images.append("www.pozix.pl/stats_show.php?label=0")
        #get_images.append("www.pozix.pl/stats_show.php?label=1")
        #get_images.append("www.pozix.pl/stats_show.php?label=2")
        #get_images.append("www.pozix.pl/stats_show.php?label=3")
        #scale=[1,30,480,5760]
    elif(targ == 164):
        det=0
        index='164'
        print('Downloading from IXP: DATAIX')
        get_images.append("graphs.dataix.ru/total.png")
        scale=[24]
    elif(targ == 165):
        det=0
        index='165'
        print('Downloading from IXP: STHIX - Stockholm')
        get_images.append("www.sthix.net/stats/sthix_total_hour.png")
        get_images.append("www.sthix.net/stats/sthix_total_day.png")
        get_images.append("www.sthix.net/stats/sthix_total_week.png")
        get_images.append("www.sthix.net/stats/sthix_total_month.png")
        get_images.append("www.sthix.net/stats/sthix_total_year.png")
        scale=[1,24,168,720,8760]
    elif(targ == 167):
        det=0
        index='167'
        print('Downloading from IXP: UA-IX')
        get_images.append("noc.ix.net.ua/ua-ix-daily.png")
        scale=[28]
    elif(targ == 168):
        det=0
        index='168'
        print('Downloading from IXP: DTEL-IX')
        get_images.append("dtel-ix.net/images/graphs.php?graph=ipv4")
        scale=[24]
    elif(targ == 169):
        det=0
        index='169'
        print('Downloading from IXP: npIX PTS')
        get_images.append("nms2.npix.net.np/grapher/ixp?id=3&type=png&period=day")
        get_images.append("nms2.npix.net.np/grapher/ixp?id=3&type=png&period=week")
        get_images.append("nms2.npix.net.np/grapher/ixp?id=3&type=png&period=month")
        scale=[34,192,792]
    elif(targ == 170):
        det=0
        index='170'
        print('Downloading from IXP: CNX')
        get_images.append("stat.sabay.com/cnx-images/cnx-peering-d.png")
        get_images.append("stat.sabay.com/cnx-images/cnx-peering-w.png")
        get_images.append("stat.sabay.com/cnx-images/cnx-peering-m.png")
        get_images.append("stat.sabay.com/cnx-images/cnx-peering-y.png")
        scale=[24,168,744,8760]
    elif(targ == 171):
        index='171'
        det=1
        print('Downloading from IXP: MadIX')
        browser = webdriver.Chrome()
        browser.get('https://stats1-cssc.net.wisc.edu/cgi-bin/genstatspage.fcgi?width=950&height=200&refresh=&rrdfunc=MAX&rrdlist=ba068eb83ef300f88991a13866943870&stack=1&options_viewable=Show+Options&time=1+hour+ago&start_time=04%2F12%2F2020++5%3A52%3A41+AM+-0500&end_time=now&percentile=&lower_limit=&upper_limit=&_graphtitle=&annotate_title=&annotate_time=')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        get_images.append(graph[3].get('src').split('data:image/png;base64,')[1])
        browser.get('https://stats1-cssc.net.wisc.edu/cgi-bin/genstatspage.fcgi?width=950&height=200&refresh=&rrdfunc=MAX&rrdlist=ba068eb83ef300f88991a13866943870&stack=1&options_viewable=Show+Options&time=1+day+ago&start_time=04%2F13%2F2020++4%3A53%3A32+AM+-0500&end_time=now&percentile=&lower_limit=&upper_limit=&_graphtitle=&annotate_title=&annotate_time=')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        get_images.append(graph[3].get('src').split('data:image/png;base64,')[1])
        browser.get('https://stats1-cssc.net.wisc.edu/cgi-bin/genstatspage.fcgi?width=950&height=200&refresh=&rrdfunc=MAX&rrdlist=ba068eb83ef300f88991a13866943870&stack=1&options_viewable=Show+Options&time=1+week+ago&start_time=04%2F12%2F2020++6%3A03%3A44+AM+-0500&end_time=now&percentile=&lower_limit=&upper_limit=&_graphtitle=&annotate_title=&annotate_time=')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        get_images.append(graph[3].get('src').split('data:image/png;base64,')[1])
        browser.get('https://stats1-cssc.net.wisc.edu/cgi-bin/genstatspage.fcgi?width=950&height=200&refresh=&rrdfunc=MAX&rrdlist=ba068eb83ef300f88991a13866943870&stack=1&options_viewable=Show+Options&time=1+month+ago&start_time=04%2F06%2F2020++6%3A04%3A39+AM+-0500&end_time=now&percentile=&lower_limit=&upper_limit=&_graphtitle=&annotate_title=&annotate_time=')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        get_images.append(graph[3].get('src').split('data:image/png;base64,')[1])
        scale=[1,24,168,744]
        browser.quit()
    elif(targ == 172):
        det=0
        index='172'
        print('Downloading from IXP: DE-CIX New York')
        get_images.append("www.de-cix.net/traffic_NYC-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_NYC-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_NYC-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_NYC-5years-1170-400.png")
        scale=[48,720,8760,43800]
    elif(targ == 173):
        det=0
        index='173'
        print('Downloading from IXP: SIX Seattle (Jumbo)')
        get_images.append("www.seattleix.net/statistics/agg.cfg-agg-d-y3.png")
        get_images.append("www.seattleix.net/statistics/agg.cfg-agg-w-y3.png")
        get_images.append("www.seattleix.net/statistics/agg.cfg-agg-m-y3.png")
        get_images.append("www.seattleix.net/statistics/agg.cfg-agg-y-y3.png")
        scale=[34,168,792,8760]
    elif(targ == 174):
        det=0
        index='174'
        print('Downloading from IXP: IX.br (PTT.br) Natal')
        get_images.append("old.ix.br/stats/cd5e96408d68a831911d14c16b5aa893/nat/images/pix/agregado_bps-daily.png")
        get_images.append("old.ix.br/stats/c5e9c78c89ef9dc0215f76a1cf9b7247/nat/images/pix/agregado_bps-weekly.png")
        get_images.append("old.ix.br/stats/091f05287b3cfb9063c7d61f44c51da3/nat/images/pix/agregado_bps-monthly.png")
        get_images.append("old.ix.br/stats/118877865e4a9d47afd2b48ab4d9c446/nat/images/pix/agregado_bps-yearly.png")
        get_images.append("old.ix.br/stats/7d4b0a727dcc5254905919ad8497bb1c/nat/images/pix/agregado_bps-decadely2.png")
        scale=[32,192,864,8760,43800]
    #elif(targ == 176):
        #det=0
        #index='176'
        #print('Downloading from IXP: NIX.SK')
        #get_images.append("www.nix.sk/mrtg/NIX/n-all-day.png")
        #get_images.append("www.nix.sk/mrtg/NIX/n-all-week.png")
        #get_images.append("www.nix.sk/mrtg/NIX/n-all-month.png")
        #get_images.append("www.nix.sk/mrtg/NIX/n-all-year.png")
        #scale=[38,216,912,10800]
    elif(targ == 177):
        det=0
        index='177'
        print('Downloading from IXP: SFINX')
        get_images.append("pasillo.renater.fr/ma/SFINX_Stats.png")
        get_images.append("pasillo.renater.fr/ma/SFINX_Monthly_Stats.png")
        get_images.append("pasillo.renater.fr/ma/SFINX_Yearly_Stats.png")
        scale=[24,744,8760]
    elif(targ == 179):
        det=0
        index='179'
        print('Downloading from IXP: KCIX')
        get_images.append("www.kcix.net/graphs/Daily.png?t=1581596670")
        get_images.append("www.kcix.net/graphs/Weekly.png?t=1581596670")
        get_images.append("www.kcix.net/graphs/Monthly.png?t=1581596670")
        scale=[24,168,720]
    elif(targ == 180):
        det=0
        index='180'
        print('Downloading from IXP: TPAIX')
        get_images.append("216.139.195.7/cacti/graph_image.php?action=view&local_graph_id=2266&rra_id=1")
        scale=[24]
    elif(targ == 182):
        det=0
        index='182'
        print('Downloading from IXP: MidWest-IX - Indy')
        get_images.append("www.fd-ix.com/wp-content/uploads/2019/07/fiberIcon.png")
        scale=[32]
    elif(targ == 185):
        det=0
        index='185'
        print('Downloading from IXP: GIXA')
        get_images.append("stats.gixa.org.gh/graph_image.php?local_graph_id=509&rra_id=5")
        get_images.append("stats.gixa.org.gh/graph_image.php?local_graph_id=509&rra_id=1")
        get_images.append("stats.gixa.org.gh/graph_image.php?local_graph_id=509&rra_id=2")
        get_images.append("stats.gixa.org.gh/graph_image.php?local_graph_id=509&rra_id=3")
        get_images.append("stats.gixa.org.gh/graph_image.php?local_graph_id=509&rra_id=4")
        scale=[1,24,168,744,8760]
    elif(targ == 186):
        det=0
        index='186'
        print('Downloading from IXP: NAPAfrica IX Johannesburg')
        get_images.append("ix.nap.africa/images/jb1.png")
        scale=[32]
    elif(targ == 187):
        det=0
        index='187'
        print('Downloading from IXP: NAPAfrica IX Cape Town')
        get_images.append("ix.nap.africa/images/ct1.png")
        scale=[32]
    elif(targ == 188):
        det=0
        index='188'
        print('Downloading from IXP: NAPAfrica IX Durban')
        get_images.append("ix.nap.africa/images/db1.png")
        scale=[32]
    elif(targ ==189):  #json file
    	det=2
    	index='189'
    	print('Downloading from IXP: ECIX-MUC / INXS by ecix')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Munich%20IX')
    	scale=[24]
    elif(targ ==190):  #json file
    	det=2
    	index='190'
    	print('Downloading from IXP: ECIX-DUS')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Dusseldorf%20IX')
    	scale=[24]
    #elif(targ == 191):
        #det=0
        #index='191'
        #print('Downloading from IXP: CATNIX')
        #get_images.append("stats.catnix.net/graph_image.php?action=view&local_graph_id=6973&rra_id=1")
        #scale=[24]
    elif(targ == 192):
        det=0
        index='192'
        print('Downloading from IXP: RoNIX')
        get_images.append("www.ronix.ro/wp-content/uploads/2019/08/RONIX-Total-Traffic.png")
        scale=[36]
    elif(targ == 193):
        det=0
        index='193'
        print('Downloading from IXP: BNIX')
        get_images.append("ftp.belnet.be/images/total-newbnix-daily.png")
        scale=[24]
    elif(targ == 194):
        det=0
        index='194'
        print('Downloading from IXP: ANIX - Albanian Neutral Internet eXchange')
        get_images.append("www.anix.al/stats/graphs/day.png")
        get_images.append("www.anix.al/stats/graphs/week.png")
        get_images.append("www.anix.al/stats/graphs/month.png")
        get_images.append("www.anix.al/stats/graphs/year.png")
        scale=[30,192,792,8760]
    elif(targ == 196):
        det=0
        index='196'
        print('Downloading from IXP: EPIX')
        get_images.append("newstats.epix.net.pl/epix-traffic-all-day.png")
        scale=[24]
    elif(targ == 198):
        det=0
        index='198'
        print('Downloading from IXP: Balcan-IX')
        get_images.append("trafic.balcan-ix.net/graph_image.php?action=view&local_graph_id=497&rra_id=1&graph_height=200&graph_width=950")
        get_images.append("trafic.balcan-ix.net/graph_image.php?action=view&local_graph_id=497&rra_id=2&graph_height=200&graph_width=950")
        get_images.append("trafic.balcan-ix.net/graph_image.php?action=view&local_graph_id=497&rra_id=3&graph_height=200&graph_width=950")
        get_images.append("trafic.balcan-ix.net/graph_image.php?action=view&local_graph_id=497&rra_id=4&graph_height=200&graph_width=950")
        scale=[24,168,744,8760]
    elif(targ ==199):  #json file
    	det=2
    	index='199'
    	print('Downloading from IXP: ECIX-HAM')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Hamburg%20IX')
    	scale=[24]
    elif(targ ==200):  #json file
    	det=2
    	index='200'
    	print('Downloading from IXP: ECIX-FRA')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Frankfurt%20IX')
    	scale=[24]
    elif(targ == 201):
        det=0
        index='201'
        print('Downloading from IXP: KazNIX')
        get_images.append("ixp.kaznix.kz/grapher/ixp?id=1&type=png")
        get_images.append("ixp.kaznix.kz/grapher/ixp?id=1&type=png&period=week")
        get_images.append("ixp.kaznix.kz/grapher/ixp?id=1&type=png&period=month")
        get_images.append("ixp.kaznix.kz/grapher/ixp?id=1&type=png&period=year")
        scale=[36,192,816,8760]
    elif(targ == 202):
        det=0
        index='202'
        print('Downloading from IXP: BDIX')
        get_images.append("202.59.208.18/grapher/ixp")
        get_images.append("202.59.208.18/grapher/ixp?period=week&type=png&category=bits&protocol=all&id=1%22")
        get_images.append("202.59.208.18/grapher/ixp?period=month&type=png&category=bits&protocol=all&id=1%22")
        get_images.append("202.59.208.18/grapher/ixp?period=year&type=png&category=bits&protocol=all&id=1%22")
        scale=[36,192,792,8760]
    elif(targ ==203):  #json file
    	det=2
    	index='203'
    	print('Downloading from IXP: ECIX-BER')
    	get_images.append('https://api.megaport.com/v2/graph/ixAggregate?ixName=Berlin%20IX')
    	scale=[24]
    elif(targ ==204):  #json file
    	det=2
    	index='204'
    	print('Downloading from IXP: LINX NoVA')
    	get_images.append('https://portal.linx.net/api/throughput/lan/nva1')
    	scale=[24]
    elif(targ == 205):
        det=0
        index='205'
        print('Downloading from IXP: Harare IX')
        get_images.append("portal.hix.org.zw/grapher/ixp?id=1&type=png")
        scale=[32]
    elif(targ == 206):
        index='206'
        det=1
        print('Downloading from IXP: KIXP - Nairobi')
        browser = webdriver.Chrome()
        browser.get('https://portal.kixp.or.ke/statistics/ixp')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        graph = soup.findAll('img')
        for i in range(len(graph)):
            if(graph[i].get('border')=='0'):
                get_images.append(graph[i].get('src').split('data:image/png;base64,')[1])
        scale=[30,192,816,8760]
        browser.quit()
    elif(targ == 207):
        det=0
        index='207'
        print('Downloading from IXP: LU-CIX')
        get_images.append("pub.lu-cix.restena.lu/graphs/totals/past-day_500x250.png")
        get_images.append("pub.lu-cix.restena.lu/graphs/totals/past-week_500x250.png")
        get_images.append("pub.lu-cix.restena.lu/graphs/totals/past-month_500x250.png")
        scale=[24,168,744]
    elif(targ == 208):
        det=0
        index='208'
        print('Downloading from IXP: N-IX')
        get_images.append("mgmnt.n-ix.net/graph/Traffic-Daily.png")
        get_images.append("mgmnt.n-ix.net/graph/Traffic-Weekly.png")
        get_images.append("mgmnt.n-ix.net/graph/Traffic-Monthly.png")
        get_images.append("mgmnt.n-ix.net/graph/Traffic-Yearly.png")
        scale=[24,168,744,8760]
    elif(targ == 209):
        det=0
        index='209'
        print('Downloading from IXP: Sea-IX')
        get_images.append("sea-ix.ru/images/stat/iptraf-daily.png")
        get_images.append("sea-ix.ru/images/stat/iptraf-weekly.png")
        get_images.append("sea-ix.ru/images/stat/iptraf-monthly.png")
        get_images.append("sea-ix.ru/images/stat/iptraf-yearly.png")
        scale=[24,168,720,8760]
    elif(targ == 210):
        det=0
        index='210'
        print('Downloading from IXP: SOLIX')
        get_images.append("cacti.lidnet.net/graph_image.php?action=view&local_graph_id=4102&rra_id=2&graph_width=400&graph_height=120")
        scale=[168]
    #elif(targ == 211):
        #det=0
        #index='211'
        #print('Downloading from IXP: APE')
        #get_images.append("ape.nzix.net/ape2.png")
        #get_images.append("ape.nzix.net/ape7.png")
        #scale=[48,168]
    elif(targ == 213):
        det=0
        index='213'
        print('Downloading from IXP: NIXI Ahmedabad')
        get_images.append("180.179.222.68/mrtg/Total_Agg/nixi-day.png")
        get_images.append("180.179.222.68/mrtg/Total_Agg/nixi-week.png")
        get_images.append("180.179.222.68/mrtg/Total_Agg/nixi-month.png")
        get_images.append("180.179.222.68/mrtg/Total_Agg/nixi-year.png")
        scale=[32,192,792,8760]
    elif(targ == 214):
        det=0
        index='214'
        print('Downloading from IXP: OmahaIX')
        get_images.append("www.omahaix.com/images/graph_145_1.png")
        get_images.append("www.omahaix.com/images/graph_145_2.png")
        get_images.append("www.omahaix.com/images/graph_145_3.png")
        get_images.append("www.omahaix.com/images/graph_145_4.png")
        scale=[24,168,744,8760]

    num=0
    for img in get_images:
        if det == 0:
            image = load_img(img,targ)
            data_path = 'D:\\graphs\\test_image2\\' + index +'-' + str(arrow.utcnow().timestamp) + '-' + str(scale[num]) + 'H.png'
            num+=1
            with open(data_path, 'wb') as fb:
                fb.write(image)
                #print('downloading...'+str(get_images.index(img)))
                fb.close()
        elif det == 1:
            data_path = 'D:\\graphs\\test_image2\\' + index +'-' + str(arrow.utcnow().timestamp) + '-' + str(scale[num]) + 'H.png'
            num+=1
            with open(data_path, 'wb') as fb:
                fb.write(base64.b64decode(img))
                #print('downloading...'+str(get_images.index(img)))
                fb.close()
        elif det == 2:
        	data_path = 'D:\\graphs\\test_json2\\' + index +'-' + str(arrow.utcnow().timestamp) + '-' + str(scale[num]) + 'H.json'
        	num+=1
        	response=requests.get(img)
        	response.encoding='utf8'
        	html=response.text
        	html=json.loads(html)
        	with open(data_path, 'w') as f:
        		json.dump(html, f)

#originally fine, but now inaccessible
#urls=[30,163,211,176,191]


#get_graph(urls[4])
urls = [n for n in range(1,215)]

def onetime(urls):
	for url in urls:
		try:
			get_graph(url)
		except:
			print('cannot download images from: '+ str(url))
		continue

while True:
	t=threading.Thread(target=onetime,args=[urls,])
	t.start()
	time.sleep(300)





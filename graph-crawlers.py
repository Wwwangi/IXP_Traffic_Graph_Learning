import requests
import urllib.request
import threading
import arrow
import re
from bs4 import BeautifulSoup
import base64
from time import sleep
from selenium import webdriver

def load_img(url):
	url = 'http://' + url
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
    elif(targ == 30):
        det=0
        index='30'
        print('Downloading from IXP: NIX')
        get_images.append("www.nix.cz/mrtg/NIX/n-all-day.png")
        get_images.append("www.nix.cz/mrtg/NIX/n-all-week.png")
        get_images.append("www.nix.cz/mrtg/NIX/n-all-month.png")
        get_images.append("www.nix.cz/mrtg/NIX/n-all-year.png")
        scale=[36,216,1008,10080]
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
    elif(targ == 52):
        det=0
        index='52'
        print('Downloading from IXP: DE-CIX Marseille')
        get_images.append("www.de-cix.net/traffic_MRS-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MRS-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MRS-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_MRS-2years-1170-400.png")
        scale=[48,720,8760,17520]
    elif(targ == 57):
        det=0
        index='57'
        print('Downloading from IXP: DE-CIX Palermo')
        get_images.append("www.de-cix.net/traffic_PMO-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_PMO-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_PMO-1year-1170-400.png")
        scale=[48,720,8760]
    elif(targ == 95):
        det=0
        index='95'
        print('Downloading from IXP: DE-CIX Delhi')
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-day.png")
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-week.png")
        get_images.append("www.mumbai-ix.net/ixp_peering-agrregate-bits-total-month.png")
        scale=[24,168,720]
    elif(targ == 114):
        det=0
        index='114'
        print('Downloading from IXP: DE-CIX Dallas')
        get_images.append("www.de-cix.net/traffic_DFW-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_DFW-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_DFW-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_DFW-2years-1170-400.png")
        scale=[48,720,8760,17520]
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
    elif(targ == 172):
        det=0
        index='172'
        print('Downloading from IXP: DE-CIX New York')
        get_images.append("www.de-cix.net/traffic_NYC-2days-1170-400.png")
        get_images.append("www.de-cix.net/traffic_NYC-1month-1170-400.png")
        get_images.append("www.de-cix.net/traffic_NYC-1year-1170-400.png")
        get_images.append("www.de-cix.net/traffic_NYC-5years-1170-400.png")
        scale=[48,720,8760,43800]

    num=0
    for img in get_images:
        if det == 0:
            image = load_img(img)
            data_path = 'D:\\graphs\\' + index +'-' + str(arrow.utcnow().timestamp) + '-' + str(scale[num]) + 'H.png'
            num+=1
            with open(data_path, 'wb') as fb:
                fb.write(image)
                print('downloading...'+str(get_images.index(img)))
                fb.close()
        elif det == 1:
            data_path = 'D:\\graphs\\' + index +'-' + str(arrow.utcnow().timestamp) + '-' + str(scale[num]) + 'H.png'
            num+=1
            with open(data_path, 'wb') as fb:
                fb.write(base64.b64decode(img))
                print('downloading...'+str(get_images.index(img)))
                fb.close()


urls = [141]
get_graph(urls[0])
'''
for url in urls:
    try:
        get_graph(url)
    except:
        print('cannot download images from: '+ str(url))
    continue


'''
'''
threads = [threading.Thread(target=get_graph, args=(url, )) for url in urls]

for t in threads:
    t.start()  
for t in threads:
    t.join()
'''
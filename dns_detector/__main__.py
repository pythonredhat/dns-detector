from .DnsDetector import DnsDetector
#from .config import *
import yaml

def main():
    with open('/Users/username/github-local/dns-detector-12-31/config.yml', 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    process = DnsDetector(cfg['subnet'], cfg['range1'], cfg['range2'])
    process.scan_range()
    #process.dump_csv()
    #process.subnet_splitter()
    #process.nslookup()

if __name__ == "__main__":
    main()

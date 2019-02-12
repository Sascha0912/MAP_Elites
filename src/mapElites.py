import argparse
def mapElites(domain, *args):   
    parse = argparse.ArgumentParser()
    parse.add_argument('domain')
    parse.add_argument('startMap',default=[])
    parse.add_argument('genPerVis',default=2**0)
    parse.add_argument('gifMap',default=False)
    parse.add_argument('genPerRecord',default=False)

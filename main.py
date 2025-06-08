import configparser
import argparse
from rich.console import Console
from rich.table import Table
from rich.table import Column
import feedparser



def tag_lister():
    config= configparser.ConfigParser()
    config.read('tags.ini')

    table=Table()

    table.add_column(header='Tags',justify='center')

    for item in config.sections():
        table.add_row(item)
    console = Console()
    console.print(table)

def feed_extractor(tag:str):

   URL=f"https://lobste.rs/t/{tag}.rss"
   feed_obj=feedparser.parse(URL)
   print(feed_obj.entries)

def parse_args():
    parser=argparse.ArgumentParser(description="""
    This program is written to extract lobste.rs articles for a perticular tag
""")
    parser.add_argument('-t','-tagname',required=False)
    parser.add_argument('-l','-list',required=False,action='store_true')
    return parser.parse_args()  

def main():   
    args = parse_args()

    if(args.l):
        tag_lister()

    if(args.t):    
        feed_extractor(args.t)
                       
if __name__ == "__main__":
    main()

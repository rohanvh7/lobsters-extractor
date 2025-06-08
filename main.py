import configparser
import argparse
import json

from rich.console import Console
from rich.table import Table
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

   table=Table(title=f"Posts Table for {tag}",show_lines=True)

   table.add_column(header="Title",justify='center')
   table.add_column(header="Link",justify='center')

   for item in json.loads(json.dumps(feed_obj.entries)):
       table.add_row(item['title'],item['link'])
    
   console = Console()
   console.print(table)

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

import datetime as dt

from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import numpy as np
import requests

def scrape_data():
    print("scraping")
    req = requests.get("https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield")
    soup = bs(req.text)
    
    
    t_body_chart = soup.find('table', class_='t-chart')
    rows_chart = t_body_chart.find_all('tr')
    rows_chart  
    
    treasury_rates = []
    for row in rows_chart:
        treasury_rates.append(list(row.stripped_strings))
    return pd.DataFrame(treasury_rates[1:],columns=treasury_rates[0:1])

def make_chart(data, filename):
    print("generating matplotlib chart")
    plt.plot(data)
    plt.savefig(f'charts/{filename}.png')
    print("completed")

def main():
    data = scrape_data()
    dt_now = dt.datetime.now()
    dt_fmt = dt_now.strftime("%m-%d-%y-%H%M%S")
    make_chart(data, f'chart-{dt_fmt}')

if __name__ == '__main__':
    main()
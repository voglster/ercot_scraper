import pandas as pd

url = 'http://www.ercot.com/content/cdr/html/real_time_spp'
df = pd.read_html(url)
df[0].to_csv('out.csv')


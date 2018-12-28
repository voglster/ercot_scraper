import pandas as pd

#example URL
# http://www.ercot.com/content/cdr/html/20181227_real_time_spp

def get_url(formatted_date=None):
  if formatted_date is not None:
      return f'http://www.ercot.com/content/cdr/html/{formatted_date}_real_time_spp'
  return 'http://www.ercot.com/content/cdr/html/real_time_spp'

df = pd.read_html(get_url())[0]
df.to_csv('out.csv')


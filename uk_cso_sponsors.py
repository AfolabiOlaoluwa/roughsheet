import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import random


def find_website(org_name, city, county):
    query = f"{org_name} {city} {county} official website"
    url = f"https://www.google.com/search?q={query}"
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15',
        'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36'
    ]
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        matching_links = []

        all_hrefs = [link['href'] for link in soup.find_all('a', href=True)]
        google_urls = [href for href in all_hrefs if href.startswith('/url?q=')]
        clean_urls = [url.replace('/url?q=', '') for url in google_urls]

        org_name_split = [word.strip() for word in re.split(r'\s+', org_name.lower()) if word.strip()]

        for href in clean_urls:
            parsed_url = urlparse(href)
            domain_parts = parsed_url.netloc.lower()

            for word in org_name_split:
                if word in domain_parts:
                    matching_links.append(domain_parts)
                    break
        return matching_links[0] if matching_links else None
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None


file_path = '~/PycharmProjects/roughsheet/uncleaned_data/2025-01-07_-_Worker_and_Temporary_Worker.csv'
data = pd.read_csv(file_path)

data['Website'] = None

# Iterate over the rows and find the website for each record
for index, row in data.iterrows():
    org_name = row.get('Organisation Name', '')
    city = row.get('Town/City', '')
    county = row.get('County', '')
    website = find_website(org_name, city, county)
    print(f"Found website for {org_name}: {website}")
    data.at[index, 'Website'] = website
    # time.sleep(random.uniform(2, 5))

output_file = '~/PycharmProjects/roughsheet/data/2025-01-07_-_Worker_and_Temporary_Worker.csv'
data.to_csv(output_file, index=False)
print(f"Updated file saved to {output_file}")


# Found website for  McMullan Shellfish: emcmullan.co.uk
# Found website for (IECC Care) Independent Excel Care Consortium Limited: iecc-care.co.uk
# Found website for ???£ ESS LTD: www.essltd.ie
# Found website for @ Architect UK Ltd: www.architectltd.co.uk
# Found website for @ Home Accommodation Services Ltd: www.homeaccommodation.co.uk
# Found website for @ Home Accommodation Services Ltd: www.homeaccommodation.co.uk
# Found website for @@@ FILER LIMITED: www.aaafiler.co.uk
# Found website for [AI] INFINITI LIMITED: aiinfiniti.com
# Found website for 007 Taxi Limited: 007taxis.co.uk
# Found website for 01 ACCOUNTING SERVICES LTD: www.01accountingservices.com
# Found website for 012 Global Ltd: 012-global.com
# Found website for 09 Care Limited: 09carelimited.com
# Found website for 0xA Technologies Ltd: oxatechnologies.com
# Found website for 1 ACE TRAINING LIMITED: www.1acetraining.co.uk
# Found website for 1 ALS LIMITED: www.alsglobal.com
# Found website for 1 AND 1 ROUGAMO LIMITED: www.rougamo.co.uk
# Found website for 1 Answer Insurance Services LTD.: www.1answer.co.uk
# Found website for 1 Bishops Avenue Limited: www.bishopslondon.com
# Found website for 1 Digitals Europe Limited: www.1digitals.com
# Found website for 1 Eclipse Care Solutions Limited: eclipsecare.uk
# Found website for 1 Green Foods Ltd: greenfoods.com
# Found website for 1 Homecare Ltd: 1homecare.co.uk
# Found website for 1 Indus Limited: documents1.worldbank.org
# Found website for 1 Key Solution Limited: 1keysolution.co.uk
# Found website for 1 Kings Dental Limited: 1kingsdental.com
# Found website for 1 MODEL MANAGEMENT LONDON LIMITED: onemanagement.com
# Found website for 1 Oak Home Care: www.1oakcare.com
# Found website for  McMullan Shellfish: emcmullan.co.uk
# Found website for ???£ ESS LTD: www.essltd.ie
# Found website for @ Architect UK Ltd: www.architectltd.co.uk
# Found website for @ Home Accommodation Services Ltd: www.homeaccommodation.co.uk
# Found website for @@@ FILER LIMITED: www.aaafiler.co.uk
# Found website for 01 ACCOUNTING SERVICES LTD: www.01accountingservices.com
# Found website for 012 Global Ltd: 012-global.com
# Found website for 0xA Technologies Ltd: oxatechnologies.com
# Found website for 1 ACE TRAINING LIMITED: www.1acetraining.co.uk
# Found website for 1 ALS LIMITED: www.alsglobal.com
# Found website for 1 Bishops Avenue Limited: www.bishopslondon.com
# Found website for 1 Digitals Europe Limited: www.1digitals.com
# Found website for 1 Eclipse Care Solutions Limited: eclipsecare.uk
# Found website for 1 Green Foods Ltd: greenfoods.com
# Found website for 1 Homecare Ltd: 1homecare.co.uk
# Found website for 1 Key Solution Limited: 1keysolution.co.uk
# Found website for 1 Kings Dental Limited: 1kingsdental.com
# Found website for 1 Oak Home Care: www.1oakcare.com
# Found website for 1 Stop Print Ltd: 1stopprint.co.uk
# Found website for 1 Stop Wash Ltd: 1stopwash.com
# Found website for 10 Squared Ltd: 10squared.co.uk
# Found website for 1000heads Ltd: 1000heads.com
# Found website for 101 Harley Street LTD: 101hs.co.uk
# Found website for 1066 PLUMBING AND HEATING LTD: www.1066plumbingandheating.co.uk
# Found website for 10ACT Ltd T/A TrackBack: www.trackback.net
# Found website for 10architect Ltd: www.10architect.com

import pandas as pd
campaigns = pd.read_csv('Campaignswithasins.csv')
prices = pd.read_csv('asinprices.csv')
rating = pd.read_csv('asinrating.csv')
reviews = pd.read_csv('asinreviews.csv')
category = pd.read_csv('asincat.csv')

campaignswithprices = campaigns.merge(prices, on='asin', how='left')
campaignswithrating = campaignswithprices.merge(rating, on='asin', how='left')
campaignswithreviews = campaignswithrating.merge(reviews, on='asin', how='left')
campaignswithcat = campaignswithreviews.merge(category, on='asin', how='left')

campaignsaveraged = campaignswithcat.groupby(['advertiser_name','ad_campaign_id','campaign_name','ad_type','campaign_start','campaign_end','optimization_type','category']).mean()

campaignsaveraged.to_csv('completecampaigns.csv')
from load_data import load_data
from country_average import get_country_average, get_market_average
from mkt_avg_bundle_chart import generate_mkt_avg_bundle_chart
from country_bundle_chart import generate_country_bundle_chart
from sort_dict_list import sort_dict_list
from file_locations import file, workbook_file
import xlsxwriter

# countries
countries = ["Burkina Faso", "Cameroon", "Ghana", "Ivory Coast"]

# create blank dictionary
ses_dict = []

# get data
load_data(file, ses_dict)

# create workbook
workbook = xlsxwriter.Workbook(workbook_file)

# get country average eff_price_per_gb_usd for each profile
# 1 GB profile
country_1gb_dict = []
for country in countries:
    country_1gb_dict.append({country: (get_country_average(country, 1.0, ses_dict))})
country_1gb_dict.append({"Market Average": get_market_average(country_1gb_dict)})

# mediocre sorting method to sort dictionary by value
country_1gb_dict_sorted = sort_dict_list(country_1gb_dict)

# create worksheet & chart
worksheet1 = workbook.add_worksheet()
generate_mkt_avg_bundle_chart(worksheet1, workbook, country_1gb_dict_sorted, "Market: 1 GB Bundle By Country")

# 5 GB profile
country_5gb_dict = []
for country in countries:
    country_5gb_dict.append({country: (get_country_average(country, 5.0, ses_dict))})
country_5gb_dict.append({"Market Average": get_market_average(country_5gb_dict)})

# mediocre sorting method to sort dictionary by value
country_5gb_dict_sorted = sort_dict_list(country_5gb_dict)

# create worksheet & chart
worksheet2 = workbook.add_worksheet()
generate_mkt_avg_bundle_chart(worksheet2, workbook, country_5gb_dict_sorted, "Market: 5 GB Bundle By Country")


# 10 GB profile
country_10gb_dict = []
for country in countries:
    country_10gb_dict.append({country: (get_country_average(country, 10.0, ses_dict))})
country_10gb_dict.append({"Market Average": get_market_average(country_10gb_dict)})

# mediocre sorting method to sort dictionary by value
country_10gb_dict_sorted = sort_dict_list(country_10gb_dict)

# create worksheet & chart
worksheet3 = workbook.add_worksheet()
generate_mkt_avg_bundle_chart(worksheet3, workbook, country_10gb_dict_sorted, "Market: 10 GB Bundle By Country")

# create worksheet
worksheet4 = workbook.add_worksheet()

# create list for each profile per country
# data is already sorted alphabetically by country & provider in Excel sheet
# BF 1 GB profile
bf_1gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Burkina Faso" and entry["bundle"] == 1.0:
        bf_1gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
bf_1gb_dict.append({"Market Average": get_market_average(bf_1gb_dict)})

# create chart
generate_country_bundle_chart(worksheet4, 4, workbook, bf_1gb_dict, 1)

# BF 5 GB profile
bf_5gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Burkina Faso" and entry["bundle"] == 5.0:
        bf_5gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
bf_5gb_dict.append({"Market Average": get_market_average(bf_5gb_dict)})

# create chart
generate_country_bundle_chart(worksheet4, 4, workbook, bf_5gb_dict, 5)

# BF 10 GB profile
bf_10gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Burkina Faso" and entry["bundle"] == 10.0:
        bf_10gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
bf_10gb_dict.append({"Market Average": get_market_average(bf_10gb_dict)})

# create chart
generate_country_bundle_chart(worksheet4, 4, workbook, bf_10gb_dict, 10)
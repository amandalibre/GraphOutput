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

# Market level
# get country average eff_price_per_gb_usd for each profile

# 1 GB profile
country_1gb_dict = []
for country in countries:
    country_1gb_dict.append({country: (get_country_average(country, 1.0, ses_dict))})
country_1gb_dict.append({"Market Average": get_market_average(country_1gb_dict)})
country_1gb_dict_sorted = sort_dict_list(country_1gb_dict)
worksheet1 = workbook.add_worksheet()
generate_mkt_avg_bundle_chart(worksheet1, workbook, country_1gb_dict_sorted, "Market: 1 GB Bundle By Country")

# 5 GB profile
country_5gb_dict = []
for country in countries:
    country_5gb_dict.append({country: (get_country_average(country, 5.0, ses_dict))})
country_5gb_dict.append({"Market Average": get_market_average(country_5gb_dict)})
country_5gb_dict_sorted = sort_dict_list(country_5gb_dict)
worksheet2 = workbook.add_worksheet()
generate_mkt_avg_bundle_chart(worksheet2, workbook, country_5gb_dict_sorted, "Market: 5 GB Bundle By Country")

# 10 GB profile
country_10gb_dict = []
for country in countries:
    country_10gb_dict.append({country: (get_country_average(country, 10.0, ses_dict))})
country_10gb_dict.append({"Market Average": get_market_average(country_10gb_dict)})
country_10gb_dict_sorted = sort_dict_list(country_10gb_dict)
worksheet3 = workbook.add_worksheet()
generate_mkt_avg_bundle_chart(worksheet3, workbook, country_10gb_dict_sorted, "Market: 10 GB Bundle By Country")

# country level
# data is already sorted alphabetically by country & provider in Excel sheet

# create worksheet
worksheet4 = workbook.add_worksheet()

# BF 1 GB profile
bf_1gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Burkina Faso" and entry["bundle"] == 1.0:
        bf_1gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
bf_1gb_dict.append({"Market Average": get_market_average(bf_1gb_dict)})
generate_country_bundle_chart(worksheet4, 4, workbook, bf_1gb_dict, 1)

# BF 5 GB profile
bf_5gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Burkina Faso" and entry["bundle"] == 5.0:
        bf_5gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
bf_5gb_dict.append({"Market Average": get_market_average(bf_5gb_dict)})
generate_country_bundle_chart(worksheet4, 4, workbook, bf_5gb_dict, 5)

# BF 10 GB profile
bf_10gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Burkina Faso" and entry["bundle"] == 10.0:
        bf_10gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
bf_10gb_dict.append({"Market Average": get_market_average(bf_10gb_dict)})
generate_country_bundle_chart(worksheet4, 4, workbook, bf_10gb_dict, 10)

# create worksheet
worksheet5 = workbook.add_worksheet()

# CM 1 GB profile
cm_1gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Cameroon" and entry["bundle"] == 1.0:
        cm_1gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
cm_1gb_dict.append({"Market Average": get_market_average(cm_1gb_dict)})
generate_country_bundle_chart(worksheet5, 5, workbook, cm_1gb_dict, 1)

# CM 5 GB profile
cm_5gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Cameroon" and entry["bundle"] == 5.0:
        cm_5gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
cm_5gb_dict.append({"Market Average": get_market_average(cm_5gb_dict)})
generate_country_bundle_chart(worksheet5, 5, workbook, cm_5gb_dict, 5)

# CM 10 GB profile
cm_10gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Cameroon" and entry["bundle"] == 10.0:
        cm_10gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
cm_10gb_dict.append({"Market Average": get_market_average(cm_10gb_dict)})
generate_country_bundle_chart(worksheet5, 5, workbook, cm_10gb_dict, 10)

# create worksheet
worksheet6 = workbook.add_worksheet()

# GH 1 GB profile
gh_1gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Ghana" and entry["bundle"] == 1.0:
        gh_1gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
gh_1gb_dict.append({"Market Average": get_market_average(gh_1gb_dict)})
generate_country_bundle_chart(worksheet6, 6, workbook, gh_1gb_dict, 1)

# GH 5 GB profile
gh_5gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Ghana" and entry["bundle"] == 5.0:
        gh_5gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
gh_5gb_dict.append({"Market Average": get_market_average(gh_5gb_dict)})
generate_country_bundle_chart(worksheet6, 6, workbook, gh_5gb_dict, 5)

# GH 10 GB profile
gh_10gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Ghana" and entry["bundle"] == 10.0:
        gh_10gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
gh_10gb_dict.append({"Market Average": get_market_average(gh_10gb_dict)})
generate_country_bundle_chart(worksheet6, 6, workbook, gh_10gb_dict, 10)

# create worksheet
worksheet7 = workbook.add_worksheet()

# IC 1 GB profile
ic_1gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Ivory Coast" and entry["bundle"] == 1.0:
        ic_1gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
ic_1gb_dict.append({"Market Average": get_market_average(ic_1gb_dict)})
generate_country_bundle_chart(worksheet7, 7, workbook, ic_1gb_dict, 1)

# IC 5 GB profile
ic_5gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Ivory Coast" and entry["bundle"] == 5.0:
        ic_5gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
ic_5gb_dict.append({"Market Average": get_market_average(ic_5gb_dict)})
generate_country_bundle_chart(worksheet7, 7, workbook, ic_5gb_dict, 5)

# IC 10 GB profile
ic_10gb_dict = []
for entry in ses_dict:
    if entry["country"] == "Ivory Coast" and entry["bundle"] == 10.0:
        ic_10gb_dict.append({entry["provider"]: "{:.2f}".format(entry["eff_price_per_gb_usd"])})
ic_10gb_dict.append({"Market Average": get_market_average(ic_10gb_dict)})
generate_country_bundle_chart(worksheet7, 7, workbook, ic_10gb_dict, 10)
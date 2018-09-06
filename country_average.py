def get_country_average(country, profile, dictionary):
    country_profile_list = []
    for entry in dictionary:
        if entry["country"] == country:
            if entry["bundle"] == profile:
                country_profile_list.append(entry["eff_price_per_gb_usd"])
    average_price = 0
    for price in country_profile_list:
        average_price += price
    average_price = "{:.2f}".format(average_price/(len(country_profile_list)))
    return average_price


def get_market_average(dictionary):
    market_average = float(0)
    for dict in dictionary:
        for key, value in dict.items():
            market_average += float(value)
    market_average = "{:.2f}".format(market_average/len(dictionary))
    return market_average
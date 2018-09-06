def generate_mkt_avg_bundle_chart(worksheet, workbook, sorted_dict, chart_title):

    # add data
    headings = ["Country", "Effective Price Per GB (USD)"]
    data = []
    for entry in sorted_dict:
        data.append([[key, float(value)] for key, value in entry.items()])

    worksheet.write_row('A1', headings)
    row = 2
    for entry in data:
        worksheet.write_row('A' + str(row), entry[0])
        row += 1

    # create bar chart
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'categories' : '=Sheet1!$A$2:$A$6',
        'values': '=Sheet1!$B$2:$B$6',
        'fill': {'color': 'blue'}
    })
    chart.set_title({'none': True})
    chart.set_y_axis({
        'name': 'Effective Price Per GB (USD)',
        'num_format': '$#,##0.00'})
    chart.set_x_axis({'name': 'Country'})
    chart.set_legend({'none': True})
    chart.set_size({'width': 624, 'height': 384})

    # insert chart
    worksheet.insert_chart('D2', chart)

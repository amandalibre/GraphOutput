def generate_country_bundle_chart(worksheet, worksheet_number, workbook, sorted_dict, bundle):

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
        'categories' : '=Sheet' + str(worksheet_number) + '!$A$2:$A$' + str(len(sorted_dict) + 1),
        'values': '=Sheet' + str(worksheet_number) + '!$B$2:$B$' + str(len(sorted_dict) + 1),
        'fill': {'color': 'blue'},
        'data_labels': {'value': True},
    })
    chart.set_title({'name': str(bundle) + ' GB Bundle by Provider'})
    chart.set_y_axis({
        'name': 'Effective Price Per GB (USD)',
        'num_format': '$#,##0.00'})
    chart.set_x_axis({'name': 'Country'})
    chart.set_legend({'none': True})
    chart.set_size({'width': 480, 'height': 240})

    # insert chart
    worksheet.insert_chart('D2', chart)
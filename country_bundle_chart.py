def generate_country_bundle_chart(worksheet, worksheet_number, workbook, sorted_dict, bundle):

    # add data
    headings = ["Country", "Effective Price Per GB (USD)"]
    data = []
    for entry in sorted_dict:
        data.append([[key, float(value)] for key, value in entry.items()])

    worksheet.write_row('A' + str(3 * bundle -1), headings)
    row = 3 * bundle
    for entry in data:
        worksheet.write_row('A' + str(row), entry[0])
        row += 1

    # create bar chart
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'categories' : '=Sheet' + str(worksheet_number) + '!$A$' + str(bundle * 3) + ':$A$' + str(bundle * 3 + len(sorted_dict) - 1),
        'values': '=Sheet' + str(worksheet_number) + '!$B$' + str(bundle * 3) + ':$B$' + str(bundle * 3 + len(sorted_dict) - 1),
        'fill': {'color': '#0070C0'},
        'data_labels': {
            'value': True,
            'font': {
                'bold': True
            }
        }
    })
    chart.set_title({
        'name': str(bundle) + ' GB Bundle by Provider',
        'name_font': {
            'bold': True,
            'size': 16
        }
    })
    chart.set_y_axis({
        'name': 'Effective Price Per GB (USD)',
        'num_format': '$#,##0.00',
        'name_font': {
            'size': 9
        }
    })
    chart.set_x_axis({
        'name': 'Operator'
    })
    chart.set_legend({'none': True})
    chart.set_size({'width': 480, 'height': 250})

    # insert chart
    worksheet.insert_chart('D' + str(bundle * 3), chart)
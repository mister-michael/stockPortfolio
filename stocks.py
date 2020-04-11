stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 )
]

# for purchase in purchases:
#     for company in stockDict:
#         if company == purchase[0]:
#             print(f"I purchased {stockDict[company]} stock for ${purchase[1] * purchase[3]}")

purchase_summary = {

}


for company in stockDict:
    purchase_summary[company] = list()
    for a, b, c, d in purchases:
        if company == a:
            purchase_summary[company].append([b, c, d])
    
print(purchase_summary)

for company in purchase_summary:
    print(f"-----{company}-----")
    total_value = 0
    for array in purchase_summary[company]:
        total_value += (array[0] * array[2])
        print(f'{array[0]} shares at {array[2]} dollars each on {array[1]}')
    if total_value != 0:
        print(f'Total value of stock portfolio: ${total_value}')

    
        


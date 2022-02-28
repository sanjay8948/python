from csv import DictWriter
with open('final.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
#writerow,writerows

    #csv_writer.writerow({

    #   'firstname':'sanjay','lastname':'kumar','age':21
    #    })
    #csv_writer.writerow({

    #   'firstname':'mohit','lastname':'yadav','age':25
    #    })



    csv_writer.writerows([

        {'firstname':'sanjay','lastname':'kumar','age':21},
        {'firstname':'mohit','lastname':'yadav','age':25},
        {'firstname':'roihit','lastname':'nishad','age':30}
        ])

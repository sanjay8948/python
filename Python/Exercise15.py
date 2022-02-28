
guitars=[
    {'model':'yahama f310','price':8400},
    {'model':'faith naptune','price':50000},
    {'model':'taylor 814ce','price':450000}
        ]
#sort according to price.
print(sorted(guitars,key=lambda d:d['price']))
print("\n")
print(sorted(guitars,key=lambda d:d['price'],reverse=True))

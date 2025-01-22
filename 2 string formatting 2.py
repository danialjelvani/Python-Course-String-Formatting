# f string

quantity = 6
fruit = 'banana'
price = 3
tax = 0.2351

print(
    f'{quantity:<2} {fruit}s cost {price:0>3} $ with {tax:.2f} $ tax'
)

# vase template tarif krdn format awlie
# k ye string ro b onvan template midim:

template = '''
{q} {f}s cost {p} $
'''
print(template.format(q=10, f='banana', p=4))

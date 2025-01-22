quantity = 6
fruit = 'banana'
price = 3

products = [
    (6, 'banana', 3),
    (2, 'apple', 5),
]
print('{} {}s cost {} $'.format(quantity, fruit, price))
print()

print('{} {}s cost {} $'.format(
    products[0][0], products[0][1], products[0][2]))
print()

for p in products:
    print('{} {}s cost {} $'.format(p[0], p[1], p[2]))
print()

# % mese .format e

# positional argument:
print(
    '{0}{0}{2}{1}'.format(5, 8, 6)
)
print()

# keyword argument:
print(
    '{quantity} {fruit}s cost {price} $'.format(
        price=3, quantity=6, fruit='banana')
)
print()

# 3 ta representation az har object darim:
# str repr ascii __str__ __repr__ __ascii__

# dar format: name!conversion:format_spec

print(
    'name: {0!s:} !!!'.format('danial')
)

print(
    '{:x}'.format(160)
)

print(
    'name: {0:<8} !!!'.format('danial')
)

print(
    'name: {0:>8} !!!'.format('danial')
)

print(
    'name: {0:J<8} !!!'.format('danial')
)

print(
    '{:>8}'.format(160)
)

print(
    '{:8}'.format(160)
)

# 8 ta ja mizare baghiasho ba sefr por mikone:
print(
    '{:08}'.format(160)
)

print(
    '{:9>11}'.format(160)
)

print(
    '{:0>10}'.format(160)
)

dic1 = {
    'Danial Jelvani': 24564,
    'ali': 54,
}
for k, v in dic1.items():
    print(
        '{:15} {:5}   {:0>6}'.format(k, v, v)
    )

print(
    '{:.2f}'.format(160)
)

print(
    '{:.1f}'.format(1604.4564)
)

print(
    '{:,.1f}'.format(1604.4564)
)

print(
    '{:,d}'.format(1645645604)
)

print(
    '{:_d}'.format(1645645604)
)

x = 5.31999
y = round(x, 4)
print(y)

# format method ham round mikone
# va tu x save nmikone serfn print mide:

print('{:.4f}'.format(x))

print(x)

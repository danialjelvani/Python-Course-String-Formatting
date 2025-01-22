
name = 'ali'
# 0 mitune bashe mitune nabashe
print()
print('welcome {0}'.format(name))
print()

# ye rahe bahal dare python vase vaghti
# k variable ee ro tarif nkrdi ghablesh
# k hamzaman tari konish bade ovordnesh
# k error nade: walrus operator x:=3

print('circle area with radius {r} is {area}'.format(r=3, area=4))
print()

# in payini error mide bedune define:

print('circle area with radius {r} is {area}'.format(
    r=(r := 3), area=3.14 * (r**2)))
print()


n = [5421241, 83992949, 331002651]
print(f'{n[0]:0>11,}\n\n{n[1]:0>11,}\n\n{n[2]:0>11,}')

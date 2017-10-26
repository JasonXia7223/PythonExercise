my_name = 'Jason Xia'
my_age = 28 # not a lie
my_height = 180 # cm
my_height_inch = my_height * 0.39370
my_weight = 64 # kg
my_weight_pound = my_weight * 2.2046
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s." % my_name)
# "%-8.2f": - means left-aligned, 8 means placeholder length, .2 means decimal count, f means float
print("He's %-8r cm  / %-8.2f inch tall." % (my_height, my_height_inch))
print("He's %-8d kg  / %-8.1f pound heavy." % (my_weight, my_weight_pound))
print("Actually, that's not heavy.")
print("He's got %s eyes and %s haor." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight))
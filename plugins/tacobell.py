#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from util import hook

counts = [
    'Double',
    'Triple',
    'Quadruple',
]
adjectives = [
    'Beefy',
    'Cheesy',
    'Spicy',
    'Fiery',
    'Crunchy',
    'Crispy',
    'Loaded',
    'Grilled',
    'Smothered',
    'Stuft',
    'Cantina',
]
fillers = [
    'Potato',
    'Nacho Cheese',
    'Bean',
    'Black Bean',
    'Rice',
    'Ground Beef',
    'Shredded Chicken',
    'Chicken',
    'Steak',
    'Fajitas',
    u'Fritos®',
    u'Doritos® Locos',
    u'Fiery Doritos® Locos',
    u'Cool Ranch® Doritos® Locos',
    u'Nacho Cheese Doritos® Locos',
]
meal_modifiers = [
    'Fiesta',
    'Fresco',
    'Fresco Grilled',
    'Lava',
]
meals = [
    'Taco',
    'Soft Taco',
    u'Double Decker® Taco',
    'Taco Salad',
    'Burrito',
    'Gordita',
    'Chalupa',
    'Crunchwrap',
    'Quesadilla',
    'Griller',
    'Mexican Pizza',
    'Quesarito',
    'Crunchwrap Slider',
    'Tostada',
    u'Meximelt®',
    'XXL Grilled Stuft Burrito',
    'Smothered Burrito',
    'Combo Burrito',
    '5-Layer Burrito',
    '7-Layer Burrito',
    'Nachos',
    u'Nachos Bellgrande®',
    u'Doritos® Locos Taco',
    u'Doritos® Locos Gordita',
    u'Doritos® Locos Chalupa',
    u'Doritos® Locos Nachos',
    'Enchirito',
    'Roll-Up',
    'Power Bowl',
]
modifiers = [
    'Crunch',
    u'Supreme®',
    'Party Pack',
]


def get_next_phrase(phrases, skips=None, randomness=0.5):
    if not random.randint(0, 100) < 100 * randomness:
        return []
    if not skips:
        skips = []
    for _ in range(len(phrases)):
        word = random.choice(phrases)
        skip = False
        for s in skips:
            if s in word:
                skip = True
        if not skip:
            break
    return [word]


@hook.command
def tacobell(msg):
    food = get_next_phrase(counts, randomness=.1)
    food += get_next_phrase(adjectives, skips=food, randomness=.85)
    food += get_next_phrase(fillers, skips=food, randomness=.75)
    food += get_next_phrase(meal_modifiers, skips=food, randomness=.1)
    food += get_next_phrase(meals, skips=food, randomness=1.0)
    food += get_next_phrase(modifiers, skips=food, randomness=.25)
    return ' '.join(food)

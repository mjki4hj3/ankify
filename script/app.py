import pandas as pd
import genanki
import random



standard_model =  genanki.Model(
    1681539936,
    "Standard Model",
    fields=[
        {'name':'Question'},
        {'name':'Answer'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt':'{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ]
)

my_note = genanki.Note(
    model = standard_model,
    fields = ['Whats my favourite drink?', 'J20']
)

programming_langauge_deck = genanki.Deck(
    1736119291,
    "Programming Language"
)


genanki.Package(programming_langauge_deck).write_to_file('output.apkg')

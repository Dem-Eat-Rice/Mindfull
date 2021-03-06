from app.models import db, Dreams_Fragment

# Adds a demo user, you can add other users here if you want


def seed_dreams_fragments():

    demo = Dreams_Fragment(dream_id=1, fragment_id=1)
    demo2 = Dreams_Fragment(dream_id=1, fragment_id=2)
    demo3 = Dreams_Fragment(dream_id=2, fragment_id=3)
    demo4 = Dreams_Fragment(dream_id=3, fragment_id=4)

    db.session.add(demo)
    db.session.add(demo2)
    db.session.add(demo3)
    db.session.add(demo4)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_dreams_fragments():
    db.session.execute('TRUNCATE dreams CASCADE;')
    db.session.commit()

from app.models import db, Fragment

# Adds a demo user, you can add other users here if you want


def seed_fragments():

    demo = Fragment(title='DemoFragment', emotions='Demonstration NotReal',
                    setting='Practice Coding Window Deadlines',
                    description='just dumb stuff happening one night',
                    user_id=1)

    demo2 = Fragment(title='DemoFragment2', emotions='Demonstration NotReal',
                     setting='Practice Coding Window Deadlines',
                     description='just dumb stuff happening one night',
                     user_id=1)

    demo3 = Fragment(title='DemoFragment3', emotions='Fear',
                     setting='Mr Bones Wild Ride',
                     description='It never ended',
                     user_id=2)

    demo4 = Fragment(title='DemoFragment4', emotions='Tired',
                     setting='Nighttime',
                     description='sleepytime',
                     user_id=1)

    db.session.add(demo)
    db.session.add(demo2)
    db.session.add(demo3)
    db.session.add(demo4)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_fragments():
    db.session.execute('TRUNCATE fragments CASCADE;')
    db.session.commit()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

import db_classes

Base = declarative_base()

def add_items(o_name, o_email, c_name,i_name):

    owner = session.query(db_classes.Owners).filter_by(email=o_email).first()
    if not owner:
        owner = db_classes.Owners(name=o_name, email=o_email)
        session.add(owner)
        session.commit()

    category = session.query(db_classes.Categories).filter_by(name=c_name).first()
    if not category:
        category = db_classes.Categories(name=c_name, owner=owner)
        session.add(category)
        session.commit()

    item = db_classes.Items(name=i_name, owner=owner, category=category)
    session.add(item)
    session.commit()
    return


engine = create_engine('postgresql://postgres:postgres@localhost:5432/catalog')

Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

add_items('Erik Arthur', 'erik@arthurweb.org', 'Skateboards', 'Vanguard Loaded')
add_items('Erik Arthur', 'erik@arthurweb.org', 'Skateboards', 'Sector9 Pin')

add_items('Erik Arthur', 'erik@arthurweb.org', 'Snowboards', 'Never Summer')
add_items('Erik Arthur', 'erik@arthurweb.org', 'Snowboards', 'Snow Mullet')
add_items('Erik Arthur', 'erik@arthurweb.org', 'Snowboards', 'Prior Split')
add_items('Erik Arthur', 'erik@arthurweb.org', 'Snowboards', 'Burton Fish')

add_items('E Arthur', 'erikarthur@gmail.com', 'Candles', 'Small Candle')
add_items('E Arthur', 'erikarthur@gmail.com', 'Candles', 'Medium Candle')
add_items('E Arthur', 'erikarthur@gmail.com', 'Candles', 'Large Candle')

add_items('Zach Arthur', 'zmaster97@live.com', 'Instruments', 'Alto Sax')
add_items('Zach Arthur', 'zmaster97@live.com', 'Instruments', 'Tenor Sax')
add_items('Zach Arthur', 'zmaster97@live.com', 'Instruments', 'Bassoon')

add_items('Zach Arthur', 'zmaster97@live.com', 'Video-Games', 'Halo V')
add_items('Zach Arthur', 'zmaster97@live.com', 'Video-Games', 'PGR III')
add_items('Zach Arthur', 'zmaster97@live.com', 'Video-Games', 'CoD IV')

add_items('Maddie Arthur', 'madz1313@live.com', 'Soccer', 'Cleats')
add_items('Maddie Arthur', 'madz1313@live.com', 'Soccer', 'Jersey')
add_items('Maddie Arthur', 'madz1313@live.com', 'Soccer', 'Shorts')
add_items('Maddie Arthur', 'madz1313@live.com', 'Soccer', 'Ball')

add_items('Maddie Arthur', 'madz1313@live.com', 'Recipes', 'Soup')
add_items('Maddie Arthur', 'madz1313@live.com', 'Recipes', 'Bread')
add_items('Maddie Arthur', 'madz1313@live.com', 'Recipes', 'Chicken')
add_items('Maddie Arthur', 'madz1313@live.com', 'Recipes', 'Cookies')

add_items('Jack Arthur', 'jwa@arthurweb.org', 'TV-Programs', '60 Minutes')
add_items('Jack Arthur', 'jwa@arthurweb.org', 'TV-Programs', 'Dateline')
add_items('Jack Arthur', 'jwa@arthurweb.org', 'TV-Programs', 'Fox and Friends')

add_items('Jack Arthur', 'jwa@arthurweb.org', 'Remote-Controls', 'TV')
add_items('Jack Arthur', 'jwa@arthurweb.org', 'Remote-Controls', 'VCR')
add_items('Jack Arthur', 'jwa@arthurweb.org', 'Remote-Controls', 'DVD')

add_items('Carol Arthur', 'carthur@hotmail.com', 'Quilting', 'Cloth')
add_items('Carol Arthur', 'carthur@hotmail.com', 'Quilting', 'Fleece')

add_items('Carol Arthur', 'carthur@hotmail.com', 'Sewing', 'Needles')
add_items('Carol Arthur', 'carthur@hotmail.com', 'Sewing', 'Thread')
add_items('Carol Arthur', 'carthur@hotmail.com', 'Sewing', 'Sewing Machine')

engine.dispose()
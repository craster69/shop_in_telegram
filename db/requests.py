from db.build import User, Product, session
from bot.src.handlers.message.start import UserData
from sqlalchemy import exc

async def add_user(data: UserData) -> None:

    user = User(
        user_id=data.user_id,
        user_name = data.user_name,
        date = data.date,
        file_id = data.file_id,
        file_path = data.file_path
    )

    try:
        result: User = await get_user_by_id(data.user_id)

        result.user_name = data.user_name
        result.file_id = data.file_id
        result.file_path = data.file_path
        session.commit()


    except exc.NoResultFound:
        session.add(user)
        session.commit()



async def get_user_by_id(user_id: int) -> User:


    data = session.query(User).filter(User.user_id == user_id).one()

    return data


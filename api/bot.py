import aiogram as tg
import asyncio as aio

from random import randint


router = tg.Router()


@router.message(tg.filters.Command("rollstats"))
async def roll_stats(msg: tg.types.Message):
    rep = str(get_stats())

    await msg.reply(rep)


def get_stats():
    stats = []
    while len(stats) < 6:
        roll = sorted([randint(1, 6) for i in range(4)])

        if roll[0] == roll[1] == 1:
            continue
        
        stats.append(roll)


    return [sum(i[1:]) for i in stats]


async def main():
    token = "1951062114:AAFHHl6FD_h0Uut6rZUh-LptfTfCjKRbu6s"
    bot = tg.Bot(token)

    dp = tg.Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


print("hello")
aio.run(main())

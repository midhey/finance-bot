import asyncio
import traceback
import sys
from aiohttp import web

from app.bot import handle_update, bot
from app.config import settings


async def webhook_handler(request: web.Request) -> web.Response:
    data = await request.json()
    try:
        await handle_update(data)
    except Exception as e:
        tb = "".join(traceback.format_exception(type(e), e, e.__traceback__))
        print(f"Error handling update:\n{tb}", file=sys.stderr, flush=True)
    return web.Response(status=200)


async def start_webhook():
    try:
        await bot.set_webhook(
            url=settings.webhook_url, allowed_updates=["message", "callback_query"]
        )
        print(f"Webhook установлен: {settings.webhook_url}", flush=True)
    except Exception as e:
        print(f"Ошибка установки webhook: {e}", flush=True)

    app = web.Application()
    app.router.add_post(settings.WEBHOOK_PATH, webhook_handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", settings.WEBHOOK_PORT)
    await site.start()

    print(
        f"Webhook-сервер запущен: http://0.0.0.0:{settings.WEBHOOK_PORT}{settings.WEBHOOK_PATH}",
        flush=True,
    )
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(start_webhook())

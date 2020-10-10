import asyncio
import webgram
import aiohttp.web
import logging
logging.basicConfig(level=logging.ERROR)

def main():
    loop = asyncio.get_event_loop()
    server = webgram.BareServer(loop)
    app = aiohttp.web.Application(client_max_size=1024*1024*20)
    app.add_routes([
        aiohttp.web.get('/', server.hello),
        aiohttp.web.get('/m3u/{peer}', server.grab_m3u),
        aiohttp.web.get('/watch/{peer}/{mid}/{name}', server.watch_stream),
        aiohttp.web.get('/watch/{hash}', server.watch_stream),
        aiohttp.web.get('/w/{h}', server.watch_stream),
        aiohttp.web.get('/watch/{hash}/{name}', server.watch_stream),
        aiohttp.web.get('/test_upload', server.test_upload),
        aiohttp.web.post('/upload_big', server.upload_big),
        aiohttp.web.post('/upload', server.upload),

    ])
    aiohttp.web.run_app(app, port=server.config.PORT)
    

if __name__ == "__main__":
    main()
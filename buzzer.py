
import uasyncio as asyncio




async def buzz_func(buz, times, dur_ms):
    for i in range(times):
        buz.on()
        print('on')
        await asyncio.sleep_ms(dur_ms)
        buz.off()
        print('off')

        await asyncio.sleep_ms(dur_ms)
    
async def main(buzz):
    asyncio.create_task(buzz_func(buzz, 10, 100))
    await asyncio.sleep_ms(10000)


from machine import Pin
buz_pin = 32
buzz = Pin(buz_pin, Pin.OUT)

asyncio.run(main(buzz))
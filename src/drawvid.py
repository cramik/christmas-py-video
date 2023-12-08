import asyncio
import cv2
import libacmchristmas.tree
import PIL.Image
import sys
import time

async def main():
    draws_per_second=24
    frames_per_draw=1
    url = "wss://blinktest.acmcsuf.com/ws/018c4bb9-6aa5-76fd-9c02-7e0f8ad4a812"
    tree = libacmchristmas.tree.TreeController(url)
    await tree.connect()
    print(f"Canvas is {tree.ix}x{tree.iy}")
    try:
        filename=sys.argv[1]
    except:
        print("Usage: python draw-image.py {filename}")
        quit()
    try:
        vid = cv2.VideoCapture(filename) 
    except:
        print(f"Could not open {filename}")
        quit()
    
    success=True
    while success:
        time.sleep(1/draws_per_second)
        for i in range(frames_per_draw): success, cv2_image = vid.read() 
        if success:
            pl_image = PIL.Image.fromarray(cv2.cvtColor(cv2_image,cv2.COLOR_BGR2RGB)).resize((tree.ix,tree.iy))
            await tree.draw(pl_image)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

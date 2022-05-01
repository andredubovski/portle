# Portle
This repo contains a prototype for an asynchronous chat webapp with a grid layout called Portle.

<img src="https://images.squarespace-cdn.com/content/v1/5b982331af20968d866b39a3/77b80c4d-739f-4811-b26d-c4398d9d904d/demo.png?format=2500w" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" height="420" />

We can read two to three times faster than speak or listen, so in verbal meetings like Zoom, there is conversational bandwidth that is not being taken advantage of. Our product, Portle, enhances online meetings and chats  by adding an accompanying textual layer on top of audio and video. Unlike traditional chat, Portle allows users to participate in parallel rather than sequentially. Our prototype web app looks like a Zoom grid view, but instead of webcams displayed in a grid, there are text fields, or “portals” for each participant and the host. Each user can type or dictate text into their portal and the instructor can also highlight portals to draw attention to them. We also have Focus Mode, where only instructor-selected portals are visible to the participants. For groups of twenty and over, Faction Mode splits the participants into subgroups of 3-7 that share a portal.

These features accomplish a few things. For one, people don’t have to take turns participating so that otherwise lost or forgotten ideas can get the exposure they deserve, allowing for greater breadth of discussion. Also, better ideas can be identified more quickly and explored more in depth rather than getting bottlenecked in a meandering exchange. Multiple facets of a single topic can be delved into and cross pollinate for a richer overall conversation. Finally, the instructor has foresight on what each participant wants to say before calling on them verbally, so the discussion can be guided in the intended direction. Here is a two minute demo of Portle in action: https://youtu.be/uQqwIYmT3BE.

#To build and run Portle on local WiFi network
1. Open root directory as a project in PyCharm (for example)
2. cd into the root directory in Terminal or other command line
3. run <code>set FLASK_APP=app.py</code> in command line
4. run <code>python -m flask run --host=0.0.0.0 --port=5001</code> in command line
5. You should see <code> * Running on http://your.internal.ip.address:5001 (Press CTRL+C to quit)</code>, among other things. Copy the address in its entirety (https and port and everything)
6. Open the file static/lounge.html and paste this full address in line 59 or whichever line says <code>const socket = io.connect("http://old.ip.address.here:5001");</code>
7. Ctrl+C in the command line where the server is running
8. run <code>python -m flask run --host=0.0.0.0 --port=5001</code> in command line again.
9. Portle is now running for anyone on your WiFi at http://your.internal.ip.address:5001

# BBC 6music stream metadata
This docker container is designed to run inside [Unraid](https://unraid.net/). It continually checks a configured Icecast
server's admin interface to see if anyone is listening to a proxy stream of
[BBC 6music](https://www.bbc.co.uk/sounds/play/live:bbc_6music). If anyone is listening it repeatedly hits FIP's
metadata endpoint for the current track playing and updates the Icecast admin interface with the current track.

You need to set the following environment variables in the Unraid config for the container:
- `HOST` the IP address of the Icecast server
- `PORT` the port for the Icecast server
- `USER` username for the admin interface on Icecast
- `PASSWORD` password for the admin interface on Icecast
- `MOUNT` mount path for FIP on the Icecast server

To build it on my M1 Mac I had to use the following:
`docker buildx build --platform linux/amd64,linux/arm64 -t shermozle/6music_metadata --push .`
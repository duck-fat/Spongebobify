# Spongebobify

Converts text to Spongebob chicken meme mocking case. On your discord server, invoke using `!spongify Python is a great scripting language`

## Getting Started
```bash
pip install -r requirements-dev.txt
# create a git pre-commit hook for linting
pre-commit install
# run it once (should be a noop)
pre-commit run --all-files
```
### Running the Bot using Docker
The bot needs a token. Someone should write better words on how to generate the token. For now, ask Eric for the token. Once you have a token, you can build the bot from the root of the repo:

```
docker build -t spongebot .
```

When running the container, you'll need to inject the token into the container's env. You can, for example, do the following:

```
docker run -e SPONGE_SECRET={token here} -dt spongebot
```

If started successfully, the bot should show as online in the Discord server.

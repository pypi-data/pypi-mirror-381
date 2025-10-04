[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# FediVis

A simple tool to create visualizations of fediverse related data, like the following:


![](doc/toot-analysis-demo.png)


## Status

Very early development (basically a concept study).

## Usage

1. clone the repo
2. install the package:
    - `pip install .`
3. from the mastodon web application copy the toot-url (of **your** instance) by right-clicking on the time stamp and choose "copy link"
3. run the command, e.g.
    - `fedivis --help` -> overview of command options
    - `fedivis -r https://social.tchncs.de/web/@fiercemilder@mastodon.ie/109319673519812702`
    - `fedivis --export-to-png -r https://social.tchncs.de/web/@fiercemilder@mastodon.ie/109319673519812702`
    - `fedivis --highlight "twitter" -r https://social.tchncs.de/web/@fiercemilder@mastodon.ie/109319673519812702`
4. find the svg (and optionally the png) file in the local path


## Tips

If you are experimenting with different highlight strings or if you are debugging, the `--use-cache` (or `-c`) switch is helpful.

## Logged-In-Mode (experimental)

To fetch more than 60 nodes, it is necessaray to be logged in. This is currently achieved via optional `config.toml` in working dir.

```toml
# example for config.toml

mastodon_url =  "https://foo.bar.social"
access_token = "DGNVUP8p6iMDfFZAOnG1W_GYwVCea93Uefek9DkIFJk"
```


```python
# how to create an access-token (interactively)

m = Mastodon.create_app(client_name="fedivis", api_base_url=mastodon_url)
# m is now a 2-tuple
m_api = Mastodon(*m, api_base_url=mastodon_url)
access_token = m_api.log_in(username=user, password=pw)
```


## Feedback

If you have any question, comment, bug report etc. contact me via the issue tracker and/or via <https://social.tchncs.de/@cark>.

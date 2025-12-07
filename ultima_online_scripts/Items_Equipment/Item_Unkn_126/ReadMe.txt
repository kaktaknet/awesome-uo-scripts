Newscast v1

Allows for a scrolling ticker on your shards website with a
live newsfeed comming from the shard itself, with any script
or admin having the ability to create a headline with an
optional link

INSTALLATION

-add newscast.htt to your \sphere\scripts\web directory

-add newsflash.scp to your \spehre\scripts\custom directory

-add the following config to the bottom of the 'webpage' section of \sphere\sphere.ini

[WEBPAGE 2]
// WEBPAGESRC=<path> determines what html file is used as base for the status page
WEBPAGESRC=scripts\web\newscast.htt
// WEBPAGEFILE=<path> determines where the status page is saved.
WEBPAGEFILE=scripts\web\newscast.html
// WEBCLIENTLISTFORM=<string>
WEBPAGEUPDATE=60
// PLEVEL=x, 0 means everyone, 6 just Admins
PLEVEL=0

- resync or restart your shard (i prefer a restart)

- add the following HTML code to your website

<IFRAME src="http://SHARDIPADDRESS:2593/netcast.html" width="140" height="150" border=0>

- create some news (.newsflash this is a test news item)

- see the results (you may have to wait up to 60 seconds for a headline to appear, and
  ticker updates itself)
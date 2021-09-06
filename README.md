# webcheck
## what is web check

webcheck is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries. The Disallow entries tell the search engines what directories or files hosted on a web server mustn't be indexed. For example, "Disallow: /portal/login" means that the content on www.example.com/portal/login it's not allowed to be indexed by crawlers like Google, Bing, Yahoo... This is the way the administrator have to not share sensitive or private information with the search engines.

But sometimes these paths typed in the Disallows entries are directly accessible by the users without using a search engine, just visiting the URL and the Path, and sometimes they are not available to be visited by anybody. Because it is really common that the administrators write a lot of Disallows and some of them are available and some of them are not, you can use webcheck in order to check the HTTP status code of each Disallow entry in order to check automatically if these directories are available or not.

Also, the fact the administrator write a robots.txt, it doesn't mean that the files or directories typed in the Dissallow entries will not be indexed by Bing, Google, Yahoo, etc. For this reason, webcheck is capable of searching in Bing to locate content indexed without the web administrator authorization. webcheck will check the HTTP status code in the same way for each Bing result.

When you execute webcheck, you can see the HTTP status codes. For example, the codes bellow:

```python

content.200 OK          The request has succeeded.
content.403 Forbidden   The server understood the request, but is refusing to fulfill it.
content.404 Not Found   The server hasn't found anything matching the Request-URI.
content.302 Found       The requested resource resides temporarily under a different URI.

```

# Installing 

```python
open terminal
git clone https://github.com/moulik-source/webcheck
cd webcheck
ls
python3 webcheck -u www.google.com
```

# Usage

```python

$ python3 webcheck -h
    
usage: webcheck.py [-h] [-u URL] [-o] [-sb]

optional arguments:
-h, --help  show this help message and exit
-u URL      Type the URL which will be analyzed
-o          Show only the "HTTP 200" status code
-sb         Search in Bing indexed Disallows
-f FILE     Scan a list of domains from a list

```

# Example

```python


root@kali:~# python3 webcheck.py -u www.example.com -sb

 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄              
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌             
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▐░▌              
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▐░▌               
▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌░▌                
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░▌                 
▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌░▌                
▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▐░▌               
▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌              
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌             
 ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀              
                                                                                                                
 ▄▄▄▄▄▄▄▄▄▄   ▄         ▄               ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄ 
▐░░░░░░░░░░▌ ▐░▌       ▐░▌             ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌             ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌           ▀▀▀▀█░█▀▀▀▀ ▐░▌ ▐░▌ 
▐░▌       ▐░▌▐░▌       ▐░▌             ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌▐░▌  
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌░▌   
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░░▌    
▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌░▌   
▐░▌       ▐░▌     ▐░▌                  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌▐░▌  
▐░█▄▄▄▄▄▄▄█░▌     ▐░▌                  ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░█▄▄▄▄ ▐░▌ ▐░▌ 
▐░░░░░░░░░░▌      ▐░▌                  ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌
 ▀▀▀▀▀▀▀▀▀▀        ▀                    ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀ 
                                                                                                                

Starting webcheck v0.75 (https://github.com/moulik-source/webcheck) at 05/22/14 11:12:55
webcheck scan report for example.com
http://example.com/download.php 302 Moved Temporarily
http://example.com/raw.php 302 Moved Temporarily
http://example.com/embed_js.php 200 OK
http://example.com/embed.php 200 OK
http://example.com/print.php 302 Moved Temporarily
http://example.com/diff.php 302 Moved Temporarily
http://example.com/share.php 404 Not Found
http://example.com/report.php 302 Moved Temporarily
http://example.com/embed_iframe.php 200 OK
                                         
[+] 9 links have been analyzed and 3 of them are available!!!
                                         
Searching the Disallows entries in Bing
                                         
http://www.bing.com/search?q=site:http://example.com/download.php
http://www.bing.com/search?q=site:http://example.com/raw.php
- example.com/raw.php/contact?i=KR9c2erd 200 OK
- example.com/raw.php/legal.aspx 302 Moved Temporarily
- example.com/raw.php/points?i=KR9c2erd 200 OK
- example.com/raw.php/image/sqrn11sp3C/zayn-tshirt-one-direction?i=... 302 Moved Temporarily
http://www.bing.com/search?q=site:http://example.com/embed_js.php
http://www.bing.com/search?q=site:http://example.com/embed.php
http://www.bing.com/search?q=site:http://example.com/print.php
http://www.bing.com/search?q=site:http://example.com/diff.php
http://www.bing.com/search?q=site:http://example.com/share.php
http://www.bing.com/search?q=site:http://example.com/report.php
http://www.bing.com/search?q=site:http://example.com/embed_iframe.php
                                         
Finished in 7.290362596511841 seconds 

```

# Disclaimer

The use of this tool is your responsability. Use parsero to audit your own servers or servers you are allowed to scan. I hereby disclaim any responsibility for actions taken with this tool.

# Author

- Moulik <Moulik at www.techyrick.com
- Web: http://www.techyrick.com
                
                

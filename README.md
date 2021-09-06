# webcheck
## what is web check

webcheck is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries. The Disallow entries tell the search engines what directories or files hosted on a web server mustn't be indexed. For example, "Disallow: /portal/login" means that the content on www.example.com/portal/login it's not allowed to be indexed by crawlers like Google, Bing, Yahoo... This is the way the administrator have to not share sensitive or private information with the search engines.

But sometimes these paths typed in the Disallows entries are directly accessible by the users without using a search engine, just visiting the URL and the Path, and sometimes they are not available to be visited by anybody. Because it is really common that the administrators write a lot of Disallows and some of them are available and some of them are not, you can use Parsero in order to check the HTTP status code of each Disallow entry in order to check automatically if these directories are available or not.

Also, the fact the administrator write a robots.txt, it doesn't mean that the files or directories typed in the Dissallow entries will not be indexed by Bing, Google, Yahoo, etc. For this reason, Parsero is capable of searching in Bing to locate content indexed without the web administrator authorization. Parsero will check the HTTP status code in the same way for each Bing result.

When you execute Parsero, you can see the HTTP status codes. For example, the codes bellow:

\\\python

The note content.200 OK          The request has succeeded.
The note content.403 Forbidden   The server understood the request, but is refusing to fulfill it.
The note content.404 Not Found   The server hasn't found anything matching the Request-URI.
The note content.302 Found       The requested resource resides temporarily under a different URI.

\\\



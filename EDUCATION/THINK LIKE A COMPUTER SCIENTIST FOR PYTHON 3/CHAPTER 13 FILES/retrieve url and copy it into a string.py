import urllib.request

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta

the_text = retrieve_page("http://www.msn.com/en-gb/?pc=EUPP_UE12&ocid=UE12DHP&inst=1&AR=1")
print(the_text)
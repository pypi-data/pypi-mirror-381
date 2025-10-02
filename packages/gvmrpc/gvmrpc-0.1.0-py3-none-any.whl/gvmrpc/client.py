import xmlrpc.client
from lxml import etree
from base64 import b64encode


"""
Greenbone Vulnerability Management RPC Client

This module provides a simple XML-RPC client for the Greenbone Vulnerability Management (GVM) Manager.
"""

def string_to_xml(string: str) -> etree.Element:
    """Helper function to convert a string to an lxml.etree.Element object.
    """
    return etree.fromstring(string)

def is_tuple_of_strings(obj):
    """Helper function to check if an object is a tuple of strings.
    """
    return isinstance(obj, tuple) and all(isinstance(item, str) for item in obj)


class _KeywordMethod(xmlrpc.client._Method):
    def __getattr__(self, name: str):
        return _KeywordMethod(self.__send, "%s.%s" % (self.__name, name))
    
    def __call__(self, *args, **kwargs):
        params = (args, kwargs)
        return self.__getattribute__('_Method__send')(self.__getattribute__('_Method__name'), params)

class GvmParsingMixin:
    def parse_response(self, response):
        """Extends the base class method to parse the response strings into lxml.etree objects.
        """
        response_set = super().parse_response(response)
        
        if is_tuple_of_strings(response_set):
            return tuple(etree.fromstring(item) for item in response_set if isinstance(item, str))
        
        return response_set


class GvmTransport(GvmParsingMixin, xmlrpc.client.Transport):
    """Custom XML-RPC transport class for GVM RPC Client.
    Handles parsing the returned strings back to lxml.etree objects.
    """
    ...
    
class GvmSafeTransport(GvmParsingMixin, xmlrpc.client.SafeTransport):
    """Custom XML-RPC transport class for GVM RPC Client.
    Handles parsing the returned strings back to lxml.etree objects.
    """
    ...

class GvmServerProxy(xmlrpc.client.ServerProxy):
    """Custom XML-RPC ServerProxy class for GVM RPC
    Handles the creation of the transport object with the required authentication headers.
    """
    def __init__(self, username, password, *args, ssl_context=None, **kwargs):
        auth_string = f"{username}:{password}".encode('utf-8')
        auth_header = b"Basic " + b64encode(auth_string).strip()
        
        transport_class = GvmTransport
        
        if ssl_context:
            transport_class = GvmSafeTransport
        
        if not kwargs.get('transport'):
            kwargs['transport'] = transport_class(
                headers=(('Authorization', auth_header),),
                **{'context': ssl_context} if ssl_context else {},
                )
            
        super().__init__(*args, **kwargs)
        
        self.username = username
        self.password = password
        
    def __getattr__(self, name: str):
        if name.startswith('_'):
            if name.endswith('__request'):
                return self.__getattribute__('_ServerProxy__request')
            return self.__getattribute__(name)
        else:
            return _KeywordMethod(self.__request, name)
        
class MultiCallIterator(xmlrpc.client.MultiCallIterator):
    """Custom XML-RPC multicall iterator class for GVM RPC
    Extends the base class to handle the parsing of the response strings into lxml.etree objects.
    """
    def __init__(self, results):
        parsed_results = []
        
        for r in results:
            if isinstance(r, list):
                parsed_results.append([etree.fromstring(item) for item in r])
                
        self.results = parsed_results

    def __getitem__(self, i):
        item = self.results[i]
        
        if isinstance(item, etree._Element):
            return item
        raise ValueError("Unexepected type in MultiCallIterator: %s" % type(item))

class MultiCall(xmlrpc.client.MultiCall):
    """Custom XML-RPC multicall class for GVM RPC
    Extends the base class to handle the parsing of the response strings into lxml.etree objects.
    """
    def __call__(self):
        marshalled_list = []
        
        for name, args in self.__call_list:
            marshalled_list.append({'methodName' : name, 'params' : args})
            
        return MultiCallIterator(self.__server.system.multicall(marshalled_list))

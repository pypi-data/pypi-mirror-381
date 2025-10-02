from gvm.errors import GvmResponseError
from gvm.xml import XmlCommandElement
from typing import Iterable, Union
from base64 import b64decode
from lxml import etree
import xmlrpc.server

"""
Greenbone Vulnerability Management RPC Server

This script starts a XML-RPC server that listens on localhost:8000 and accepts
XML-RPC requests that are forwarded to the Greenbone Vulnerability Management
Protocol (GMP) server via Unix socket.
"""


def clean_auth_header(auth_header: str) -> tuple[str, str]:
    """
    Helper function which decodes the base64 encoded username and password from
    the Authorization header of a HTTP request, and returns them as a tuple.
    """
    if isinstance(auth_header, bytes):
        auth_header = auth_header.decode('utf-8')

    auth_type, auth_value = auth_header.split(' ')
    assert auth_type.lower() == 'basic', 'Only basic authentication supported'

    return b64decode(auth_value).decode('utf-8').split(':')


def stringify_xml_response(response: etree.Element) -> str:
    """
    Helper function to convert an lxml.etree.Element object to a string.
    """
    if isinstance(response, etree._Element):
        xml_object = XmlCommandElement(response)
        return xml_object.to_string()
    return response


class GvmRequestHandler(xmlrpc.server.SimpleXMLRPCRequestHandler):
    """Custom request handler for the GVM RPC server.

    This request handler overrides the do_POST method to add basic authentication
    to the XML-RPC server. The authentication is done by calling the authenticate
    method, which extracts the username and password from the Authorization header
    and tries to authenticate against the GVM server. If the authentication fails,
    a 401 Unauthorized response is sent back to the client.
    """
    rpc_paths = ('/RPC2',)

    def authenticate(self):
        """Added function to authenticate against the GVM server.
        """
        # Pull the Authorization header from the request
        auth = self.headers.get('Authorization')
        # Attempt to pull the username and password from the headers
        username, password = clean_auth_header(auth)

        # Connect to the GVM server and authenticate
        self.server.instance.connect()
        self.server.instance.authenticate(username, password)

    def do_POST(self):
        """Overrides the do_POST method to add basic authentication to 
        the XML-RPC server on a per-call basis.
        """
        try:
            _ = self.authenticate()
            return super().do_POST()
        except GvmResponseError:
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="GVM RPC"')
            self.end_headers()
            return
        finally:
            self.server.instance.disconnect()


class GvmRpcServer(xmlrpc.server.SimpleXMLRPCServer):
    """Custom XML-RPC server for the GVM RPC server.
    """

    def __init__(self, addr, *args, **kwargs):
        super().__init__(addr, requestHandler=GvmRequestHandler, *args, **kwargs)

    def _dispatch(self, method: str, params: Iterable) -> Union[object, Exception]:
        """Overrides the _dispatch method to convert received lxml.etree
        responses to strings before forwarding them to the requesting client.
        """
        args, kwargs = params
        
        try:
            func = self.funcs[method]
        except KeyError:
            pass
        else:
            if func is not None:
                return stringify_xml_response(
                    func(*args, **kwargs)
                    )
            raise Exception('method "%s" is not supported' % method)
        
        if self.instance is not None:
            if hasattr(self.instance, '_dispatch'):
                return self.instance._dispatch(method, params)
            try:
                func = xmlrpc.server.resolve_dotted_attribute(
                    self.instance,
                    method,
                    self.allow_dotted_names
                )
            except AttributeError:
                pass
            else:
                if func is not None:
                    return stringify_xml_response(func(*args, **kwargs))


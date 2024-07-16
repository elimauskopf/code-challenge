import usaddress
import json
import sys
import logging
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError

logger = logging.getLogger(__name__)

class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        try:
            address = request.query_params.get('address', 'default')
            #logger.debug("TEST")
            logger.error(address + "here")
            address_components, address_type = self.parse(address)
        

            data = {
                'input_string': address,
                'adress_components': address_components,
                'adress_type': address_type
            }

            return Response(data)       
        except:
            raise ParseError(ParseError)
        

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        address_components, address_type = usaddress.tag(address)

        return address_components, address_type

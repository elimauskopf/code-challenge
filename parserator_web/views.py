import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            address = request.query_params.get('address')
            if (len(address) > 0):
                address_components, address_type = self.parse(address)

                return Response({
                    'input_string': address,
                    'address_components': address_components,
                    'address_type': address_type
                })
            else:
                raise ValueError()

        except usaddress.RepeatedLabelError:
            raise ParseError(detail="Address has repeated labels", code=400)
        except ValueError:
            raise ParseError(detail="No address provided", code=400)

    def parse(self, address):
        address_components, address_type = usaddress.tag(address)
        return address_components, address_type

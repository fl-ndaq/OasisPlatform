from rest_framework import views
from rest_framework.response import Response
from oasislmf import __version__ as oasislmf_package_ver
from oasislmf.utils.peril import PERIL_GROUPS, PERILS


class PerilcodesView(views.APIView):
    """
    Return a list of all support OED peril codes in the oasislmf package
    """
    http_method_names = ['get']
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        peril_codes = {PERILS[p]['id']: {'desc': PERILS[p]['desc']} for p in PERILS.keys()}
        peril_groups = {PERIL_GROUPS[g]['id']: {
                                                'desc': PERIL_GROUPS[g]['desc'],
                                                'peril_ids': PERIL_GROUPS[g]['peril_ids']
                                                }  for g in PERIL_GROUPS.keys()}

        return Response({'oasislmf_version': oasislmf_package_ver,
                        'peril_codes': peril_codes,
                        'peril_groups': peril_groups})

class SummaryLevelsView(views.APIView)
    """
    Return a list of all support OED columns for summary_level selection
    """
    def get(self, request):
        return Response({})

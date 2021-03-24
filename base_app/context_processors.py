from info_app.models import KontaktDatenModel
from .models import MasterObjekt

def load_master_objekt(request):
    master_objekt = MasterObjekt(request)
    return {'master_objekt': master_objekt}

def global_footer_info(request):
    contant_info = KontaktDatenModel.objects.all().first()
    return {'contant_info':contant_info,}

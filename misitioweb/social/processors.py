from .models import RRSS

def ctx_dict(request):
    ctx = {}
    redes = RRSS.objects.all()
    for red in redes:
        ctx[red.key] = red.url
    return ctx
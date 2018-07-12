from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.utils import timezone
import requests


from .models import MaterialTransaction, Material


def index(request):
    # return HttpResponse("Hello, world. You're at the test page of origin chain mobileapp.")
    template = loader.get_template('mobileapp/index.html')
    context = {
        'index': index
    }
    return HttpResponse(template.render(context, request))

def MoveInput(request):
    return render(request, 'mobileapp/moveinput.html', {})


def Movement(request):
    try:
        # First get all the form elements
        UserId = request.POST.get('user_id')
        FormMatId = request.POST.get('material_id')
        MatId = Material.objects.get(material_id=FormMatId)
        TransType = request.POST.get('trans_type')

        # Now translate the Transaction Type to DB format
        if TransType == 'MoveIn' :
            TransType = '1'
        elif TransType == 'MoveOut' :
            TransType = '2'

        # Now save it in the database
        MatTrans = MaterialTransaction(trans_type=TransType, user_id=UserId, material_id_id=MatId.id, trans_date=timezone.now())
        MatTrans.save()

        # Now write it on the blockchain
        # url = 'http://localhost:parityPort'
        # payload = {'key': 'val'}
        # headers = {}
        # res = requests.post(url, data=payload, headers=headers)

    except Material.DoesNotExist:
        raise Http404("Movement could not be recorded")
    return render(request, 'mobileapp/moveconfirm.html', {'FormMatId': FormMatId})

def MovementConfirm(request):
    return HttpResponse("You're checking out the following material")


def ViewAntecedents(request):
    transaction = MaterialTransaction.objects.order_by('-trans_date')[:5]
    template = loader.get_template('mobileapp/viewantecedents.html')
    context = {
        'transaction': transaction,
    }
    return HttpResponse(template.render(context, request))

def ShowAntecedents(request):

    try:
        materialID_id = Material.objects.get(material_id=request.POST.get('material_id'))
        antecedents = MaterialTransaction.objects.filter(material_id_id=materialID_id.id)

        # Query the data from blockchain
        # url = 'http://localhost:parityPort'
        # payload = {'key': 'val'}
        # headers = {}
        # res = requests.post(url, data=payload, headers=headers)



    except (KeyError, Material.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'mobileapp/viewantecedents.html', {
            'material_id': request.POST.get('material_id'),
            'error_message': "The material does not exist",
        })
    else:

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('mobileapp:ViewAntecedents'))
        template = loader.get_template('mobileapp/showantecedents.html')
        context = {
            'antecedents': antecedents,
        }
        return HttpResponse(template.render(context, request))

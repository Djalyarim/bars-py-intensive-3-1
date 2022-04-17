from day_19.models import Workers
from django.http import HttpResponse
import names

def create_workers(request):
    Workers.objects.bulk_create(
        [Workers(name=names.get_first_name()),
        Workers(name=names.get_first_name()),
        Workers(name=names.get_first_name())]
    )
    new_workers = Workers.objects.all().values_list().order_by('-id')[:3]
    
    return HttpResponse(new_workers)

def main(request):
    main_workers = Workers.objects.using('default').all().values_list()

    return HttpResponse(main_workers)

def replica(request):
    replica_workers = Workers.objects.using('replica').all().values_list()

    return HttpResponse(replica_workers)

def choose_db(requset):
    if Workers.objects.using('default').filter(pk=1).exists():
        workers = Workers.objects.using('default').all().values_list()
    elif Workers.objects.using('replica').filter(pk=1).exists():
        workers = Workers.objects.using('replica').all().values_list()
    else:
        workers = 'Отсутствует подключение к БД'
    
    return HttpResponse(workers)
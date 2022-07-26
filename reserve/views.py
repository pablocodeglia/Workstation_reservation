from datetime import datetime
import json
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from reserve.models import Reservations, Workstations, User
from reserve.forms import ReservationDateForm, MakeReservationForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models.functions import Concat
from django.db.models import Q, CharField, Value as V


@login_required(login_url="/accounts/login/")
def index(request):
    return render(request, 'reserve/index.html')


@login_required(login_url="/accounts/login/")
def history_view(request):
    today = datetime.today()
    query_history = Reservations.objects.filter(employee=request.user).filter(reservation_date__lt=today)
    
    context = {
        'history' : query_history
    }
    return render(request, 'reserve/history.html', context=context)
    

@login_required(login_url="/accounts/login/")
def find_coworkers_view(request):
    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        # concat first and last name, so search supports full name
        annotate_names =  Reservations.objects.annotate(coworker_full_name=Concat('employee__first_name', V(' ') ,'employee__last_name'))
        coworkers = annotate_names.filter(reservation_date = datetime.today()).filter(coworker_full_name__icontains = url_parameter)

    else:
        coworkers = {}

    context["coworkers"] = coworkers

    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json
    
    if is_ajax_request:

        html = render_to_string(
            template_name="reserve/find_coworkers_results.html", 
            context={"coworkers": coworkers}
        )

        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "reserve/find_coworkers.html", context=context)


@login_required(login_url="/accounts/login/")
def reservation_view(request):
    if request.method == "POST":
        # Checks which form was submitted
        if 'check_availability' in request.POST:
            form = ReservationDateForm(request.POST)
            if form.is_valid():
                # Get today's date
                picked_date = form.cleaned_data['date']
                print(picked_date)

                # Get all workstations with reservations for the day
                occupied_workstations = []
                q1= Reservations.objects.filter(reservation_date=picked_date).all().select_related("employee")
                for result in q1:
                    occupied_workstations.append(result.workstation_id_id)
                # print("occupied workstations:", occupied_workstations)

                # Get a list of all the workstations
                workstations = Workstations.objects.all().order_by('code')

                # Testing JSON passing
                result_list = list(workstations.values('code','monitors','seats','sector'))

                # Loop through 'occupied_workstations' and add the reserved ws status to 'result_list'
                for item in result_list:
                    if item['code'] in occupied_workstations:
                        # print("OCCUPIED")
                        item['status'] = 'booked'
                    else:
                        # print("FREE")
                        item['status'] = 'available'
                ws_json = json.dumps(result_list)

                # Passing Context
                context = {
                    'workstations': workstations,
                    'occupied':occupied_workstations,
                    'date':picked_date,
                    'form': form,
                    'ws_json': ws_json,
                }
                return render(request, "reserve/workstations_list.html", context = context)
            else:
                print(form.errors)
                return render(request, "reserve/workstations_list.html", {'form': form})

        elif 'make_reservation' in request.POST:
            form = MakeReservationForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                return redirect("reserve:my_reservations")
    else:
        form = ReservationDateForm()
        context = {
            'form': form,
        }
        return render(request, "reserve/workstations_list.html", context = context)


class ReservationsListView(LoginRequiredMixin, ListView):
    model = Reservations
    
    def get_queryset(self):
        today = datetime.today()
        return Reservations.objects.filter(employee=self.request.user).filter(reservation_date__gte=today).order_by('reservation_date')

    context_object_name = "future_reservations"

@login_required(login_url="/accounts/login/")
def delete_reservation(request, id):
    reservation = Reservations.objects.get(pk=id)
    if request.method == "POST":        
        reservation.delete()
    else:
        pass

    return redirect("reserve:my_reservations")
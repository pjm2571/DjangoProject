from django.shortcuts import render
from rest_framework.views import APIView

from reservation.models import Reservation
from user.models import User, Dog


class Main(APIView):
    def get(self, request):
        context = {}

        loginCheck = request.session.get('loginCheck', '')

        if loginCheck == '':
            context['loginCheck'] = False
            context['user'] = None
            context['reservation'] = None
        else:
            context['loginCheck'] = True
            email = request.session['email']
            user = User.objects.filter(email=email).first()
            context['user'] = user

            dogs = Dog.objects.filter(user=user)
            context['dogs'] = dogs

            reservation = Reservation.objects.filter(user=user).first()

            if reservation is None:
                context["reservation"] = None
            else:
                context["reservation"] = reservation

        return render(request, 'main/main.html', context)


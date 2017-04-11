from django.shortcuts import render
from .ticketmaster import get_all_current_venues
from .models import Venue


def homepage(request):

    # This section checks to see if the Venue table is empty and if it is, writes all
    # venues in Minnesota to it. I couldn;t think of another way to initialize this data.

    venue_check_query = Venue.objects.all()

    if not venue_check_query:

        venue_dict = get_all_current_venues()

        for key, value in venue_dict.items():

            place = key
            city = value
            state = 'MN'

            Venue.objects.create(name = place, city = city, state = state)


    return render(request, 'lmn/home.html')

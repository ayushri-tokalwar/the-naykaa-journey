from django.shortcuts import render


def home(request):
    """
    Renders Page 1: Home — Introduction to Falguni Nayar and the Nykaa empire.
    """
    context = {
        'active_page': 'home',
        'title': 'Home | Falguni Nayar — The Visionary Behind Nykaa',
    }
    return render(request, 'home.html', context)


def success_story(request):
    """
    Renders Page 2: Success Story — From Investment Banking to Building India's Beauty Empire.
    """
    context = {
        'active_page': 'success_story',
        'title': 'The Journey from Banker to Entrepreneur | Success Story',
    }
    return render(request, 'success_story.html', context)


def achievements(request):
    """
    Renders Page 3: Achievements and Recognition — Milestones that made history.
    """
    context = {
        'active_page': 'achievements',
        'title': 'Achievements That Made History | Falguni Nayar',
    }
    return render(request, 'achievements.html', context)


def personal_life(request):
    """
    Renders Page 4: Education, Personal Life and Family Background.
    """
    context = {
        'active_page': 'personal_life',
        'title': 'Beyond Business: The Person Behind the Brand | Biography',
    }
    return render(request, 'personal_life.html', context)


def about_nykaa(request):
    """
    Renders Page 5: Nykaa — The Brand and Its Impact.
    """
    context = {
        'active_page': 'about_nykaa',
        'title': 'Inside the Nykaa Business Story | Brand & Impact',
    }
    return render(request, 'about_nykaa.html', context)


def gallery(request):
    """
    Renders Page 6: Moments from the Nykaa Journey — Photo & Media Gallery.
    """
    context = {
        'active_page': 'gallery',
        'title': 'Moments from the Nykaa Journey | Curated Gallery',
    }
    return render(request, 'gallery.html', context)


def custom_404_view(request, exception=None):
    """
    Custom 404 error page.
    """
    context = {
        'active_page': '404',
        'title': 'Page Not Found | The Nykaa Journey',
    }
    return render(request, '404.html', context, status=404)

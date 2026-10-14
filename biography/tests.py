from django.test import TestCase, Client, override_settings
from django.urls import reverse


class NykaaJourneyWebTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_loads_and_displays_real_photo(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Falguni Sanjay Nayar')
        self.assertContains(response, "She Didn't Just Build a Brand. She Built an Empire.")
        # Verify authentic photo and alt text
        self.assertContains(response, 'falguni-nayar.jpg')
        self.assertContains(response, 'alt="Falguni Nayar, founder of Nykaa"')
        # Verify no academic announcement bar
        self.assertNotContains(response, 'ACADEMIC PROJECT')
        self.assertNotContains(response, 'top-bar')
        # Verify no feedback links
        self.assertNotContains(response, 'Feedback')

    def test_success_story_page_loads(self):
        response = self.client.get(reverse('success_story'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story.html')
        self.assertContains(response, 'The Journey from Banker to Entrepreneur')
        self.assertContains(response, 'IIM Ahmedabad')
        self.assertContains(response, 'Kotak Mahindra')
        self.assertNotContains(response, 'top-bar')

    def test_achievements_page_loads(self):
        response = self.client.get(reverse('achievements'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'achievements.html')
        self.assertContains(response, 'Achievements That Made History')
        self.assertContains(response, 'EY World Entrepreneur of the Year')
        self.assertNotContains(response, 'top-bar')

    def test_personal_life_page_loads(self):
        response = self.client.get(reverse('personal_life'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personal_life.html')
        self.assertContains(response, 'Beyond Business: The Person Behind the Brand')
        self.assertContains(response, 'Sanjay Nayar')
        self.assertContains(response, 'Anchit Nayar')
        self.assertContains(response, 'Adwaita Nayar')
        self.assertNotContains(response, 'top-bar')

    def test_about_nykaa_page_loads(self):
        response = self.client.get(reverse('about_nykaa'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_nykaa.html')
        self.assertContains(response, 'Inside the Nykaa Business Story')
        self.assertContains(response, 'Inventory-Led Advantage')
        self.assertNotContains(response, 'top-bar')

    def test_gallery_page_loads(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        self.assertContains(response, 'Moments from the Nykaa Journey')
        self.assertContains(response, 'falguni-nayar.jpg')
        self.assertNotContains(response, 'top-bar')

    @override_settings(DEBUG=False, ALLOWED_HOSTS=['*'])
    def test_custom_404_page(self):
        response = self.client.get('/this-path-does-not-exist-at-all/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, 'Page Not Found', status_code=404)

    def test_no_javascript_restriction(self):
        """Verifies that no script tags are present in any of the rendered templates."""
        urls = ['home', 'success_story', 'achievements', 'personal_life', 'about_nykaa', 'gallery']
        for u in urls:
            response = self.client.get(reverse(u))
            content = response.content.decode('utf-8').lower()
            self.assertNotIn('<script', content, f'Found disallowed <script> tag in {u} page.')
            self.assertNotIn('feedback', content, f'Found disallowed feedback reference in {u} page.')

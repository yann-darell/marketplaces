from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import Product, Category
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductCRUDTests(TestCase):
	def setUp(self):
		self.client = Client()
		# create a seller user
		self.seller = User.objects.create_user(username='seller1', password='testpass')
		profile_seller, _ = Profile.objects.get_or_create(user=self.seller, defaults={'role':'seller'})
		profile_seller.role = 'seller'
		profile_seller.save()
		# create a normal user
		self.user = User.objects.create_user(username='buyer1', password='testpass')
		profile_buyer, _ = Profile.objects.get_or_create(user=self.user, defaults={'role':'buyer'})
		profile_buyer.role = 'buyer'
		profile_buyer.save()
		# category
		self.cat = Category.objects.create(name='TestCat')

	def test_product_list_view(self):
		url = reverse('product_list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_create_product_requires_seller(self):
		url = reverse('create_product')
		# anonymous should be redirected to login
		response = self.client.get(url)
		self.assertEqual(response.status_code, 302)
		# login as buyer
		self.client.login(username='buyer1', password='testpass')
		response = self.client.get(url)
		# buyer should be redirected or forbidden (view redirects to home)
		self.assertNotEqual(response.status_code, 200)
		self.client.logout()
		# login as seller
		self.client.login(username='seller1', password='testpass')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_create_product_post(self):
		self.client.login(username='seller1', password='testpass')
		url = reverse('create_product')
		data = {
			'category': self.cat.id,
			'title': 'Test Product',
			'description': 'A nice product',
			'price': '19.99',
			'stock': '10',
			'is_active': True,
		}
		# include a small in-memory image for the required image field
		small_gif = (
			b'GIF87a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
		)
		image = SimpleUploadedFile('test.gif', small_gif, content_type='image/gif')
		data['image'] = image
		response = self.client.post(url, data)
		# Should normally redirect to product_detail (302) on success.
		# If status_code == 200 then form was re-rendered (invalid) — surface errors.
		if response.status_code == 200:
			# try to find form errors in context and raise informative failure
			form = None
			# Collect possible values from different context container types
			values = []
			if hasattr(response, 'context') and response.context:
				for ctx in response.context:
					# dict-like contexts
					if hasattr(ctx, 'items'):
						try:
							values.extend([v for _, v in ctx.items()])
						except Exception:
							pass
					# RequestContext may expose .dicts (list of dicts)
					elif hasattr(ctx, 'dicts'):
						for d in ctx.dicts:
							if isinstance(d, dict):
								values.extend(d.values())
					# last-resort: try to convert to dict
					else:
						try:
							d = dict(ctx)
							values.extend(d.values())
						except Exception:
							# give up on this ctx
							continue
			# locate first form-like object with errors
			for v in values:
				if hasattr(v, 'errors'):
					form = v
					break
			errors = form.errors if form is not None else 'No form in context'
			self.fail(f'Form invalid when posting create_product: {errors}')

		self.assertIn(response.status_code, (302, 301))
		prod = Product.objects.filter(title='Test Product').first()
		self.assertIsNotNone(prod)
		self.assertEqual(prod.seller, self.seller)

	def tearDown(self):
		Product.objects.all().delete()
		Category.objects.all().delete()
		User.objects.all().delete()
		Profile.objects.all().delete()

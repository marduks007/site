from django.http import request, JsonResponse
from django.shortcuts import render
from django.views.generic import FormView

from websiteProject import settings
from .forms import CheckoutForm

from cart.models import Cart
from websiteProject.mixins import FormErrors



class CheckoutView(FormView):
    form_class = CheckoutForm
    template_name = 'account/checkout.html'


    def get_context_data(self,**kwargs):
        context = super(CheckoutView,self).get_context_data(**kwargs)
        context['cart'] = Cart.objects.get(user=self.request.user,ordered=False)
        return context




    def form_valid(self, form):
        user = request.user
        up = user.userprofile

        form = CheckoutForm(instance=up)

        if request.is_ajax():
            form = CheckoutForm(data=self.request.POST, instance=up)
            if form.is_valid():
                obj = form.save()
                obj.has_profile = True
                obj.save()
                result = "Success"
                message = "Your profile has been updated"
            else:
                message = FormErrors(form)
            data = {'result': result, 'message': message}
            return JsonResponse(data)

        else:

            context = {'form': form}
            context['google_api_key'] = settings.GOOGLE_API_KEY
            context['base_country'] = settings.BASE_COUNTRY

            return render(self.request, self.template_name, context)




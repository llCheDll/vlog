from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
import logging


class BaseView(TemplateView):
    template_name = ''
    logger = logging.getLogger(__name__)
    # logger.setLevel(logging.INFO)
    #
    # file_handler = logging.FileHandler('../src/logs/view.log')
    # logger.addHandler(file_handler)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

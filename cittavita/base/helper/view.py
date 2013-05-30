import json
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import ContextMixin


class JSONResponseMixin(object):
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(
            self.convert_context_to_json(context),
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        result = {}
        for key in context.keys():
            if key in ('view'):
                continue
            result[key] = context[key]
        return json.dumps(result)

#todo go to wadofstuff.django.serializers.json
class JSONResponseMixinList(JSONResponseMixin):
    def convert_context_to_json(self, context):
        result = {}
        context_object_name = self.get_context_object_name(context['object_list'])

        for key in context.keys():
            if key in ('object_list', 'view', context_object_name):
                continue
            result[key] = context[key]

        result['object_list'] = json.loads(serializers.serialize('json', context['object_list']))

        return json.dumps(result, indent=4)


class JSONResponseMixinDetail(JSONResponseMixin):
    def convert_context_to_json(self, context):
        serializers.serialize('json', context['object'])


class ViewWithContextMixin(ContextMixin, View):
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

class JSONView(JSONResponseMixin, ViewWithContextMixin):
    pass
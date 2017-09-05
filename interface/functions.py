from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.html import escape
import xhtml2pdf.pisa as pisa
from io import StringIO, BytesIO
import os
from ProjetoControleEstoque import settings


def fetch_resources(uri, rel):
    if uri.startswith(settings.MEDIA_URL):
        path = settings.MEDIA_ROOT
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.BASE_DIR, 'interface')
    else:
        path = os.path.join(settings.BASE_DIR, 'interface')

    path += uri
    if not os.path.isfile(path):
        path = settings.MEDIA_ROOT

        if not os.path.isfile(path):
            raise Exception(u'media urls must start with %s or %s' % (
                settings.MEDIA_ROOT, settings.STATIC_ROOT))
    print(path)
    return path


def render_to_pdf(template_src, context_dict, filename="documento.pdf"):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(StringIO(html),
                            dest=result,
                            encoding='UTF-8',
                            link_callback=fetch_resources)
    if not pdf.err:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        response.write(result.getvalue())
        return response

    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

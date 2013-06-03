
_GOOGLE_ACCOUNT_EXISTS = False

try:
    from cittavita.settings import GOOGLE_ACCOUNT
    _GOOGLE_ACCOUNT_EXISTS = True
except ImportError:
    GOOGLE_ACCOUNT = None


from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def google_counter(context):
    if not _GOOGLE_ACCOUNT_EXISTS:
        return ''

    return '''<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', '%s']);
_gaq.push(['_setDomainName', 'cittavita.ru']);
_gaq.push(['_setAllowLinker', true]);
_gaq.push(['_trackPageview']);
(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>''' % GOOGLE_ACCOUNT



@register.simple_tag(takes_context=True)
def google_push_event(context):
    if not _GOOGLE_ACCOUNT_EXISTS:
        return ''

    return '''_gaq.push(['_trackEvent', 'Videos', 'Play', 'Baby\'s First Birthday']);'''